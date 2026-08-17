from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum, auto

from .vector import Vec3

FOCUS_ACQUIRE_FRAMES = 12
OUT_OF_RANGE_ALT_DEG = -1.5
RETURN_ALT_DEG = 1.0
VISIBILITY_CONFIRM_FRAMES = 12


class FocusTargetKind(Enum):
    STAR = auto()
    CONSTELLATION = auto()
    ASTERISM = auto()
    SKY_PATH = auto()


class FocusLockPhase(Enum):
    OFF = auto()
    ACQUIRING = auto()
    TRACKING = auto()
    OUT_OF_RANGE = auto()


@dataclass(slots=True, frozen=True)
class FocusTarget:
    kind: FocusTargetKind
    target_id: str | int
    anchor_ra_rad: float | None = None
    anchor_dec_rad: float | None = None


@dataclass(slots=True)
class FocusLockState:
    phase: FocusLockPhase = FocusLockPhase.OFF
    target: FocusTarget | None = None
    acquire_start_frame: int = 0
    start_yaw: float = 0.0
    start_pitch: float = 0.0
    last_valid_yaw: float = 0.0
    last_valid_pitch: float = 0.0
    hidden_frames: int = 0
    visible_frames: int = 0

    @property
    def enabled(self) -> bool:
        return self.phase is not FocusLockPhase.OFF

    def clear(self) -> None:
        self.phase = FocusLockPhase.OFF
        self.target = None
        self.hidden_frames = 0
        self.visible_frames = 0


def mean_direction(directions: list[Vec3] | tuple[Vec3, ...]) -> Vec3 | None:
    if not directions:
        return None
    x = sum(direction.x for direction in directions)
    y = sum(direction.y for direction in directions)
    z = sum(direction.z for direction in directions)
    length_squared = x * x + y * y + z * z
    if length_squared < 1e-10:
        return None
    length = math.sqrt(length_squared)
    return Vec3(x / length, y / length, z / length)


def altitude_deg(direction: Vec3) -> float:
    length = direction.length()
    if length <= 0.0:
        return -90.0
    return math.degrees(math.asin(max(-1.0, min(1.0, direction.z / length))))


def all_hidden_below_horizon(directions: list[Vec3] | tuple[Vec3, ...]) -> bool:
    return bool(directions) and all(altitude_deg(direction) <= OUT_OF_RANGE_ALT_DEG for direction in directions)


def any_visible_above_horizon(directions: list[Vec3] | tuple[Vec3, ...]) -> bool:
    return any(altitude_deg(direction) >= RETURN_ALT_DEG for direction in directions)


def acquire_ease(frame_count: int, start_frame: int) -> float:
    age = max(0, frame_count - start_frame)
    t = min(1.0, age / max(1, FOCUS_ACQUIRE_FRAMES - 1))
    return t * t * (3.0 - 2.0 * t)
