from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import datetime, timedelta

from src.astronomy.catalog import Star
from src.astronomy.coordinates import equatorial_to_enu
from src.astronomy.observer import Observer
from src.astronomy.time import julian_date, local_sidereal_time
from .camera import SkyCamera
from .capture import ScreenPoint


@dataclass(slots=True)
class SimulationClock:
    current_time: datetime
    running: bool = False
    speed: float = 600.0

    def __post_init__(self) -> None:
        if self.current_time.tzinfo is None:
            raise ValueError("SimulationClock.current_time must be timezone-aware")

    def update(self, real_dt: float) -> None:
        if self.running:
            self.current_time += timedelta(seconds=real_dt * self.speed)

    def add_minutes(self, minutes: float) -> None:
        self.current_time += timedelta(minutes=minutes)

    def add_days(self, days: float) -> None:
        self.current_time += timedelta(days=days)

    def play(self) -> None:
        self.running = True

    def pause(self) -> None:
        self.running = False


def star_direction(star: Star, observer: Observer, observation_time: datetime):
    jd = julian_date(observation_time)
    lst = local_sidereal_time(jd, math.radians(observer.longitude_deg))
    return equatorial_to_enu(star.ra_rad, star.dec_rad, math.radians(observer.latitude_deg), lst)


def project_visible_stars(
    stars: tuple[Star, ...],
    observer: Observer,
    observation_time: datetime,
    camera: SkyCamera,
    screen_width: int,
    screen_height: int,
) -> dict[int, ScreenPoint]:
    jd = julian_date(observation_time)
    lst = local_sidereal_time(jd, math.radians(observer.longitude_deg))
    lat = math.radians(observer.latitude_deg)
    points: dict[int, ScreenPoint] = {}
    for star in stars:
        direction = equatorial_to_enu(star.ra_rad, star.dec_rad, lat, lst)
        if direction.z <= 0.0:
            continue
        projected = camera.project(direction, screen_width, screen_height)
        if projected is None:
            continue
        x, y = projected
        if -24 <= x <= screen_width + 24 and -24 <= y <= screen_height + 24:
            points[star.id] = ScreenPoint(x, y, star.magnitude, star.color_index, direction)
    return points

