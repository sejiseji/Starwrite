from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Observer:
    latitude_deg: float
    longitude_deg: float

    def __post_init__(self) -> None:
        if not -90.0 <= self.latitude_deg <= 90.0:
            raise ValueError("latitude_deg must be in [-90, 90]")
        if not -180.0 <= self.longitude_deg <= 180.0:
            raise ValueError("longitude_deg must be in [-180, 180]")

