import sys
import types
import unittest

sys.modules.setdefault("pyxel", types.SimpleNamespace(width=396, height=696))

from ui.hud import moon_body_hit_rect


class MoonHitRectTests(unittest.TestCase):
    def test_moon_body_hit_rect_is_finger_sized_and_centered(self) -> None:
        rect = moon_body_hit_rect((120.4, 240.8))

        self.assertEqual(rect, (102, 222, 37, 37))

    def test_moon_body_hit_rect_contains_center_only_with_expected_margin(self) -> None:
        x, y, w, h = moon_body_hit_rect((120.0, 240.0))

        self.assertLessEqual(x, 120)
        self.assertLessEqual(y, 240)
        self.assertLess(120, x + w)
        self.assertLess(240, y + h)
        self.assertEqual(w, h)


if __name__ == "__main__":
    unittest.main()
