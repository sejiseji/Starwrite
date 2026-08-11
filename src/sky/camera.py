from __future__ import annotations

import math
from dataclasses import dataclass

from .vector import Vec3, cross

MIN_FOV_DEG = 20.0
MAX_FOV_DEG = 120.0


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


@dataclass(slots=True)
class SkyCamera:
    yaw: float
    pitch: float
    fov_deg: float

    def __post_init__(self) -> None:
        self.pitch = _clamp(self.pitch, -math.pi / 2.0, math.pi / 2.0)
        self.fov_deg = _clamp(self.fov_deg, MIN_FOV_DEG, MAX_FOV_DEG)

    def clamp(self) -> None:
        self.pitch = _clamp(self.pitch, -math.pi / 2.0, math.pi / 2.0)
        self.fov_deg = _clamp(self.fov_deg, MIN_FOV_DEG, MAX_FOV_DEG)

    def front(self) -> Vec3:
        cos_pitch = math.cos(self.pitch)
        return Vec3(
            math.sin(self.yaw) * cos_pitch,
            math.cos(self.yaw) * cos_pitch,
            math.sin(self.pitch),
        ).normalized()

    def right(self) -> Vec3:
        return Vec3(math.cos(self.yaw), -math.sin(self.yaw), 0.0).normalized()

    def up(self) -> Vec3:
        return cross(self.right(), self.front()).normalized()

    def world_to_camera(self, direction: Vec3) -> Vec3:
        unit = direction.normalized()
        return Vec3(
            unit.dot(self.right()),
            unit.dot(self.up()),
            unit.dot(self.front()),
        )

    def project(
        self,
        direction: Vec3,
        screen_width: int,
        screen_height: int,
    ) -> tuple[float, float] | None:
        cam = self.world_to_camera(direction)
        if cam.z <= 0.0001:
            return None
        focal = min(screen_width, screen_height) * 0.5 / math.tan(math.radians(self.fov_deg) * 0.5)
        x = screen_width * 0.5 + cam.x * focal / cam.z
        y = screen_height * 0.5 - cam.y * focal / cam.z
        return (x, y)

