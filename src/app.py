from __future__ import annotations

import json
import math
import os
import random
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(__file__))

import pyxel

from astronomy.coordinates import equatorial_to_enu
from astronomy.catalog import Constellation
from astronomy.events import MeteorShowerEvent
from astronomy.observer import Observer
from astronomy.time import julian_date, local_sidereal_time
from data.constellations import CONSTELLATIONS
from data.meteor_showers import EVENT_SOURCE_LABEL, METEOR_SHOWERS
from data.preset_letters import PRESET_LETTER_PACKS
from data.sky_features import SKY_PATHS
from data.stars import STARS, STARS_BY_ID, STAR_NAMES
from sky.camera import SkyCamera
from sky.capture import ScreenPoint, SkyCapture, can_capture, capture_from_dict, capture_to_dict
from sky.letters import (
    ExchangeLog,
    PresetLetter,
    append_log,
    load_letters_from_packs,
    log_from_dict,
    log_to_dict,
    match_letter,
)
from sky.meteors import (
    active_meteor_event,
    adjacent_meteor_event,
    meteor_peak_datetime,
    meteor_radiant_direction,
)
from sky.renderer import SkyRenderer
from sky.simulation import SimulationClock, project_visible_stars, star_direction
from ui.hud import (
    back_button_rect,
    draw_compact_time,
    draw_cut_in,
    draw_event_banner,
    draw_hud,
    draw_constellation_labels,
    draw_focused_star,
    draw_letter_view,
    draw_log_list,
    draw_main_buttons,
    draw_meteor_event,
    draw_menu_button,
    draw_menu_panel,
    draw_slider,
    draw_sky_features,
    draw_tool_buttons,
    menu_button_rect,
    menu_close_rect,
    log_item_rects,
    letter_close_rect,
    letter_panel_rect,
    letter_view_panel_rect,
    log_panel_rect,
    main_button_rects,
    panel_toggle_rects,
    set_desktop_letter_text_mode,
    slider_rects,
    tool_button_rects,
)
from ui.localization import next_language, normalize_language, star_name

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


def _aware_datetime(value: str | None) -> datetime:
    if value:
        try:
            parsed = datetime.fromisoformat(value)
            if parsed.tzinfo is not None:
                return parsed
        except ValueError:
            pass
    return datetime(2026, 8, 10, 21, 0, tzinfo=timezone(timedelta(hours=9)))


