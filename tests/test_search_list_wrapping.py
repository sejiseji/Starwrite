from __future__ import annotations

import sys
import types
import unittest

sys.modules.setdefault("pyxel", types.SimpleNamespace(width=396, height=696))

from data.sky_features import ASTERISMS, SKY_PATHS
from data.stars import STAR_NAMES
from ui.localization import sky_feature_name, star_name
from src.ui.hud import (
    _search_button_label_lines,
    constellation_list_button_rects,
    star_magnitude_color,
    star_magnitude_rank,
    text_width,
)


class SearchListWrappingTests(unittest.TestCase):
    def test_english_star_and_feature_labels_fit_three_lines(self) -> None:
        rect = constellation_list_button_rects(396, 696, 1, 0)[0]
        max_width = rect[2] - 8
        labels = [
            *(star_name(star_id, english_name, "en") for star_id, english_name in STAR_NAMES.items()),
            *(sky_feature_name(feature, "en") for feature in (*ASTERISMS, *SKY_PATHS)),
        ]

        for label in labels:
            with self.subTest(label=label):
                lines = _search_button_label_lines(label, "en", max_width)
                self.assertLessEqual(len(lines), 3)
                for line in lines:
                    self.assertLessEqual(text_width(line.upper()), max_width)

    def test_star_magnitude_rank_uses_visual_magnitude_classes(self) -> None:
        self.assertEqual(star_magnitude_rank(-1.46), 1)
        self.assertEqual(star_magnitude_rank(1.50), 1)
        self.assertEqual(star_magnitude_rank(1.51), 2)
        self.assertEqual(star_magnitude_rank(5.50), 5)
        self.assertEqual(star_magnitude_rank(5.51), 6)
        self.assertIn(star_magnitude_color(2.1), range(16))


if __name__ == "__main__":
    unittest.main()
