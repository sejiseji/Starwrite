from __future__ import annotations

import unittest

from data.constellations import CONSTELLATIONS
from data.stars import NAMED_STARS, STAR_NAMES
from data.stars import STARS_BY_ID


class CatalogTests(unittest.TestCase):
    def test_named_stars_have_display_names(self) -> None:
        self.assertEqual({star.id for star in NAMED_STARS}, set(STAR_NAMES))

    def test_prototype_has_22_constellations(self) -> None:
        self.assertEqual(len(CONSTELLATIONS), 22)

    def test_constellation_star_references_exist(self) -> None:
        for constellation in CONSTELLATIONS:
            for star_id in constellation.main_star_ids:
                self.assertIn(star_id, STARS_BY_ID, constellation.id)
            for a_id, b_id in constellation.edges:
                self.assertIn(a_id, STARS_BY_ID, constellation.id)
                self.assertIn(b_id, STARS_BY_ID, constellation.id)
