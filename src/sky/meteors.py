from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import datetime, time

from astronomy.coordinates import equatorial_to_enu
from astronomy.events import MeteorShowerEvent
from astronomy.observer import Observer
from astronomy.time import julian_date, local_sidereal_time
from .camera import SkyCamera
from .vector import Vec3


@dataclass(slots=True, frozen=True)
class MeteorEventView:
    event: MeteorShowerEvent
    radiant_direction: Vec3
    radiant_screen: tuple[float, float] | None
    activity: float
    camera: SkyCamera


def meteor_activity(event: MeteorShowerEvent, observation_time: datetime) -> float:
    if observation_time.tzinfo is None:
        raise ValueError("observation_time must be timezone-aware")

    tz = observation_time.tzinfo
    start = datetime.combine(event.display_start, time(20, 0), tzinfo=tz)
    end = datetime.combine(event.display_end, time(5, 59), tzinfo=tz)
    if not start <= observation_time <= end:
        return 0.0

    peak = datetime.combine(event.display_end, time(event.peak_hour_local, 0), tzinfo=tz)
    hours_from_peak = abs((observation_time - peak).total_seconds()) / 3600.0
    return max(0.25, 1.0 - hours_from_peak / 10.0)


def meteor_radiant_direction(
    event: MeteorShowerEvent,
    observer: Observer,
    observation_time: datetime,
) -> Vec3:
    jd = julian_date(observation_time)
    lst = local_sidereal_time(jd, math.radians(observer.longitude_deg))
    return equatorial_to_enu(
        event.radiant_ra_rad,
        event.radiant_dec_rad,
        math.radians(observer.latitude_deg),
        lst,
    )


def active_meteor_event(
    events: tuple[MeteorShowerEvent, ...],
    observer: Observer,
    observation_time: datetime,
    camera: SkyCamera,
    screen_width: int,
    screen_height: int,
) -> MeteorEventView | None:
    best: MeteorEventView | None = None
    for event in events:
        activity = meteor_activity(event, observation_time)
        if activity <= 0.0:
            continue
        radiant = meteor_radiant_direction(event, observer, observation_time)
        if radiant.z <= 0.0:
            continue
        projected = camera.project(radiant, screen_width, screen_height)
        view = MeteorEventView(event, radiant, projected, activity, camera)
        if best is None or view.activity > best.activity:
            best = view
    return best
