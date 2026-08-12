from __future__ import annotations

import pyxel

from astronomy.catalog import Constellation
from astronomy.observer import Observer
from data.sky_features import ASTERISMS, SKY_PATHS, Asterism, SkyPath
from data.font_jp import FONT_CELL_HEIGHT, FONT_CELL_WIDTH, FONT_COLUMNS, FONT_IMAGE_BANK, GLYPHS
from sky.capture import ScreenPoint, SkyCapture
from sky.camera import SkyCamera
from sky.letters import ExchangeLog, PresetLetter, display_letter_text
from sky.meteors import MeteorEventView
from sky.simulation import SimulationClock
from ui.localization import Language, constellation_name, meteor_event_name, sky_feature_name

SCALE = 2
GLYPH_W = 3
GLYPH_H = 5
CHAR_STEP = 8
LINE_STEP = 13
JAPANESE_CONSTELLATION_LABEL_LIMIT = 8
FEATURE_COLOR = 11
_font_atlas_ready = False
_display_width_cache: dict[str, int] = {}
_glyph_locations: dict[int, tuple[int, int, int]] = {}

FONT = {
    " ": ("000", "000", "000", "000", "000"),
    "(": ("010", "100", "100", "100", "010"),
    ")": ("010", "001", "001", "001", "010"),
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


def display_text_width(text: str) -> int:
    if text.isascii():
        return text_width(text)
    cached = _display_width_cache.get(text)
    if cached is not None:
        return cached
    width = sum(_glyph_advance(char) for char in text)
    _display_width_cache[text] = width
    return width


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


def draw_display_bold_text(x: int, y: int, text: str, col: int) -> None:
    if text.isascii():
        draw_bold_text(x, y, text.upper(), col)
        return
    _draw_bitmap_text(x + 1, y + 1, text, 0)
    _draw_bitmap_text(x, y, text, col)


def draw_display_text(x: int, y: int, text: str, col: int) -> None:
    if text.isascii():
        draw_big_text(x, y, text.upper(), col)
        return
    _draw_bitmap_text(x, y, text, col)


def _glyph_advance(char: str) -> int:
    glyph = GLYPHS.get(ord(char)) or GLYPHS.get(ord("?"))
    if glyph is None:
        return FONT_CELL_WIDTH
    return glyph[0]


def _ensure_font_atlas() -> None:
    global _font_atlas_ready
    if _font_atlas_ready:
        return
    image = pyxel.image(FONT_IMAGE_BANK)
    for index, (codepoint, (advance, rows)) in enumerate(GLYPHS.items()):
        x = index % FONT_COLUMNS * FONT_CELL_WIDTH
        y = index // FONT_COLUMNS * FONT_CELL_HEIGHT
        image.set(x, y, list(rows))
        _glyph_locations[codepoint] = (x, y, advance)
    _font_atlas_ready = True


def _draw_bitmap_text(x: int, y: int, text: str, col: int) -> None:
    _ensure_font_atlas()
    cursor_x = x
    if col != 7:
        pyxel.pal(7, col)
    for char in text:
        codepoint = ord(char)
        location = _glyph_locations.get(codepoint) or _glyph_locations.get(ord("?"))
        if location is None:
            cursor_x += FONT_CELL_WIDTH
            continue
        source_x, source_y, advance = location
        pyxel.blt(cursor_x, y, FONT_IMAGE_BANK, source_x, source_y, FONT_CELL_WIDTH, FONT_CELL_HEIGHT, 0)
        cursor_x += advance
    if col != 7:
        pyxel.pal()


def draw_bold_text_scaled(x: int, y: int, text: str, col: int, scale: int) -> None:
    draw_text_scaled(x + 1, y, text, 0, scale)
    draw_text_scaled(x, y, text, col, scale)


def menu_button_rect(width: int, height: int) -> tuple[int, int, int, int]:
    button_w = 70
    button_h = 22
    return ((width - button_w) // 2, height - button_h - 38, button_w, button_h)


def main_button_rects(width: int, height: int) -> dict[str, tuple[int, int, int, int]]:
    gap = 6
    side = 8
    button_h = 26
    y = height - button_h - 6
    button_w = max(64, (width - side * 2 - gap * 2) // 3)
    return {
        "letter": (side, y, button_w, button_h),
        "log": (side + button_w + gap, y, button_w, button_h),
        "capture": (side + (button_w + gap) * 2, y, button_w, button_h),
    }


def back_button_rect(_width: int, _height: int) -> tuple[int, int, int, int]:
    return (8, 8, 64, 24)


def log_item_rects(width: int, height: int, count: int) -> list[tuple[int, int, int, int]]:
    x = 24
    y = 76
    w = width - 48
    row_h = 24
    visible_count = min(count, max(0, (height - y - 52) // row_h))
    return [(x, y + index * row_h, w, row_h - 3) for index in range(visible_count)]


def letter_panel_rect(width: int, height: int) -> tuple[int, int, int, int]:
    x = 18
    y = max(76, height // 2 - 84)
    w = width - 36
    h = min(230, height - y - 44)
    return (x, y, w, h)


def letter_close_rect(width: int, height: int) -> tuple[int, int, int, int]:
    x, y, w, _ = letter_panel_rect(width, height)
    return (x + w - 30, y + 6, 22, 22)


def log_panel_rect(width: int, height: int) -> tuple[int, int, int, int]:
    return (18, 52, width - 36, height - 96)


def menu_panel_rect(width: int, height: int) -> tuple[int, int, int, int]:
    panel_w = min(width - 16, 244)
    panel_h = 208
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
        "features": (x + 8, y + 64, min(112, w - 16), 24),
        "side": (x + 8, y + 104, min(96, w - 16), 24),
        "language": (x + 8, y + 176, min(96, w - 16), 24),
    }


def draw_button(rect: tuple[int, int, int, int], label: str, active: bool) -> None:
    x, y, w, h = rect
    fill = 5 if active else 1
    edge = 10 if active else 13
    pyxel.rect(x, y, w, h, fill)
    pyxel.rectb(x, y, w, h, edge)
    draw_big_text(x + max(4, (w - text_width(label)) // 2), y + 7, label, 7)


def draw_main_buttons(has_unread: bool, capture_pending: bool) -> None:
    rects = main_button_rects(pyxel.width, pyxel.height)
    draw_button(rects["letter"], "LETTER ." if has_unread else "LETTER", has_unread)
    draw_button(rects["log"], "LOG", False)
    draw_button(rects["capture"], "CAPTURE" if not capture_pending else "WAIT", False)


def draw_back_button() -> None:
    draw_button(back_button_rect(pyxel.width, pyxel.height), "BACK", False)


def draw_cut_in(message: str, frame_age: int, duration_frames: int) -> None:
    if frame_age < 0 or frame_age >= duration_frames:
        return
    edge = max(1, duration_frames // 5)
    if frame_age < edge:
        color = 13
    elif frame_age > duration_frames - edge:
        color = 13
    else:
        color = 7
    width = display_text_width(message)
    x = max(8, min(pyxel.width - width - 8, (pyxel.width - width) // 2))
    y = 42
    pyxel.rect(max(0, x - 10), y - 8, min(pyxel.width, width + 20), 28, 0)
    pyxel.rectb(max(0, x - 10), y - 8, min(pyxel.width, width + 20), 28, 1)
    draw_display_bold_text(x, y, message, color)


def draw_hud(
    observer: Observer,
    clock: SimulationClock,
    camera: SkyCamera,
    mode: str,
    selected: Constellation,
    show_constellations: bool,
    can_capture: bool,
    latest_capture: SkyCapture | None,
    language: Language,
) -> None:
    lines = _hud_lines(observer, clock, camera, mode, selected, show_constellations, language)
    y = 8
    for line in lines:
        draw_display_bold_text(8, y, line, 7)
        y += LINE_STEP

    if can_capture:
        draw_big_text(8, pyxel.height - 48, f"{selected.id} FOUND", 10)
        draw_big_text(8, pyxel.height - 35, "ENTER CAPTURE", 7)
    elif latest_capture is not None:
        draw_big_text(8, pyxel.height - 35, f"CAPTURED {latest_capture.selected_constellation_id or 'SKY'}", 11)


def draw_compact_time(clock: SimulationClock) -> None:
    scale = 3
    draw_bold_text_scaled(8, 8, clock.current_time.strftime("%b %d"), 7, scale)
    draw_bold_text_scaled(8, 27, clock.current_time.strftime("%H:%M"), 7, scale)


def draw_constellation_labels(
    constellations: tuple[Constellation, ...],
    selected_constellation: Constellation,
    points: dict[int, ScreenPoint],
    language: Language,
) -> None:
    candidates = [
        (index, constellation, _constellation_label_center(constellation, points))
        for index, constellation in enumerate(constellations)
    ]
    visible = [(index, constellation, center) for index, constellation, center in candidates if center is not None]
    if language == "ja":
        screen_center_x = pyxel.width * 0.5
        screen_center_y = pyxel.height * 0.5
        visible.sort(
            key=lambda item: (
                item[1].id != selected_constellation.id,
                (item[2][0] - screen_center_x) ** 2 + (item[2][1] - screen_center_y) ** 2,
            )
        )
        visible = visible[:JAPANESE_CONSTELLATION_LABEL_LIMIT]
    for index, constellation, center in visible:
        selected = constellation.id == selected_constellation.id
        draw_constellation_label(
            constellation,
            center,
            10 if selected else 13,
            index,
            language,
            selected,
        )


def _constellation_label_center(
    constellation: Constellation,
    points: dict[int, ScreenPoint],
) -> tuple[int, int] | None:
    visible = [points[star_id] for star_id in constellation.main_star_ids if star_id in points]
    if len(visible) < 2:
        return None
    center_x = int(sum(point.x for point in visible) / len(visible))
    center_y = int(sum(point.y for point in visible) / len(visible))
    return center_x, center_y


def draw_constellation_label(
    constellation: Constellation,
    center: tuple[int, int],
    color: int,
    index: int,
    language: Language,
    selected: bool,
) -> None:
    center_x, center_y = center
    label = constellation_name(constellation, language)
    width = display_text_width(label)
    label_x = max(4, min(pyxel.width - width - 4, center_x + 10))
    label_y = max(88, min(pyxel.height - 76, center_y - 18 + (index % 3) * 12))
    pyxel.line(center_x, center_y, label_x - 3, label_y + 6, color)
    if selected:
        draw_display_bold_text(label_x, label_y, label, color)
    else:
        draw_display_text(label_x, label_y, label, color)


def draw_sky_features(
    points: dict[int, ScreenPoint],
    sky_paths: dict[str, list[tuple[float, float] | None]],
    language: Language,
) -> None:
    for path in SKY_PATHS:
        draw_sky_path(path, sky_paths.get(path.id, []), language)
    for index, asterism in enumerate(ASTERISMS):
        draw_asterism(asterism, points, index, language)


def draw_asterism(
    asterism: Asterism,
    points: dict[int, ScreenPoint],
    index: int,
    language: Language,
) -> None:
    visible = [points[star_id] for star_id in asterism.star_ids if star_id in points]
    if len(visible) < 2:
        return
    for a_id, b_id in asterism.edges:
        a = points.get(a_id)
        b = points.get(b_id)
        if a is None or b is None:
            continue
        pyxel.line(int(a.x), int(a.y), int(b.x), int(b.y), FEATURE_COLOR)
    center_x = int(sum(point.x for point in visible) / len(visible))
    center_y = int(sum(point.y for point in visible) / len(visible))
    label = sky_feature_name(asterism, language)
    width = display_text_width(label)
    label_x = max(4, min(pyxel.width - width - 4, center_x + 8))
    label_y = max(58, min(pyxel.height - 76, center_y - 22 + (index % 2) * 12))
    pyxel.line(center_x, center_y, label_x - 3, label_y + 6, FEATURE_COLOR)
    draw_display_text(label_x, label_y, label, FEATURE_COLOR)


def draw_sky_path(
    path: SkyPath,
    points: list[tuple[float, float] | None],
    language: Language,
) -> None:
    if not points:
        return
    last: tuple[float, float] | None = None
    visible_points: list[tuple[float, float]] = []
    for index, point in enumerate(points):
        if point is None:
            last = None
            continue
        x, y = point
        if 0 <= x < pyxel.width and 0 <= y < pyxel.height:
            visible_points.append(point)
        if last is not None and index % 2 == 0:
            pyxel.line(int(last[0]), int(last[1]), int(x), int(y), FEATURE_COLOR)
        elif index % 2 == 1:
            pyxel.pset(int(x), int(y), FEATURE_COLOR)
        last = point
    if len(visible_points) < 2:
        return
    label_x, label_y = visible_points[len(visible_points) // 2]
    label = sky_feature_name(path, language)
    width = display_text_width(label)
    x = max(4, min(pyxel.width - width - 4, int(label_x) + 8))
    y = max(58, min(pyxel.height - 76, int(label_y) - 10))
    draw_display_text(x, y, label, FEATURE_COLOR)


def draw_focused_star(point: ScreenPoint, name: str) -> None:
    x = int(point.x)
    y = int(point.y)
    pyxel.rectb(x - 5, y - 5, 11, 11, 8)
    pyxel.rectb(x - 6, y - 6, 13, 13, 8)
    label = name
    width = display_text_width(label)
    label_x = x + 12
    if label_x + width > pyxel.width - 4:
        label_x = x - width - 12
    label_x = max(4, min(pyxel.width - width - 4, label_x))
    label_y = max(4, min(pyxel.height - 18, y - 7))
    line_x = label_x - 3 if label_x > x else label_x + width + 3
    pyxel.line(x + 7 if label_x > x else x - 7, y, line_x, label_y + 6, 8)
    draw_display_bold_text(label_x, label_y, label, 8)


def draw_meteor_event(event_view: MeteorEventView, language: Language) -> None:
    if event_view.radiant_screen is None:
        return
    radiant_x, radiant_y = event_view.radiant_screen
    label = meteor_event_name(event_view.event, language)
    width = display_text_width(label)
    label_x = max(4, min(pyxel.width - width - 4, int(radiant_x) + 10))
    label_y = max(58, min(pyxel.height - 76, int(radiant_y) - 8))
    if 0 <= radiant_x < pyxel.width and 0 <= radiant_y < pyxel.height:
        x = int(radiant_x)
        y = int(radiant_y)
        pyxel.rectb(x - 4, y - 4, 9, 9, 10)
        pyxel.line(x, y, label_x - 3 if label_x > x else label_x + width + 3, label_y + 6, 10)
    draw_display_bold_text(label_x, label_y, label, 10)


def draw_event_banner(event_view: MeteorEventView, language: Language) -> None:
    label = meteor_event_name(event_view.event, language)
    width = display_text_width(label)
    x = max(4, min(pyxel.width - width - 4, (pyxel.width - width) // 2))
    draw_display_bold_text(x, 8, label, 10)
    period = _event_period_label(event_view)
    period_x = max(4, min(pyxel.width - text_width(period) - 4, (pyxel.width - text_width(period)) // 2))
    draw_bold_text(period_x, 21, period, 10)


def _event_period_label(event_view: MeteorEventView) -> str:
    start = event_view.event.display_start
    end = event_view.event.display_end
    if start.year == end.year and start.month == end.month:
        date_range = f"{start:%Y/%m/%d}-{end:%d}"
    elif start.year == end.year:
        date_range = f"{start:%Y/%m/%d}-{end:%m/%d}"
    else:
        date_range = f"{start:%Y/%m/%d}-{end:%Y/%m/%d}"
    return f"( {date_range} MIDNIGHT)"


def _hud_lines(
    observer: Observer,
    clock: SimulationClock,
    camera: SkyCamera,
    mode: str,
    selected: Constellation,
    show_constellations: bool,
    language: Language,
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
        f"{selected.id} {constellation_name(selected, language).upper()} C:{'ON' if show_constellations else 'OFF'} F:{camera.fov_deg:03.0f}",
    ]


def draw_menu_button(opened: bool) -> None:
    draw_button(menu_button_rect(pyxel.width, pyxel.height), "CLOSE" if opened else "MENU", True)


def draw_menu_panel(
    show_info: bool,
    show_guides: bool,
    show_constellations: bool,
    show_features: bool,
    slider_side: str,
    event_source_label: str,
    event_count: int,
    language: Language,
) -> None:
    x, y, w, h = menu_panel_rect(pyxel.width, pyxel.height)
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 13)
    draw_big_text(x + 8, y + 8, "DISPLAY", 7)
    draw_button(panel_toggle_rects(pyxel.width, pyxel.height)["info"], "INFO", show_info)
    draw_button(panel_toggle_rects(pyxel.width, pyxel.height)["guides"], "GUIDE", show_guides)
    draw_button(panel_toggle_rects(pyxel.width, pyxel.height)["constellations"], "CONST", show_constellations)
    draw_button(panel_toggle_rects(pyxel.width, pyxel.height)["features"], "FEATURE", show_features)
    draw_big_text(x + 8, y + 93, "SLIDER", 7)
    draw_button(panel_toggle_rects(pyxel.width, pyxel.height)["side"], slider_side.upper(), True)
    draw_big_text(x + 8, y + 135, f"EVENT SRC {event_source_label}", 13)
    draw_big_text(x + 8, y + 148, f"EVENTS {event_count}", 13)
    draw_big_text(x + 8, y + 162, "LANGUAGE", 7)
    language_label = "JA" if language == "en" else "EN"
    draw_button(panel_toggle_rects(pyxel.width, pyxel.height)["language"], language_label, True)


def draw_letter_view(log: ExchangeLog, letter: PresetLetter, language: Language) -> None:
    x, y, w, h = letter_panel_rect(pyxel.width, pyxel.height)
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 13)
    draw_back_button()
    draw_big_text(x + 10, y + 10, "LETTER", 7)
    draw_button(letter_close_rect(pyxel.width, pyxel.height), "X", False)

    primary, original = display_letter_text(letter, language)
    cursor_y = y + 34
    for line in _wrap_body_lines(primary, w - 20):
        _draw_body_text(x + 10, cursor_y, line, 7)
        cursor_y += 15
    if original is not None and cursor_y < y + h - 58:
        cursor_y += 4
        draw_big_text(x + 10, cursor_y, "- ORIGINAL -", 13)
        cursor_y += 14
        for line in _wrap_body_lines(original, w - 20)[:5]:
            _draw_body_text(x + 10, cursor_y, line, 13)
            cursor_y += 15

    location = _letter_location(letter)
    draw_display_text(x + 10, y + h - 22, f"FROM {location}", 13)


def draw_log_list(logs: tuple[ExchangeLog, ...], letters_by_id: dict[str, PresetLetter]) -> None:
    x, y, w, h = log_panel_rect(pyxel.width, pyxel.height)
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 13)
    draw_back_button()
    draw_big_text(x + 10, y + 12, "LOG", 7)
    visible_logs = tuple(reversed(logs))[: len(log_item_rects(pyxel.width, pyxel.height, len(logs)))]
    if not visible_logs:
        draw_big_text(x + 10, y + 42, "NO LETTERS", 13)
        return
    for index, log in enumerate(visible_logs):
        rect = log_item_rects(pyxel.width, pyxel.height, len(logs))[index]
        letter = letters_by_id.get(log.received_letter_id)
        label = _log_row_label(log, letter)
        pyxel.rect(rect[0], rect[1], rect[2], rect[3], 0)
        pyxel.rectb(rect[0], rect[1], rect[2], rect[3], 1)
        draw_big_text(rect[0] + 8, rect[1] + 7, label, 13)


def _log_row_label(log: ExchangeLog, letter: PresetLetter | None) -> str:
    constellation = log.capture.selected_constellation_id or "---"
    country = letter.country_code if letter is not None else "--"
    return f"{log.received_at:%m.%d} {constellation[:10]:<10} {country}"


def _letter_location(letter: PresetLetter) -> str:
    parts = [letter.country_code]
    if letter.region:
        parts.append(letter.region)
    if letter.city:
        parts.append(letter.city)
    return " / ".join(parts)


def _wrap_display_lines(text: str, max_width: int) -> list[str]:
    if not text:
        return [""]
    lines: list[str] = []
    current = ""
    tokens = text.split(" ") if text.isascii() else list(text)
    separator = " " if text.isascii() else ""
    for token in tokens:
        candidate = token if not current else current + separator + token
        if current and display_text_width(candidate) > max_width:
            lines.append(current)
            current = token
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def _wrap_body_lines(text: str, max_width: int) -> list[str]:
    if not text:
        return [""]
    lines: list[str] = []
    current = ""
    tokens = text.split(" ") if text.isascii() else list(text)
    separator = " " if text.isascii() else ""
    for token in tokens:
        candidate = token if not current else current + separator + token
        if current and _body_text_width(candidate) > max_width:
            lines.append(current)
            current = token
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def _body_text_width(text: str) -> int:
    return sum(_glyph_advance(char) for char in text)


def _draw_body_text(x: int, y: int, text: str, col: int) -> None:
    _draw_bitmap_text(x, y, text, col)


def tool_button_rects(width: int, _height: int) -> dict[str, tuple[int, int, int, int]]:
    button_w = 62
    button_h = 22
    x = max(6, width - button_w - 6)
    return {
        "time": (x, 8, button_w, button_h),
        "month": (x, 34, button_w, button_h),
        "event": (x, 60, button_w, button_h),
        "reset": (x, 86, button_w, button_h),
    }


def draw_tool_buttons(show_time_slider: bool, show_month_slider: bool, show_event_slider: bool) -> None:
    rects = tool_button_rects(pyxel.width, pyxel.height)
    draw_button(rects["time"], "TIME", show_time_slider)
    draw_button(rects["month"], "DAY", show_month_slider)
    draw_button(rects["event"], "EVENT", show_event_slider)
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
        "event_minus": (x + 5, y + 8, 24, 22),
        "event_track": (x + 15, y + 34, 4, panel_h - 68),
        "event_knob": (x + 8, y + panel_h // 2 - 10, 18, 20),
        "event_plus": (x + 5, y + panel_h - 30, 24, 22),
        "panel": (x, y, panel_w, panel_h),
    }


def draw_slider(side: str, label: str, knob_ratio: float = 0.5, rect_key: str | None = None) -> None:
    rects = slider_rects(pyxel.width, pyxel.height, side)
    key = rect_key or label.lower()
    x, y, w, h = rects["panel"]
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 13)
    label_x = max(4, min(pyxel.width - text_width(label) - 4, x + 5))
    draw_big_text(label_x, y - 14, label, 7)
    draw_button(rects[f"{key}_minus"], "+", False)
    track = rects[f"{key}_track"]
    pyxel.rect(track[0], track[1], track[2], track[3], 13)
    knob = rects[f"{key}_knob"]
    knob_y = int(track[1] + max(0.0, min(1.0, knob_ratio)) * track[3] - knob[3] / 2)
    knob_y = max(track[1], min(track[1] + track[3] - knob[3], knob_y))
    pyxel.rect(knob[0], knob_y, knob[2], knob[3], 5)
    pyxel.rectb(knob[0], knob_y, knob[2], knob[3], 10)
    draw_button(rects[f"{key}_plus"], "-", False)
