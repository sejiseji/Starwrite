from __future__ import annotations

import math
import unittest

from data.sky_features import ASTERISMS, SKY_PATHS
from data.stars import STAR_NAMES
from ui.localization import sky_feature_name


class SkyFeatureTests(unittest.TestCase):
    def test_summer_triangle_uses_three_named_stars(self) -> None:
        features = {feature.id: feature for feature in ASTERISMS}

        summer_triangle = features["SUMMER_TRIANGLE"]

        self.assertEqual(summer_triangle.star_ids, (91262, 97649, 102098))
        self.assertEqual(len(summer_triangle.edges), 3)

    def test_feature_ids_are_unique(self) -> None:
        ids = [feature.id for feature in ASTERISMS]

        self.assertEqual(len(ids), len(set(ids)))

    def test_feature_edges_use_declared_named_stars(self) -> None:
        self.assertGreaterEqual(len(ASTERISMS), 22)
        for feature in ASTERISMS:
            star_ids = set(feature.star_ids)
            self.assertTrue(star_ids <= set(STAR_NAMES), feature.id)
            for a, b in feature.edges:
                self.assertIn(a, star_ids, feature.id)
                self.assertIn(b, star_ids, feature.id)

    def test_milky_way_path_is_radian_equatorial_data(self) -> None:
        paths = {path.id: path for path in SKY_PATHS}

        milky_way = paths["MILKY_WAY"]

        self.assertGreaterEqual(len(milky_way.points), 12)
        for ra_rad, dec_rad in milky_way.points:
            self.assertGreaterEqual(ra_rad, 0.0)
            self.assertLessEqual(ra_rad, math.tau)
            self.assertGreaterEqual(dec_rad, -math.pi / 2.0)
            self.assertLessEqual(dec_rad, math.pi / 2.0)

    def test_feature_names_are_localized(self) -> None:
        feature = next(item for item in ASTERISMS if item.id == "SUMMER_TRIANGLE")

        self.assertEqual(sky_feature_name(feature, "en"), "Summer Triangle")
        self.assertEqual(sky_feature_name(feature, "ja"), "夏の大三角")

    def test_added_feature_names_are_localized(self) -> None:
        features = {feature.id: feature for feature in ASTERISMS}
        paths = {path.id: path for path in SKY_PATHS}

        self.assertEqual(sky_feature_name(features["GREAT_SQUARE"], "ja"), "秋の四辺形")
        self.assertEqual(sky_feature_name(features["NORTHERN_CROSS"], "ja"), "北十字")
        self.assertEqual(sky_feature_name(features["TEAPOT"], "en"), "Teapot")
        self.assertEqual(sky_feature_name(features["SCORPIUS_HOOK"], "ja"), "さそりの釣り針")
        self.assertEqual(sky_feature_name(features["FALSE_CROSS"], "en"), "False Cross")
        self.assertEqual(sky_feature_name(paths["MAGELLAN_CLOUD_REGION"], "ja"), "マゼラン雲の領域")


if __name__ == "__main__":
    unittest.main()
