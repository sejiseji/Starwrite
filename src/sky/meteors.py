from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import datetime, time, timedelta, tzinfo

from src.astronomy.coordinates import equatorial_to_enu
from src.astronomy.events import MeteorShowerEvent
from src.astronomy.observer import Observer
from src.astronomy.time import julian_date, local_sidereal_time
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

    peak = meteor_peak_datetime(event, tz)
    hours_from_peak = abs((observation_time - peak).total_seconds()) / 3600.0
    return max(0.25, 1.0 - hours_from_peak / 10.0)


def meteor_peak_datetime(event: MeteorShowerEvent, tz: tzinfo) -> datetime:
    return datetime.combine(event.display_end, time(event.peak_hour_local, 0), tzinfo=tz)


def adjacent_meteor_event_time(
    events: tuple[MeteorShowerEvent, ...],
    current_time: datetime,
    direction: int,
) -> datetime | None:
    event = adjacent_meteor_event(events, current_time, direction)
    return meteor_peak_datetime(event, current_time.tzinfo) if event is not None else None


def adjacent_meteor_event(
    events: tuple[MeteorShowerEvent, ...],
    current_time: datetime,
    direction: int,
) -> MeteorShowerEvent | None:
    if current_time.tzinfo is None:
        raise ValueError("current_time must be timezone-aware")
    if not events:
        return None

    event_times = sorted(
        ((meteor_peak_datetime(event, current_time.tzinfo), event) for event in events),
        key=lambda item: (item[0], item[1].id),
    )
    if direction >= 0:
        for event_time, event in event_times:
            if event_time > current_time + timedelta(minutes=1):
                return event
        return event_times[0][1]

    for event_time, event in reversed(event_times):
        if event_time < current_time - timedelta(minutes=1):
            return event
    return event_times[-1][1]


def adjacent_visible_meteor_event(
    events: tuple[MeteorShowerEvent, ...],
    observer: Observer,
    current_time: datetime,
    direction: int,
) -> MeteorShowerEvent | None:
    if current_time.tzinfo is None:
        raise ValueError("current_time must be timezone-aware")
    if not events:
        return None

    event_times = sorted(
        ((meteor_peak_datetime(event, current_time.tzinfo), event) for event in events),
        key=lambda item: (item[0], item[1].id),
    )
    ordered = event_times if direction >= 0 else tuple(reversed(event_times))
    margin = timedelta(minutes=1)
    for event_time, event in ordered:
        if direction >= 0 and event_time <= current_time + margin:
            continue
        if direction < 0 and event_time >= current_time - margin:
            continue
        if meteor_radiant_direction(event, observer, event_time).z > 0.0:
            return event

    wrapped = event_times if direction >= 0 else tuple(reversed(event_times))
    for event_time, event in wrapped:
        if meteor_radiant_direction(event, observer, event_time).z > 0.0:
            return event
    return None


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
