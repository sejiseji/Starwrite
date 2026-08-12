from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

from .capture import SkyCapture, capture_from_dict, capture_to_dict

MAX_LOGS = 100
MATCH_TOP_LIMIT = 36
MATCH_RELATIVE_FLOOR = 0.2
MATCH_SCORE_WEIGHT_SCALE = 120.0
JAPANESE_SOFT_REPLACEMENTS = (
    ("真夜中", "まよなか"),
    ("帰り道", "かえりみち"),
    ("洗濯物", "せんたくもの"),
    ("手袋", "てぶくろ"),
    ("見送った", "見おくった"),
    ("取りこむ", "とりこむ"),
    ("間違った", "まちがった"),
    ("湿って", "しめって"),
    ("向こう", "むこう"),
    ("残り", "のこり"),
    ("渡した", "わたした"),
    ("空には", "そらには"),
    ("空に", "そらに"),
    ("空を", "そらを"),
    ("空は", "そらは"),
    ("少しだけ", "すこしだけ"),
    ("少し", "すこし"),
    ("明日", "あした"),
    ("昨日", "きのう"),
    ("今日", "きょう"),
    ("最後", "さいご"),
    ("最初", "さいしょ"),
    ("全部", "ぜんぶ"),
    ("一緒", "いっしょ"),
    ("一枚", "一まい"),
    ("一回", "一かい"),
    ("一通", "一つう"),
    ("二回", "二かい"),
    ("三つ", "みっつ"),
    ("一つ", "ひとつ"),
    ("何も", "なにも"),
    ("何度", "なんど"),
    ("誰", "だれ"),
    ("家に", "いえに"),
    ("家へ", "いえへ"),
    ("家は", "いえは"),
    ("家まで", "いえまで"),
    ("外へ", "そとへ"),
    ("外に", "そとに"),
    ("外で", "そとで"),
    ("外は", "そとは"),
    ("窓辺", "まどべ"),
    ("窓", "まど"),
    ("屋根", "やね"),
    ("階段", "かいだん"),
    ("椅子", "いす"),
    ("机", "つくえ"),
    ("袋", "ふくろ"),
    ("指", "ゆび"),
    ("足", "あし"),
    ("冷た", "つめた"),
    ("寒", "さむ"),
    ("重", "おも"),
    ("眠", "ねむ"),
    ("忘れ", "わすれ"),
    ("思った", "おもった"),
    ("思う", "おもう"),
    ("言う", "いう"),
    ("言わ", "いわ"),
    ("聞いた", "きいた"),
    ("聞こえ", "きこえ"),
    ("見え", "みえ"),
    ("見た", "みた"),
    ("見て", "みて"),
    ("見る", "みる"),
    ("開け", "あけ"),
    ("閉じ", "とじ"),
    ("食べ", "たべ"),
    ("飲ん", "のん"),
    ("買った", "かった"),
    ("買う", "かう"),
    ("待って", "まって"),
    ("歩いた", "あるいた"),
    ("戻", "もど"),
    ("帰", "かえ"),
    ("終わった", "おわった"),
    ("出て", "でて"),
    ("出した", "だした"),
    ("入れ", "いれ"),
    ("持って", "もって"),
    ("落と", "おと"),
    ("洗濯", "せんたく"),
    ("風呂", "ふろ"),
    ("冷凍庫", "れいとうこ"),
    ("電線", "でんせん"),
)


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
        score += 100.0
    if capture.selected_constellation_id is not None and capture.selected_constellation_id in letter.constellation_ids:
        score += 60.0
    event_tag = _event_tag(capture.selected_event_id)
    if event_tag is not None and event_tag in letter.event_tags:
        score += 30.0
    if _time_tag(capture.captured_at.hour) in letter.time_tags:
        score += 15.0
    if _season_tag(capture.captured_at.month) in letter.season_tags:
        score += 10.0
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

    floor = best_score * MATCH_RELATIVE_FLOOR
    top = [(letter, score) for letter, score in ranked[:MATCH_TOP_LIMIT] if score >= floor]
    return _weighted_choice(top or ranked[:1], chooser)


def display_letter_text(letter: PresetLetter, language: str) -> tuple[str, str | None]:
    if letter.original_language == language:
        if language == "ja":
            english_text = letter.translations.get("en")
            if english_text is not None:
                return soften_japanese_message(letter.original_text), english_text
        return _message_for_display(letter.original_text, letter.original_language), None
    translated = letter.translations.get(language)
    if translated is not None:
        return _message_for_display(translated, language), _message_for_display(letter.original_text, letter.original_language)
    return _message_for_display(letter.original_text, letter.original_language), None


def soften_japanese_message(text: str) -> str:
    softened = text
    for source, replacement in JAPANESE_SOFT_REPLACEMENTS:
        softened = softened.replace(source, replacement)
    return softened


def _message_for_display(text: str, language: str) -> str:
    if language == "ja":
        return soften_japanese_message(text)
    return text


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
