from __future__ import annotations

import math
import unittest
from datetime import UTC, datetime, timedelta

from astronomy.coordinates import equatorial_to_enu
from astronomy.observer import Observer
from data.stars import NAMED_STARS
from sky.simulation import star_direction


def _polaris():
    return next(star for star in NAMED_STARS if star.id == 11767)


def _sirius():
    return next(star for star in NAMED_STARS if star.id == 32349)


class CoordinateTests(unittest.TestCase):
    def test_enu_direction_is_normalized(self) -> None:
        direction = equatorial_to_enu(1.0, 0.5, 0.3, 2.0)
        self.assertTrue(math.isclose(direction.length(), 1.0, abs_tol=1e-12))

    def test_equator_star_on_meridian_is_overhead(self) -> None:
        direction = equatorial_to_enu(1.0, 0.0, 0.0, 1.0)
        self.assertGreater(direction.z, 0.999)

    def test_star_below_horizon_after_half_sidereal_day(self) -> None:
        direction = equatorial_to_enu(1.0, 0.0, 0.0, 1.0 + math.pi)
        self.assertLess(direction.z, -0.999)

    def test_polaris_is_roughly_north_from_northern_mid_latitude(self) -> None:
        direction = star_direction(_polaris(), Observer(35.7, 139.7), datetime(2026, 8, 10, 12, 0, tzinfo=UTC))
        self.assertGreater(direction.y, 0.70)
        self.assertGreater(direction.z, 0.40)

    def test_latitude_changes_star_altitude(self) -> None:
        time = datetime(2026, 8, 10, 12, 0, tzinfo=UTC)
        north = star_direction(_polaris(), Observer(35.7, 139.7), time)
        south = star_direction(_polaris(), Observer(-35.7, 139.7), time)
        self.assertGreater(north.z - south.z, 0.8)

    def test_time_change_rotates_stars_and_sidereal_day_returns(self) -> None:
        star = _sirius()
        observer = Observer(35.7, 139.7)
        t0 = datetime(2026, 8, 10, 12, 0, tzinfo=UTC)
        t1 = t0 + timedelta(hours=6)
        ts = t0 + timedelta(hours=23, minutes=56, seconds=4)
        d0 = star_direction(star, observer, t0)
        d1 = star_direction(star, observer, t1)
        ds = star_direction(star, observer, ts)
        self.assertGreater(abs(d0.x - d1.x), 0.005)
        self.assertGreater(d0.dot(ds), 0.999)
