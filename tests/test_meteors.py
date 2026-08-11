from __future__ import annotations

import unittest
from datetime import datetime, timedelta, timezone

from astronomy.observer import Observer
from data.meteor_showers import METEOR_SHOWERS
from sky.meteors import meteor_activity, meteor_radiant_direction


class MeteorTests(unittest.TestCase):
    def test_perseids_2026_peak_night_is_active(self) -> None:
        event = METEOR_SHOWERS[0]
        observation_time = datetime(2026, 8, 13, 2, 0, tzinfo=timezone(timedelta(hours=9)))

        self.assertGreater(meteor_activity(event, observation_time), 0.9)

    def test_perseids_2026_outside_target_night_is_inactive(self) -> None:
        event = METEOR_SHOWERS[0]
        observation_time = datetime(2026, 8, 11, 22, 0, tzinfo=timezone(timedelta(hours=9)))

        self.assertEqual(meteor_activity(event, observation_time), 0.0)

    def test_meteor_radiant_direction_is_normalized(self) -> None:
        event = METEOR_SHOWERS[0]
        observer = Observer(35.7, 139.7)
        observation_time = datetime(2026, 8, 13, 2, 0, tzinfo=timezone(timedelta(hours=9)))

        direction = meteor_radiant_direction(event, observer, observation_time)

        self.assertAlmostEqual(direction.length(), 1.0)
