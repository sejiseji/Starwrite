from __future__ import annotations

import sys
import types
import unittest
from unittest.mock import Mock, patch

sys.modules.setdefault("pyxel", types.SimpleNamespace(width=396, height=696))
from src import app_pyxres_sounds as app


class TouchInputRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.window = types.SimpleNamespace(
            starwriteInputCancelSequence=0, starwritePinchActive=False,
            starwritePinchDelta=0, starwritePinchSuppressUntil=0)
        self.pressed = False
        self.down = False
        self.pyxel = types.SimpleNamespace(
            frame_count=1, mouse_x=100, mouse_y=200, mouse_wheel=0,
            MOUSE_BUTTON_LEFT=1, width=396, height=696,
            btn=lambda key: self.down, btnp=lambda key: self.pressed)
        for patcher in (
            patch.object(app, "pyxel", self.pyxel),
            patch.object(app, "_load_json", return_value={}),
            patch.dict(sys.modules, {"js": types.SimpleNamespace(
                window=self.window, Date=types.SimpleNamespace(now=lambda: 1000))}),
        ):
            patcher.start()
            self.addCleanup(patcher.stop)
        self.sky = app.StarSkyApp(start_pyxel=False)
        self.sky.sound_enabled = False
        self.sky.bgm_enabled = False
        self.sky._select_constellation_at_point = Mock(return_value=True)
        self.sky._handle_constellation_list_tap = Mock(return_value=True)
        self.sky._handle_ui_click = Mock(return_value=False)

    def cancel(self):
        self.window.starwriteInputCancelSequence += 1

    def test_cancel_release_does_not_select_pending_sky_tap(self):
        self.sky.sky_pointer_down = (100, 200)
        self.sky.sky_pointer_dragged = False
        self.sky.last_mouse = (100, 200)
        self.cancel()
        self.sky._handle_mouse()
        self.sky._select_constellation_at_point.assert_not_called()
        self.assertIsNone(self.sky.sky_pointer_down)
        self.assertIsNone(self.sky.last_mouse)

    def test_cancel_release_does_not_select_pending_list_tap(self):
        self.sky.ui_state = "CONSTELLATION_LIST"
        self.sky.constellation_list_pointer_down = (100, 200)
        self.sky.constellation_list_pointer_last = (100, 200)
        self.sky.constellation_list_pointer_dragged = False
        self.cancel()
        self.sky._handle_mouse()
        self.sky._handle_constellation_list_tap.assert_not_called()
        self.assertIsNone(self.sky.constellation_list_pointer_down)

    def test_cancel_clears_slider_and_pinch_frame_delay(self):
        self.sky.active_slider = "time"
        self.sky.slider_last_tick_value = 42
        self.sky.slider_knob_ratio = 0.9
        self.sky.pinch_ignore_frames = 4
        self.sky._update_slider_drag = Mock()
        self.down = True
        self.cancel()
        self.sky._handle_mouse()
        self.sky._update_slider_drag.assert_not_called()
        self.assertIsNone(self.sky.active_slider)
        self.assertIsNone(self.sky.slider_last_tick_value)
        self.assertEqual(self.sky.slider_knob_ratio, 0.5)
        self.assertEqual(self.sky.pinch_ignore_frames, 0)

    def test_same_frame_new_ui_press_is_not_discarded(self):
        self.sky.sky_pointer_down = (50, 50)
        self.sky.pinch_ignore_frames = 4
        self.sky._handle_ui_click.return_value = True
        self.cancel()
        self.down = self.pressed = True
        self.sky._handle_mouse()
        self.sky._handle_ui_click.assert_called_once_with((100, 200))
        self.sky._select_constellation_at_point.assert_not_called()

    def test_same_frame_new_sky_press_then_release_selects_once(self):
        self.sky.sky_pointer_down = (50, 50)
        self.cancel()
        self.down = self.pressed = True
        self.sky._handle_mouse()
        self.assertEqual(self.sky.sky_pointer_down, (100, 200))
        self.assertFalse(self.sky.sky_pointer_dragged)
        self.down = self.pressed = False
        self.sky._handle_mouse()
        self.sky._select_constellation_at_point.assert_called_once_with((100, 200))

    def test_same_frame_new_list_press_then_release_selects_once(self):
        self.sky.ui_state = "CONSTELLATION_LIST"
        self.sky.constellation_list_pointer_down = (50, 50)
        self.cancel()
        self.down = self.pressed = True
        self.sky._handle_mouse()
        self.assertEqual(self.sky.constellation_list_pointer_down, (100, 200))
        self.down = self.pressed = False
        self.sky._handle_mouse()
        self.sky._handle_constellation_list_tap.assert_called_once_with((100, 200))

    def test_unchanged_sequence_preserves_normal_sky_tap(self):
        self.down = self.pressed = True
        self.sky._handle_mouse()
        self.down = self.pressed = False
        self.sky._handle_mouse()
        self.sky._select_constellation_at_point.assert_called_once_with((100, 200))

    def test_each_cancellation_is_consumed_once(self):
        self.cancel()
        self.sky._discard_cancelled_pointer()
        self.sky.sky_pointer_down = (111, 222)
        self.sky._discard_cancelled_pointer()
        self.assertEqual(self.sky.sky_pointer_down, (111, 222))
        self.cancel()
        self.sky._discard_cancelled_pointer()
        self.assertIsNone(self.sky.sky_pointer_down)

    def test_live_pinch_still_blocks_new_ui_press_after_cancel(self):
        self.cancel()
        self.window.starwritePinchActive = True
        self.down = self.pressed = True
        self.sky._handle_mouse()
        self.sky._handle_ui_click.assert_not_called()
        self.assertIsNone(self.sky.sky_pointer_down)

    def test_missing_browser_bridge_leaves_pending_input_unchanged(self):
        self.sky.sky_pointer_down = (111, 222)
        with patch.dict(sys.modules, {"js": None}):
            self.sky._discard_cancelled_pointer()
        self.assertEqual(self.sky.sky_pointer_down, (111, 222))


if __name__ == "__main__":
    unittest.main()
