from __future__ import annotations

import json
import math
import os
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(__file__))

import pyxel

from astronomy.catalog import Constellation
from astronomy.events import MeteorShowerEvent
from astronomy.observer import Observer
from data.constellations import CONSTELLATIONS
from data.meteor_showers import EVENT_SOURCE_LABEL, METEOR_SHOWERS
from data.stars import STARS, STARS_BY_ID, STAR_NAMES
from sky.camera import SkyCamera
from sky.capture import ScreenPoint, SkyCapture, can_capture
from sky.meteors import (
    active_meteor_event,
    adjacent_meteor_event,
    meteor_peak_datetime,
    meteor_radiant_direction,
)
from sky.renderer import SkyRenderer
from sky.simulation import SimulationClock, project_visible_stars, star_direction
from ui.hud import (
    begin_display_text_frame,
    draw_compact_time,
    draw_event_banner,
    draw_hud,
    draw_constellation_labels,
    draw_focused_star,
    draw_meteor_event,
    draw_menu_button,
    draw_menu_panel,
    draw_slider,
    draw_tool_buttons,
    menu_button_rect,
    panel_toggle_rects,
    slider_rects,
    tool_button_rects,
)
from ui.localization import next_language, normalize_language, star_name

DESKTOP_SCREEN_SIZE = (480, 360)
IPHONE16_SCREEN_HEIGHT = 696
IPHONE16_MIN_SCREEN_WIDTH = 396
IPHONE16_MAX_SCREEN_WIDTH = 430
SETTINGS_KEY = "starwrite_v02_settings"
CAPTURE_KEY = "starwrite_v01_latest_capture"


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
    return DESKTOP_SCREEN_SIZE


SCREEN_WIDTH, SCREEN_HEIGHT = _screen_size()


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
        self.slider_side = settings.get("slider_side", "right")
        if self.slider_side not in ("left", "right"):
            self.slider_side = "right"
        self.show_time_slider = bool(settings.get("show_time_slider", False))
        self.show_month_slider = bool(settings.get("show_month_slider", False))
        self.show_event_slider = bool(settings.get("show_event_slider", False))
        self.language = normalize_language(settings.get("language", "en"))
        self.menu_open = False
        self.selected_index = int(settings.get("selected_index", 0)) % len(CONSTELLATIONS)
        self.latest_capture = self._load_capture()
        self.last_mouse: tuple[int, int] | None = None
        self.active_slider: str | None = None
        self.slider_drag_start_y = 0
        self.slider_drag_start_time = self.clock.current_time
        self.slider_knob_ratio = 0.5
        self.projected = {}
        self.meteor_event = None
        self.capture_ready = False
        self.ready_signaled = False

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
            return SkyCapture(
                schema_version=int(data["schema_version"]),
                constellation_id=str(data["constellation_id"]),
                anchor_star_id=data.get("anchor_star_id"),
                camera_yaw=float(data["camera_yaw"]),
                camera_pitch=float(data["camera_pitch"]),
                fov_deg=float(data["fov_deg"]),
                observation_time=_aware_datetime(data["observation_time"]),
            )
        except Exception:
            return None

    def update(self) -> None:
        self.clock.update(1.0 / 30.0)
        self._handle_keys()
        self._handle_mouse()
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
        if pyxel.frame_count % 30 == 0:
            self._save_settings()

    def _handle_keys(self) -> None:
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
        if pyxel.btnp(pyxel.KEY_RETURN) and self.capture_ready:
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

    def _handle_mouse(self) -> None:
        current = (pyxel.mouse_x, pyxel.mouse_y)
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

    def _handle_ui_click(self, point: tuple[int, int]) -> bool:
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
        for key, rect in panel_toggle_rects(SCREEN_WIDTH, SCREEN_HEIGHT).items():
            if not self._point_in_rect(point, rect):
                continue
            if key == "info":
                self.show_info = not self.show_info
            elif key == "guides":
                self.show_guides = not self.show_guides
            elif key == "constellations":
                self.show_constellations = not self.show_constellations
            elif key == "side":
                self.slider_side = "left" if self.slider_side == "right" else "right"
            elif key == "language":
                self.language = next_language(self.language)
            return True
        return self._point_in_rect(point, self._menu_panel_hit_rect())

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

    def _menu_panel_hit_rect(self) -> tuple[int, int, int, int]:
        from ui.hud import menu_panel_rect

        return menu_panel_rect(SCREEN_WIDTH, SCREEN_HEIGHT)

    def _point_in_rect(self, point: tuple[int, int], rect: tuple[int, int, int, int]) -> bool:
        px, py = point
        x, y, w, h = rect
        return x <= px < x + w and y <= py < y + h

    def _expanded_rect(self, rect: tuple[int, int, int, int], amount: int) -> tuple[int, int, int, int]:
        x, y, w, h = rect
        return (x - amount, y - amount, w + amount * 2, h + amount * 2)

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
        selected = self.selected_constellation
        self.latest_capture = SkyCapture(
            schema_version=1,
            constellation_id=selected.id,
            anchor_star_id=selected.anchor_star_id,
            camera_yaw=self.camera.yaw,
            camera_pitch=self.camera.pitch,
            fov_deg=self.camera.fov_deg,
            observation_time=self.clock.current_time,
        )
        _save_json(
            CAPTURE_KEY,
            {
                "schema_version": self.latest_capture.schema_version,
                "constellation_id": self.latest_capture.constellation_id,
                "anchor_star_id": self.latest_capture.anchor_star_id,
                "camera_yaw": self.latest_capture.camera_yaw,
                "camera_pitch": self.latest_capture.camera_pitch,
                "fov_deg": self.latest_capture.fov_deg,
                "observation_time": self.latest_capture.observation_time.isoformat(),
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
                "slider_side": self.slider_side,
                "show_time_slider": self.show_time_slider,
                "show_month_slider": self.show_month_slider,
                "show_event_slider": self.show_event_slider,
                "language": self.language,
            },
        )

    def draw(self) -> None:
        begin_display_text_frame()
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
                self.slider_side,
                EVENT_SOURCE_LABEL,
                len(METEOR_SHOWERS),
                self.language,
            )
        draw_menu_button(self.menu_open)
        self._signal_ready()

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
