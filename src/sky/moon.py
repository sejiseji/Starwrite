from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from astronomy.moon import MoonState, compute_moon


@dataclass(slots=True)
class MoonController:
    state: MoonState | None = None
    cache_key: tuple[int, float, float] | None = None

    def update(self, dt_utc: datetime, latitude_deg: float, longitude_deg: float) -> None:
        key = (
            int(dt_utc.timestamp() // 60),
            round(latitude_deg, 4),
            round(longitude_deg, 4),
        )
        if key == self.cache_key:
            return
        self.state = compute_moon(dt_utc, latitude_deg, longitude_deg)
        self.cache_key = key
