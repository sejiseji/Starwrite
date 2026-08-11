from __future__ import annotations

import unittest

from data.constellations import CONSTELLATIONS
from data.meteor_showers import METEOR_SHOWERS
from ui.localization import constellation_name, meteor_event_name, normalize_language, star_name


class LocalizationTests(unittest.TestCase):
    def test_normalize_language_defaults_to_english(self) -> None:
        self.assertEqual(normalize_language("ja"), "ja")
        self.assertEqual(normalize_language("en"), "en")
        self.assertEqual(normalize_language("unknown"), "en")

    def test_constellation_name_can_be_japanese(self) -> None:
        perseus = next(constellation for constellation in CONSTELLATIONS if constellation.id == "PER")

        self.assertEqual(constellation_name(perseus, "ja"), "ペルセウス座")
        self.assertEqual(constellation_name(perseus, "en"), "Perseus")

    def test_star_name_can_be_japanese(self) -> None:
        self.assertEqual(star_name(11767, "Polaris", "ja"), "ポラリス")
        self.assertEqual(star_name(11767, "Polaris", "en"), "Polaris")

    def test_meteor_event_name_can_be_japanese(self) -> None:
        perseids = next(event for event in METEOR_SHOWERS if event.id == "PER-2026")

        self.assertEqual(meteor_event_name(perseids, "ja"), "ペルセウス座流星群")
        self.assertEqual(meteor_event_name(perseids, "en"), "Perseids")


if __name__ == "__main__":
    unittest.main()
