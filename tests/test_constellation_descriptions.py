from __future__ import annotations

import unittest

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


if __name__ == "__main__":
    unittest.main()
