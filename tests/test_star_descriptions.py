from __future__ import annotations

import unittest

from data.constellations import CONSTELLATIONS
from data.star_descriptions import STAR_DESCRIPTIONS
from data.stars import STAR_NAMES
from ui.localization import STAR_NAMES_JA


class StarDescriptionTests(unittest.TestCase):
    def test_descriptions_cover_named_stars(self) -> None:
        self.assertEqual(set(STAR_DESCRIPTIONS), set(STAR_NAMES))

    def test_descriptions_are_two_line_summaries(self) -> None:
        constellation_ids = {constellation.id for constellation in CONSTELLATIONS}
        for star_id, descriptions in STAR_DESCRIPTIONS.items():
            self.assertIn(descriptions.get("constellation_id"), constellation_ids, star_id)
            self.assertIn(star_id, STAR_NAMES_JA, star_id)
            self.assertEqual(len(descriptions["ja"]), 2, star_id)
            self.assertEqual(len(descriptions["en"]), 2, star_id)
            for line in descriptions["ja"]:
                self.assertLessEqual(len(line), 24, star_id)
            for line in descriptions["en"]:
                self.assertLessEqual(len(line), 36, star_id)

    def test_descriptions_keep_source_authored_copy(self) -> None:
        self.assertEqual(
            STAR_DESCRIPTIONS[11767]["ja"],
            ("北極近くで脈打つ超巨星。", "長い夜の方角を静かに示す。"),
        )
        self.assertEqual(
            STAR_DESCRIPTIONS[32349]["en"],
            ("The brightest star in our night.", "White fire leads the winter hound."),
        )


if __name__ == "__main__":
    unittest.main()
