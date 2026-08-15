from __future__ import annotations

import unittest

from data.constellations import CONSTELLATIONS
from data.meteor_showers import METEOR_SHOWERS
from data.sky_features import ASTERISMS, SKY_PATHS
from data.stars import STAR_NAMES
from ui.localization import (
    city_name,
    constellation_name,
    constellation_sort_key,
    country_name,
    meteor_event_name,
    normalize_language,
    sky_feature_name,
    sky_feature_sort_key,
    star_name,
    star_sort_key,
)


class LocalizationTests(unittest.TestCase):
    def test_normalize_language_defaults_to_english(self) -> None:
        self.assertEqual(normalize_language("ja"), "ja")
        self.assertEqual(normalize_language("en"), "en")
        self.assertEqual(normalize_language("unknown"), "en")

    def test_constellation_name_can_be_japanese(self) -> None:
        perseus = next(constellation for constellation in CONSTELLATIONS if constellation.id == "PER")
        aquarius = next(constellation for constellation in CONSTELLATIONS if constellation.id == "AQR")

        self.assertEqual(constellation_name(perseus, "ja"), "ペルセウス座")
        self.assertEqual(constellation_name(perseus, "en"), "Perseus")
        self.assertEqual(constellation_name(aquarius, "ja"), "みずがめ座")

    def test_constellation_sort_key_matches_display_language(self) -> None:
        ja_ordered = sorted(CONSTELLATIONS, key=lambda item: constellation_sort_key(item, "ja"))
        en_ordered = sorted(CONSTELLATIONS, key=lambda item: constellation_sort_key(item, "en"))
        ja_names = [constellation_name(constellation, "ja") for constellation in ja_ordered[:5]]
        en_names = [constellation.name for constellation in en_ordered[:5]]

        self.assertEqual(
            ja_names,
            ["アンドロメダ座", "いっかくじゅう座", "いて座", "いるか座", "インディアン座"],
        )
        self.assertEqual(en_names, ["Andromeda", "Antlia", "Apus", "Aquarius", "Aquila"])

    def test_star_name_can_be_japanese(self) -> None:
        self.assertEqual(star_name(11767, "Polaris", "ja"), "ポラリス")
        self.assertEqual(star_name(11767, "Polaris", "en"), "Polaris")

    def test_star_sort_key_matches_display_language(self) -> None:
        ja_ordered = sorted(STAR_NAMES, key=lambda star_id: star_sort_key(star_id, STAR_NAMES[star_id], "ja"))
        en_ordered = sorted(STAR_NAMES, key=lambda star_id: star_sort_key(star_id, STAR_NAMES[star_id], "en"))

        self.assertEqual(star_name(ja_ordered[0], STAR_NAMES[ja_ordered[0]], "ja"), "11・かみのけ")
        self.assertEqual(star_name(en_ordered[0], STAR_NAMES[en_ordered[0]], "en"), "1 Lacertae")

    def test_sky_feature_sort_key_matches_display_language(self) -> None:
        features = (*ASTERISMS, *SKY_PATHS)
        ja_ordered = sorted(features, key=lambda feature: sky_feature_sort_key(feature, "ja"))
        en_ordered = sorted(features, key=lambda feature: sky_feature_sort_key(feature, "en"))

        self.assertEqual(sky_feature_name(ja_ordered[0], "ja"), "アルゴー船の名残")
        self.assertEqual(sky_feature_name(en_ordered[0], "en"), "Argo Ship Remnant")

    def test_meteor_event_name_can_be_japanese(self) -> None:
        perseids = next(event for event in METEOR_SHOWERS if event.id == "PER-2026")

        self.assertEqual(meteor_event_name(perseids, "ja"), "ペルセウス座流星群")
        self.assertEqual(meteor_event_name(perseids, "en"), "Perseids")

    def test_location_name_can_be_japanese(self) -> None:
        self.assertEqual(country_name("BR", "ja"), "ブラジル")
        self.assertEqual(country_name("BR", "en"), "BRAZIL")
        self.assertEqual(city_name("Sao Paulo", "ja"), "サンパウロ")
        self.assertEqual(city_name("Sao Paulo", "en"), "Sao Paulo")


if __name__ == "__main__":
    unittest.main()
