from __future__ import annotations

import math
import unittest
from datetime import UTC, datetime

from astronomy.time import greenwich_sidereal_time, julian_date, local_sidereal_time
from sky.simulation import SimulationClock


class TimeTests(unittest.TestCase):
    def test_julian_date_known_j2000_value(self) -> None:
        self.assertEqual(julian_date(datetime(2000, 1, 1, 12, 0, tzinfo=UTC)), 2451545.0)

    def test_julian_date_requires_timezone(self) -> None:
        with self.assertRaises(ValueError):
            julian_date(datetime(2000, 1, 1, 12, 0))

    def test_sidereal_time_is_wrapped(self) -> None:
        gst = greenwich_sidereal_time(2451545.0)
        self.assertTrue(0.0 <= gst < math.tau)
        self.assertTrue(math.isclose(gst, math.radians(280.46061837), abs_tol=1e-10))

    def test_local_sidereal_time_applies_east_longitude(self) -> None:
        jd = 2451545.0
        gst = greenwich_sidereal_time(jd)
        lst = local_sidereal_time(jd, math.radians(30.0))
        self.assertTrue(math.isclose((lst - gst) % math.tau, math.radians(30.0), abs_tol=1e-10))

    def test_simulation_clock_datetime_changes(self) -> None:
        clock = SimulationClock(datetime(2026, 8, 10, 21, 0, tzinfo=UTC), running=True, speed=600.0)
        clock.update(1.0)
        self.assertEqual(clock.current_time.minute, 10)
        clock.add_minutes(-10)
        self.assertEqual(clock.current_time.minute, 0)
        clock.add_days(1)
        self.assertEqual(clock.current_time.day, 11)
