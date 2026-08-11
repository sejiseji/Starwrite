from __future__ import annotations

import pyxel

from astronomy.catalog import Constellation
from astronomy.observer import Observer
from sky.capture import ScreenPoint, SkyCapture
from sky.camera import SkyCamera
from sky.simulation import SimulationClock

SCALE = 2
GLYPH_W = 3
GLYPH_H = 5
CHAR_STEP = 8
LINE_STEP = 13

FONT = {
    " ": ("000", "000", "000", "000", "000"),
    ".": ("000", "000", "000", "000", "010"),
    ":": ("000", "010", "000", "010", "000"),
    "-": ("000", "000", "111", "000", "000"),
    "+": ("000", "010", "111", "010", "000"),
    "/": ("001", "001", "010", "100", "100"),
    "[": ("110", "100", "100", "100", "110"),
    "]": ("011", "001", "001", "001", "011"),
    "0": ("111", "101", "101", "101", "111"),
    "1": ("010", "110", "010", "010", "111"),
    "2": ("111", "001", "111", "100", "111"),
    "3": ("111", "001", "111", "001", "111"),
    "4": ("101", "101", "111", "001", "001"),
    "5": ("111", "100", "111", "001", "111"),
    "6": ("111", "100", "111", "101", "111"),
    "7": ("111", "001", "010", "010", "010"),
    "8": ("111", "101", "111", "101", "111"),
    "9": ("111", "101", "111", "001", "111"),
    "A": ("010", "101", "111", "101", "101"),
    "B": ("110", "101", "110", "101", "110"),
    "C": ("111", "100", "100", "100", "111"),
    "D": ("110", "101", "101", "101", "110"),
    "E": ("111", "100", "110", "100", "111"),
    "F": ("111", "100", "110", "100", "100"),
    "G": ("111", "100", "101", "101", "111"),
    "H": ("101", "101", "111", "101", "101"),
    "I": ("111", "010", "010", "010", "111"),
    "J": ("001", "001", "001", "101", "111"),
    "K": ("101", "101", "110", "101", "101"),
    "L": ("100", "100", "100", "100", "111"),
    "M": ("101", "111", "111", "101", "101"),
    "N": ("101", "111", "111", "111", "101"),
    "O": ("111", "101", "101", "101", "111"),
    "P": ("111", "101", "111", "100", "100"),
    "Q": ("111", "101", "101", "111", "001"),
    "R": ("111", "101", "111", "110", "101"),
    "S": ("111", "100", "111", "001", "111"),
    "T": ("111", "010", "010", "010", "010"),
    "U": ("101", "101", "101", "101", "111"),
    "V": ("101", "101", "101", "101", "010"),
    "W": ("101", "101", "111", "111", "101"),
    "X": ("101", "101", "010", "101", "101"),
    "Y": ("101", "101", "010", "010", "010"),
    "Z": ("111", "001", "010", "100", "111"),
}


def text_width(text: str) -> int:
    return max(0, len(text) * CHAR_STEP - 2)


def text_width_scaled(text: str, scale: int) -> int:
    return max(0, len(text) * (GLYPH_W * scale + 2) - 2)


def draw_text_scaled(x: int, y: int, text: str, col: int, scale: int) -> None:
    cursor_x = x
    for char in text.upper():
        glyph = FONT.get(char, FONT[" "])
        for row, bits in enumerate(glyph):
            for column, bit in enumerate(bits):
                if bit == "1":
                    pyxel.rect(
                        cursor_x + column * scale,
                        y + row * scale,
                        scale,
                        scale,
                        col,
                    )
        cursor_x += GLYPH_W * scale + 2


def draw_big_text(x: int, y: int, text: str, col: int) -> None:
    draw_text_scaled(x, y, text, col, SCALE)


def draw_bold_text(x: int, y: int, text: str, col: int) -> None:
    draw_big_text(x + 1, y, text, 0)
    draw_big_text(x, y, text, col)


def draw_bold_text_scaled(x: int, y: int, text: str, col: int, scale: int) -> None:
    draw_text_scaled(x + 1, y, text, 0, scale)
    draw_text_scaled(x, y, text, col, scale)


