from __future__ import annotations

import math
import unittest
from datetime import datetime, timezone

from sky.capture import SkyCapture, capture_to_dict
from sky.focus_lock import (
    FOCUS_ACQUIRE_FRAMES,
    FocusLockPhase,
    FocusLockState,
    FocusTarget,
    FocusTargetKind,
    acquire_ease,
    all_hidden_below_horizon,
    altitude_deg,
    any_visible_above_horizon,
    mean_direction,
)
from sky.vector import Vec3


class FocusLockTests(unittest.TestCase):
    def test_mean_direction_uses_all_vectors_and_normalizes(self) -> None:
        direction = mean_direction(
            (
                Vec3(1.0, 0.0, 1.0).normalized(),
                Vec3(1.0, 0.0, -1.0).normalized(),
                Vec3(0.0, 1.0, 0.0),
            )
        )
        self.assertIsNotNone(direction)
        assert direction is not None
        self.assertTrue(math.isclose(direction.length(), 1.0, abs_tol=1e-9))
        self.assertGreater(direction.x, 0.0)
        self.assertGreater(direction.y, 0.0)
        self.assertAlmostEqual(direction.z, 0.0, places=9)

    def test_mean_direction_returns_none_for_cancelled_vectors(self) -> None:
        self.assertIsNone(mean_direction((Vec3(1.0, 0.0, 0.0), Vec3(-1.0, 0.0, 0.0))))

    def test_altitude_deg_uses_vector_height(self) -> None:
        self.assertAlmostEqual(altitude_deg(Vec3(0.0, 0.0, 1.0)), 90.0)
        self.assertAlmostEqual(altitude_deg(Vec3(1.0, 0.0, 0.0)), 0.0)
        self.assertAlmostEqual(altitude_deg(Vec3(0.0, 0.0, -1.0)), -90.0)

    def test_horizon_hysteresis_thresholds(self) -> None:
        hidden = Vec3(math.cos(math.radians(-2.0)), 0.0, math.sin(math.radians(-2.0)))
        barely_hidden = Vec3(math.cos(math.radians(-1.0)), 0.0, math.sin(math.radians(-1.0)))
        visible = Vec3(math.cos(math.radians(2.0)), 0.0, math.sin(math.radians(2.0)))
        self.assertTrue(all_hidden_below_horizon((hidden, hidden)))
        self.assertFalse(all_hidden_below_horizon((hidden, barely_hidden)))
        self.assertTrue(any_visible_above_horizon((hidden, visible)))
        self.assertFalse(any_visible_above_horizon((hidden, barely_hidden)))

    def test_acquire_ease_starts_and_finishes_cleanly(self) -> None:
        start = 100
        self.assertEqual(acquire_ease(start, start), 0.0)
        self.assertEqual(acquire_ease(start + FOCUS_ACQUIRE_FRAMES - 1, start), 1.0)
        self.assertLess(acquire_ease(start + 1, start), acquire_ease(start + FOCUS_ACQUIRE_FRAMES // 2, start))

    def test_state_clear_does_not_preserve_target(self) -> None:
        state = FocusLockState(
            phase=FocusLockPhase.TRACKING,
            target=FocusTarget(FocusTargetKind.STAR, 1),
            hidden_frames=4,
            visible_frames=5,
        )
        state.clear()
        self.assertEqual(state.phase, FocusLockPhase.OFF)
        self.assertIsNone(state.target)
        self.assertEqual(state.hidden_frames, 0)
        self.assertEqual(state.visible_frames, 0)

    def test_focus_lock_is_not_serialized_in_capture(self) -> None:
        capture = SkyCapture(
            schema_version=1,
            captured_at=datetime(2026, 8, 17, 12, 0, tzinfo=timezone.utc),
            latitude_deg=35.2,
            longitude_deg=136.9,
            camera_yaw=0.1,
            camera_pitch=0.2,
            camera_roll=0.0,
            fov_deg=75.0,
            selected_constellation_id="ORI",
            selected_star_id=None,
            selected_feature_id=None,
            selected_event_id=None,
            render_seed=42,
        )
        data = capture_to_dict(capture)
        self.assertNotIn("focus_lock", data)
        self.assertNotIn("focus_lock_target", data)


if __name__ == "__main__":
    unittest.main()
