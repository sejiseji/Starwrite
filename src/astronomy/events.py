from __future__ import annotations

from dataclasses import dataclass
from datetime import date


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
