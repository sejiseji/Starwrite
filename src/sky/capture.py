from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from astronomy.catalog import Constellation
from .vector import Vec3


@dataclass(slots=True, frozen=True)
class ScreenPoint:
    x: float
    y: float
    magnitude: float
    color_index: float | None
    direction: Vec3


@dataclass(slots=True, frozen=True)
class SkyCapture:
    schema_version: int
    constellation_id: str
    anchor_star_id: int | None
    camera_yaw: float
    camera_pitch: float
    fov_deg: float
    observation_time: datetime


def can_capture(
    constellation: Constellation,
    projected_stars: dict[int, ScreenPoint],
    screen_width: int,
    screen_height: int,
    margin: int = 18,
    min_span: float = 18.0,
) -> bool:
    points = [projected_stars.get(star_id) for star_id in constellation.main_star_ids]
    if any(point is None for point in points):
        return False

    xs = [point.x for point in points if point is not None]
    ys = [point.y for point in points if point is not None]
    if not all(margin <= x <= screen_width - margin for x in xs):
        return False
    if not all(margin <= y <= screen_height - margin for y in ys):
        return False
    return max(max(xs) - min(xs), max(ys) - min(ys)) >= min_span

