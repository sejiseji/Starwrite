from __future__ import annotations

import unittest

from data.stars import NAMED_STARS, STAR_NAMES


class CatalogTests(unittest.TestCase):
    def test_named_stars_have_display_names(self) -> None:
        self.assertEqual({star.id for star in NAMED_STARS}, set(STAR_NAMES))

