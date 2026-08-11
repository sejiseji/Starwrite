from __future__ import annotations

import math

import pyxel

from astronomy.catalog import Constellation
from .camera import SkyCamera
from .capture import ScreenPoint
from .vector import Vec3

STAR_WHITE = 7
STAR_BLUE_WHITE = 12
STAR_YELLOW_WHITE = 10
STAR_YELLOW = 9
STAR_ORANGE = 4
STAR_RED = 8
LINE_DIM = 5
LINE_SELECTED = 10
HORIZON = 13


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
    period = 720 + star_id % 840
    phase = (frame_count + star_id * 17) % period
    pulse_width = 2 if magnitude < 2.5 else 3
    if phase < pulse_width:
        return 2
    return 1


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
    ) -> None:
        pyxel.cls(0)
        if show_guides:
            self.draw_background(width, height)
        self.draw_horizon(camera, width, height)
        if show_constellations:
            self.draw_constellations(points, constellations, selected_constellation)
        self.draw_stars(points)

    def draw_background(self, width: int, height: int) -> None:
        for y in range(0, height, 12):
            color = 1 if y < height * 0.65 else 0
            pyxel.line(0, y, width, y, color)

    def draw_stars(self, points: dict[int, ScreenPoint]) -> None:
        frame_count = pyxel.frame_count
        for star_id, point in sorted(points.items(), key=lambda item: item[1].magnitude, reverse=True):
            x = int(point.x)
            y = int(point.y)
            col = star_color(point.color_index)
            radius = star_radius(point.magnitude)
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
