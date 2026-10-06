from __future__ import annotations

import json
import sys
import types
import unittest
from dataclasses import replace
from datetime import datetime, timezone
from unittest.mock import Mock, patch

sys.modules.setdefault("pyxel", types.SimpleNamespace(width=396, height=696))

from src import app_pyxres_sounds as app
from src.sky.capture import SkyCapture, capture_to_dict
from src.sky.letters import ExchangeLog, log_to_dict

read_session_settings = app._load_session_settings


class MemoryStorage:
    def __init__(self):
        self.values = {}
        self.writes = []
        self.reject = False

    def getItem(self, key):
        return self.values.get(key)

    def setItem(self, key, value):
        if self.reject:
            raise RuntimeError("Synthetic storage rejection")
        self.writes.append((key, value))
        self.values[key] = value

    def removeItem(self, key):
        raise AssertionError("Reads must not remove saved data")


def sample_capture():
    return SkyCapture(1, datetime(2026, 8, 13, 2, tzinfo=timezone.utc),
                      35.7, 139.7, 0.0, 0.6, 0.0, 75.0, "CYG", None,
                      None, None, 123)


class AppStorageAndCacheTests(unittest.TestCase):
    def setUp(self):
        self.storage = MemoryStorage()
        self.pyxel = types.SimpleNamespace(frame_count=1, width=396, height=696)
        for target, value in (("_storage", lambda: self.storage),
                              ("_load_session_settings", lambda: {}),
                              ("pyxel", self.pyxel)):
            patcher = patch.object(app, target, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def make_app(self):
        return app.StarSkyApp(start_pyxel=False)

    def store(self, key, value):
        self.storage.values[key] = json.dumps(value)

    def test_non_object_json_and_broken_text_are_read_only(self):
        for value in ([], None, 1, "text", True):
            with self.subTest(value=value):
                self.store(app.LETTER_STORE_KEY, value)
                before = dict(self.storage.values)
                self.assertEqual(app._load_json(app.LETTER_STORE_KEY), {})
                self.make_app()
                self.assertEqual(self.storage.values, before)
        self.storage.values[app.LETTER_STORE_KEY] = "{broken"
        self.make_app()
        self.assertEqual(self.storage.values[app.LETTER_STORE_KEY], "{broken")
        self.assertEqual(self.storage.writes, [])

    def test_malformed_store_fields_do_not_block_startup(self):
        for data in ({"schema_version": "broken"}, {"schema_version": None},
                     {"schema_version": []}, {"schema_version": float("inf")},
                     {"logs": None}, {"logs": {}}, {"logs": "wrong"},
                     {"seen_letter_ids": None}, {"seen_letter_ids": {}},
                     {"seen_letter_ids": [[], {}, None, "legacy"]},
                     {"unread_log_id": []}):
            with self.subTest(data=data):
                self.store(app.LETTER_STORE_KEY, data)
                before = dict(self.storage.values)
                self.make_app()
                self.assertEqual(self.storage.values, before)
        self.assertEqual(self.storage.writes, [])

    def test_valid_history_survives_mixed_invalid_logs_and_legacy_ids(self):
        log = ExchangeLog("delivered", sample_capture(), "base_011_024",
                          datetime(2026, 8, 13, 3, tzinfo=timezone.utc))
        raw = {"schema_version": 1, "logs": [None, [], {"bad": True}, log_to_dict(log)],
               "seen_letter_ids": ["base_011_024", "ambiguous_old_pending", None, []],
               "unread_log_id": "delivered"}
        self.store(app.LETTER_STORE_KEY, raw)
        before = dict(self.storage.values)
        sky = self.make_app()
        self.assertEqual(sky.exchange_logs, (log,))
        self.assertEqual(sky.seen_letter_ids, {"base_011_024", "ambiguous_old_pending"})
        self.assertEqual(sky.unread_log_id, "delivered")
        self.assertEqual(self.storage.values, before)
        self.assertEqual(self.storage.writes, [])

    def test_bad_nested_capture_data_is_skipped_without_rewriting(self):
        log = ExchangeLog("good", sample_capture(), "base_011_024", sample_capture().captured_at)
        for changes in ({"camera_yaw": float("nan")}, {"latitude_deg": 100},
                        {"selected_star_id": []}, {"selected_constellation_id": {}},
                        {"moon": []}, {"moon": {"illumination": "bad"}},
                        {"captured_at": "2026-08-13T02:00:00"}):
            with self.subTest(changes=changes):
                bad = capture_to_dict(sample_capture()) | changes
                self.store(app.CAPTURE_KEY, bad)
                invalid_log = log_to_dict(log) | {"id": "bad", "capture": bad}
                self.store(app.LETTER_STORE_KEY, {"logs": [invalid_log, log_to_dict(log)]})
                before = dict(self.storage.values)
                sky = self.make_app()
                self.assertIsNone(sky.latest_capture)
                self.assertEqual(sky.exchange_logs, (log,))
                self.assertEqual(self.storage.values, before)

    def test_legacy_capture_format_is_preserved(self):
        old = {"observation_time": sample_capture().captured_at.isoformat(),
               "camera_yaw": 0.0, "camera_pitch": 0.6, "fov_deg": 75.0,
               "constellation_id": "CYG", "anchor_star_id": 102098}
        self.store(app.CAPTURE_KEY, old)
        sky = self.make_app()
        self.assertEqual(sky.latest_capture.selected_star_id, 102098)
        self.assertEqual(json.loads(self.storage.values[app.CAPTURE_KEY]), old)

    def test_invalid_session_numbers_fall_back_without_storage_writes(self):
        settings = {key: value for key, value in (
            ("latitude", []), ("longitude", float("nan")), ("yaw", float("inf")),
            ("pitch", {}), ("fov", None), ("selected_index", "broken"),
            ("rotate_time_speed_level", []), ("rotate_camera_speed_level", None),
            ("utc_offset_minutes", float("inf")), ("search_scroll_by_tab", {"star": float("inf")}),
            ("location_country", []), ("location_city", {}))}
        with patch.object(app, "_load_session_settings", return_value=settings):
            sky = self.make_app()
        self.assertEqual(sky.observer.latitude_deg, 35.7)
        self.assertEqual(sky.observer.longitude_deg, 139.7)
        self.assertEqual(sky.camera.yaw, 0.0)
        self.assertEqual(self.storage.writes, [])

    def test_session_json_must_be_an_object(self):
        for value in ([], None, 1, "wrong"):
            window = types.SimpleNamespace(**{app.SESSION_SETTINGS_ATTR: json.dumps(value)})
            with patch.dict(sys.modules, {"js": types.SimpleNamespace(window=window)}):
                self.assertEqual(read_session_settings(), {})

    def test_json_save_returns_success_or_failure(self):
        self.assertTrue(app._save_json(app.CAPTURE_KEY, {"value": 1}))
        before = dict(self.storage.values)
        self.storage.reject = True
        self.assertFalse(app._save_json(app.CAPTURE_KEY, {"value": 2}))
        self.assertEqual(self.storage.values, before)
        with patch.object(app, "_storage", return_value=None):
            self.assertFalse(app._save_json(app.CAPTURE_KEY, {}))
            self.assertTrue(app._save_json(app.SETTINGS_KEY, {}))

    def test_save_failure_notice_is_quiet_and_does_not_replace_arrival(self):
        sky = self.make_app()
        self.storage.reject = True
        self.assertFalse(sky._save_letter_store())
        sky.cut_in_start_frame = 1
        sky.cut_in_message = "something arrived."
        with patch.object(app, "draw_cut_in") as draw:
            sky._draw_active_cut_in()
            self.assertEqual(draw.call_args.args[0], "SAVE FAILED")
            self.assertEqual(sky.cut_in_message, "something arrived.")
            self.pyxel.frame_count = 1 + app.CUT_IN_FRAMES
            sky._draw_active_cut_in()
            self.assertIsNone(sky.storage_notice_start_frame)
        self.assertEqual(self.storage.values, {})

    def test_restart_discards_pending_but_does_not_mark_new_id_seen(self):
        sky = self.make_app()
        chosen = sky.letters[0]
        with patch.object(app, "match_letter", return_value=chosen):
            sky._capture()
        self.assertEqual(sky.pending_letter_id, chosen.id)
        self.assertNotIn(chosen.id, sky.seen_letter_ids)
        restarted = self.make_app()
        self.assertIsNone(restarted.pending_letter_id)
        self.assertIsNone(restarted.pending_deliver_frame)
        self.assertNotIn(chosen.id, restarted.seen_letter_ids)
        self.assertNotIn(app.LETTER_STORE_KEY, self.storage.values)

    def test_delivery_marks_seen_once_and_repeat_capture_keeps_pending(self):
        sky = self.make_app()
        with patch.object(app, "match_letter", return_value=sky.letters[0]) as match:
            sky._capture()
            pending = (sky.pending_capture, sky.pending_letter_id, sky.pending_deliver_frame)
            self.pyxel.frame_count += 1
            sky._capture()
            self.assertEqual((sky.pending_capture, sky.pending_letter_id, sky.pending_deliver_frame), pending)
            self.assertEqual(match.call_count, 1)
        self.pyxel.frame_count = sky.pending_deliver_frame
        with patch.object(sky, "_play_letter_received_sound"):
            sky._update_pending_receive()
            sky._update_pending_receive()
        self.assertEqual(len(sky.exchange_logs), 1)
        self.assertIn(pending[1], sky.seen_letter_ids)
        restarted = self.make_app()
        self.assertEqual(restarted.exchange_logs, sky.exchange_logs)
        self.assertEqual(restarted.seen_letter_ids, sky.seen_letter_ids)
        self.assertIsNone(restarted.pending_deliver_frame)

    def test_rejected_delivery_save_keeps_session_log_and_reports_failure(self):
        sky = self.make_app()
        with patch.object(app, "match_letter", return_value=sky.letters[0]):
            sky._capture()
        self.storage.reject = True
        self.pyxel.frame_count = sky.pending_deliver_frame
        with patch.object(sky, "_play_letter_received_sound"):
            sky._update_pending_receive()
            sky._update_pending_receive()
        self.assertEqual(len(sky.exchange_logs), 1)
        self.assertIsNotNone(sky.storage_notice_start_frame)
        self.assertNotIn(app.LETTER_STORE_KEY, self.storage.values)

    def test_background_cache_reuses_geometry_and_invalidates_dimensions_log_and_capture(self):
        sky = self.make_app()
        capture = sample_capture()
        original = app.project_visible_stars
        with patch.object(app, "project_visible_stars", wraps=original) as project:
            first = sky._capture_background_geometry(capture)
            self.assertIs(sky._capture_background_geometry(capture), first)
            sky.selected_log_id = "other-log"
            second = sky._capture_background_geometry(capture)
            self.assertIsNot(second, first)
            with patch.object(app, "SCREEN_WIDTH", 480), patch.object(app, "SCREEN_HEIGHT", 360):
                third = sky._capture_background_geometry(capture)
                self.assertIsNot(third, second)
            fourth = sky._capture_background_geometry(replace(capture, camera_yaw=0.5))
            self.assertIsNot(fourth, third)
            self.assertEqual(project.call_count, 4)

    def test_cached_background_keeps_drawing_every_frame_and_respects_display_flags(self):
        sky = self.make_app()
        capture = sample_capture()
        sky.renderer = types.SimpleNamespace(draw=Mock())
        with patch.object(app, "draw_constellation_labels"), patch.object(app, "draw_event_banner"):
            sky._draw_capture_background(capture)
            cached = sky.capture_background_cache
            sky.show_constellations = False
            sky.language = "ja"
            self.pyxel.frame_count += 1
            sky._draw_capture_background(capture)
        self.assertIs(sky.capture_background_cache, cached)
        self.assertEqual(sky.renderer.draw.call_count, 2)
        self.assertFalse(sky.renderer.draw.call_args.args[3])


if __name__ == "__main__":
    unittest.main()
