from __future__ import annotations

import unittest
from datetime import datetime, timedelta, timezone

from astronomy.observer import Observer
from data.constellations import CONSTELLATIONS
from data.meteor_showers import EVENT_YEAR_END, EVENT_YEAR_START, METEOR_SHOWERS, RECURRING_METEOR_SHOWERS
from sky.meteors import adjacent_meteor_event, adjacent_meteor_event_time, meteor_activity, meteor_radiant_direction


class MeteorTests(unittest.TestCase):
    def _event(self, event_id: str):
        for event in METEOR_SHOWERS:
            if event.id == event_id:
                return event
        raise AssertionError(f"missing event {event_id}")

    def test_event_catalog_covers_20_years_each_side(self) -> None:
        year_count = EVENT_YEAR_END - EVENT_YEAR_START + 1

        self.assertEqual(len(METEOR_SHOWERS), year_count * len(RECURRING_METEOR_SHOWERS))
        self.assertEqual(len(METEOR_SHOWERS), 492)

    def test_perseids_2026_peak_night_is_active(self) -> None:
        event = self._event("PER-2026")
        observation_time = datetime(2026, 8, 13, 2, 0, tzinfo=timezone(timedelta(hours=9)))

        self.assertGreater(meteor_activity(event, observation_time), 0.9)

    def test_perseids_2026_outside_target_night_is_inactive(self) -> None:
        event = self._event("PER-2026")
        observation_time = datetime(2026, 8, 11, 22, 0, tzinfo=timezone(timedelta(hours=9)))

        self.assertEqual(meteor_activity(event, observation_time), 0.0)

    def test_meteor_radiant_direction_is_normalized(self) -> None:
        event = self._event("PER-2026")
        observer = Observer(35.7, 139.7)
        observation_time = datetime(2026, 8, 13, 2, 0, tzinfo=timezone(timedelta(hours=9)))

        direction = meteor_radiant_direction(event, observer, observation_time)

        self.assertAlmostEqual(direction.length(), 1.0)

    def test_adjacent_event_time_uses_registered_peak(self) -> None:
        current_time = datetime(2026, 8, 10, 21, 0, tzinfo=timezone(timedelta(hours=9)))

        event_time = adjacent_meteor_event_time(METEOR_SHOWERS, current_time, 1)

        self.assertEqual(event_time, datetime(2026, 8, 13, 2, 0, tzinfo=current_time.tzinfo))

    def test_adjacent_event_returns_event_metadata(self) -> None:
        current_time = datetime(2026, 8, 10, 21, 0, tzinfo=timezone(timedelta(hours=9)))

        event = adjacent_meteor_event(METEOR_SHOWERS, current_time, 1)

        self.assertIsNotNone(event)
        assert event is not None
        self.assertEqual(event.id, "PER-2026")
        self.assertEqual(event.related_constellation_id, "PER")

    def test_all_events_have_related_constellation_in_catalog(self) -> None:
        constellation_ids = {constellation.id for constellation in CONSTELLATIONS}

        missing = sorted(
            {
                event.related_constellation_id
                for event in METEOR_SHOWERS
                if event.related_constellation_id not in constellation_ids
            }
        )

        self.assertEqual(missing, [])
