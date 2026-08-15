from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime


@dataclass(slots=True, frozen=True)
class MeteorShowerEvent:
    id: str
    name: str
    year: int
    display_start: date
    display_end: date
    peak_hour_local: int
    radiant_ra_rad: float
    radiant_dec_rad: float
    zhr: int
    parent: str
    related_constellation_id: str | None = None


@dataclass(slots=True, frozen=True)
class LunarEclipseEvent:
    id: str
    name: str
    year: int
    display_start: date
    display_end: date
    greatest_at_utc: datetime
    eclipse_type: str
    umbral_magnitude: float
    duration_minutes: int
    totality_minutes: int | None
    visibility_region: str


SkyEvent = MeteorShowerEvent | LunarEclipseEvent
