from __future__ import annotations

import math
import unittest

from data.sky_features import ASTERISMS, SKY_PATHS
from data.stars import STAR_NAMES
from ui.localization import sky_feature_name


class SkyFeatureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.features = {feature.id: feature for feature in ASTERISMS}

    def test_summer_triangle_uses_three_named_stars(self) -> None:
        summer_triangle = self.features["SUMMER_TRIANGLE"]

        self.assertEqual(summer_triangle.star_ids, (91262, 97649, 102098))
        self.assertEqual(len(summer_triangle.edges), 3)

    def test_feature_ids_are_unique(self) -> None:
        ids = [feature.id for feature in ASTERISMS]

        self.assertEqual(len(ids), len(set(ids)))

    def test_feature_edges_use_declared_named_stars(self) -> None:
        self.assertGreaterEqual(len(ASTERISMS), 28)
        for feature in ASTERISMS:
            star_ids = set(feature.star_ids)
            self.assertEqual(len(star_ids), len(feature.star_ids), feature.id)
            self.assertTrue(star_ids <= set(STAR_NAMES), feature.id)
            seen_edges: set[frozenset[int]] = set()
            for a, b in feature.edges:
                self.assertNotEqual(a, b, feature.id)
                self.assertIn(a, star_ids, feature.id)
                self.assertIn(b, star_ids, feature.id)
                edge_key = frozenset((a, b))
                self.assertNotIn(edge_key, seen_edges, feature.id)
                seen_edges.add(edge_key)

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
        paths = {path.id: path for path in SKY_PATHS}

        self.assertEqual(sky_feature_name(self.features["GREAT_SQUARE"], "ja"), "秋の四辺形")
        self.assertEqual(sky_feature_name(self.features["NORTHERN_CROSS"], "ja"), "北十字")
        self.assertEqual(sky_feature_name(self.features["TEAPOT"], "en"), "Teapot")
        self.assertEqual(sky_feature_name(self.features["SCORPIUS_HOOK"], "ja"), "さそりの釣り針")
        self.assertEqual(sky_feature_name(self.features["FALSE_CROSS"], "en"), "False Cross")
        self.assertEqual(sky_feature_name(paths["MAGELLAN_CLOUD_REGION"], "ja"), "マゼラン雲の領域")
        self.assertEqual(sky_feature_name(self.features["PLEIADES"], "ja"), "プレアデス星団")
        self.assertEqual(sky_feature_name(self.features["KEYSTONE_OF_HERCULES"], "en"), "Keystone of Hercules")

    def test_safe_feature_patch_shapes_are_applied(self) -> None:
        self.assertIn((59774, 54061), self.features["BIG_DIPPER"].edges)
        self.assertEqual(
            self.features["SPRING_ARC"].edges,
            ((62956, 65378), (65378, 67301), (67301, 69673), (69673, 65474)),
        )
        self.assertEqual(len(self.features["TEAPOT"].star_ids), 8)
        self.assertEqual(len(self.features["TEAPOT"].edges), 11)
        self.assertEqual(self.features["SCORPIUS_HOOK"].edges[-1], (85696, 85927))
        self.assertEqual(
            self.features["WATER_JAR"].edges,
            ((110960, 110395), (110960, 111497), (110960, 110672)),
        )

    def test_safe_feature_patch_catalog_names_are_corrected(self) -> None:
        self.assertEqual(STAR_NAMES[45941], "Markeb")
        self.assertEqual(STAR_NAMES[42913], "Alsephina")
        self.assertEqual(STAR_NAMES[20889], "Epsilon Tauri")
        self.assertEqual(STAR_NAMES[92041], "Phi Sagittarii")
        self.assertEqual(STAR_NAMES[115738], "Kappa Piscium")


if __name__ == "__main__":
    unittest.main()
