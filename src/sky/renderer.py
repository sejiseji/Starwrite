from __future__ import annotations

import math

import pyxel

from src.astronomy.catalog import Constellation
from src.astronomy.events import MeteorShowerEvent
from src.astronomy.moon import MoonState, moon_light_level
from .camera import SkyCamera
from .capture import ScreenPoint
from .meteors import MeteorEventView
from .vector import Vec3, cross

MILKY_WAY_PATH_ID = "MILKY_WAY"
STAR_WHITE = 7
STAR_BLUE_WHITE = 12
STAR_YELLOW_WHITE = 10
STAR_YELLOW = 9
STAR_ORANGE = 4
STAR_RED = 8
LINE_DIM = 5
LINE_SELECTED = 10
HORIZON = 13
POLARIS_ID = 11767
MOON_RADIUS_PX = 5
BASE_LIMIT_MAG = 6.2
MILKY_WAY_BAND_WIDTH_PX = 58.0
MILKY_WAY_SEGMENT_PARTICLES = 30


def _dim_star_color(color: int) -> int:
    if color in (STAR_BLUE_WHITE, STAR_WHITE):
        return HORIZON
    if color in (STAR_YELLOW_WHITE, STAR_YELLOW):
        return STAR_ORANGE
    return STAR_RED


def star_color(color_index: float | None) -> int:
    if color_index is None:
        return STAR_WHITE
    if color_index < 0.0:
        return STAR_BLUE_WHITE
    if color_index < 0.45:
        return STAR_WHITE
    if color_index < 0.85:
        return STAR_YELLOW_WHITE
    if color_index < 1.25:
        return STAR_YELLOW
    if color_index < 1.65:
        return STAR_ORANGE
    return STAR_RED


def star_radius(magnitude: float) -> int:
    if magnitude < -0.5:
        return 3
    if magnitude < 1.0:
        return 2
    if magnitude < 2.5:
        return 1
    return 0


def twinkle_level(star_id: int, magnitude: float, frame_count: int) -> int:
    period = 600 + star_id % 720
    phase = (frame_count + star_id * 17) % period
    pulse_width = 2 if magnitude < 2.5 else 3
    if phase < pulse_width:
        return 2
    return 1


def moon_direction(state: MoonState) -> Vec3:
    az = math.radians(state.azimuth_deg)
    alt = math.radians(state.altitude_deg)
    cos_alt = math.cos(alt)
    return Vec3(math.sin(az) * cos_alt, math.cos(az) * cos_alt, math.sin(alt)).normalized()


def moon_screen_point(
    state: MoonState | None,
    camera: SkyCamera,
    width: int,
    height: int,
) -> tuple[float, float] | None:
    if state is None or not state.visible:
        return None
    return camera.project(moon_direction(state), width, height)