class StarSkyApp:
    def __init__(self) -> None:
        settings = _load_json(SETTINGS_KEY)
        self.observer = Observer(
            float(settings.get("latitude", 35.7)),
            float(settings.get("longitude", 139.7)),
        )
        self.clock = SimulationClock(_aware_datetime(settings.get("time")))
        self.camera = SkyCamera(
            float(settings.get("yaw", 0.0)),
            float(settings.get("pitch", math.radians(45.0))),
            float(settings.get("fov", 75.0)),
        )
        self.renderer = SkyRenderer()
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
        self.language = normalize_language(settings.get("language", "en"))
        self.menu_open = False
        self.ui_state = "SKY"
        self.selected_index = int(settings.get("selected_index", 0)) % len(CONSTELLATIONS)
        self.latest_capture = self._load_capture()
        self.letters = load_letters_from_packs(PRESET_LETTER_PACKS)
        self.letters_by_id: dict[str, PresetLetter] = {letter.id: letter for letter in self.letters}
        letter_store = self._load_letter_store()
        self.exchange_logs: tuple[ExchangeLog, ...] = letter_store["logs"]
        self.seen_letter_ids: set[str] = letter_store["seen_letter_ids"]
        self.unread_log_id: str | None = letter_store["unread_log_id"]
        self.pending_capture: SkyCapture | None = None
        self.pending_letter_id: str | None = None
        self.pending_deliver_frame: int | None = None
        self.selected_log_id: str | None = None
        self.cut_in_start_frame: int | None = None
        self.cut_in_message = ""
        self.last_mouse: tuple[int, int] | None = None
        self.active_slider: str | None = None
        self.slider_drag_start_y = 0
        self.slider_drag_start_time = self.clock.current_time
        self.slider_knob_ratio = 0.5
        self.projected = {}
        self.projected_sky_paths: dict[str, list[tuple[float, float] | None]] = {}
        self.meteor_event = None
        self.capture_ready = False
        self.ready_signaled = False

        set_desktop_letter_text_mode(DESKTOP_VIEW)
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Starwrite Sky", fps=30)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    @property
    def selected_constellation(self):
        return CONSTELLATIONS[self.selected_index]

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

    def update(self) -> None:
        if self.ui_state == "SKY":
            self.clock.update(1.0 / 30.0)
        self._update_pending_receive()
        self._handle_keys()
        self._handle_mouse()
        if self.ui_state != "SKY":
            if pyxel.frame_count % 30 == 0:
                self._save_settings()
            return
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
        self.meteor_event = active_meteor_event(
            METEOR_SHOWERS,
            self.observer,
            self.clock.current_time,
            self.camera,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
        )
        self.projected_sky_paths = self._project_sky_paths() if self.show_features else {}
        if pyxel.frame_count % 30 == 0:
            self._save_settings()

    def _handle_keys(self) -> None:
        if self.ui_state != "SKY":
            if self._key_pressed("KEY_ESCAPE") or self._key_pressed("KEY_BACKSPACE"):
                self._go_back()
            return
        if pyxel.btnp(pyxel.KEY_H):
            self.show_info = not self.show_info
        if pyxel.btnp(pyxel.KEY_G):
            self.show_guides = not self.show_guides
        if pyxel.btnp(pyxel.KEY_C):
            self.show_constellations = not self.show_constellations
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.clock.pause() if self.clock.running else self.clock.play()
        if pyxel.btnp(pyxel.KEY_M):
            self.mode = "DATE" if self.mode == "TONIGHT" else "TONIGHT"
            self.clock.speed = 86400.0 if self.mode == "DATE" else 600.0
        if pyxel.btnp(pyxel.KEY_TAB):
            self._select_constellation(-1 if self._shift_pressed() else 1)
        if pyxel.btnp(pyxel.KEY_F):
            self._frame_selected_constellation()
        if pyxel.btnp(pyxel.KEY_RETURN):
            self._capture()

        step = -1 if pyxel.btn(pyxel.KEY_LEFT) else 1 if pyxel.btn(pyxel.KEY_RIGHT) else 0
        if step and pyxel.frame_count % 5 == 0:
            if self.mode == "DATE":
                self.clock.add_days(step)
            else:
                self.clock.add_minutes(step * 10)

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
        if self.ui_state != "SKY":
            self._consume_pinch_zoom_delta()
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
            self.slider_knob_ratio = 0.5
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self._handle_ui_click(current):
            self.last_mouse = None
            return
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if self.last_mouse is not None:
                dx = current[0] - self.last_mouse[0]
                dy = current[1] - self.last_mouse[1]
                self.camera.yaw -= dx * 0.008
                self.camera.pitch += dy * 0.008
                self.camera.clamp()
            self.last_mouse = current
        else:
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
                self.show_time_slider = not self.show_time_slider
                if self.show_time_slider:
                    self.show_month_slider = False
                    self.show_event_slider = False
            elif key == "month":
                self.show_month_slider = not self.show_month_slider
                if self.show_month_slider:
                    self.show_time_slider = False
                    self.show_event_slider = False
            elif key == "event":
                self.show_event_slider = not self.show_event_slider
                if self.show_event_slider:
                    self.show_time_slider = False
                    self.show_month_slider = False
            elif key == "reset":
                self._reset_view()
            return True
        if self._handle_slider_click(point):
            return True
        if self._point_in_rect(point, menu_button_rect(SCREEN_WIDTH, SCREEN_HEIGHT)):
            self.menu_open = not self.menu_open
            return True
        if not self.menu_open:
            return False
        if self._point_in_rect(point, menu_close_rect(SCREEN_WIDTH, SCREEN_HEIGHT)):
            self.menu_open = False
            return True
        for key, rect in panel_toggle_rects(SCREEN_WIDTH, SCREEN_HEIGHT).items():
            if not self._point_in_rect(point, rect):
                continue
            if key == "info":
                self.show_info = not self.show_info
            elif key == "guides":
                self.show_guides = not self.show_guides
            elif key == "constellations":
                self.show_constellations = not self.show_constellations
            elif key == "features":
                self.show_features = not self.show_features
            elif key == "side":
                self.slider_side = "left" if self.slider_side == "right" else "right"
            elif key == "language":
                self.language = next_language(self.language)
                self._save_settings()
            self.menu_open = False
            return True
        if self._point_in_rect(point, self._menu_panel_hit_rect()):
            return True
        self.menu_open = False
        return True

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
        if label == "event" and self._point_in_rect(point, self._expanded_rect(rects["event_track"], 12)):
            track = rects["event_track"]
            self._advance_event(1 if point[1] <= track[1] + track[3] // 2 else -1)
            return True
        if label == "event" and self._point_in_rect(point, self._expanded_rect(rects["event_knob"], 8)):
            return True
        if self._point_in_rect(point, self._expanded_rect(rects[f"{label}_knob"], 8)):
            self._start_slider_drag(label, point[1])
            return True
        if self._point_in_rect(point, self._expanded_rect(rects[f"{label}_track"], 12)):
            self._start_slider_drag(label, point[1])
            self._update_slider_drag(point[1])
            return True
        if self._point_in_rect(point, rects["panel"]):
            return True
        return False

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
                return True
        return True

    def _open_letter(self) -> None:
        target_id = self.unread_log_id
        if target_id is None and self.exchange_logs:
            target_id = self.exchange_logs[-1].id
        if target_id is None:
            return
        self.selected_log_id = target_id
        self.ui_state = "LETTER"
        if self.unread_log_id == target_id:
            self.unread_log_id = None
            self._save_letter_store()

    def _go_back(self) -> None:
        if self.ui_state == "LOG_DETAIL":
            self.ui_state = "LOG"
            return
        self.ui_state = "SKY"
        self.selected_log_id = None

    def _step_slider(self, label: str, direction: int) -> None:
        if label == "event":
            self._advance_event(direction)
        elif label == "time":
            self.clock.add_minutes(direction * 15)
        else:
            self.clock.add_days(direction)

    def _start_slider_drag(self, label: str, y: int) -> None:
        self.active_slider = label
        self.slider_drag_start_y = y
        self.slider_drag_start_time = self.clock.current_time
        self.clock.pause()

    def _update_slider_drag(self, y: int) -> None:
        if self.active_slider is None:
            return
        rects = slider_rects(SCREEN_WIDTH, SCREEN_HEIGHT, self.slider_side)
        track = rects[f"{self.active_slider}_track"]
        self.slider_knob_ratio = max(0.0, min(1.0, (y - track[1]) / max(1, track[3])))
        delta_y = self.slider_drag_start_y - y
        if self.active_slider == "time":
            minutes = int(delta_y * 720 / max(1, track[3]))
            self.clock.current_time = self.slider_drag_start_time + timedelta(minutes=minutes)
        else:
            days = int(delta_y * 360 / max(1, track[3]))
            self.clock.current_time = self.slider_drag_start_time + timedelta(days=days)

    def _advance_event(self, direction: int) -> None:
        event = adjacent_meteor_event(METEOR_SHOWERS, self.clock.current_time, direction)
        if event is None:
            return
        tz = self.clock.current_time.tzinfo
        if tz is None:
            return
        self.clock.pause()
        self.clock.current_time = meteor_peak_datetime(event, tz)
        self._frame_event(event)

    def _reset_view(self) -> None:
        self.clock.pause()
        self.clock.current_time = datetime(2026, 8, 10, 21, 0, tzinfo=timezone(timedelta(hours=9)))
        self.camera.yaw = 0.0
        self.camera.pitch = math.radians(45.0)
        self.camera.fov_deg = 75.0
        self.camera.clamp()
        self.mode = "TONIGHT"
        self.show_time_slider = False
        self.show_month_slider = False
        self.show_event_slider = False

    def _project_sky_paths(self) -> dict[str, list[tuple[float, float] | None]]:
        jd = julian_date(self.clock.current_time)
        lst = local_sidereal_time(jd, math.radians(self.observer.longitude_deg))
        lat = math.radians(self.observer.latitude_deg)
        projected_paths: dict[str, list[tuple[float, float] | None]] = {}
        for path in SKY_PATHS:
            points: list[tuple[float, float] | None] = []
            for ra_rad, dec_rad in path.points:
                direction = equatorial_to_enu(ra_rad, dec_rad, lat, lst)
                if direction.z <= 0.0:
                    points.append(None)
                    continue
                projected = self.camera.project(direction, SCREEN_WIDTH, SCREEN_HEIGHT)
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
        from ui.hud import menu_panel_rect

        return menu_panel_rect(SCREEN_WIDTH, SCREEN_HEIGHT)

    def _active_letter_panel_rect(self) -> tuple[int, int, int, int]:
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

    def _frame_selected_constellation(self) -> None:
        self._frame_constellation(self.selected_constellation)

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

    def _frame_event(self, event: MeteorShowerEvent) -> None:
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
        self.pending_capture = None
        self.pending_letter_id = None
        self.pending_deliver_frame = None
        self._save_letter_store()

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
                "language": self.language,
            },
        )

    def draw(self) -> None:
        if self.ui_state == "LOG":
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
            )
            draw_log_list(self.exchange_logs, self.letters_by_id)
            self._draw_active_cut_in()
            self._signal_ready()
            return

        if self.ui_state in ("LETTER", "LOG_DETAIL"):
            log = self._selected_log()
            if log is not None:
                self._draw_capture_background(log.capture)
                letter = self.letters_by_id.get(log.received_letter_id)
                if letter is not None:
                    draw_letter_view(log, letter, self.language)
                self._draw_active_cut_in()
            else:
                self.ui_state = "SKY"
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
            draw_compact_time(self.clock)
        if self.meteor_event is not None:
            draw_event_banner(self.meteor_event, self.language)
        draw_constellation_labels(CONSTELLATIONS, self.selected_constellation, self.projected, self.language)
        if self.show_features:
            draw_sky_features(self.projected, self.projected_sky_paths, self.language)
        if self.meteor_event is not None:
            draw_meteor_event(self.meteor_event, self.language)
        focused_star = self._focused_star()
        if focused_star is not None:
            star_id, point = focused_star
            draw_focused_star(point, star_name(star_id, STAR_NAMES[star_id], self.language))
        draw_tool_buttons(self.show_time_slider, self.show_month_slider, self.show_event_slider)
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
                self.show_features,
                self.slider_side,
                EVENT_SOURCE_LABEL,
                len(METEOR_SHOWERS),
                self.language,
            )
        draw_menu_button(self.menu_open)
        draw_main_buttons(self.unread_log_id is not None, self.pending_deliver_frame is not None)
        self._draw_active_cut_in()
        self._signal_ready()

    def _draw_active_cut_in(self) -> None:
        if self.cut_in_start_frame is not None:
            age = pyxel.frame_count - self.cut_in_start_frame
            if age < CUT_IN_FRAMES:
                draw_cut_in(self.cut_in_message, age, CUT_IN_FRAMES)
            else:
                self.cut_in_start_frame = None

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
        meteor_event = active_meteor_event(METEOR_SHOWERS, observer, capture.captured_at, camera, SCREEN_WIDTH, SCREEN_HEIGHT)
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


StarSkyApp()
