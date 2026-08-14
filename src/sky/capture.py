from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from src.astronomy.catalog import Constellation
from .vector import Vec3


@dataclass(slots=True, frozen=True)
class ScreenPoint:
    x: float
    y: float
    magnitude: float
    color_index: float | None
    direction: Vec3


@dataclass(slots=True, frozen=True)
class SkyCapture:
    schema_version: int
    captured_at: datetime
    latitude_deg: float
    longitude_deg: float
    camera_yaw: float
    camera_pitch: float
    camera_roll: float
    fov_deg: float
    selected_constellation_id: str | None
    selected_star_id: int | None
    selected_feature_id: str | None
    selected_event_id: str | None
    render_seed: int
    moon: dict | None = None


def capture_to_dict(capture: SkyCapture) -> dict:
    return {
        "schema_version": capture.schema_version,
        "captured_at": capture.captured_at.isoformat(),
        "latitude_deg": capture.latitude_deg,
        "longitude_deg": capture.longitude_deg,
        "camera_yaw": capture.camera_yaw,
        "camera_pitch": capture.camera_pitch,
        "camera_roll": capture.camera_roll,
        "fov_deg": capture.fov_deg,
        "selected_constellation_id": capture.selected_constellation_id,
        "selected_star_id": capture.selected_star_id,
        "selected_feature_id": capture.selected_feature_id,
        "selected_event_id": capture.selected_event_id,
        "render_seed": capture.render_seed,
        "moon": capture.moon,
    }


def capture_from_dict(data: dict) -> SkyCapture:
    if "captured_at" in data:
        captured_at = datetime.fromisoformat(str(data["captured_at"]))
        return SkyCapture(
            schema_version=int(data.get("schema_version", 1)),
            captured_at=captured_at,
            latitude_deg=float(data["latitude_deg"]),
            longitude_deg=float(data["longitude_deg"]),
            camera_yaw=float(data["camera_yaw"]),
            camera_pitch=float(data["camera_pitch"]),
            camera_roll=float(data.get("camera_roll", 0.0)),
            fov_deg=float(data["fov_deg"]),
            selected_constellation_id=data.get("selected_constellation_id"),
            selected_star_id=data.get("selected_star_id"),
            selected_feature_id=data.get("selected_feature_id"),
            selected_event_id=data.get("selected_event_id"),
            render_seed=int(data.get("render_seed", 0)),
            moon=data.get("moon"),
        )

    observation_time = datetime.fromisoformat(str(data["observation_time"]))
    return SkyCapture(
        schema_version=int(data.get("schema_version", 1)),
        captured_at=observation_time,
        latitude_deg=float(data.get("latitude_deg", 35.7)),
        longitude_deg=float(data.get("longitude_deg", 139.7)),
        camera_yaw=float(data["camera_yaw"]),
        camera_pitch=float(data["camera_pitch"]),
        camera_roll=0.0,
        fov_deg=float(data["fov_deg"]),
        selected_constellation_id=data.get("constellation_id"),
        selected_star_id=data.get("anchor_star_id"),
        selected_feature_id=None,
        selected_event_id=None,
        render_seed=0,
        moon=data.get("moon"),
    )


def can_capture(
    constellation: Constellation,
    projected_stars: dict[int, ScreenPoint],
    screen_width: int,
    screen_height: int,
    margin: int = 18,
    min_span: float = 18.0,
) -> bool:
    points = [projected_stars.get(star_id) for star_id in constellation.main_star_ids]
    if any(point is None for point in points):
        return False

    xs = [point.x for point in points if point is not None]
    ys = [point.y for point in points if point is not None]
    if not all(margin <= x <= screen_width - margin for x in xs):
        return False
    if not all(margin <= y <= screen_height - margin for y in ys):
        return False
    return max(max(xs) - min(xs), max(ys) - min(ys)) >= min_span
