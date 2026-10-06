from __future__ import annotations

import math
from dataclasses import dataclass

from .vector import Vec3, cross

MIN_FOV_DEG = 20.0
MAX_FOV_DEG = 120.0


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


@dataclass(slots=True, frozen=True)
class CameraProjection:
    """Camera constants shared by one batch; rebuild after camera changes."""

    right: Vec3
    up: Vec3
    front: Vec3
    focal: float
    center_x: float
    center_y: float

    def project(self, direction: Vec3) -> tuple[float, float] | None:
        unit = direction.normalized()
        cam = Vec3(unit.dot(self.right), unit.dot(self.up), unit.dot(self.front))
        if cam.z <= 0.0001:
            return None
        return (
            self.center_x + cam.x * self.focal / cam.z,
            self.center_y - cam.y * self.focal / cam.z,
        )


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

    def projection(self, screen_width: int, screen_height: int) -> CameraProjection:
        right = self.right()
        front = self.front()
        return CameraProjection(
            right,
            cross(right, front).normalized(),
            front,
            min(screen_width, screen_height) * 0.5 / math.tan(math.radians(self.fov_deg) * 0.5),
            screen_width * 0.5,
            screen_height * 0.5,
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
