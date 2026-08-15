from __future__ import annotations

import json
import math
import os
import random
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(__file__))

import pyxel

if not hasattr(pyxel, "pix") and hasattr(pyxel, "pset"):
    pyxel.pix = pyxel.pset

from src.audio.bgm import install_starwrite_bgm, play_starwrite_bgm, stop_starwrite_bgm
from src.audio.ui_sfx import StarwriteUISfx
from src.astronomy.coordinates import equatorial_to_enu
from src.astronomy.catalog import Constellation
from src.astronomy.events import LunarEclipseEvent, SkyEvent
from src.astronomy.moon import get_phase_name, moon_light_level, moon_state_from_dict, moon_state_to_dict
from src.astronomy.observer import Observer
from src.astronomy.time import julian_date, local_sidereal_time
from src.data.constellations import CONSTELLATIONS
from src.data.sky_events import EVENT_SOURCE_LABEL, SKY_EVENTS
from src.data.sky_features import ASTERISMS, SKY_PATHS, Asterism, SkyPath
from src.data.stars import STARS, STARS_BY_ID, STAR_NAMES
from src.sky.camera import SkyCamera
from src.sky.capture import ScreenPoint, SkyCapture, can_capture, capture_from_dict, capture_to_dict
from src.sky.letters import (
    ExchangeLog,
    PresetLetter,
    append_log,
    load_letters_from_packs,
    log_from_dict,
    log_to_dict,
    match_letter,
)
from src.sky.meteors import (
    active_sky_event,
    adjacent_visible_sky_event,
    event_peak_datetime,
    meteor_radiant_direction,
)
from src.sky.moon import MoonController
from src.sky.renderer import SkyRenderer, moon_direction, moon_screen_point
from src.sky.simulation import SimulationClock, project_visible_stars, star_direction
from src.ui.hud import (
    back_button_rect,
    constellation_label_hit_rects,
    constellation_list_button_rects,
    constellation_list_close_rect,
    constellation_list_max_scroll,
    constellation_list_panel_rect,
    constellation_list_tab_rects,
    constellation_list_view_rect,
    SearchListItem,
    draw_compact_time,
    draw_search_list,
    draw_cut_in,
    draw_event_banner,
    draw_hud,
    draw_constellation_labels,
    draw_focused_star,
    draw_focused_moon,
    draw_letter_view,
    draw_location_badge,
    draw_log_list,
    draw_main_buttons,
    draw_meteor_event,
    draw_menu_button,
    draw_menu_panel,
    draw_setup_restart_confirm,
    draw_rotate_camera_speed_control,
    draw_rotate_speed_control,
    draw_selected_constellation_summary,
    draw_slider,
    draw_sky_features,
    draw_tool_buttons,
    focused_moon_hit_rect,
    focused_star_hit_rect,
    menu_button_rect,
    menu_close_rect,
    setup_restart_confirm_rects,
    log_item_rects,
    letter_close_rect,
    letter_panel_rect,
    letter_view_panel_rect,
    log_panel_rect,
    main_button_rects,
    panel_toggle_rects,
    rotate_camera_speed_control_rects,
    rotate_speed_control_rects,
    set_desktop_letter_text_mode,
    sky_feature_label_hit_rects,
    slider_rects,
    tool_button_rects,
)
from src.ui.localization import (
    constellation_name,
    constellation_sort_key,
    next_language,
    sky_feature_name,
    sky_feature_sort_key,
    star_name,
    star_sort_key,
)

IPHONE16_SCREEN_HEIGHT = 696
IPHONE16_MIN_SCREEN_WIDTH = 396
IPHONE16_MAX_SCREEN_WIDTH = 430
SMARTPHONE_FIRST_SCREEN_SIZE = (IPHONE16_MIN_SCREEN_WIDTH, IPHONE16_SCREEN_HEIGHT)
SETTINGS_KEY = "starwrite_v02_settings"
CAPTURE_KEY = "starwrite_v01_latest_capture"
LETTER_STORE_KEY = "starwrite_v01_letter_store"
CUT_IN_FRAMES = 150
LETTER_RECEIVE_DELAY_MIN_SECONDS = 5.0
LETTER_RECEIVE_DELAY_MAX_SECONDS = 8.0
PYXEL_TARGET_FPS = 30.0
SUMMARY_PANEL_ANIMATION_FRAMES = 24
LETTER_VIEW_ANIMATION_FRAMES = 18
LETTER_VIEW_CLOSE_ANIMATION_FRAMES = 18
STARWRITE_SOUND_RESOURCES = (
    "starwrite.pyxres",
    "./starwrite.pyxres",
    "../starwrite.pyxres",
)
UI_SOUND_CHANNEL = 3
SOUND_RESET = 0
SOUND_LETTER_RECEIVED = 1
SOUND_LETTER_OPEN = 2
SOUND_LETTER_CLOSE = 3
SOUND_TOOL_ON = 4
SOUND_SLIDER_TICK = 5
SOUND_LETTER_RECEIVED_REPEAT_DELAY_FRAMES = CUT_IN_FRAMES // 2
LETTER_UI_SOUND_VOLUME = "4"
STARWRITE_SOUND_FALLBACKS = {
    SOUND_RESET: ("f#2e2d2d3e3f3g3a3", "t" * 8, "4" * 8, "n" * 8, 5),
    SOUND_LETTER_RECEIVED: ("g3d4g4g4g3d4g4g4", "t" * 8, LETTER_UI_SOUND_VOLUME * 8, "n" * 8, 8),
    SOUND_LETTER_OPEN: ("f3f3b3b3f#4f#4", "t" * 6, LETTER_UI_SOUND_VOLUME * 6, "n" * 6, 4),
    SOUND_LETTER_CLOSE: ("f3d3a2d2", "t" * 4, LETTER_UI_SOUND_VOLUME * 4, "n" * 4, 4),
    SOUND_TOOL_ON: ("c4e4", "tt", "44", "nn", 3),
    SOUND_SLIDER_TICK: ("c5g5", "pp", "32", "ff", 3),
}
STAR_TAP_RADIUS_PX = 14
STAR_TAP_MOVE_TOLERANCE_PX = 6


def _screen_size() -> tuple[int, int]:
    try:
        from js import window  # type: ignore

        width = float(window.innerWidth)
        height = float(window.innerHeight)
        is_portrait_phone = width <= 500 and height / max(width, 1.0) >= 1.7
        if is_portrait_phone:
            screen_width = int(round(IPHONE16_SCREEN_HEIGHT * width / max(height, 1.0))) + 2
            screen_width = max(IPHONE16_MIN_SCREEN_WIDTH, min(IPHONE16_MAX_SCREEN_WIDTH, screen_width))
            return (screen_width, IPHONE16_SCREEN_HEIGHT)
    except Exception:
        pass
    return SMARTPHONE_FIRST_SCREEN_SIZE


def _is_desktop_view() -> bool:
    try:
        from js import window  # type: ignore

        width = float(window.innerWidth)
        height = float(window.innerHeight)
        return width >= 700 and height >= 500
    except Exception:
        return False


SCREEN_WIDTH, SCREEN_HEIGHT = _screen_size()
DESKTOP_VIEW = _is_desktop_view()
ROTATE_TIME_SPEEDS = {-3: -3600.0, -2: -1200.0, -1: -300.0, 0: 0.0, 1: 300.0, 2: 1200.0, 3: 3600.0}
ROTATE_CAMERA_SPEEDS = {-3: -24.0, -2: -12.0, -1: -4.0, 0: 0.0, 1: 4.0, 2: 12.0, 3: 24.0}
ROTATION_LIMIT = timedelta(days=365.25 * 20)
CONSTELLATION_SEARCH_DAYS = 3
CONSTELLATION_SEARCH_STEP_MINUTES = 15
CONSTELLATION_AUTO_PAN_FRAMES = int(PYXEL_TARGET_FPS * 1.5)
CONSTELLATION_LIST_DRAG_TOLERANCE_PX = 8


def _storage():
    try:
        from js import window  # type: ignore

        return window.localStorage
    except Exception:
        return None


def _load_json(key: str) -> dict:
    storage = _storage()
    if storage is None:
        return {}
    try:
        raw = storage.getItem(key)
        return json.loads(raw) if raw else {}
    except Exception:
        return {}


def _save_json(key: str, value: dict) -> None:
    storage = _storage()
    if storage is None:
        return
    try:
        storage.setItem(key, json.dumps(value))
    except Exception:
        pass


def _timezone_from_offset(offset_minutes: int) -> timezone:
    return timezone(timedelta(minutes=offset_minutes))


