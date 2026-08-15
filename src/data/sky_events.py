from __future__ import annotations

from src.astronomy.events import SkyEvent
from src.data.lunar_eclipses import LUNAR_ECLIPSES, LUNAR_ECLIPSE_SOURCE_LABEL
from src.data.meteor_showers import EVENT_SOURCE_LABEL as METEOR_SOURCE_LABEL
from src.data.meteor_showers import METEOR_SHOWERS

EVENT_SOURCE_LABEL = f"{METEOR_SOURCE_LABEL}/{LUNAR_ECLIPSE_SOURCE_LABEL}"
SKY_EVENTS: tuple[SkyEvent, ...] = (*METEOR_SHOWERS, *LUNAR_ECLIPSES)
