from __future__ import annotations

import unittest
from datetime import datetime, timedelta, timezone

from astronomy.moon import compute_moon, moon_light_level, moon_tags_from_state
from sky.moon import MoonController


class MoonTests(unittest.TestCase):
    def test_moon_state_range(self) -> None:
        state = compute_moon(datetime(2026, 8, 13, 12, 0, tzinfo=timezone.utc), 35.7, 139.7)

        self.assertGreaterEqual(state.azimuth_deg, 0.0)
        self.assertLess(state.azimuth_deg, 360.0)
        self.assertGreaterEqual(state.altitude_deg, -90.0)
        self.assertLessEqual(state.altitude_deg, 90.0)
        self.assertGreaterEqual(state.right_ascension_deg, 0.0)
        self.assertLess(state.right_ascension_deg, 360.0)
        self.assertGreaterEqual(state.declination_deg, -90.0)
        self.assertLessEqual(state.declination_deg, 90.0)

    def test_moon_illumination_range(self) -> None:
        state = compute_moon(datetime(2026, 8, 13, 12, 0, tzinfo=timezone.utc), 35.7, 139.7)

        self.assertGreaterEqual(state.illumination, 0.0)
        self.assertLessEqual(state.illumination, 1.0)
        self.assertGreaterEqual(state.phase_angle_deg, 0.0)
        self.assertLessEqual(state.phase_angle_deg, 180.0)

    def test_moon_position_changes_with_time(self) -> None:
        start = datetime(2026, 8, 13, 12, 0, tzinfo=timezone.utc)
        a = compute_moon(start, 35.7, 139.7)
        b = compute_moon(start + timedelta(hours=6), 35.7, 139.7)

        self.assertGreater(abs(a.azimuth_deg - b.azimuth_deg) + abs(a.altitude_deg - b.altitude_deg), 5.0)

    def test_moon_position_changes_with_location(self) -> None:
        dt = datetime(2026, 8, 13, 12, 0, tzinfo=timezone.utc)
        tokyo = compute_moon(dt, 35.7, 139.7)
        sydney = compute_moon(dt, -33.9, 151.2)

        self.assertGreater(abs(tokyo.azimuth_deg - sydney.azimuth_deg) + abs(tokyo.altitude_deg - sydney.altitude_deg), 10.0)

    def test_moon_phase_changes_with_day(self) -> None:
        start = datetime(2026, 8, 13, 12, 0, tzinfo=timezone.utc)
        a = compute_moon(start, 35.7, 139.7)
        b = compute_moon(start + timedelta(days=7), 35.7, 139.7)

        self.assertGreater(abs(a.illumination - b.illumination), 0.1)
        self.assertTrue(any(tag.startswith("moon_") for tag in moon_tags_from_state(a)))

    def test_moon_visibility_below_horizon(self) -> None:
        start = datetime(2026, 8, 13, 0, 0, tzinfo=timezone.utc)
        states = [compute_moon(start + timedelta(hours=hour), 35.7, 139.7) for hour in range(48)]
        below = next(state for state in states if state.altitude_deg <= 0.0)

        self.assertFalse(below.visible)
        self.assertEqual(moon_light_level(below), 0.0)

    def test_moon_cache(self) -> None:
        controller = MoonController()
        dt = datetime(2026, 8, 13, 12, 0, tzinfo=timezone.utc)

        controller.update(dt, 35.7, 139.7)
        first_state = controller.state
        controller.update(dt + timedelta(seconds=30), 35.7, 139.7)
        self.assertIs(controller.state, first_state)

        controller.update(dt + timedelta(seconds=61), 35.7, 139.7)
        self.assertIsNot(controller.state, first_state)


if __name__ == "__main__":
    unittest.main()