def _coerce_utc_offset(value: object) -> int | None:
    try:
        minutes = int(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
    return max(-720, min(840, minutes))


def _location_utc_offset_minutes(settings: dict) -> int:
    stored = _coerce_utc_offset(settings.get("utc_offset_minutes"))
    if stored is not None:
        return stored

    try:
        longitude = float(settings.get("longitude", 139.7))
    except (TypeError, ValueError):
        longitude = 139.7
    return max(-720, min(840, int(round(longitude / 15.0) * 60)))


def _current_observation_datetime(offset_minutes: int | None = None) -> datetime:
    now = datetime.now().astimezone()
    if offset_minutes is not None:
        now = now.astimezone(_timezone_from_offset(offset_minutes))
    return now.replace(second=0, microsecond=0)


class StarSkyApp:
    def __init__(self, start_pyxel: bool = True) -> None:
        settings = _load_json(SETTINGS_KEY)
        self.location_country = settings.get("location_country")
        self.location_city = settings.get("location_city")
        self.utc_offset_minutes = _location_utc_offset_minutes(settings)
        self.observer = Observer(
            float(settings.get("latitude", 35.7)),
            float(settings.get("longitude", 139.7)),
        )
        self.clock = SimulationClock(_current_observation_datetime(self.utc_offset_minutes))
        self.camera = SkyCamera(
            float(settings.get("yaw", 0.0)),
            float(settings.get("pitch", math.radians(45.0))),
            float(settings.get("fov", 75.0)),
        )
        self.renderer = SkyRenderer()
        self.moon = MoonController()
        self.mode = settings.get("mode", "TONIGHT")
        self.show_info = bool(settings.get("show_info", False))
        self.show_guides = bool(settings.get("show_guides", False))
        self.show_constellations = bool(settings.get("show_constellations", True))
        self.show_features = bool(settings.get("show_features", False))
        self.slider_side = settings.get("slider_side", "right")
        if self.slider_side not in ("left", "right"):
            self.slider_side = "right"
        self.show_time_slider = bool(settings.get("show_time_slider", False))
        self.show_month_slider = bool(settings.get("show_month_slider", False))
        self.show_event_slider = bool(settings.get("show_event_slider", False))
        self.rotate_time = bool(settings.get("rotate_time", False))
        self.rotate_time_speed_level = int(settings.get("rotate_time_speed_level", 2))
        self.rotate_time_speed_level = max(-3, min(3, self.rotate_time_speed_level))
        self.rotate_camera = bool(settings.get("rotate_camera", False))
        self.rotate_camera_speed_level = int(settings.get("rotate_camera_speed_level", 1))
        self.rotate_camera_speed_level = max(-3, min(3, self.rotate_camera_speed_level))
        self.sound_enabled = bool(settings.get("sound_enabled", True))
        self.bgm_enabled = bool(settings.get("bgm_enabled", True))
        language = settings.get("language", "en")
        self.language = language if language in ("en", "ja") else "en"
        self.setup_complete = bool(settings.get("setup_complete", False))
        self.menu_open = False
        self.confirm_setup_restart = False
        self.request_setup_restart = False
        self.ui_state = "SKY"
        self.search_tab = "constellation"
        self.constellation_list_scroll = 0
        self.constellation_list_available_ids: set[str] = set()
        self.constellation_list_pointer_down: tuple[int, int] | None = None
        self.constellation_list_pointer_last: tuple[int, int] | None = None
        self.constellation_list_pointer_dragged = False
        self.constellation_auto_pan: dict[str, object] | None = None
        self.selected_index = int(settings.get("selected_index", 0)) % len(CONSTELLATIONS)
        self.constellation_star_ids = {star_id for constellation in CONSTELLATIONS for star_id in constellation.main_star_ids}
        self.latest_capture = self._load_capture()
        self.letters: tuple[PresetLetter, ...] = ()
        self.letters_by_id: dict[str, PresetLetter] = {}
        self.star_descriptions: dict[int, dict[str, tuple[str, str]]] | None = None
        self.sky_feature_descriptions: dict[str, dict[str, tuple[str, str]]] | None = None
        self._load_info_panel_data()
        letter_store = self._load_letter_store()
        self.exchange_logs: tuple[ExchangeLog, ...] = letter_store["logs"]
        self.seen_letter_ids: set[str] = letter_store["seen_letter_ids"]
        self.unread_log_id: str | None = letter_store["unread_log_id"]
        self._ensure_letters_loaded()
        self.pending_capture: SkyCapture | None = None
        self.pending_letter_id: str | None = None
        self.pending_deliver_frame: int | None = None
        self.selected_log_id: str | None = None
        self.selected_star_id: int | None = None
        self.selected_feature_id: str | None = None
        self.selected_moon = False
        self.summary_panel_animation_start_frame: int | None = None
        self.letter_view_animation_start_frame: int | None = None
        self.letter_view_close_start_frame: int | None = None
        self.letter_view_closing_target_state: str | None = None
        self.cut_in_start_frame: int | None = None
        self.cut_in_message = ""
        self.last_mouse: tuple[int, int] | None = None
        self.sky_pointer_down: tuple[int, int] | None = None
        self.sky_pointer_dragged = False
        self.active_slider: str | None = None
        self.slider_drag_start_y = 0
        self.slider_drag_start_time = self.clock.current_time
        self.slider_last_tick_value: int | None = None
        self.slider_knob_ratio = 0.5
        self.projected = {}
        self.projected_sky_paths: dict[str, list[tuple[float, float] | None]] = {}
        self.meteor_event = None
        self.capture_ready = False
        self.ready_signaled = False
        self.audio_ready = False
        self.ui_sfx = StarwriteUISfx()
        self.bgm_installed = False
        self.bgm_playing = False
        self.scheduled_ui_sounds: list[tuple[int, int]] = []
        self.rotation_anchor_time: datetime | None = None
        self._select_initial_visible_constellation()
        if self.rotate_time:
            self._set_rotate_time(True)
        if self.rotate_camera:
            self._set_rotate_camera(True)

        set_desktop_letter_text_mode(DESKTOP_VIEW)
        if start_pyxel:
            pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Starwrite Sky", fps=30)
            pyxel.mouse(True)
            pyxel.run(self.update, self.draw)

    @property
    def selected_constellation(self):
        return CONSTELLATIONS[self.selected_index]

    def _select_initial_visible_constellation(self) -> None:
        projected = project_visible_stars(
            STARS,
            self.observer,
            self.clock.current_time,
            self.camera,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
        )
        self.projected = projected
        current_score = self._initial_constellation_score(self.selected_constellation, projected)
        if current_score >= 250.0:
            return

        best_index = self.selected_index
        best_score = current_score
        for index, constellation in enumerate(CONSTELLATIONS):
            score = self._initial_constellation_score(constellation, projected)
            if score > best_score:
                best_index = index
                best_score = score
        if best_score < 0.0 or best_index == self.selected_index:
            return
        self.selected_index = best_index
        self.selected_star_id = None
        self.selected_feature_id = None
        self.selected_moon = False

    def _initial_constellation_score(
        self,
        constellation: Constellation,
        projected: dict[int, ScreenPoint],
    ) -> float:
        points = [projected.get(star_id) for star_id in constellation.main_star_ids]
        canvas_points = [
            point
            for point in points
            if point is not None and 0 <= point.x <= SCREEN_WIDTH and 0 <= point.y <= SCREEN_HEIGHT
        ]
        required_points = 1 if len(constellation.main_star_ids) <= 1 else 2
        if len(canvas_points) < required_points:
            return -1.0

        sky_right = SCREEN_WIDTH - 72
        sky_bottom = SCREEN_HEIGHT - 104
        safe_points = [
            point
            for point in canvas_points
            if 12 <= point.x <= sky_right and 12 <= point.y <= sky_bottom
        ]
        if not safe_points:
            return -1.0

        xs = [point.x for point in canvas_points]
        ys = [point.y for point in canvas_points]
        span = max(max(xs) - min(xs), max(ys) - min(ys))
        center_x = sum(point.x for point in canvas_points) / len(canvas_points)
        center_y = sum(point.y for point in canvas_points) / len(canvas_points)
        target_x = (SCREEN_WIDTH - 72) * 0.5
        target_y = (SCREEN_HEIGHT - 104) * 0.5
        center_distance = math.hypot(center_x - target_x, center_y - target_y)

        score = len(canvas_points) * 80.0 + len(safe_points) * 45.0
        score += min(span, 160.0) * 0.7
        score += max(0.0, 260.0 - center_distance)
        if can_capture(constellation, projected, SCREEN_WIDTH, SCREEN_HEIGHT, margin=24, min_span=14.0):
            score += 1000.0
        anchor_id = constellation.anchor_star_id
        if anchor_id is not None:
            anchor = projected.get(anchor_id)
            if anchor in safe_points:
                score += 180.0
            elif anchor in canvas_points:
                score += 80.0
        return score

    def _load_capture(self) -> SkyCapture | None:
        data = _load_json(CAPTURE_KEY)
        if not data:
            return None
        try:
            return capture_from_dict(data)
        except Exception:
            return None

    def _load_letter_store(self) -> dict:
        data = _load_json(LETTER_STORE_KEY)
        if int(data.get("schema_version", 1)) != 1:
            return {"logs": (), "seen_letter_ids": set(), "unread_log_id": None}
        logs = []
        for item in data.get("logs", []):
            try:
                logs.append(log_from_dict(item))
            except Exception:
                continue
        return {
            "logs": tuple(logs[-100:]),
            "seen_letter_ids": {str(value) for value in data.get("seen_letter_ids", [])},
            "unread_log_id": data.get("unread_log_id"),
        }

    def _ensure_letters_loaded(self) -> None:
        if self.letters:
            return
        from src.data.preset_letters import PRESET_LETTER_PACKS

        self.letters = load_letters_from_packs(PRESET_LETTER_PACKS)
        self.letters_by_id = {letter.id: letter for letter in self.letters}

    def _load_info_panel_data(self) -> None:
        from src.data.moon_descriptions import MOON_DESCRIPTIONS, MOON_PHASE_DESCRIPTIONS
        from src.data.sky_feature_descriptions import SKY_FEATURE_DESCRIPTIONS
        from src.data.star_descriptions import STAR_DESCRIPTIONS

        self.star_descriptions = STAR_DESCRIPTIONS
        self.sky_feature_descriptions = SKY_FEATURE_DESCRIPTIONS
        # Keep the moon description module loaded before the first moon tap.
        _ = (MOON_DESCRIPTIONS, MOON_PHASE_DESCRIPTIONS)

    def _star_description_for(self, star_id: int) -> dict[str, tuple[str, str]]:
        if self.star_descriptions is None:
            from src.data.star_descriptions import STAR_DESCRIPTIONS

            self.star_descriptions = STAR_DESCRIPTIONS
        return self.star_descriptions.get(star_id, {})

    def _sky_feature_description_for(self, feature_id: str) -> dict[str, tuple[str, str]]:
        if self.sky_feature_descriptions is None:
            from src.data.sky_feature_descriptions import SKY_FEATURE_DESCRIPTIONS

            self.sky_feature_descriptions = SKY_FEATURE_DESCRIPTIONS
        return self.sky_feature_descriptions.get(feature_id, {})

    def update(self) -> None:
        if self.ready_signaled:
            self._update_bgm()
        self._finish_letter_close_animation()
        if self.ui_state == "SKY":
            if self.constellation_auto_pan is None:
                self.clock.update(1.0 / 30.0)
                self._update_rotate_camera(1.0 / 30.0)
                self._enforce_rotation_limit()
            else:
                self.clock.pause()
        self._update_pending_receive()
        self._update_scheduled_ui_sounds()
        self._handle_keys()
        self._handle_mouse()
        if self.ui_state == "SKY":
            self._update_constellation_auto_pan()
        if self.ui_state != "SKY":
            if pyxel.frame_count % 30 == 0:
                self._save_settings()
            return
        self.moon.update(self.clock.current_time, self.observer.latitude_deg, self.observer.longitude_deg)
        self.projected = project_visible_stars(
            STARS,
            self.observer,
            self.clock.current_time,
            self.camera,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
        )
        self.capture_ready = can_capture(
            self.selected_constellation,
            self.projected,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
        )
        self.meteor_event = active_sky_event(
            SKY_EVENTS,
            self.observer,
            self.clock.current_time,
            self.camera,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
        )
        self.projected_sky_paths = self._project_sky_paths()
        if pyxel.frame_count % 30 == 0:
            self._save_settings()

    def _handle_keys(self) -> None:
        if self.ui_state != "SKY":
            if self._letter_view_is_closing():
                return
            if self._key_pressed("KEY_ESCAPE") or self._key_pressed("KEY_BACKSPACE"):
                self._go_back()
            return
        if self.constellation_auto_pan is not None:
            return
        if pyxel.btnp(pyxel.KEY_H):
            self.show_info = not self.show_info
        if pyxel.btnp(pyxel.KEY_G):
            self.show_guides = not self.show_guides
        if pyxel.btnp(pyxel.KEY_C):
            self.show_constellations = not self.show_constellations
        if pyxel.btnp(pyxel.KEY_SPACE):
            self._set_rotate_time(not self.rotate_time)
        if pyxel.btnp(pyxel.KEY_M):
            self._set_rotate_time(False)
            self._set_rotate_camera(False)
            self.mode = "DATE" if self.mode == "TONIGHT" else "TONIGHT"
            self.clock.speed = 86400.0 if self.mode == "DATE" else 600.0
        if pyxel.btnp(pyxel.KEY_TAB):
            self._select_constellation(-1 if self._shift_pressed() else 1)
        if pyxel.btnp(pyxel.KEY_F):
            self._set_rotate_camera(False)
            self._frame_selected_constellation()
        if pyxel.btnp(pyxel.KEY_RETURN):
            self._capture()

        step = -1 if pyxel.btn(pyxel.KEY_LEFT) else 1 if pyxel.btn(pyxel.KEY_RIGHT) else 0
        if step and pyxel.frame_count % 5 == 0:
            if self.mode == "DATE":
                self.clock.add_days(step)
            else:
                self.clock.add_minutes(step * 10)

        camera_key_active = (
            pyxel.btn(pyxel.KEY_A)
            or pyxel.btn(pyxel.KEY_D)
            or pyxel.btn(pyxel.KEY_W)
            or pyxel.btn(pyxel.KEY_S)
            or pyxel.btnp(pyxel.KEY_Z, 10, 4)
            or pyxel.btnp(pyxel.KEY_X, 10, 4)
        )
        if camera_key_active:
            self._set_rotate_camera(False)
        if pyxel.btn(pyxel.KEY_A):
            self.camera.yaw -= 0.035
        if pyxel.btn(pyxel.KEY_D):
            self.camera.yaw += 0.035
        if pyxel.btn(pyxel.KEY_W):
            self.camera.pitch += 0.025
        if pyxel.btn(pyxel.KEY_S):
            self.camera.pitch -= 0.025
        if pyxel.btnp(pyxel.KEY_Q, 10, 4):
            self._set_longitude(self.observer.longitude_deg - 1.0)
        if pyxel.btnp(pyxel.KEY_E, 10, 4):
            self._set_longitude(self.observer.longitude_deg + 1.0)
        if pyxel.btnp(pyxel.KEY_UP, 10, 4):
            self._set_latitude(self.observer.latitude_deg + 1.0)
        if pyxel.btnp(pyxel.KEY_DOWN, 10, 4):
            self._set_latitude(self.observer.latitude_deg - 1.0)
        if pyxel.btnp(pyxel.KEY_Z, 10, 4):
            self.camera.fov_deg += 2.0
        if pyxel.btnp(pyxel.KEY_X, 10, 4):
            self.camera.fov_deg -= 2.0
        self.camera.clamp()

    def _shift_pressed(self) -> bool:
        key_names = ("KEY_SHIFT", "KEY_LSHIFT", "KEY_RSHIFT")
        return any(hasattr(pyxel, name) and pyxel.btn(getattr(pyxel, name)) for name in key_names)

    def _key_pressed(self, key_name: str) -> bool:
        return hasattr(pyxel, key_name) and pyxel.btnp(getattr(pyxel, key_name))

    def _handle_mouse(self) -> None:
        current = (pyxel.mouse_x, pyxel.mouse_y)
        if self.constellation_auto_pan is not None:
            self._consume_pinch_zoom_delta()
            self.active_slider = None
            self.last_mouse = None
            self.sky_pointer_down = None
            return
        if self.confirm_setup_restart:
            self._consume_pinch_zoom_delta()
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self._handle_setup_restart_confirm_click(current)
            self.active_slider = None
            self.last_mouse = None
            self.sky_pointer_down = None
            return
        if self.ui_state != "SKY":
            self._consume_pinch_zoom_delta()
            if self._letter_view_is_closing():
                self.last_mouse = None
                return
            if self.ui_state == "CONSTELLATION_LIST":
                self._handle_constellation_list_mouse(current)
                self.last_mouse = None
                return
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self._handle_modal_click(current)
            self.last_mouse = None
            return
        if self.active_slider is not None:
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self._update_slider_drag(current[1])
                self.last_mouse = None
                return
            self.active_slider = None
            self.slider_last_tick_value = None
            self.slider_knob_ratio = 0.5
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self._handle_ui_click(current):
            self.last_mouse = None
            self.sky_pointer_down = None
            return
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.sky_pointer_down = current
            self.sky_pointer_dragged = False
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if self.last_mouse is not None:
                dx = current[0] - self.last_mouse[0]
                dy = current[1] - self.last_mouse[1]
                if dx * dx + dy * dy > STAR_TAP_MOVE_TOLERANCE_PX * STAR_TAP_MOVE_TOLERANCE_PX:
                    self.sky_pointer_dragged = True
                    self._set_rotate_camera(False)
                self.camera.yaw -= dx * 0.008
                self.camera.pitch += dy * 0.008
                self.camera.clamp()
            self.last_mouse = current
        else:
            if self.sky_pointer_down is not None and not self.sky_pointer_dragged:
                down_x, down_y = self.sky_pointer_down
                dx = current[0] - down_x
                dy = current[1] - down_y
                if dx * dx + dy * dy <= STAR_TAP_MOVE_TOLERANCE_PX * STAR_TAP_MOVE_TOLERANCE_PX:
                    self._select_constellation_at_point(current)
            self.sky_pointer_down = None
            self.last_mouse = None

        wheel = getattr(pyxel, "mouse_wheel", 0)
        if wheel:
            self.camera.fov_deg -= float(wheel) * 3.0
            self.camera.clamp()
        pinch_delta = self._consume_pinch_zoom_delta()
        if pinch_delta:
            self.camera.fov_deg -= pinch_delta * 0.08
            self.camera.clamp()

    def _handle_ui_click(self, point: tuple[int, int]) -> bool:
        if self.confirm_setup_restart:
            return self._handle_setup_restart_confirm_click(point)
        for key, rect in main_button_rects(SCREEN_WIDTH, SCREEN_HEIGHT).items():
            if not self._point_in_rect(point, rect):
                continue
            if key == "letter":
                self._open_letter()
            elif key == "log":
                self.ui_state = "LOG"
            elif key == "capture":
                self._capture()
            return True
        for key, rect in tool_button_rects(SCREEN_WIDTH, SCREEN_HEIGHT).items():
            if not self._point_in_rect(point, rect):
                continue
            if key == "time":
                next_state = not self.show_time_slider
                self.show_time_slider = next_state
                if self.show_time_slider:
                    self.show_month_slider = False
                    self.show_event_slider = False
                self._play_ui_sound(SOUND_TOOL_ON if next_state else SOUND_LETTER_CLOSE)
            elif key == "month":
                next_state = not self.show_month_slider
                self.show_month_slider = next_state
                if self.show_month_slider:
                    self.show_time_slider = False
                    self.show_event_slider = False
                self._play_ui_sound(SOUND_TOOL_ON if next_state else SOUND_LETTER_CLOSE)
            elif key == "event":
                next_state = not self.show_event_slider
                self.show_event_slider = next_state
                if self.show_event_slider:
                    self.show_time_slider = False
                    self.show_month_slider = False
                self._play_ui_sound(SOUND_TOOL_ON if next_state else SOUND_LETTER_CLOSE)
            elif key == "rotate":
                next_state = not self.rotate_time
                self._set_rotate_time(next_state)
                self._play_ui_sound(SOUND_TOOL_ON if next_state else SOUND_LETTER_CLOSE)
            elif key == "rotate_camera":
                next_state = not self.rotate_camera
                self._set_rotate_camera(next_state)
                self._play_ui_sound(SOUND_TOOL_ON if next_state else SOUND_LETTER_CLOSE)
            elif key == "features":
                next_state = not self.show_features
                self.show_features = next_state
                if not self.show_features:
                    self.selected_feature_id = None
                self._play_ui_sound(SOUND_TOOL_ON if next_state else SOUND_LETTER_CLOSE)
            elif key == "reset":
                self._reset_view()
                self._play_ui_sound(SOUND_RESET)
            elif key == "search":
                self._open_constellation_list()
            return True
        if self._handle_slider_click(point):
            return True
        if self.rotate_time and self._handle_rotate_speed_click(point):
            return True
        if self.rotate_camera and self._handle_rotate_camera_speed_click(point):
            return True
        if self._point_in_rect(point, menu_button_rect(SCREEN_WIDTH, SCREEN_HEIGHT)):
            next_state = not self.menu_open
            self.menu_open = next_state
            self._play_ui_sound(SOUND_TOOL_ON if next_state else SOUND_LETTER_CLOSE)
            return True
        if not self.menu_open:
            return False
        if self._point_in_rect(point, menu_close_rect(SCREEN_WIDTH, SCREEN_HEIGHT)):
            self.menu_open = False
            self._play_ui_sound(SOUND_LETTER_CLOSE)
            return True
        for key, rect in panel_toggle_rects(SCREEN_WIDTH, SCREEN_HEIGHT).items():
            if not self._point_in_rect(point, rect):
                continue
            if key == "info":
                self.show_info = not self.show_info
                self._play_ui_sound(SOUND_TOOL_ON if self.show_info else SOUND_LETTER_CLOSE)
            elif key == "guides":
                self.show_guides = not self.show_guides
                self._play_ui_sound(SOUND_TOOL_ON if self.show_guides else SOUND_LETTER_CLOSE)
            elif key == "constellations":
                self.show_constellations = not self.show_constellations
                self._play_ui_sound(SOUND_TOOL_ON if self.show_constellations else SOUND_LETTER_CLOSE)
            elif key == "side":
                self.slider_side = "left" if self.slider_side == "right" else "right"
                self._play_ui_sound(SOUND_TOOL_ON)
            elif key == "location":
                self.menu_open = False
                self.confirm_setup_restart = True
                self._play_ui_sound(SOUND_TOOL_ON)
            elif key == "language":
                self.language = next_language(self.language)
                self._save_settings()
                self._play_ui_sound(SOUND_TOOL_ON)
            elif key == "sound":
                next_state = not self.sound_enabled
                if not next_state:
                    self._play_ui_sound(SOUND_LETTER_CLOSE)
                self.sound_enabled = next_state
                if not self.sound_enabled:
                    self.scheduled_ui_sounds = []
                else:
                    self._play_ui_sound(SOUND_TOOL_ON)
                self._save_settings()
            elif key == "bgm":
                self.bgm_enabled = not self.bgm_enabled
                self._play_ui_sound(SOUND_TOOL_ON if self.bgm_enabled else SOUND_LETTER_CLOSE)
                if not self.bgm_enabled:
                    self._stop_bgm()
                else:
                    self._play_bgm()
                self._save_settings()
            return True
        if self._point_in_rect(point, self._menu_panel_hit_rect()):
            return True
        self.menu_open = False
        self._play_ui_sound(SOUND_LETTER_CLOSE)
        return True

    def _handle_setup_restart_confirm_click(self, point: tuple[int, int]) -> bool:
        rects = setup_restart_confirm_rects(SCREEN_WIDTH, SCREEN_HEIGHT)
        if self._point_in_rect(point, rects["yes"]):
            self._play_ui_sound(SOUND_TOOL_ON)
            self._request_setup_restart()
            return True
        if self._point_in_rect(point, rects["no"]):
            self.confirm_setup_restart = False
            self._play_ui_sound(SOUND_LETTER_CLOSE)
            return True
        if not self._point_in_rect(point, rects["panel"]):
            self.confirm_setup_restart = False
            self._play_ui_sound(SOUND_LETTER_CLOSE)
            return True
        return True

    def _request_setup_restart(self) -> None:
        self.confirm_setup_restart = False
        self.menu_open = False
        self._save_settings()
        self._stop_bgm()
        self.request_setup_restart = True

    def _handle_slider_click(self, point: tuple[int, int]) -> bool:
        if not (self.show_time_slider or self.show_month_slider or self.show_event_slider):
            return False
        label = "time" if self.show_time_slider else "month" if self.show_month_slider else "event"
        rects = slider_rects(SCREEN_WIDTH, SCREEN_HEIGHT, self.slider_side)
        if self._point_in_rect(point, rects[f"{label}_minus"]):
            self._step_slider(label, 1)
            return True
        if self._point_in_rect(point, rects[f"{label}_plus"]):
            self._step_slider(label, -1)
            return True
        if label == "event" and self._point_in_rect(point, rects["event_panel"]):
            return True
        if label != "event" and self._point_in_rect(point, self._expanded_rect(rects[f"{label}_knob"], 8)):
            self._start_slider_drag(label, point[1])
            return True
        if label != "event" and self._point_in_rect(point, self._expanded_rect(rects[f"{label}_track"], 12)):
            self._start_slider_drag(label, point[1])
            self._update_slider_drag(point[1])
            return True
        panel_rect = rects["event_panel"] if label == "event" else rects["panel"]
        if self._point_in_rect(point, panel_rect):
            return True
        return False

    def _handle_rotate_speed_click(self, point: tuple[int, int]) -> bool:
        rects = rotate_speed_control_rects(SCREEN_WIDTH, SCREEN_HEIGHT)
        if self._point_in_rect(point, rects["down"]):
            self._change_rotate_speed(-1)
            return True
        if self._point_in_rect(point, rects["up"]):
            self._change_rotate_speed(1)
            return True
        return self._point_in_rect(point, rects["panel"])

    def _handle_rotate_camera_speed_click(self, point: tuple[int, int]) -> bool:
        rects = rotate_camera_speed_control_rects(SCREEN_WIDTH, SCREEN_HEIGHT)
        if self._point_in_rect(point, rects["down"]):
            self._change_rotate_camera_speed(-1)
            return True
        if self._point_in_rect(point, rects["up"]):
            self._change_rotate_camera_speed(1)
            return True
        return self._point_in_rect(point, rects["panel"])

    def _handle_modal_click(self, point: tuple[int, int]) -> bool:
        if self._point_in_rect(point, back_button_rect(SCREEN_WIDTH, SCREEN_HEIGHT)):
            self._go_back()
            return True
        if self.ui_state in ("LETTER", "LOG_DETAIL"):
            letter_panel = self._active_letter_panel_rect()
            if self._point_in_rect(point, self._expanded_rect(letter_close_rect(SCREEN_WIDTH, SCREEN_HEIGHT, letter_panel), 6)):
                self._go_back()
                return True
            if not self._point_in_rect(point, letter_panel):
                self._go_back()
                return True
        if self.ui_state == "LOG":
            if not self._point_in_rect(point, log_panel_rect(SCREEN_WIDTH, SCREEN_HEIGHT)):
                self._go_back()
                return True
            visible_logs = tuple(reversed(self.exchange_logs))
            for index, rect in enumerate(log_item_rects(SCREEN_WIDTH, SCREEN_HEIGHT, len(visible_logs))):
                if not self._point_in_rect(point, rect):
                    continue
                if index < len(visible_logs):
                    self.selected_log_id = visible_logs[index].id
                    self.ui_state = "LOG_DETAIL"
                    self._start_letter_view_animation()
                    self._play_ui_sound(SOUND_LETTER_OPEN)
                return True
        return True

    def _open_constellation_list(self) -> None:
        self._set_rotate_time(False)
        self._set_rotate_camera(False)
        self.show_time_slider = False
        self.show_month_slider = False
        self.show_event_slider = False
        self.menu_open = False
        self.search_tab = "constellation"
        self.constellation_list_scroll = 0
        self.constellation_list_available_ids = {
            constellation.id for constellation in CONSTELLATIONS if self._constellation_can_rise(constellation)
        }
        self.constellation_list_pointer_down = None
        self.constellation_list_pointer_last = None
        self.constellation_list_pointer_dragged = False
        self.ui_state = "CONSTELLATION_LIST"
        self._play_ui_sound(SOUND_TOOL_ON)

    def _handle_constellation_list_mouse(self, point: tuple[int, int]) -> None:
        wheel = getattr(pyxel, "mouse_wheel", 0)
        if wheel:
            self._scroll_constellation_list(self.constellation_list_scroll - int(float(wheel) * 42))

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.constellation_list_pointer_down = point
            self.constellation_list_pointer_last = point
            self.constellation_list_pointer_dragged = False
            return

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if self.constellation_list_pointer_last is not None:
                dy = point[1] - self.constellation_list_pointer_last[1]
                if abs(dy) >= 1:
                    self._scroll_constellation_list(self.constellation_list_scroll - dy)
                if self.constellation_list_pointer_down is not None:
                    total_dx = point[0] - self.constellation_list_pointer_down[0]
                    total_dy = point[1] - self.constellation_list_pointer_down[1]
                    if total_dx * total_dx + total_dy * total_dy > CONSTELLATION_LIST_DRAG_TOLERANCE_PX ** 2:
                        self.constellation_list_pointer_dragged = True
                self.constellation_list_pointer_last = point
            return

        if self.constellation_list_pointer_down is not None and not self.constellation_list_pointer_dragged:
            self._handle_constellation_list_tap(point)
        self.constellation_list_pointer_down = None
        self.constellation_list_pointer_last = None
        self.constellation_list_pointer_dragged = False

    def _handle_constellation_list_tap(self, point: tuple[int, int]) -> bool:
        if self._point_in_rect(point, constellation_list_close_rect(SCREEN_WIDTH, SCREEN_HEIGHT)):
            self._go_back()
            return True
        panel = constellation_list_panel_rect(SCREEN_WIDTH, SCREEN_HEIGHT)
        if not self._point_in_rect(point, panel):
            self._go_back()
            return True
        for tab, rect in constellation_list_tab_rects(SCREEN_WIDTH, SCREEN_HEIGHT).items():
            if self._point_in_rect(point, rect):
                if tab != self.search_tab:
                    self.search_tab = tab
                    self.constellation_list_scroll = 0
                    self._play_ui_sound(SOUND_TOOL_ON)
                return True
        view = constellation_list_view_rect(SCREEN_WIDTH, SCREEN_HEIGHT)
        if not self._point_in_rect(point, view):
            return True
        items = self._search_list_items()
        for index, rect in enumerate(
            constellation_list_button_rects(
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
                len(items),
                self.constellation_list_scroll,
            )
        ):
            _x, rect_y, _w, rect_h = rect
            _view_x, view_y, _view_w, view_h = view
            if rect_y < view_y or rect_y + rect_h > view_y + view_h:
                continue
            if not self._point_in_rect(point, rect):
                continue
            item = items[index]
            if not item.available:
                self._play_ui_sound(SOUND_LETTER_CLOSE)
                return True
            if self._start_search_item_auto_pan(item):
                self.ui_state = "SKY"
                self._play_selection_sound(self._selection_sound_kind_for_search_tab())
            else:
                self._play_ui_sound(SOUND_LETTER_CLOSE)
            return True
        return True

    def _scroll_constellation_list(self, value: int) -> None:
        max_scroll = constellation_list_max_scroll(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            len(self._search_list_items()),
        )
        self.constellation_list_scroll = max(0, min(max_scroll, int(value)))

    def _search_list_items(self) -> tuple[SearchListItem, ...]:
        if self.search_tab == "star":
            return tuple(
                SearchListItem(
                    f"star:{star_id}",
                    star_name(star_id, STAR_NAMES[star_id], self.language),
                    self.selected_star_id == star_id,
                    self._star_can_rise(STARS_BY_ID[star_id]),
                )
                for star_id in self._search_list_star_ids()
                if star_id in STARS_BY_ID
            )
        if self.search_tab == "group":
            return tuple(
                SearchListItem(
                    f"feature:{feature.id}",
                    sky_feature_name(feature, self.language),
                    self.selected_feature_id == feature.id,
                    self._sky_feature_can_rise(feature),
                )
                for feature in self._search_list_sky_features()
            )
        return tuple(
            SearchListItem(
                f"constellation:{constellation.id}",
                constellation_name(constellation, self.language),
                constellation.id == self.selected_constellation.id,
                self._constellation_can_rise(constellation),
                None,
            )
            for constellation in self._constellation_list_constellations()
        )

    def _search_list_star_ids(self) -> tuple[int, ...]:
        return tuple(sorted(STAR_NAMES, key=lambda star_id: star_sort_key(star_id, STAR_NAMES[star_id], self.language)))

    def _search_list_sky_features(self) -> tuple[Asterism | SkyPath, ...]:
        return tuple(sorted((*ASTERISMS, *SKY_PATHS), key=lambda feature: sky_feature_sort_key(feature, self.language)))

    def _selection_sound_kind_for_search_tab(self) -> str:
        if self.search_tab == "star":
            return "star"
        if self.search_tab == "group":
            return "feature"
        return "constellation"

    def _start_search_item_auto_pan(self, item: SearchListItem) -> bool:
        kind, _sep, raw_id = item.id.partition(":")
        if kind == "star":
            try:
                return self._start_star_auto_pan(int(raw_id))
            except ValueError:
                return False
        if kind == "feature":
            return self._start_sky_feature_auto_pan(raw_id)
        source_index = self._constellation_index_by_id(raw_id)
        return source_index is not None and self._start_constellation_auto_pan(source_index)

    def _constellation_list_constellations(self) -> tuple[Constellation, ...]:
        return tuple(sorted(CONSTELLATIONS, key=lambda constellation: constellation_sort_key(constellation, self.language)))

    def _constellation_index_by_id(self, constellation_id: str) -> int | None:
        for index, constellation in enumerate(CONSTELLATIONS):
            if constellation.id == constellation_id:
                return index
        return None

    def _open_letter(self) -> None:
        self._ensure_letters_loaded()
        target_id = self.unread_log_id
        if target_id is None and self.exchange_logs:
            target_id = self.exchange_logs[-1].id
        if target_id is None:
            return
        self.selected_log_id = target_id
        self.ui_state = "LETTER"
        self._start_letter_view_animation()
        self._play_ui_sound(SOUND_LETTER_OPEN)
        if self.unread_log_id == target_id:
            self.unread_log_id = None
            self._save_letter_store()

    def _go_back(self) -> None:
        closing_state = self.ui_state
        if closing_state in ("LETTER", "LOG_DETAIL"):
            self._start_letter_close_animation("LOG" if closing_state == "LOG_DETAIL" else "SKY")
            self._play_ui_sound(SOUND_LETTER_CLOSE)
            return
        self.ui_state = "SKY"
        self.selected_log_id = None
        if closing_state != "SKY":
            self._play_ui_sound(SOUND_LETTER_CLOSE)

    def _start_letter_view_animation(self) -> None:
        self.letter_view_close_start_frame = None
        self.letter_view_closing_target_state = None
        self.letter_view_animation_start_frame = pyxel.frame_count

    def _start_letter_close_animation(self, target_state: str) -> None:
        if self.letter_view_close_start_frame is not None:
            return
        self.letter_view_animation_start_frame = None
        self.letter_view_close_start_frame = pyxel.frame_count
        self.letter_view_closing_target_state = target_state

    def _letter_view_is_closing(self) -> bool:
        return self.letter_view_close_start_frame is not None

    def _finish_letter_close_animation(self) -> None:
        if self.letter_view_close_start_frame is None:
            return
        if pyxel.frame_count - self.letter_view_close_start_frame < LETTER_VIEW_CLOSE_ANIMATION_FRAMES:
            return
        target_state = self.letter_view_closing_target_state or "SKY"
        self.letter_view_close_start_frame = None
        self.letter_view_closing_target_state = None
        self.ui_state = target_state
        if target_state == "SKY":
            self.selected_log_id = None

    def _letter_view_animation_state(self) -> tuple[int | None, int]:
        if self.letter_view_close_start_frame is not None:
            return pyxel.frame_count - self.letter_view_close_start_frame, -1
        if self.letter_view_animation_start_frame is None:
            return None, 1
        age = pyxel.frame_count - self.letter_view_animation_start_frame
        if age >= LETTER_VIEW_ANIMATION_FRAMES:
            self.letter_view_animation_start_frame = None
            return None, 1
        return age, 1

    def _step_slider(self, label: str, direction: int) -> None:
        self._set_rotate_time(False)
        self._set_rotate_camera(False)
        before = self.clock.current_time
        before_tick = self._slider_tick_value(label, before)
        if label == "event":
            changed = self._advance_event(direction)
        elif label == "time":
            self.clock.add_minutes(direction * 15)
            changed = self._slider_tick_value(label, self.clock.current_time) != before_tick
        else:
            self.clock.add_days(direction)
            changed = self.clock.current_time != before
        if changed:
            if label == "event":
                self._play_selection_sound("feature")
                return
            self._play_ui_sound(SOUND_SLIDER_TICK)

    def _start_slider_drag(self, label: str, y: int) -> None:
        self._set_rotate_time(False)
        self._set_rotate_camera(False)
        self.active_slider = label
        self.slider_drag_start_y = y
        self.slider_drag_start_time = self.clock.current_time
        self.slider_last_tick_value = self._slider_tick_value(label, self.clock.current_time)
        self.clock.pause()

    def _set_rotate_time(self, enabled: bool) -> None:
        self.rotate_time = enabled
        if enabled:
            self._ensure_rotation_anchor()
            self.mode = "TONIGHT"
            self.clock.speed = ROTATE_TIME_SPEEDS[self.rotate_time_speed_level]
            self.clock.play()
        else:
            self.clock.pause()
            self._clear_rotation_anchor_if_idle()

    def _change_rotate_speed(self, direction: int) -> None:
        next_level = max(-3, min(3, self.rotate_time_speed_level + direction))
        if next_level == self.rotate_time_speed_level:
            self._play_ui_sound(SOUND_LETTER_CLOSE)
            return
        self.rotate_time_speed_level = next_level
        if self.rotate_time:
            self.clock.speed = ROTATE_TIME_SPEEDS[self.rotate_time_speed_level]
        self._play_ui_sound(SOUND_SLIDER_TICK)

    def _set_rotate_camera(self, enabled: bool) -> None:
        self.rotate_camera = enabled

    def _change_rotate_camera_speed(self, direction: int) -> None:
        next_level = max(-3, min(3, self.rotate_camera_speed_level + direction))
        if next_level == self.rotate_camera_speed_level:
            self._play_ui_sound(SOUND_LETTER_CLOSE)
            return
        self.rotate_camera_speed_level = next_level
        self._play_ui_sound(SOUND_SLIDER_TICK)

    def _update_rotate_camera(self, real_dt: float) -> None:
        if not self.rotate_camera:
            return
        degrees = ROTATE_CAMERA_SPEEDS[self.rotate_camera_speed_level] * real_dt
        if degrees:
            self.camera.yaw = (self.camera.yaw + math.radians(degrees) + math.pi) % (math.tau) - math.pi
            self.camera.clamp()

    def _ensure_rotation_anchor(self) -> None:
        if self.rotation_anchor_time is None:
            self.rotation_anchor_time = self.clock.current_time

    def _clear_rotation_anchor_if_idle(self) -> None:
        if not self.rotate_time:
            self.rotation_anchor_time = None

    def _enforce_rotation_limit(self) -> None:
        if self.rotation_anchor_time is None or not self.rotate_time:
            return
        upper = self.rotation_anchor_time + ROTATION_LIMIT
        lower = self.rotation_anchor_time - ROTATION_LIMIT
        if self.clock.current_time > upper:
            self.clock.current_time = upper
        elif self.clock.current_time < lower:
            self.clock.current_time = lower
        else:
            return
        self.rotate_time = False
        self.clock.pause()
        self.rotation_anchor_time = None

    def _update_slider_drag(self, y: int) -> None:
        if self.active_slider is None:
            return
        rects = slider_rects(SCREEN_WIDTH, SCREEN_HEIGHT, self.slider_side)
        track = rects[f"{self.active_slider}_track"]
        self.slider_knob_ratio = max(0.0, min(1.0, (y - track[1]) / max(1, track[3])))
        delta_y = self.slider_drag_start_y - y
        if self.active_slider == "time":
            minutes = int(delta_y * 720 / max(1, track[3]))
            next_time = self.slider_drag_start_time + timedelta(minutes=minutes)
        else:
            days = int(delta_y * 360 / max(1, track[3]))
            next_time = self.slider_drag_start_time + timedelta(days=days)
        self.clock.current_time = next_time
        tick_value = self._slider_tick_value(self.active_slider, next_time)
        if tick_value != self.slider_last_tick_value:
            self.slider_last_tick_value = tick_value
            self._play_ui_sound(SOUND_SLIDER_TICK)

    def _slider_tick_value(self, label: str, value: datetime) -> int:
        if label == "time":
            return int(value.timestamp() // (60 * 60))
        if label == "event":
            return int(value.timestamp())
        return value.year * 12 + value.month

    def _advance_event(self, direction: int) -> bool:
        self._set_rotate_time(False)
        self._set_rotate_camera(False)
        event_tz = _timezone_from_offset(self.utc_offset_minutes)
        event = adjacent_visible_sky_event(
            SKY_EVENTS,
            self.observer,
            self.clock.current_time,
            direction,
            event_tz,
        )
        if event is None:
            return False
        before = self.clock.current_time
        self.clock.pause()
        self.clock.current_time = event_peak_datetime(event, event_tz)
        self._frame_event(event)
        return self.clock.current_time != before

    def _reset_view(self) -> None:
        self._set_rotate_time(False)
        self._set_rotate_camera(False)
        self.clock.current_time = _current_observation_datetime(self.utc_offset_minutes)
        self.camera.yaw = 0.0
        self.camera.pitch = math.radians(45.0)
        self.camera.fov_deg = 75.0
        self.camera.clamp()
        self.mode = "TONIGHT"
        self.show_time_slider = False
        self.show_month_slider = False
        self.show_event_slider = False
        self.selected_star_id = None
        self.selected_feature_id = None
        self.selected_moon = False

    def _project_sky_paths(self) -> dict[str, list[tuple[float, float] | None]]:
        return self._project_sky_paths_for(self.camera, self.observer, self.clock.current_time)

    def _project_sky_paths_for(
        self,
        camera: SkyCamera,
        observer: Observer,
        observation_time: datetime,
    ) -> dict[str, list[tuple[float, float] | None]]:
        jd = julian_date(observation_time)
        lst = local_sidereal_time(jd, math.radians(observer.longitude_deg))
        lat = math.radians(observer.latitude_deg)
        projected_paths: dict[str, list[tuple[float, float] | None]] = {}
        for path in SKY_PATHS:
            points: list[tuple[float, float] | None] = []
            for ra_rad, dec_rad in path.points:
                direction = equatorial_to_enu(ra_rad, dec_rad, lat, lst)
                if direction.z <= 0.0:
                    points.append(None)
                    continue
                projected = camera.project(direction, SCREEN_WIDTH, SCREEN_HEIGHT)
                if projected is None:
                    points.append(None)
                    continue
                x, y = projected
                if -24 <= x <= SCREEN_WIDTH + 24 and -24 <= y <= SCREEN_HEIGHT + 24:
                    points.append((x, y))
                else:
                    points.append(None)
            projected_paths[path.id] = points
        return projected_paths

    def _menu_panel_hit_rect(self) -> tuple[int, int, int, int]:
        from src.ui.hud import menu_panel_rect

        return menu_panel_rect(SCREEN_WIDTH, SCREEN_HEIGHT)

    def _active_letter_panel_rect(self) -> tuple[int, int, int, int]:
        self._ensure_letters_loaded()
        log = self._selected_log()
        if log is None:
            return letter_panel_rect(SCREEN_WIDTH, SCREEN_HEIGHT)
        letter = self.letters_by_id.get(log.received_letter_id)
        if letter is None:
            return letter_panel_rect(SCREEN_WIDTH, SCREEN_HEIGHT)
        return letter_view_panel_rect(SCREEN_WIDTH, SCREEN_HEIGHT, letter, self.language)

    def _point_in_rect(self, point: tuple[int, int], rect: tuple[int, int, int, int]) -> bool:
        px, py = point
        x, y, w, h = rect
        return x <= px < x + w and y <= py < y + h

    def _point_near_center(self, point: tuple[float, float], radius: int) -> bool:
        dx = point[0] - SCREEN_WIDTH * 0.5
        dy = point[1] - SCREEN_HEIGHT * 0.5
        return dx * dx + dy * dy <= radius * radius

    def _expanded_rect(self, rect: tuple[int, int, int, int], amount: int) -> tuple[int, int, int, int]:
        x, y, w, h = rect
        return (x - amount, y - amount, w + amount * 2, h + amount * 2)

    def _consume_pinch_zoom_delta(self) -> float:
        try:
            from js import window  # type: ignore

            delta = float(getattr(window, "starwritePinchDelta", 0.0))
            window.starwritePinchDelta = 0.0
            return delta
        except Exception:
            return 0.0

    def _set_latitude(self, value: float) -> None:
        self.observer = Observer(max(-90.0, min(90.0, value)), self.observer.longitude_deg)

    def _set_longitude(self, value: float) -> None:
        wrapped = ((value + 180.0) % 360.0) - 180.0
        self.observer = Observer(self.observer.latitude_deg, wrapped)

    def _select_constellation(self, delta: int) -> None:
        self.selected_index = (self.selected_index + delta) % len(CONSTELLATIONS)
        self.selected_star_id = None
        self.selected_feature_id = None
        self.selected_moon = False
        self._play_selection_sound("constellation")

    def _selected_constellation_anchor_label(self) -> str | None:
        star_id = self.selected_constellation.anchor_star_id
        if star_id is None and self.selected_constellation.main_star_ids:
            star_id = self.selected_constellation.main_star_ids[0]
        if star_id is None:
            return None
        english_name = STAR_NAMES.get(star_id)
        if english_name is None:
            return None
        return star_name(star_id, english_name, self.language)

    def _select_constellation_at_point(self, point: tuple[int, int]) -> bool:
        if self._select_focused_star_at_point(point):
            return True
        if self._select_sky_feature_at_point(point):
            return True
        if self._select_focused_moon_at_point(point):
            return True
        if self._select_constellation_label_at_point(point):
            self.selected_star_id = None
            self.selected_feature_id = None
            self.selected_moon = False
            self._play_selection_sound("constellation")
            return True
        star_id = self._nearest_constellation_star_id(point, STAR_TAP_RADIUS_PX)
        if star_id is None:
            return False
        for index, constellation in enumerate(CONSTELLATIONS):
            if star_id in constellation.main_star_ids:
                self.selected_index = index
                self.selected_star_id = None
                self.selected_feature_id = None
                self.selected_moon = False
                self._play_selection_sound("constellation")
                return True
        return False

    def _select_focused_star_at_point(self, point: tuple[int, int]) -> bool:
        focused_star = self._focused_star()
        if focused_star is None:
            return False
        star_id, screen_point = focused_star
        english_name = STAR_NAMES.get(star_id)
        if english_name is None:
            return False
        label = star_name(star_id, english_name, self.language)
        if not self._point_in_rect(point, focused_star_hit_rect(screen_point, label)):
            return False
        self.selected_star_id = star_id
        self.selected_feature_id = None
        self.selected_moon = False
        self._play_selection_sound("star")
        return True

    def _select_focused_moon_at_point(self, point: tuple[int, int]) -> bool:
        if self.moon.state is None:
            return False
        moon_point = moon_screen_point(self.moon.state, self.camera, SCREEN_WIDTH, SCREEN_HEIGHT)
        if moon_point is None or not self._point_near_center(moon_point, 46):
            return False
        if not self._point_in_rect(point, focused_moon_hit_rect(moon_point, self.moon.state, self.language)):
            return False
        self.selected_star_id = None
        self.selected_feature_id = None
        self.selected_moon = True
        self._play_selection_sound("star")
        return True

    def _select_sky_feature_at_point(self, point: tuple[int, int]) -> bool:
        if not self.show_features:
            return False
        for feature_id, rect in sky_feature_label_hit_rects(self.projected, self.projected_sky_paths, self.language):
            if self._point_in_rect(point, rect):
                self.selected_feature_id = feature_id
                self.selected_star_id = None
                self.selected_moon = False
                self._play_selection_sound("feature")
                return True
        return False

    def _selected_star_summary(self) -> tuple[str, tuple[str, str], int] | None:
        if self.selected_star_id is None:
            return None
        star = STARS_BY_ID.get(self.selected_star_id)
        english_name = STAR_NAMES.get(self.selected_star_id)
        if star is None or english_name is None:
            return None
        name = star_name(self.selected_star_id, english_name, self.language)
        description = self._star_description_for(self.selected_star_id)
        description_lines = description.get(self.language)
        if isinstance(description_lines, tuple) and len(description_lines) == 2:
            return (f"STAR  {name.upper() if self.language == 'en' else name}", description_lines, 8)
        constellation = self._constellation_for_star(self.selected_star_id)
        constellation_label = constellation_name(constellation, self.language) if constellation is not None else None
        if self.language == "ja":
            title = f"STAR  {name}"
            line1 = f"明るさ {star.magnitude:.1f}"
            line2 = f"{constellation_label}の星" if constellation_label is not None else "名のある星"
        else:
            title = f"STAR  {name.upper()}"
            line1 = f"magnitude {star.magnitude:.1f}"
            line2 = f"star in {constellation.name}" if constellation is not None else "named star"
        return (title, (line1, line2), 8)

    def _selected_feature_summary(self) -> tuple[str, tuple[str, str], int] | None:
        if self.selected_feature_id is None:
            return None
        feature = self._sky_feature_by_id(self.selected_feature_id)
        if feature is None:
            return None
        descriptions = self._sky_feature_description_for(self.selected_feature_id)
        lines = descriptions.get(self.language)
        if lines is None:
            return None
        title = sky_feature_name(feature, self.language)
        return (title.upper() if self.language == "en" else title, lines, 11)

    def _selected_moon_summary(self) -> tuple[str, tuple[str, str], int] | None:
        if not self.selected_moon or self.moon.state is None:
            return None
        from src.data.moon_descriptions import moon_description, moon_phase_description, moon_phase_title

        phase_key = get_phase_name(self.moon.state.illumination, self.moon.state.waxing)
        return (
            moon_phase_title(phase_key, self.language),
            (moon_description(self.language), moon_phase_description(phase_key, self.language)),
            10,
        )

    def _selected_panel_summary(self) -> tuple[str, tuple[str, str], int] | None:
        return self._selected_star_summary() or self._selected_feature_summary() or self._selected_moon_summary()

    def _clear_detail_selection(self) -> None:
        self.selected_star_id = None
        self.selected_feature_id = None
        self.selected_moon = False

    def _selected_panel_highlight_color(self) -> int:
        summary = self._selected_panel_summary()
        if summary is not None:
            return summary[2]
        return 10

    def _constellation_for_star(self, star_id: int) -> Constellation | None:
        for constellation in CONSTELLATIONS:
            if star_id in constellation.main_star_ids:
                return constellation
        return None

    def _sky_feature_by_id(self, feature_id: str):
        for feature in (*ASTERISMS, *SKY_PATHS):
            if feature.id == feature_id:
                return feature
        return None

    def _select_constellation_label_at_point(self, point: tuple[int, int]) -> bool:
        for index, rect in constellation_label_hit_rects(
            CONSTELLATIONS,
            self.selected_constellation,
            self.projected,
            self.language,
        ):
            if self._point_in_rect(point, rect):
                self.selected_index = index
                return True
        return False

    def _nearest_constellation_star_id(self, point: tuple[int, int], radius: int) -> int | None:
        px, py = point
        best_id: int | None = None
        best_distance = radius * radius
        for star_id, screen_point in self.projected.items():
            if star_id not in self.constellation_star_ids:
                continue
            dx = screen_point.x - px
            dy = screen_point.y - py
            distance = dx * dx + dy * dy
            if distance <= best_distance:
                best_id = star_id
                best_distance = distance
        return best_id

    def _frame_selected_constellation(self) -> None:
        self._frame_constellation(self.selected_constellation)

    def _constellation_can_rise(self, constellation: Constellation) -> bool:
        for star_id in constellation.main_star_ids:
            star = STARS_BY_ID.get(star_id)
            if star is None:
                continue
            if self._star_can_rise(star):
                return True
        return False

    def _star_can_rise(self, star) -> bool:
        declination = math.degrees(star.dec_rad)
        return 90.0 - abs(self.observer.latitude_deg - declination) > 1.0

    def _sky_feature_can_rise(self, feature: Asterism | SkyPath) -> bool:
        if isinstance(feature, Asterism):
            return any(
                star is not None and self._star_can_rise(star)
                for star_id in feature.star_ids
                for star in (STARS_BY_ID.get(star_id),)
            )
        return any(90.0 - abs(self.observer.latitude_deg - math.degrees(dec_rad)) > 1.0 for _ra_rad, dec_rad in feature.points)

    def _start_constellation_auto_pan(self, index: int) -> bool:
        target = self._nearest_constellation_observation_target(CONSTELLATIONS[index])
        if target is None:
            return False
        target_time, target_direction = target
        self.selected_index = index
        self._clear_detail_selection()
        self.summary_panel_animation_start_frame = pyxel.frame_count
        return self._start_direction_auto_pan(target_time, target_direction, max(self.camera.fov_deg, 76.0))

    def _start_star_auto_pan(self, star_id: int) -> bool:
        star = STARS_BY_ID.get(star_id)
        if star is None:
            return False
        target = self._nearest_star_observation_target(star)
        if target is None:
            return False
        target_time, target_direction = target
        constellation = self._constellation_for_star(star_id)
        if constellation is not None:
            source_index = self._constellation_index_by_id(constellation.id)
            if source_index is not None:
                self.selected_index = source_index
        self.selected_star_id = star_id
        self.selected_feature_id = None
        self.selected_moon = False
        self.summary_panel_animation_start_frame = pyxel.frame_count
        return self._start_direction_auto_pan(target_time, target_direction, max(self.camera.fov_deg, 62.0))

    def _start_sky_feature_auto_pan(self, feature_id: str) -> bool:
        feature = self._sky_feature_by_id(feature_id)
        if not isinstance(feature, (Asterism, SkyPath)):
            return False
        target = self._nearest_sky_feature_observation_target(feature)
        if target is None:
            return False
        target_time, target_direction = target
        self.selected_feature_id = feature_id
        self.selected_star_id = None
        self.selected_moon = False
        self.summary_panel_animation_start_frame = pyxel.frame_count
        return self._start_direction_auto_pan(target_time, target_direction, max(self.camera.fov_deg, 78.0))

    def _start_direction_auto_pan(self, target_time: datetime, target_direction, target_fov: float) -> bool:
        target_yaw, target_pitch = self._camera_angles_for_direction(
            target_direction.x,
            target_direction.y,
            target_direction.z,
        )
        self._set_rotate_time(False)
        self._set_rotate_camera(False)
        self.clock.pause()
        self.show_time_slider = False
        self.show_month_slider = False
        self.show_event_slider = False
        self.constellation_auto_pan = {
            "start_frame": pyxel.frame_count,
            "duration": CONSTELLATION_AUTO_PAN_FRAMES,
            "start_time": self.clock.current_time,
            "target_time": target_time,
            "start_yaw": self.camera.yaw,
            "target_yaw": target_yaw,
            "start_pitch": self.camera.pitch,
            "target_pitch": target_pitch,
            "start_fov": self.camera.fov_deg,
            "target_fov": target_fov,
        }
        return True

    def _nearest_constellation_observation_target(self, constellation: Constellation):
        if not self._constellation_can_rise(constellation):
            return None
        thresholds = (0.35, 0.16)
        for threshold in thresholds:
            target = self._first_constellation_target_above(constellation, threshold)
            if target is not None:
                return target
        return self._best_constellation_target(constellation)

    def _first_constellation_target_above(self, constellation: Constellation, threshold: float):
        max_steps = int(CONSTELLATION_SEARCH_DAYS * 24 * 60 / CONSTELLATION_SEARCH_STEP_MINUTES)
        for step in range(max_steps + 1):
            when = self.clock.current_time + timedelta(minutes=step * CONSTELLATION_SEARCH_STEP_MINUTES)
            direction = self._constellation_center_direction_at(constellation, when)
            if direction is not None and direction.z >= threshold:
                return when, direction
        return None

    def _best_constellation_target(self, constellation: Constellation):
        max_steps = int(CONSTELLATION_SEARCH_DAYS * 24 * 60 / CONSTELLATION_SEARCH_STEP_MINUTES)
        best: tuple[datetime, object] | None = None
        best_z = -1.0
        for step in range(max_steps + 1):
            when = self.clock.current_time + timedelta(minutes=step * CONSTELLATION_SEARCH_STEP_MINUTES)
            direction = self._constellation_center_direction_at(constellation, when, relaxed=True)
            if direction is None:
                continue
            if direction.z > best_z:
                best = (when, direction)
                best_z = direction.z
        return best

    def _constellation_center_direction_at(
        self,
        constellation: Constellation,
        observation_time: datetime,
        relaxed: bool = False,
    ):
        directions = []
        for star_id in constellation.main_star_ids:
            star = STARS_BY_ID.get(star_id)
            if star is None:
                continue
            direction = star_direction(star, self.observer, observation_time)
            if direction.z > (0.0 if relaxed else 0.04):
                directions.append(direction)
        required = 1 if relaxed else max(1, min(3, (len(constellation.main_star_ids) + 1) // 2))
        if len(directions) < required:
            return None
        x = sum(direction.x for direction in directions) / len(directions)
        y = sum(direction.y for direction in directions) / len(directions)
        z = sum(direction.z for direction in directions) / len(directions)
        length = math.sqrt(x * x + y * y + z * z)
        if length <= 0.0:
            return None
        from src.sky.vector import Vec3

        return Vec3(x / length, y / length, z / length)

    def _nearest_star_observation_target(self, star):
        if not self._star_can_rise(star):
            return None
        for threshold in (0.35, 0.16, 0.04):
            target = self._first_star_target_above(star, threshold)
            if target is not None:
                return target
        return self._best_star_target(star)

    def _first_star_target_above(self, star, threshold: float):
        max_steps = int(CONSTELLATION_SEARCH_DAYS * 24 * 60 / CONSTELLATION_SEARCH_STEP_MINUTES)
        for step in range(max_steps + 1):
            when = self.clock.current_time + timedelta(minutes=step * CONSTELLATION_SEARCH_STEP_MINUTES)
            direction = star_direction(star, self.observer, when)
            if direction.z >= threshold:
                return when, direction
        return None

    def _best_star_target(self, star):
        max_steps = int(CONSTELLATION_SEARCH_DAYS * 24 * 60 / CONSTELLATION_SEARCH_STEP_MINUTES)
        best: tuple[datetime, object] | None = None
        best_z = -1.0
        for step in range(max_steps + 1):
            when = self.clock.current_time + timedelta(minutes=step * CONSTELLATION_SEARCH_STEP_MINUTES)
            direction = star_direction(star, self.observer, when)
            if direction.z > best_z:
                best = (when, direction)
                best_z = direction.z
        return best if best_z > 0.0 else None

    def _nearest_sky_feature_observation_target(self, feature: Asterism | SkyPath):
        if not self._sky_feature_can_rise(feature):
            return None
        for threshold in (0.35, 0.16):
            target = self._first_sky_feature_target_above(feature, threshold)
            if target is not None:
                return target
        return self._best_sky_feature_target(feature)

    def _first_sky_feature_target_above(self, feature: Asterism | SkyPath, threshold: float):
        max_steps = int(CONSTELLATION_SEARCH_DAYS * 24 * 60 / CONSTELLATION_SEARCH_STEP_MINUTES)
        for step in range(max_steps + 1):
            when = self.clock.current_time + timedelta(minutes=step * CONSTELLATION_SEARCH_STEP_MINUTES)
            direction = self._sky_feature_center_direction_at(feature, when)
            if direction is not None and direction.z >= threshold:
                return when, direction
        return None

    def _best_sky_feature_target(self, feature: Asterism | SkyPath):
        max_steps = int(CONSTELLATION_SEARCH_DAYS * 24 * 60 / CONSTELLATION_SEARCH_STEP_MINUTES)
        best: tuple[datetime, object] | None = None
        best_z = -1.0
        for step in range(max_steps + 1):
            when = self.clock.current_time + timedelta(minutes=step * CONSTELLATION_SEARCH_STEP_MINUTES)
            direction = self._sky_feature_center_direction_at(feature, when, relaxed=True)
            if direction is None:
                continue
            if direction.z > best_z:
                best = (when, direction)
                best_z = direction.z
        return best

    def _sky_feature_center_direction_at(
        self,
        feature: Asterism | SkyPath,
        observation_time: datetime,
        relaxed: bool = False,
    ):
        directions = []
        if isinstance(feature, Asterism):
            for star_id in feature.star_ids:
                star = STARS_BY_ID.get(star_id)
                if star is None:
                    continue
                direction = star_direction(star, self.observer, observation_time)
                if direction.z > (0.0 if relaxed else 0.04):
                    directions.append(direction)
            required = 1 if relaxed else max(1, min(3, (len(feature.star_ids) + 1) // 2))
        else:
            jd = julian_date(observation_time)
            lst = local_sidereal_time(jd, math.radians(self.observer.longitude_deg))
            lat = math.radians(self.observer.latitude_deg)
            for ra_rad, dec_rad in feature.points:
                direction = equatorial_to_enu(ra_rad, dec_rad, lat, lst)
                if direction.z > (0.0 if relaxed else 0.04):
                    directions.append(direction)
            required = 1 if relaxed else 2
        if len(directions) < required:
            return None
        x = sum(direction.x for direction in directions) / len(directions)
        y = sum(direction.y for direction in directions) / len(directions)
        z = sum(direction.z for direction in directions) / len(directions)
        length = math.sqrt(x * x + y * y + z * z)
        if length <= 0.0:
            return None
        from src.sky.vector import Vec3

        return Vec3(x / length, y / length, z / length)

    def _camera_angles_for_direction(self, x: float, y: float, z: float) -> tuple[float, float]:
        length = math.sqrt(x * x + y * y + z * z)
        if length <= 0.0:
            return self.camera.yaw, self.camera.pitch
        return math.atan2(x, y), math.asin(max(-1.0, min(1.0, z / length)))

    def _update_constellation_auto_pan(self) -> None:
        pan = self.constellation_auto_pan
        if pan is None:
            return
        start_frame = int(pan["start_frame"])
        duration = max(1, int(pan["duration"]))
        t = max(0.0, min(1.0, (pyxel.frame_count - start_frame) / duration))
        eased = t * t * (3.0 - 2.0 * t)
        start_time = pan["start_time"]
        target_time = pan["target_time"]
        if isinstance(start_time, datetime) and isinstance(target_time, datetime):
            start_ts = start_time.timestamp()
            target_ts = target_time.timestamp()
            self.clock.current_time = datetime.fromtimestamp(
                start_ts + (target_ts - start_ts) * eased,
                start_time.tzinfo,
            )
        self.camera.yaw = self._lerp_angle(float(pan["start_yaw"]), float(pan["target_yaw"]), eased)
        self.camera.pitch = self._lerp(float(pan["start_pitch"]), float(pan["target_pitch"]), eased)
        self.camera.fov_deg = self._lerp(float(pan["start_fov"]), float(pan["target_fov"]), eased)
        self.camera.clamp()
        if t >= 1.0:
            self.constellation_auto_pan = None

    def _lerp(self, start: float, end: float, t: float) -> float:
        return start + (end - start) * t

    def _lerp_angle(self, start: float, end: float, t: float) -> float:
        delta = (end - start + math.pi) % math.tau - math.pi
        return start + delta * t

    def _frame_constellation(self, constellation: Constellation) -> bool:
        directions = []
        for star_id in constellation.main_star_ids:
            star = STARS_BY_ID.get(star_id)
            if star is None:
                continue
            direction = star_direction(star, self.observer, self.clock.current_time)
            if direction.z > 0:
                directions.append(direction)
        if not directions:
            return False
        x = sum(direction.x for direction in directions) / len(directions)
        y = sum(direction.y for direction in directions) / len(directions)
        z = sum(direction.z for direction in directions) / len(directions)
        return self._frame_direction(x, y, z)

    def _frame_event(self, event: SkyEvent) -> None:
        self._clear_detail_selection()
        if isinstance(event, LunarEclipseEvent):
            self.moon.update(self.clock.current_time, self.observer.latitude_deg, self.observer.longitude_deg)
            if self.moon.state is not None and self.moon.state.visible:
                self.selected_moon = True
                direction = moon_direction(self.moon.state)
                self._frame_direction(direction.x, direction.y, direction.z)
            return
        if event.related_constellation_id is not None:
            for index, constellation in enumerate(CONSTELLATIONS):
                if constellation.id != event.related_constellation_id:
                    continue
                self.selected_index = index
                if self._frame_constellation(constellation):
                    return
                break
        direction = meteor_radiant_direction(event, self.observer, self.clock.current_time)
        self._frame_direction(direction.x, direction.y, direction.z)

    def _frame_direction(self, x: float, y: float, z: float) -> bool:
        length = math.sqrt(x * x + y * y + z * z)
        if length == 0:
            return False
        self.camera.yaw = math.atan2(x, y)
        self.camera.pitch = math.asin(max(-1.0, min(1.0, z / length)))
        self.camera.fov_deg = max(self.camera.fov_deg, 70.0)
        self.camera.clamp()
        return True

    def _capture(self) -> None:
        self._ensure_letters_loaded()
        focused_star = self._focused_star()
        self.latest_capture = SkyCapture(
            schema_version=1,
            captured_at=self.clock.current_time,
            latitude_deg=self.observer.latitude_deg,
            longitude_deg=self.observer.longitude_deg,
            camera_yaw=self.camera.yaw,
            camera_pitch=self.camera.pitch,
            camera_roll=0.0,
            fov_deg=self.camera.fov_deg,
            selected_constellation_id=self.selected_constellation.id,
            selected_star_id=focused_star[0] if focused_star is not None else self.selected_constellation.anchor_star_id,
            selected_feature_id=None,
            selected_event_id=self.meteor_event.event.id if self.meteor_event is not None else None,
            render_seed=pyxel.frame_count,
            moon=moon_state_to_dict(self.moon.state) if self.moon.state is not None else None,
        )
        _save_json(CAPTURE_KEY, capture_to_dict(self.latest_capture))
        if self.pending_deliver_frame is not None:
            return
        recent_ids = tuple(log.received_letter_id for log in self.exchange_logs[-30:])
        letter = match_letter(self.latest_capture, self.letters, self.seen_letter_ids, recent_ids)
        delay_seconds = random.uniform(LETTER_RECEIVE_DELAY_MIN_SECONDS, LETTER_RECEIVE_DELAY_MAX_SECONDS)
        delay_frames = int(delay_seconds * PYXEL_TARGET_FPS)
        self.pending_capture = self.latest_capture
        self.pending_letter_id = letter.id
        self.pending_deliver_frame = pyxel.frame_count + delay_frames
        self.seen_letter_ids.add(letter.id)
        self._save_letter_store()

    def _update_pending_receive(self) -> None:
        if self.pending_deliver_frame is None or pyxel.frame_count < self.pending_deliver_frame:
            return
        if self.pending_capture is None or self.pending_letter_id is None:
            self.pending_deliver_frame = None
            return
        received_at = self.clock.current_time
        log = ExchangeLog(
            id=f"log_{self.pending_letter_id}_{pyxel.frame_count}",
            capture=self.pending_capture,
            received_letter_id=self.pending_letter_id,
            received_at=received_at,
        )
        self.exchange_logs = append_log(self.exchange_logs, log)
        self.unread_log_id = log.id
        self.cut_in_start_frame = pyxel.frame_count
        self.cut_in_message = "なにかとどいたみたい。" if self.language == "ja" else "something arrived."
        self._play_letter_received_sound()
        self.pending_capture = None
        self.pending_letter_id = None
        self.pending_deliver_frame = None
        self._save_letter_store()

    def _setup_audio(self) -> None:
        for resource in STARWRITE_SOUND_RESOURCES:
            try:
                pyxel.load(resource)
                self._setup_audio_fallback_sounds()
                self._install_bgm()
                self._install_selection_sfx()
                self.audio_ready = True
                return
            except Exception:
                continue
        self._setup_audio_fallback_sounds()
        self._install_bgm()
        self._install_selection_sfx()
        self.audio_ready = True

    def _install_selection_sfx(self) -> None:
        try:
            self.ui_sfx.install()
        except Exception:
            pass

    def _install_bgm(self) -> None:
        try:
            install_starwrite_bgm()
            self.bgm_installed = True
        except Exception:
            self.bgm_installed = False

    def _setup_audio_fallback_sounds(self) -> None:
        for sound_id, definition in STARWRITE_SOUND_FALLBACKS.items():
            try:
                notes, tones, volumes, effects, speed = definition
                pyxel.sound(sound_id).set(notes, tones, volumes, effects, speed)
            except Exception:
                continue

    def _play_ui_sound(self, sound_id: int) -> None:
        if not self.sound_enabled:
            return
        if not self.audio_ready:
            self._setup_audio()
        try:
            pyxel.play(UI_SOUND_CHANNEL, sound_id)
        except Exception:
            pass

    def _play_selection_sound(self, kind: str) -> None:
        self.summary_panel_animation_start_frame = pyxel.frame_count
        if not self.sound_enabled:
            return
        if not self.audio_ready:
            self._setup_audio()
        try:
            if kind == "constellation":
                self.ui_sfx.constellation()
            elif kind == "star":
                self.ui_sfx.star()
            elif kind == "feature":
                self.ui_sfx.feature()
        except Exception:
            pass

    def _update_bgm(self) -> None:
        if not self.bgm_enabled:
            if self.bgm_playing:
                self._stop_bgm()
            return
        if not self.audio_ready:
            self._setup_audio()
        if self.bgm_enabled and self.audio_ready and self.bgm_installed and not self.bgm_playing:
            self._play_bgm()

    def _play_bgm(self) -> None:
        if not self.audio_ready or not self.bgm_installed:
            return
        try:
            play_starwrite_bgm(loop=True)
            self.bgm_playing = True
        except Exception:
            self.bgm_playing = False

    def _stop_bgm(self) -> None:
        try:
            stop_starwrite_bgm()
        except Exception:
            pass
        self.bgm_playing = False

    def _play_letter_received_sound(self) -> None:
        if not self.sound_enabled:
            return
        self._play_ui_sound(SOUND_LETTER_RECEIVED)
        self.scheduled_ui_sounds.append(
            (pyxel.frame_count + SOUND_LETTER_RECEIVED_REPEAT_DELAY_FRAMES, SOUND_LETTER_RECEIVED)
        )

    def _update_scheduled_ui_sounds(self) -> None:
        if not self.sound_enabled:
            self.scheduled_ui_sounds = []
            return
        if not self.scheduled_ui_sounds:
            return
        remaining: list[tuple[int, int]] = []
        for play_frame, sound_id in self.scheduled_ui_sounds:
            if pyxel.frame_count >= play_frame:
                self._play_ui_sound(sound_id)
            else:
                remaining.append((play_frame, sound_id))
        self.scheduled_ui_sounds = remaining

    def _save_letter_store(self) -> None:
        _save_json(
            LETTER_STORE_KEY,
            {
                "schema_version": 1,
                "logs": [log_to_dict(log) for log in self.exchange_logs],
                "seen_letter_ids": sorted(self.seen_letter_ids),
                "unread_log_id": self.unread_log_id,
            },
        )

    def _save_settings(self) -> None:
        _save_json(
            SETTINGS_KEY,
            {
                "latitude": self.observer.latitude_deg,
                "longitude": self.observer.longitude_deg,
                "time": self.clock.current_time.isoformat(),
                "yaw": self.camera.yaw,
                "pitch": self.camera.pitch,
                "fov": self.camera.fov_deg,
                "mode": self.mode,
                "selected_index": self.selected_index,
                "show_hud": self.show_info,
                "show_info": self.show_info,
                "show_guides": self.show_guides,
                "show_constellations": self.show_constellations,
                "show_features": self.show_features,
                "slider_side": self.slider_side,
                "show_time_slider": self.show_time_slider,
                "show_month_slider": self.show_month_slider,
                "show_event_slider": self.show_event_slider,
                "rotate_time": self.rotate_time,
                "rotate_time_speed_level": self.rotate_time_speed_level,
                "rotate_camera": self.rotate_camera,
                "rotate_camera_speed_level": self.rotate_camera_speed_level,
                "sound_enabled": self.sound_enabled,
                "bgm_enabled": self.bgm_enabled,
                "language": self.language,
                "location_country": self.location_country,
                "location_city": self.location_city,
                "utc_offset_minutes": self.utc_offset_minutes,
                "setup_complete": self.setup_complete,
            },
        )

    def draw(self) -> None:
        if self.ui_state == "LOG":
            self._ensure_letters_loaded()
            self.renderer.draw(
                self.projected,
                CONSTELLATIONS,
                self.selected_constellation,
                self.show_constellations,
                self.show_guides,
                self.camera,
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
                self.meteor_event,
                self.moon.state,
                self.observer.latitude_deg,
                self.projected_sky_paths,
            )
            draw_log_list(self.exchange_logs, self.letters_by_id)
            self._draw_active_cut_in()
            self._signal_ready()
            return

        if self.ui_state in ("LETTER", "LOG_DETAIL"):
            self._ensure_letters_loaded()
            log = self._selected_log()
            if log is not None:
                self._draw_capture_background(log.capture)
                letter = self.letters_by_id.get(log.received_letter_id)
                if letter is not None:
                    animation_age, animation_direction = self._letter_view_animation_state()
                    draw_letter_view(log, letter, self.language, animation_age, animation_direction)
                self._draw_active_cut_in()
            else:
                self.ui_state = "SKY"
            self._signal_ready()
            return

        if self.ui_state == "CONSTELLATION_LIST":
            self.renderer.draw(
                self.projected,
                CONSTELLATIONS,
                self.selected_constellation,
                self.show_constellations,
                self.show_guides,
                self.camera,
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
                self.meteor_event,
                self.moon.state,
                self.observer.latitude_deg,
                self.projected_sky_paths,
            )
            draw_search_list(self._search_list_items(), self.search_tab, self.language, self.constellation_list_scroll)
            self._draw_active_cut_in()
            self._signal_ready()
            return

        self.renderer.draw(
            self.projected,
            CONSTELLATIONS,
            self.selected_constellation,
            self.show_constellations,
            self.show_guides,
            self.camera,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            self.meteor_event,
            self.moon.state,
            self.observer.latitude_deg,
            self.projected_sky_paths,
        )
        if self.show_info:
            draw_hud(
                self.observer,
                self.clock,
                self.camera,
                self.mode,
                self.selected_constellation,
                self.show_constellations,
                self.capture_ready,
                self.latest_capture,
                self.language,
            )
        else:
            draw_compact_time(self.clock, self.show_month_slider, self.show_time_slider or self.rotate_time)
        draw_constellation_labels(CONSTELLATIONS, self.selected_constellation, self.projected, self.language)
        if self.show_features:
            draw_sky_features(self.projected, self.projected_sky_paths, self.language, moon_light_level(self.moon.state))
        if self.meteor_event is not None:
            draw_meteor_event(self.meteor_event, self.language)
        draw_selected_constellation_summary(
            self.selected_constellation,
            self.language,
            self._selected_constellation_anchor_label(),
            self._selected_panel_summary(),
            self._summary_panel_animation_age(),
            self._selected_panel_highlight_color(),
        )
        if self.meteor_event is not None:
            draw_event_banner(self.meteor_event, self.language)
        focused_star = self._focused_star()
        if focused_star is not None:
            star_id, point = focused_star
            draw_focused_star(point, star_name(star_id, STAR_NAMES[star_id], self.language))
        else:
            moon_point = moon_screen_point(self.moon.state, self.camera, SCREEN_WIDTH, SCREEN_HEIGHT)
            if moon_point is not None and self._point_near_center(moon_point, 46):
                draw_focused_moon(moon_point, self.moon.state, self.language)
        draw_tool_buttons(
            self.show_time_slider,
            self.show_month_slider,
            self.show_event_slider,
            self.rotate_time,
            self.rotate_camera,
            self.show_features,
        )
        if self.rotate_camera:
            draw_rotate_camera_speed_control(self.rotate_camera_speed_level)
        if self.rotate_time:
            draw_rotate_speed_control(self.rotate_time_speed_level)
        if self.show_time_slider:
            draw_slider(self.slider_side, "TIME", self.slider_knob_ratio if self.active_slider == "time" else 0.5)
        if self.show_month_slider:
            draw_slider(self.slider_side, "DAY", self.slider_knob_ratio if self.active_slider == "month" else 0.5, "month")
        if self.show_event_slider:
            draw_slider(self.slider_side, "EVENT", self.slider_knob_ratio if self.active_slider == "event" else 0.5)
        if self.menu_open:
            draw_menu_panel(
                self.show_info,
                self.show_guides,
                self.show_constellations,
                self.sound_enabled,
                self.bgm_enabled,
                self.slider_side,
                EVENT_SOURCE_LABEL,
                len(SKY_EVENTS),
                self.language,
            )
        if not self.menu_open:
            draw_location_badge(self.location_country, self.location_city, self.language)
        draw_menu_button(self.menu_open)
        draw_main_buttons(self.unread_log_id is not None, self.pending_deliver_frame is not None)
        if self.confirm_setup_restart:
            draw_setup_restart_confirm(self.language)
        self._draw_active_cut_in()
        self._signal_ready()

    def _draw_active_cut_in(self) -> None:
        if self.cut_in_start_frame is not None:
            age = pyxel.frame_count - self.cut_in_start_frame
            if age < CUT_IN_FRAMES:
                draw_cut_in(self.cut_in_message, age, CUT_IN_FRAMES)
            else:
                self.cut_in_start_frame = None

    def _summary_panel_animation_age(self) -> int | None:
        if self.summary_panel_animation_start_frame is None:
            return None
        age = pyxel.frame_count - self.summary_panel_animation_start_frame
        if age >= SUMMARY_PANEL_ANIMATION_FRAMES:
            self.summary_panel_animation_start_frame = None
            return None
        return age

    def _draw_capture_background(self, capture: SkyCapture) -> None:
        observer = Observer(capture.latitude_deg, capture.longitude_deg)
        camera = SkyCamera(capture.camera_yaw, capture.camera_pitch, capture.fov_deg)
        projected = project_visible_stars(
            STARS,
            observer,
            capture.captured_at,
            camera,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
        )
        selected_constellation = self._constellation_by_id(capture.selected_constellation_id) or self.selected_constellation
        meteor_event = active_sky_event(SKY_EVENTS, observer, capture.captured_at, camera, SCREEN_WIDTH, SCREEN_HEIGHT)
        projected_sky_paths = self._project_sky_paths_for(camera, observer, capture.captured_at)
        self.renderer.draw(
            projected,
            CONSTELLATIONS,
            selected_constellation,
            self.show_constellations,
            self.show_guides,
            camera,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            meteor_event,
            moon_state_from_dict(capture.moon),
            capture.latitude_deg,
            projected_sky_paths,
        )
        draw_constellation_labels(CONSTELLATIONS, selected_constellation, projected, self.language)
        if meteor_event is not None:
            draw_event_banner(meteor_event, self.language)

    def _constellation_by_id(self, constellation_id: str | None) -> Constellation | None:
        if constellation_id is None:
            return None
        for constellation in CONSTELLATIONS:
            if constellation.id == constellation_id:
                return constellation
        return None

    def _selected_log(self) -> ExchangeLog | None:
        if self.selected_log_id is None:
            return None
        for log in self.exchange_logs:
            if log.id == self.selected_log_id:
                return log
        return None

    def _focused_star(self) -> tuple[int, ScreenPoint] | None:
        center_x = SCREEN_WIDTH * 0.5
        center_y = SCREEN_HEIGHT * 0.5
        best: tuple[int, ScreenPoint] | None = None
        best_distance = 999999.0
        for star_id, point in self.projected.items():
            if star_id not in STAR_NAMES:
                continue
            dx = point.x - center_x
            dy = point.y - center_y
            distance = dx * dx + dy * dy
            if distance < best_distance:
                best = (star_id, point)
                best_distance = distance
        if best is None or best_distance > 42 * 42:
            return None
        return best

    def _signal_ready(self) -> None:
        if self.ready_signaled:
            return
        self.ready_signaled = True
        try:
            from js import CustomEvent, document, window  # type: ignore

            document.body.dataset.starwriteReady = "1"
            window.dispatchEvent(CustomEvent.new("starwrite-ready"))
        except Exception:
            pass


def main() -> None:
    StarSkyApp()


if __name__ == "__main__":
    main()
