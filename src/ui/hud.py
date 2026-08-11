from __future__ import annotations

import pyxel

from astronomy.catalog import Constellation
from astronomy.observer import Observer
from sky.capture import SkyCapture
from sky.camera import SkyCamera
from sky.simulation import SimulationClock


def draw_hud(
    observer: Observer,
    clock: SimulationClock,
    camera: SkyCamera,
    mode: str,
    selected: Constellation,
    show_constellations: bool,
    can_capture: bool,
    latest_capture: SkyCapture | None,
) -> None:
    lines = [
        f"LAT {observer.latitude_deg:+05.1f} LON {observer.longitude_deg:+06.1f}",
        clock.current_time.strftime("DATE %Y-%m-%d  TIME %H:%M:%S %z"),
        f"MODE {mode}  {'PLAY' if clock.running else 'PAUSE'}",
        f"{selected.id} {selected.name}  C:{'ON' if show_constellations else 'OFF'} FOV:{camera.fov_deg:03.0f}",
    ]
    y = 4
    for line in lines:
        pyxel.text(4, y, line, 6)
        y += 7

    if can_capture:
        pyxel.text(4, pyxel.height - 17, f"{selected.name.upper()} FOUND", 10)
        pyxel.text(4, pyxel.height - 9, "ENTER CAPTURE", 7)
    elif latest_capture is not None:
        pyxel.text(4, pyxel.height - 9, f"CAPTURED {latest_capture.constellation_id}", 11)

