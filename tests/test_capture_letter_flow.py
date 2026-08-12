from __future__ import annotations

import random
import unittest
from datetime import datetime, timedelta, timezone

from data.preset_letters import PRESET_LETTER_PACKS
from sky.capture import SkyCapture, capture_from_dict, capture_to_dict
from sky.letters import (
    ExchangeLog,
    append_log,
    display_letter_text,
    load_letters_from_packs,
    match_letter,
    score_letter,
)


def _capture(
    constellation_id: str = "CYG",
    star_id: int | None = 102098,
    event_id: str | None = None,
) -> SkyCapture:
    return SkyCapture(
        schema_version=1,
        captured_at=datetime(2026, 8, 13, 2, 0, tzinfo=timezone(timedelta(hours=9))),
        latitude_deg=35.7,
        longitude_deg=139.7,
        camera_yaw=0.25,
        camera_pitch=0.6,
        camera_roll=0.0,
        fov_deg=72.0,
        selected_constellation_id=constellation_id,
        selected_star_id=star_id,
        selected_feature_id=None,
        selected_event_id=event_id,
        render_seed=1234,
    )


class CaptureLetterFlowTests(unittest.TestCase):
    def test_preset_letter_catalog_has_expected_growth_room(self) -> None:
        letters = load_letters_from_packs(PRESET_LETTER_PACKS)
        ids = [letter.id for letter in letters]

        self.assertGreaterEqual(len(letters), 112)
        self.assertEqual(len(ids), len(set(ids)))

    def test_preset_letters_all_have_english_text_available(self) -> None:
        letters = load_letters_from_packs(PRESET_LETTER_PACKS)

        missing = [
            letter.id
            for letter in letters
            if letter.original_language != "en" and "en" not in letter.translations
        ]

        self.assertEqual(missing, [])

    def test_capture_serializes_camera_and_selection(self) -> None:
        capture = _capture("PER", 15863, "PER-2026")

        restored = capture_from_dict(capture_to_dict(capture))

        self.assertEqual(restored.captured_at, capture.captured_at)
        self.assertEqual(restored.latitude_deg, 35.7)
        self.assertEqual(restored.longitude_deg, 139.7)
        self.assertEqual(restored.camera_yaw, 0.25)
        self.assertEqual(restored.camera_pitch, 0.6)
        self.assertEqual(restored.camera_roll, 0.0)
        self.assertEqual(restored.selected_constellation_id, "PER")
        self.assertEqual(restored.selected_star_id, 15863)
        self.assertEqual(restored.selected_event_id, "PER-2026")

    def test_anchor_match_scores_higher_than_constellation_only(self) -> None:
        letters = load_letters_from_packs(PRESET_LETTER_PACKS)
        capture = _capture("CYG", 102098)
        cygnus_anchor = next(letter for letter in letters if letter.id == "base_000_002")
        cygnus_without_anchor = next(letter for letter in letters if letter.id == "base_000_005")

        self.assertGreater(score_letter(capture, cygnus_anchor), score_letter(capture, cygnus_without_anchor))

    def test_matcher_avoids_seen_letters_when_possible(self) -> None:
        letters = load_letters_from_packs(PRESET_LETTER_PACKS)
        seen = {"base_000_002"}

        selected = match_letter(_capture("CYG", 102098), letters, seen, rng=random.Random(1))

        self.assertNotEqual(selected.id, "base_000_002")

    def test_matcher_avoids_recent_letters_when_possible(self) -> None:
        letters = load_letters_from_packs(PRESET_LETTER_PACKS)
        recent = ("base_000_002", "base_001_018", "base_003_012")

        selected = match_letter(_capture("CYG", 102098), letters, set(), recent, rng=random.Random(1))

        self.assertNotIn(selected.id, recent)

    def test_matcher_spreads_repeatable_capture_across_nearby_candidates(self) -> None:
        letters = load_letters_from_packs(PRESET_LETTER_PACKS)
        capture = _capture("CYG", 102098)

        selected_ids = {
            match_letter(capture, letters, set(), rng=random.Random(seed)).id
            for seed in range(60)
        }

        self.assertGreaterEqual(len(selected_ids), 5)

    def test_display_uses_ui_language_then_original(self) -> None:
        letters = load_letters_from_packs(PRESET_LETTER_PACKS)
        letter = next(item for item in letters if item.id == "base_000_001")

        primary, original = display_letter_text(letter, "ja")

        self.assertIn("ポテト", primary)
        self.assertIn("Grabbed chips", original or "")

    def test_display_shows_english_companion_for_japanese_originals(self) -> None:
        letters = load_letters_from_packs(PRESET_LETTER_PACKS)
        letter = next(item for item in letters if item.id == "base_001_001")

        primary, original = display_letter_text(letter, "ja")

        self.assertIn("終電", primary)
        self.assertIn("last train", original or "")

    def test_display_uses_curated_japanese_text_without_runtime_rewrite(self) -> None:
        letters = load_letters_from_packs(PRESET_LETTER_PACKS)
        letter = next(item for item in letters if item.id == "base_003_001")

        primary, _original = display_letter_text(letter, "ja")

        self.assertEqual(primary, letter.original_text)
        self.assertIn("せんたくもの", primary)
        self.assertIn("白鳥座", primary)

    def test_log_keeps_latest_100_fifo(self) -> None:
        capture = _capture()
        logs: tuple[ExchangeLog, ...] = ()
        for index in range(101):
            logs = append_log(
                logs,
                ExchangeLog(
                    id=f"log_{index}",
                    capture=capture,
                    received_letter_id="base_000_001",
                    received_at=capture.captured_at + timedelta(minutes=index),
                ),
            )

        self.assertEqual(len(logs), 100)
        self.assertEqual(logs[0].id, "log_1")
        self.assertEqual(logs[-1].id, "log_100")


if __name__ == "__main__":
    unittest.main()
