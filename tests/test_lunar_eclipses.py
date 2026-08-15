from __future__ import annotations

import unittest
from datetime import datetime, timedelta, timezone

from astronomy.events import LunarEclipseEvent
from astronomy.observer import Observer
from data.lunar_eclipses import LUNAR_ECLIPSES, LUNAR_ECLIPSE_SOURCE_LABEL
from data.sky_events import EVENT_SOURCE_LABEL, SKY_EVENTS
from sky.meteors import (
    adjacent_visible_sky_event,
    event_peak_datetime,
    lunar_eclipse_activity,
    lunar_eclipse_visible,
)
from ui.localization import sky_event_name


class LunarEclipseTests(unittest.TestCase):
    def _event(self, event_id: str) -> LunarEclipseEvent:
        for event in LUNAR_ECLIPSES:
            if event.id == event_id:
                return event
        raise AssertionError(f"missing event {event_id}")

    def test_lunar_eclipse_catalog_uses_nasa_source_label(self) -> None:
        self.assertEqual(LUNAR_ECLIPSE_SOURCE_LABEL, "NASA")
        self.assertIn("NASA", EVENT_SOURCE_LABEL)
        self.assertEqual(len(LUNAR_ECLIPSES), 59)

    def test_catalog_contains_2026_total_lunar_eclipse(self) -> None:
        event = self._event("TLE-2026-03-03")

        self.assertEqual(event.eclipse_type, "total")
        self.assertEqual(event.name, "Total Lunar Eclipse")
        self.assertAlmostEqual(event.umbral_magnitude, 1.151)
        self.assertEqual(event.totality_minutes, 58)

    def test_lunar_eclipse_peak_datetime_converts_to_city_timezone(self) -> None:
        event = self._event("TLE-2026-03-03")
        jst = timezone(timedelta(hours=9))

        self.assertEqual(event_peak_datetime(event, jst), datetime(2026, 3, 3, 20, 34, 52, tzinfo=jst))

    def test_lunar_eclipse_activity_is_limited_to_event_window(self) -> None:
        event = self._event("TLE-2026-03-03")
        jst = timezone(timedelta(hours=9))

        self.assertGreater(lunar_eclipse_activity(event, datetime(2026, 3, 3, 20, 34, tzinfo=jst)), 0.9)
        self.assertEqual(lunar_eclipse_activity(event, datetime(2026, 3, 4, 2, 0, tzinfo=jst)), 0.0)

    def test_lunar_eclipse_visibility_uses_selected_observer(self) -> None:
        event = self._event("TLE-2026-03-03")
        tokyo = Observer(35.7, 139.7)

        self.assertTrue(lunar_eclipse_visible(event, tokyo))

    def test_adjacent_visible_sky_event_can_return_lunar_eclipse(self) -> None:
        current_time = datetime(2026, 3, 2, 21, 0, tzinfo=timezone(timedelta(hours=9)))
        observer = Observer(35.7, 139.7)

        event = adjacent_visible_sky_event(tuple(LUNAR_ECLIPSES), observer, current_time, 1, current_time.tzinfo)

        self.assertIsNotNone(event)
        assert event is not None
        self.assertEqual(event.id, "TLE-2026-03-03")

    def test_sky_events_include_lunar_eclipses_without_changing_meteor_catalog(self) -> None:
        self.assertGreater(len(SKY_EVENTS), len(LUNAR_ECLIPSES))
        self.assertIn(self._event("TLE-2026-03-03"), SKY_EVENTS)

    def test_lunar_eclipse_name_can_be_japanese(self) -> None:
        total = self._event("TLE-2026-03-03")
        partial = self._event("PLE-2026-08-28")

        self.assertEqual(sky_event_name(total, "ja"), "皆既月食")
        self.assertEqual(sky_event_name(partial, "ja"), "部分月食")
        self.assertEqual(sky_event_name(total, "en"), "Total Lunar Eclipse")


if __name__ == "__main__":
    unittest.main()