def menu_button_rect(width: int, height: int) -> tuple[int, int, int, int]:
    button_w = 70
    button_h = 22
    return ((width - button_w) // 2, height - button_h - 8, button_w, button_h)


def menu_panel_rect(width: int, height: int) -> tuple[int, int, int, int]:
    panel_w = min(width - 16, 244)
    panel_h = 118
    button_x, button_y, _, _ = menu_button_rect(width, height)
    x = max(8, min(width - panel_w - 8, button_x + 35 - panel_w // 2))
    return (x, max(8, button_y - panel_h - 6), panel_w, panel_h)


def panel_toggle_rects(width: int, height: int) -> dict[str, tuple[int, int, int, int]]:
    x, y, w, _ = menu_panel_rect(width, height)
    button_w = max(68, (w - 32) // 3)
    return {
        "info": (x + 8, y + 34, button_w, 24),
        "guides": (x + 12 + button_w, y + 34, button_w, 24),
        "constellations": (x + 16 + button_w * 2, y + 34, button_w, 24),
        "side": (x + 8, y + 74, min(96, w - 16), 24),
    }


def draw_button(rect: tuple[int, int, int, int], label: str, active: bool) -> None:
    x, y, w, h = rect
    fill = 5 if active else 1
    edge = 10 if active else 13
    pyxel.rect(x, y, w, h, fill)
    pyxel.rectb(x, y, w, h, edge)
    draw_big_text(x + max(4, (w - text_width(label)) // 2), y + 7, label, 7)


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
    lines = _hud_lines(observer, clock, camera, mode, selected, show_constellations)
    y = 8
    for line in lines:
        draw_big_text(8, y, line, 7)
        y += LINE_STEP

    if can_capture:
        draw_big_text(8, pyxel.height - 48, f"{selected.id} FOUND", 10)
        draw_big_text(8, pyxel.height - 35, "ENTER CAPTURE", 7)
    elif latest_capture is not None:
        draw_big_text(8, pyxel.height - 35, f"CAPTURED {latest_capture.constellation_id}", 11)


def draw_compact_time(clock: SimulationClock) -> None:
    scale = 3
    draw_bold_text_scaled(8, 8, clock.current_time.strftime("%b %d"), 7, scale)
    draw_bold_text_scaled(8, 27, clock.current_time.strftime("%H:%M"), 7, scale)


def draw_constellation_labels(
    constellations: tuple[Constellation, ...],
    selected_constellation: Constellation,
    points: dict[int, ScreenPoint],
) -> None:
    for index, constellation in enumerate(constellations):
        draw_constellation_label(
            constellation,
            points,
            10 if constellation.id == selected_constellation.id else 13,
            index,
        )


def draw_constellation_label(
    constellation: Constellation,
    points: dict[int, ScreenPoint],
    color: int,
    index: int,
) -> None:
    visible = [points[star_id] for star_id in constellation.main_star_ids if star_id in points]
    if len(visible) < 2:
        return
    center_x = int(sum(point.x for point in visible) / len(visible))
    center_y = int(sum(point.y for point in visible) / len(visible))
    label = constellation.name.upper()
    label_x = max(4, min(pyxel.width - text_width(label) - 4, center_x + 10))
    label_y = max(88, min(pyxel.height - 76, center_y - 18 + (index % 3) * 12))
    pyxel.line(center_x, center_y, label_x - 3, label_y + 6, color)
    draw_bold_text(label_x, label_y, label, color)


def draw_focused_star(point: ScreenPoint, name: str) -> None:
    x = int(point.x)
    y = int(point.y)
    pyxel.rectb(x - 5, y - 5, 11, 11, 8)
    pyxel.rectb(x - 6, y - 6, 13, 13, 8)
    label = name.upper()
    label_x = x + 12
    if label_x + text_width(label) > pyxel.width - 4:
        label_x = x - text_width(label) - 12
    label_x = max(4, min(pyxel.width - text_width(label) - 4, label_x))
    label_y = max(4, min(pyxel.height - 18, y - 7))
    line_x = label_x - 3 if label_x > x else label_x + text_width(label) + 3
    pyxel.line(x + 7 if label_x > x else x - 7, y, line_x, label_y + 6, 8)
    draw_bold_text(label_x, label_y, label, 8)


def _hud_lines(
    observer: Observer,
    clock: SimulationClock,
    camera: SkyCamera,
    mode: str,
    selected: Constellation,
    show_constellations: bool,
) -> list[str]:
    if pyxel.width < 300:
        return [
            f"LAT {observer.latitude_deg:+04.1f}",
            f"LON {observer.longitude_deg:+05.1f}",
            clock.current_time.strftime("%Y-%m-%d"),
            clock.current_time.strftime("%H:%M %z"),
            f"{mode} {'PLAY' if clock.running else 'PAUSE'}",
            f"{selected.id} C:{'ON' if show_constellations else 'OFF'} F:{camera.fov_deg:03.0f}",
        ]
    return [
        f"LAT {observer.latitude_deg:+04.1f} LON {observer.longitude_deg:+05.1f}",
        clock.current_time.strftime("%Y-%m-%d  %H:%M %z"),
        f"{mode} {'PLAY' if clock.running else 'PAUSE'}",
        f"{selected.id} {selected.name.upper()} C:{'ON' if show_constellations else 'OFF'} F:{camera.fov_deg:03.0f}",
    ]


def draw_menu_button(opened: bool) -> None:
    draw_button(menu_button_rect(pyxel.width, pyxel.height), "CLOSE" if opened else "MENU", True)


def draw_menu_panel(
    show_info: bool,
    show_guides: bool,
    show_constellations: bool,
    slider_side: str,
) -> None:
    x, y, w, h = menu_panel_rect(pyxel.width, pyxel.height)
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 13)
    draw_big_text(x + 8, y + 8, "DISPLAY", 7)
    draw_button(panel_toggle_rects(pyxel.width, pyxel.height)["info"], "INFO", show_info)
    draw_button(panel_toggle_rects(pyxel.width, pyxel.height)["guides"], "GUIDE", show_guides)
    draw_button(panel_toggle_rects(pyxel.width, pyxel.height)["constellations"], "CONST", show_constellations)
    draw_big_text(x + 8, y + 63, "SLIDER", 7)
    draw_button(panel_toggle_rects(pyxel.width, pyxel.height)["side"], slider_side.upper(), True)


def tool_button_rects(width: int, _height: int) -> dict[str, tuple[int, int, int, int]]:
    button_w = 62
    button_h = 22
    x = max(6, width - button_w - 6)
    return {
        "time": (x, 8, button_w, button_h),
        "month": (x, 34, button_w, button_h),
        "reset": (x, 60, button_w, button_h),
    }


def draw_tool_buttons(show_time_slider: bool, show_month_slider: bool) -> None:
    rects = tool_button_rects(pyxel.width, pyxel.height)
    draw_button(rects["time"], "TIME", show_time_slider)
    draw_button(rects["month"], "MONTH", show_month_slider)
    draw_button(rects["reset"], "RESET", False)


def slider_rects(width: int, height: int, side: str) -> dict[str, tuple[int, int, int, int]]:
    panel_w = 34
    panel_h = min(440, max(230, height - 210))
    x = width - panel_w - 6 if side == "right" else 6
    y = max(92, (height - panel_h) // 2)
    return {
        "time_minus": (x + 5, y + 8, 24, 22),
        "time_track": (x + 15, y + 34, 4, panel_h - 68),
        "time_knob": (x + 8, y + panel_h // 2 - 10, 18, 20),
        "time_plus": (x + 5, y + panel_h - 30, 24, 22),
        "month_minus": (x + 5, y + 8, 24, 22),
        "month_track": (x + 15, y + 34, 4, panel_h - 68),
        "month_knob": (x + 8, y + panel_h // 2 - 10, 18, 20),
        "month_plus": (x + 5, y + panel_h - 30, 24, 22),
        "panel": (x, y, panel_w, panel_h),
    }


def draw_slider(side: str, label: str, knob_ratio: float = 0.5) -> None:
    rects = slider_rects(pyxel.width, pyxel.height, side)
    x, y, w, h = rects["panel"]
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 13)
    label_x = max(4, min(pyxel.width - text_width(label) - 4, x + 5))
    draw_big_text(label_x, y - 14, label, 7)
    draw_button(rects[f"{label.lower()}_minus"], "-", False)
    track = rects[f"{label.lower()}_track"]
    pyxel.rect(track[0], track[1], track[2], track[3], 13)
    knob = rects[f"{label.lower()}_knob"]
    knob_y = int(track[1] + max(0.0, min(1.0, knob_ratio)) * track[3] - knob[3] / 2)
    knob_y = max(track[1], min(track[1] + track[3] - knob[3], knob_y))
    pyxel.rect(knob[0], knob_y, knob[2], knob[3], 5)
    pyxel.rectb(knob[0], knob_y, knob[2], knob[3], 10)
    draw_button(rects[f"{label.lower()}_plus"], "+", False)
