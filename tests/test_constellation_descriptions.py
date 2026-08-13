from __future__ import annotations

import unittest
from pathlib import Path

from data.constellation_descriptions import CONSTELLATION_DESCRIPTIONS
from data.constellations import CONSTELLATIONS


class ConstellationDescriptionTests(unittest.TestCase):
    def test_descriptions_cover_current_constellations(self) -> None:
        expected = {constellation.id for constellation in CONSTELLATIONS}

        self.assertEqual(set(CONSTELLATION_DESCRIPTIONS), expected)

    def test_descriptions_fit_summary_panel(self) -> None:
        for constellation_id, descriptions in CONSTELLATION_DESCRIPTIONS.items():
            self.assertEqual(set(descriptions), {"ja", "en"}, constellation_id)
            self.assertEqual(len(descriptions["ja"]), 2, constellation_id)
            self.assertEqual(len(descriptions["en"]), 2, constellation_id)
            for line in descriptions["ja"]:
                self.assertLessEqual(len(line), 24, constellation_id)
            for line in descriptions["en"]:
                self.assertLessEqual(len(line), 34, constellation_id)

    def test_descriptions_keep_source_authored_copy(self) -> None:
        self.assertEqual(
            CONSTELLATION_DESCRIPTIONS["ORI"]["ja"],
            ("三つ星を帯に並べた狩人。", "冬空でひときわ堂々と立つ。"),
        )
        self.assertEqual(
            CONSTELLATION_DESCRIPTIONS["CYG"]["ja"],
            ("十字の翼で天の川を渡る。", "尾には青白いデネブが光る。"),
        )
        self.assertEqual(
            CONSTELLATION_DESCRIPTIONS["CAS"]["ja"],
            ("五つの星が描く折れた王座。", "北の空で季節ごとに向きを変える。"),
        )

    def test_old_anchor_copy_fallback_is_not_used(self) -> None:
        hud_source = Path("src/ui/hud.py").read_text(encoding="utf-8")

        self.assertNotIn("ふくむ星座", hud_source)
        self.assertNotIn("includes {anchor_star_label}", hud_source)


if __name__ == "__main__":
    unittest.main()
