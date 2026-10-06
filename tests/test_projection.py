from __future__ import annotations

import math
import unittest
from datetime import datetime, timezone

from sky.camera import SkyCamera
from sky.vector import Vec3
from src.data.stars import STARS
from src.astronomy.observer import Observer
from src.sky.simulation import project_visible_stars, star_direction
from src.sky.capture import ScreenPoint


class ProjectionTests(unittest.TestCase):
    def test_batch_projection_matches_single_projection_exactly(self) -> None:
        directions = [Vec3(x, y, z) for x in (-1.0, 0.01, 0.7)
                      for y in (-1.0, 0.0001, 1.0) for z in (-0.8, 0.0, 1.0)]
        for yaw, pitch, fov, width, height in (
            (0.0, 0.0, 75, 396, 696), (2.7, 0.6, 20, 480, 360),
            (-3.0, -math.pi / 2, 120, 430, 696), (10.0, math.pi / 2, 90, 200, 100),
        ):
            camera = SkyCamera(yaw, pitch, fov)
            batch = camera.projection(width, height)
            for direction in directions:
                self.assertEqual(batch.project(direction), camera.project(direction, width, height))

    def test_batch_visible_ids_and_coordinates_match_legacy_projection(self) -> None:
        camera = SkyCamera(0, 0, 75)
        for latitude, longitude, month, yaw, pitch, fov, width, height in (
            (35.7, 139.7, 8, 0.0, 0.6, 75, 396, 696),
            (35.7, 139.7, 8, 1.8, 0.6, 20, 396, 696),
            (-33.9, 151.2, 1, -2.0, -0.4, 120, 430, 696),
            (60.2, 25.0, 12, 3.1, math.pi / 2, 75, 480, 360),
            (0.0, -74.0, 6, 0.5, -math.pi / 2, 90, 396, 696),
            (-90.0, -180.0, 3, 6.0, 0.0, 120, 480, 360),
        ):
            with self.subTest(latitude=latitude, yaw=yaw, fov=fov):
                observer = Observer(latitude, longitude)
                when = datetime(2026, month, 13, 2, tzinfo=timezone.utc)
                # Mutate the same camera to detect stale batch constants.
                camera.yaw, camera.pitch, camera.fov_deg = yaw, pitch, fov
                expected = {}
                for star in STARS:
                    direction = star_direction(star, observer, when)
                    if direction.z <= 0:
                        continue
                    point = camera.project(direction, width, height)
                    if point is not None and -24 <= point[0] <= width + 24 and -24 <= point[1] <= height + 24:
                        expected[star.id] = ScreenPoint(*point, star.magnitude, star.color_index, direction)
                self.assertEqual(project_visible_stars(STARS, observer, when, camera, width, height), expected)

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
