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
    if magnitude < 0.5:
        return 2
    if magnitude < 2.0:
        return 1
    return 0


class SkyRenderer:
    def draw(
        self,
        points: dict[int, ScreenPoint],
        constellations: tuple[Constellation, ...],
        selected_constellation: Constellation,
        show_constellations: bool,
        camera: SkyCamera,
        width: int,
        height: int,
    ) -> None:
        pyxel.cls(0)
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
        for point in sorted(points.values(), key=lambda p: p.magnitude, reverse=True):
            x = int(point.x)
            y = int(point.y)
            col = star_color(point.color_index)
            radius = star_radius(point.magnitude)
            if radius >= 2:
                pyxel.circ(x, y, radius, col)
            elif radius == 1:
                pyxel.pset(x - 1, y, col)
                pyxel.pset(x, y - 1, col)
                pyxel.pset(x, y, col)
                pyxel.pset(x + 1, y, col)
                pyxel.pset(x, y + 1, col)
            else:
                pyxel.pset(x, y, col)

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
