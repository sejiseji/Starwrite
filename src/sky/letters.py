from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

from .capture import SkyCapture, capture_from_dict, capture_to_dict

MAX_LOGS = 100
ANCHOR_STAR_SCORE = 12.0
CONSTELLATION_SCORE = 8.0
EVENT_SCORE = 18.0
TIME_SCORE = 10.0
SEASON_SCORE = 8.0
MATCH_SCORE_WEIGHT_SCALE = 180.0


class RandomLike(Protocol):
    def random(self) -> float:
        ...

    def choice(self, sequence):
        ...


@dataclass(slots=True, frozen=True)
class PresetLetter:
    id: str
    country_code: str
    region: str | None
    city: str | None
    original_language: str
    original_text: str
    translations: dict[str, str]
    constellation_ids: tuple[str, ...]
    anchor_star_ids: tuple[int, ...]
    season_tags: tuple[str, ...]
    time_tags: tuple[str, ...]
    event_tags: tuple[str, ...]
    weight: float = 1.0


@dataclass(slots=True, frozen=True)
class ExchangeLog:
    id: str
    capture: SkyCapture
    received_letter_id: str
    received_at: datetime


def letter_from_dict(data: dict) -> PresetLetter:
    return PresetLetter(
        id=str(data["id"]),
        country_code=str(data["country_code"]),
        region=data.get("region"),
        city=data.get("city"),
        original_language=str(data["original_language"]),
        original_text=str(data["original_text"]),
        translations={str(key): str(value) for key, value in data.get("translations", {}).items()},
        constellation_ids=tuple(str(value) for value in data.get("constellation_ids", ())),
        anchor_star_ids=tuple(int(value) for value in data.get("anchor_star_ids", ())),
        season_tags=tuple(str(value) for value in data.get("season_tags", ())),
        time_tags=tuple(str(value) for value in data.get("time_tags", ())),
        event_tags=tuple(str(value) for value in data.get("event_tags", ())),
        weight=float(data.get("weight", 1.0)),
    )


def load_letters_from_packs(packs: dict[str, tuple[dict, ...]], pack_ids: tuple[str, ...] | None = None) -> tuple[PresetLetter, ...]:
    selected_pack_ids = pack_ids or tuple(packs)
    letters: list[PresetLetter] = []
    for pack_id in selected_pack_ids:
        for item in packs.get(pack_id, ()):
            letters.append(letter_from_dict(item))
    return tuple(letters)


def score_letter(capture: SkyCapture, letter: PresetLetter) -> float:
    score = 0.0
    if capture.selected_star_id is not None and capture.selected_star_id in letter.anchor_star_ids:
        score += ANCHOR_STAR_SCORE
    if capture.selected_constellation_id is not None and capture.selected_constellation_id in letter.constellation_ids:
        score += CONSTELLATION_SCORE
    event_tag = _event_tag(capture.selected_event_id)
    if event_tag is not None and event_tag in letter.event_tags:
        score += EVENT_SCORE
    if _time_tag(capture.captured_at.hour) in letter.time_tags:
        score += TIME_SCORE
    if _season_tag(capture.captured_at.month) in letter.season_tags:
        score += SEASON_SCORE
    return score * max(0.1, letter.weight)


def match_letter(
    capture: SkyCapture,
    letters: tuple[PresetLetter, ...],
    seen_letter_ids: set[str],
    recent_letter_ids: tuple[str, ...] = (),
    rng: RandomLike | None = None,
) -> PresetLetter:
    if not letters:
        raise ValueError("letters must not be empty")
    chooser = rng or random
    recent = set(recent_letter_ids[-30:])
    candidates = [letter for letter in letters if letter.id not in seen_letter_ids and letter.id not in recent]
    if not candidates:
        candidates = [letter for letter in letters if letter.id not in recent]
    if not candidates:
        candidates = list(letters)

    scored = [(letter, score_letter(capture, letter)) for letter in candidates]
    ranked = sorted(scored, key=lambda item: item[1], reverse=True)
    best_score = ranked[0][1]
    if best_score <= 0.0:
        return chooser.choice([letter for letter, _score in ranked])

    return _weighted_choice(ranked, chooser)


def display_letter_text(letter: PresetLetter, language: str) -> tuple[str, str | None]:
    if letter.original_language == language:
        if language == "ja":
            english_text = letter.translations.get("en")
            if english_text is not None:
                return letter.original_text, english_text
        return letter.original_text, None
    translated = letter.translations.get(language)
    if translated is not None:
        return translated, letter.original_text
    return letter.original_text, None


def log_to_dict(log: ExchangeLog) -> dict:
    return {
        "id": log.id,
        "capture": capture_to_dict(log.capture),
        "received_letter_id": log.received_letter_id,
        "received_at": log.received_at.isoformat(),
    }


def log_from_dict(data: dict) -> ExchangeLog:
    return ExchangeLog(
        id=str(data["id"]),
        capture=capture_from_dict(data["capture"]),
        received_letter_id=str(data["received_letter_id"]),
        received_at=datetime.fromisoformat(str(data["received_at"])),
    )


def append_log(logs: tuple[ExchangeLog, ...], log: ExchangeLog, max_logs: int = MAX_LOGS) -> tuple[ExchangeLog, ...]:
    values = [*logs, log]
    while len(values) > max_logs:
        values.pop(0)
    return tuple(values)


def _weighted_choice(letters: list[tuple[PresetLetter, float]], rng: RandomLike) -> PresetLetter:
    total = sum(_selection_weight(letter, score) for letter, score in letters)
    cursor = rng.random() * total
    for letter, score in letters:
        cursor -= _selection_weight(letter, score)
        if cursor <= 0.0:
            return letter
    return letters[-1][0]


def _selection_weight(letter: PresetLetter, score: float) -> float:
    return max(0.1, letter.weight) * (1.0 + max(0.0, score) / MATCH_SCORE_WEIGHT_SCALE)


def _event_tag(event_id: str | None) -> str | None:
    if event_id is None:
        return None
    return event_id.split("-", 1)[0]


def _season_tag(month: int) -> str:
    if month in (3, 4, 5):
        return "spring"
    if month in (6, 7, 8):
        return "summer"
    if month in (9, 10, 11):
        return "autumn"
    return "winter"


def _time_tag(hour: int) -> str:
    if 17 <= hour < 21:
        return "evening"
    if 21 <= hour or hour < 3:
        return "night"
    return "late"
