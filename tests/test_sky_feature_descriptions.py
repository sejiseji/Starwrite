from __future__ import annotations

import unittest

from data.sky_feature_descriptions import SKY_FEATURE_DESCRIPTIONS
from data.sky_features import ASTERISMS, SKY_PATHS
from ui.localization import SKY_FEATURE_NAMES_JA


class SkyFeatureDescriptionTests(unittest.TestCase):
    def test_descriptions_cover_current_features(self) -> None:
        expected = {feature.id for feature in (*ASTERISMS, *SKY_PATHS)}

        self.assertEqual(set(SKY_FEATURE_DESCRIPTIONS), expected)

    def test_descriptions_are_two_line_summaries(self) -> None:
        for feature_id, descriptions in SKY_FEATURE_DESCRIPTIONS.items():
            self.assertIn(feature_id, SKY_FEATURE_NAMES_JA)
            self.assertEqual(set(descriptions), {"ja", "en"}, feature_id)
            self.assertEqual(len(descriptions["ja"]), 2, feature_id)
            self.assertEqual(len(descriptions["en"]), 2, feature_id)
            for line in descriptions["ja"]:
                self.assertLessEqual(len(line), 24, feature_id)
            for line in descriptions["en"]:
                self.assertLessEqual(len(line), 36, feature_id)

    def test_descriptions_keep_source_authored_copy(self) -> None:
        self.assertEqual(
            SKY_FEATURE_DESCRIPTIONS["SUMMER_TRIANGLE"]["ja"],
            ("ベガ・デネブ・アルタイルを結ぶ。", "夏の天の川をまたぐ大きな三角。"),
        )
        self.assertEqual(
            SKY_FEATURE_DESCRIPTIONS["MILKY_WAY"]["en"],
            ("Countless stars blend into a band.", "We see our galaxy from within."),
        )


if __name__ == "__main__":
    unittest.main()
