from __future__ import annotations

import math
import unittest

from sky.camera import SkyCamera
from sky.vector import Vec3


class ProjectionTests(unittest.TestCase):
    def test_camera_front_projects_to_screen_center(self) -> None:
        camera = SkyCamera(yaw=0.0, pitch=0.0, fov_deg=90.0)
        point = camera.project(Vec3(0.0, 1.0, 0.0), 200, 100)
        self.assertIsNotNone(point)
        assert point is not None
        self.assertTrue(math.isclose(point[0], 100.0, abs_tol=1e-9))
        self.assertTrue(math.isclose(point[1], 50.0, abs_tol=1e-9))

    def test_camera_back_is_not_projected(self) -> None:
        camera = SkyCamera(yaw=0.0, pitch=0.0, fov_deg=90.0)
        self.assertIsNone(camera.project(Vec3(0.0, -1.0, 0.0), 200, 100))

    def test_yaw_changes_screen_position(self) -> None:
        camera = SkyCamera(yaw=0.0, pitch=0.0, fov_deg=90.0)
        original = camera.project(Vec3(0.4, 1.0, 0.0).normalized(), 200, 100)
        camera.yaw = 0.2
        moved = camera.project(Vec3(0.4, 1.0, 0.0).normalized(), 200, 100)
        self.assertIsNotNone(original)
        self.assertIsNotNone(moved)
        assert original is not None and moved is not None
        self.assertLess(moved[0], original[0])

    def test_fov_changes_apparent_width(self) -> None:
        direction = Vec3(0.4, 1.0, 0.0).normalized()
        narrow = SkyCamera(yaw=0.0, pitch=0.0, fov_deg=45.0).project(direction, 200, 100)
        wide = SkyCamera(yaw=0.0, pitch=0.0, fov_deg=100.0).project(direction, 200, 100)
        self.assertIsNotNone(narrow)
        self.assertIsNotNone(wide)
        assert narrow is not None and wide is not None
        self.assertGreater(abs(narrow[0] - 100.0), abs(wide[0] - 100.0))