class SkyRenderer:
    def draw(
        self,
        points: dict[int, ScreenPoint],
        constellations: tuple[Constellation, ...],
        selected_constellation: Constellation,
        show_constellations: bool,
        show_guides: bool,
        camera: SkyCamera,
        width: int,
        height: int,
        meteor_event: MeteorEventView | None = None,
        moon_state: MoonState | None = None,
        observer_latitude_deg: float = 0.0,
        sky_paths: dict[str, list[tuple[float, float] | None]] | None = None,
    ) -> None:
        pyxel.cls(0)
        moon_light = moon_light_level(moon_state)
        if show_guides:
            self.draw_background(width, height)
            self.draw_horizon(camera, width, height)
        self.draw_milky_way(
            [] if sky_paths is None else sky_paths.get(MILKY_WAY_PATH_ID, []),
            moon_light,
            width,
            height,
        )
        if show_constellations:
            self.draw_constellations(points, constellations, selected_constellation)
        self.draw_stars(points, moon_light)
        self.draw_moon(moon_state, camera, width, height, observer_latitude_deg)
        if meteor_event is not None:
            self.draw_meteors(meteor_event, width, height)

    def draw_background(self, width: int, height: int) -> None:
        for y in range(0, height, 12):
            color = 1 if y < height * 0.65 else 0
            pyxel.line(0, y, width, y, color)

    def draw_stars(self, points: dict[int, ScreenPoint], moon_light: float = 0.0) -> None:
        frame_count = pyxel.frame_count
        effective_limit_mag = BASE_LIMIT_MAG - moon_light * 1.5
        for star_id, point in sorted(points.items(), key=lambda item: item[1].magnitude, reverse=True):
            if point.magnitude > effective_limit_mag and star_id != POLARIS_ID:
                continue
            x = int(point.x)
            y = int(point.y)
            col = star_color(point.color_index)
            radius = star_radius(point.magnitude)
            if star_id == POLARIS_ID:
                radius = max(radius, 2)
            twinkle = twinkle_level(star_id, point.magnitude, frame_count)
            if twinkle == 0:
                if radius == 0:
                    continue
                col = _dim_star_color(col)
                radius = max(0, radius - 1)
            if radius >= 3:
                pyxel.circ(x, y, radius, col)
                pyxel.pset(x - radius - 1, y, 13)
                pyxel.pset(x + radius + 1, y, 13)
                pyxel.pset(x, y - radius - 1, 13)
                pyxel.pset(x, y + radius + 1, 13)
            elif radius == 2:
                pyxel.circ(x, y, radius, col)
                if twinkle == 2:
                    pyxel.pset(x - 3, y, HORIZON)
                    pyxel.pset(x + 3, y, HORIZON)
            elif radius == 1:
                pyxel.pset(x - 1, y, col)
                pyxel.pset(x, y - 1, col)
                pyxel.pset(x, y, col)
                pyxel.pset(x + 1, y, col)
                pyxel.pset(x, y + 1, col)
                if twinkle == 2:
                    pyxel.pset(x + 2, y, HORIZON)
            else:
                pyxel.pset(x, y, col)
                if twinkle == 2:
                    pyxel.pset(x + 1, y, HORIZON)

    def draw_milky_way(
        self,
        points: list[tuple[float, float] | None],
        moon_light: float,
        width: int,
        height: int,
    ) -> None:
        if len(points) < 2:
            return
        strength = max(0.0, min(1.0, 1.0 - moon_light * 0.9))
        if strength <= 0.08:
            return

        frame_count = pyxel.frame_count
        band_width = MILKY_WAY_BAND_WIDTH_PX * (0.55 + strength * 0.45)
        samples = max(6, int(MILKY_WAY_SEGMENT_PARTICLES * strength))
        for segment_index in range(len(points) - 1):
            start = points[segment_index]
            end = points[segment_index + 1]
            if start is None or end is None:
                continue
            x1, y1 = start
            x2, y2 = end
            dx = x2 - x1
            dy = y2 - y1
            length = math.sqrt(dx * dx + dy * dy)
            if length < 2.0:
                continue
            tangent_x = dx / length
            tangent_y = dy / length
            normal_x = -tangent_y
            normal_y = tangent_x

            for sample_index in range(samples):
                seed = segment_index * 4099 + sample_index * 197 + 23
                t = (sample_index + 0.5 + (_pseudo_random(seed) - 0.5) * 0.75) / samples
                spread = _pseudo_random(seed + 1) * 2.0 - 1.0
                core_bias = spread * abs(spread)
                offset = core_bias * band_width * (0.35 + _pseudo_random(seed + 2) * 0.65)
                jitter = (_pseudo_random(seed + 3) - 0.5) * 8.0
                x = x1 + dx * t + normal_x * offset + tangent_x * jitter
                y = y1 + dy * t + normal_y * offset + tangent_y * jitter
                if x < -2 or width + 2 < x or y < -2 or height + 2 < y:
                    continue

                distance_from_core = abs(offset) / max(1.0, band_width)
                bright_chance = max(0.06, 0.38 * strength * (1.0 - distance_from_core))
                warm_chance = 0.12 + 0.12 * (1.0 - distance_from_core)
                grain = _pseudo_random(seed + 4)
                if grain < bright_chance:
                    color = STAR_WHITE
                elif grain < bright_chance + warm_chance:
                    color = STAR_YELLOW_WHITE
                elif distance_from_core < 0.5:
                    color = HORIZON
                else:
                    color = LINE_DIM

                pulse_period = 420 + int(_pseudo_random(seed + 5) * 360)
                if (frame_count + seed) % pulse_period < 2 and color in (STAR_WHITE, STAR_YELLOW_WHITE):
                    color = STAR_YELLOW
                px = int(x)
                py = int(y)
                pyxel.pset(px, py, color)
                if strength > 0.72 and distance_from_core < 0.32 and _pseudo_random(seed + 6) > 0.93:
                    pyxel.pset(px + 1, py, HORIZON)

    def draw_moon(
        self,
        state: MoonState | None,
        camera: SkyCamera,
        width: int,
        height: int,
        observer_latitude_deg: float,
    ) -> None:
        projected = moon_screen_point(state, camera, width, height)
        if state is None or projected is None:
            return
        x, y = int(projected[0]), int(projected[1])
        if x < -MOON_RADIUS_PX or width + MOON_RADIUS_PX < x:
            return
        if y < -MOON_RADIUS_PX or height + MOON_RADIUS_PX < y:
            return
        lit_color = STAR_YELLOW if state.altitude_deg < 5.0 else STAR_YELLOW_WHITE
        dark_color = 1
        edge_color = STAR_WHITE if state.illumination > 0.85 else HORIZON
        radius = MOON_RADIUS_PX
        lit_side = 1 if state.waxing else -1
        if observer_latitude_deg < 0.0:
            lit_side *= -1
        threshold = 1.0 - 2.0 * max(0.0, min(1.0, state.illumination))
        for dy in range(-radius, radius + 1):
            for dx in range(-radius, radius + 1):
                if dx * dx + dy * dy > radius * radius:
                    continue
                normalized_x = lit_side * dx / radius
                color = lit_color if normalized_x >= threshold else dark_color
                pyxel.pset(x + dx, y + dy, color)
        pyxel.circb(x, y, radius, edge_color)
        if state.illumination > 0.08:
            pyxel.pset(x + lit_side * (radius + 1), y, edge_color)

    def draw_meteors(self, event_view: MeteorEventView, width: int, height: int) -> None:
        if not isinstance(event_view.event, MeteorShowerEvent):
            return
        if event_view.radiant_screen is None:
            return
        radiant_x, radiant_y = event_view.radiant_screen
        shower_strength = min(1.0, event_view.event.zhr / 100.0)
        count = 5 + int(event_view.activity * 6) + int(shower_strength * 4)
        frame_count = pyxel.frame_count
        seed_base = sum(ord(char) for char in event_view.event.id)
        east = cross(event_view.radiant_direction, Vec3(0.0, 0.0, 1.0))
        if east.length() < 0.001:
            east = Vec3(1.0, 0.0, 0.0)
        else:
            east = east.normalized()
        northish = cross(east, event_view.radiant_direction).normalized()
        for index in range(count):
            period = 58 + int(_pseudo_random(seed_base + index * 83) * 54) + index * 7
            age = (frame_count + seed_base + index * 53) % period
            life = 14 + int(_pseudo_random(seed_base + index * 67) * 10) + int(event_view.activity * 5)
            if age >= life:
                continue
            burst = (frame_count + seed_base + index * 53 - age) // period
            angle = math.tau * _pseudo_random(seed_base + index * 101 + burst * 17)
            spread = 0.22 + 0.98 * _pseudo_random(seed_base + index * 191 + burst * 29)
            start_direction = _add_vec(
                _scale_vec(event_view.radiant_direction, math.cos(spread)),
                _add_vec(
                    _scale_vec(east, math.cos(angle) * math.sin(spread)),
                    _scale_vec(northish, math.sin(angle) * math.sin(spread)),
                ),
            ).normalized()
            if start_direction.z <= 0.0:
                continue
            brightness = _pseudo_random(seed_base + index * 47 + burst * 31)
            fireball = brightness > 0.86 or (index == 0 and event_view.activity > 0.72)
            length = (
                24
                + event_view.activity * 44
                + shower_strength * 18
                + _pseudo_random(seed_base + index * 41 + burst) * (54 if fireball else 34)
            )
            progress = age / max(1, life - 1)
            visible = _ease_out(progress)
            fade = 1.0 - progress
            start_projected = event_view.camera.project(start_direction, width, height)
            if start_projected is None:
                continue
            start_x, start_y = start_projected
            screen_dx = start_x - radiant_x
            screen_dy = start_y - radiant_y
            screen_distance = math.sqrt(screen_dx * screen_dx + screen_dy * screen_dy)
            if screen_distance < 24.0:
                continue
            screen_dx /= screen_distance
            screen_dy /= screen_distance
            head_x = start_x + screen_dx * visible * length
            head_y = start_y + screen_dy * visible * length
            tail_length = length * (0.42 + 0.58 * min(1.0, visible + 0.2))
            tail_x = head_x - screen_dx * tail_length
            tail_y = head_y - screen_dy * tail_length
            if not _line_intersects_screen(tail_x, tail_y, head_x, head_y, width, height):
                continue
            core_color = STAR_YELLOW_WHITE if fireball else STAR_WHITE
            head_color = STAR_WHITE if fade > 0.25 else HORIZON
            self._draw_meteor_streak(tail_x, tail_y, head_x, head_y, core_color, head_color, fireball)

    def _draw_meteor_streak(
        self,
        tail_x: float,
        tail_y: float,
        head_x: float,
        head_y: float,
        core_color: int,
        head_color: int,
        fireball: bool,
    ) -> None:
        dx = head_x - tail_x
        dy = head_y - tail_y
        length = math.sqrt(dx * dx + dy * dy)
        if length < 1.0:
            return
        normal_x = -dy / length
        normal_y = dx / length

        dim_x = tail_x + dx * 0.46
        dim_y = tail_y + dy * 0.46
        mid_x = tail_x + dx * 0.72
        mid_y = tail_y + dy * 0.72
        bright_x = tail_x + dx * 0.88
        bright_y = tail_y + dy * 0.88

        pyxel.line(int(tail_x), int(tail_y), int(dim_x), int(dim_y), 1)
        pyxel.line(int(dim_x), int(dim_y), int(mid_x), int(mid_y), HORIZON)
        pyxel.line(int(mid_x), int(mid_y), int(head_x), int(head_y), core_color)
        pyxel.line(int(bright_x), int(bright_y), int(head_x), int(head_y), head_color)

        if fireball:
            offset = 1.0
            pyxel.line(
                int(mid_x + normal_x * offset),
                int(mid_y + normal_y * offset),
                int(head_x + normal_x * offset),
                int(head_y + normal_y * offset),
                STAR_YELLOW,
            )
            pyxel.line(
                int(mid_x - normal_x * offset),
                int(mid_y - normal_y * offset),
                int(head_x - normal_x * offset),
                int(head_y - normal_y * offset),
                HORIZON,
            )
            pyxel.circ(int(head_x), int(head_y), 1, head_color)
            pyxel.pset(int(head_x + normal_x * 3), int(head_y + normal_y * 3), HORIZON)
            pyxel.pset(int(head_x - normal_x * 3), int(head_y - normal_y * 3), HORIZON)
        else:
            pyxel.pset(int(head_x), int(head_y), head_color)

    def draw_constellations(
        self,
        points: dict[int, ScreenPoint],
        constellations: tuple[Constellation, ...],
        selected_constellation: Constellation,
    ) -> None:
        for constellation in constellations:
            col = LINE_SELECTED if constellation.id == selected_constellation.id else LINE_DIM
            for a_id, b_id in constellation.edges:
                a = points.get(a_id)
                b = points.get(b_id)
                if a is None or b is None:
                    continue
                pyxel.line(int(a.x), int(a.y), int(b.x), int(b.y), col)

    def draw_horizon(self, camera: SkyCamera, width: int, height: int) -> None:
        last: tuple[float, float] | None = None
        for i in range(73):
            az = math.tau * i / 72.0
            direction = Vec3(math.sin(az), math.cos(az), 0.0)
            projected = camera.project(direction, width, height)
            if projected is None:
                last = None
                continue
            x, y = projected
            if -width <= x <= width * 2 and -height <= y <= height * 2:
                if last is not None:
                    pyxel.line(int(last[0]), int(last[1]), int(x), int(y), HORIZON)
                last = (x, y)
            else:
                last = None


def _pseudo_random(seed: int) -> float:
    return (math.sin(seed * 12.9898) * 43758.5453) % 1.0


def _ease_out(value: float) -> float:
    clamped = max(0.0, min(1.0, value))
    return 1.0 - (1.0 - clamped) * (1.0 - clamped)


def _scale_vec(vector: Vec3, scale: float) -> Vec3:
    return Vec3(vector.x * scale, vector.y * scale, vector.z * scale)


def _add_vec(a: Vec3, b: Vec3) -> Vec3:
    return Vec3(a.x + b.x, a.y + b.y, a.z + b.z)


def _line_intersects_screen(x1: float, y1: float, x2: float, y2: float, width: int, height: int) -> bool:
    return (
        max(x1, x2) >= 0
        and min(x1, x2) <= width
        and max(y1, y2) >= 0
        and min(y1, y2) <= height
    )
