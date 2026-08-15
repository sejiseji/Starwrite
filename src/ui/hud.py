from __future__ import annotations

from dataclasses import dataclass

import pyxel

from src.astronomy.catalog import Constellation
from src.astronomy.events import LunarEclipseEvent, MeteorShowerEvent
from src.astronomy.moon import MoonState
from src.astronomy.observer import Observer
try:
    from src.data.constellation_descriptions import CONSTELLATION_DESCRIPTIONS
except Exception:
    # GitHub Pages can briefly serve cached 404s for new Python modules.
    # Keep a source-authored fallback here so the sky never falls back to anchor-star copy.
    CONSTELLATION_DESCRIPTIONS: dict[str, dict[str, tuple[str, str]]] = {'ORI': {'ja': ('三つ星を帯に並べた狩人。', '冬空でひときわ堂々と立つ。'),
             'en': ('Three stars belt the great hunter.', 'He rules the winter night.')},
     'CYG': {'ja': ('十字の翼で天の川を渡る。', '尾には青白いデネブが光る。'),
             'en': ('A swan crosses the Milky Way.', 'Deneb burns at its tail.')},
     'CAS': {'ja': ('五つの星が描く折れた王座。', '北の空で季節ごとに向きを変える。'),
             'en': ('Five stars bend into a throne.', 'It wheels around the northern sky.')},
     'UMA': {'ja': ('北斗七星を背に抱く大熊。', '春の夜空を大きく歩く。'),
             'en': ('The Great Bear bears the Dipper.', 'Spring finds it roaming the north.')},
     'SCO': {'ja': ('赤い心臓を抱く長いさそり。', '夏の南天で尾を鋭く曲げる。'),
             'en': ('A red heart burns in the scorpion.', 'Its hooked tail cuts the south.')},
     'LEO': {'ja': ('逆向きのはてなが獅子を描く。', '春空を駆ける王者の横顔。'),
             'en': ('A backward hook outlines the lion.', 'The lion strides through spring.')},
     'TAU': {'ja': ('V字の顔と角を掲げる牡牛。', '冬の星群を押し分けて進む。'),
             'en': ('A V-shaped face lifts two horns.', 'The bull shoulders through winter.')},
     'GEM': {'ja': ('並んで輝く双子の頭。', '肩を寄せて冬の空を旅する。'),
             'en': ('Twin heads shine side by side.', 'They cross the winter sky as one.')},
     'CMA': {'ja': ('シリウスを先頭に走る大犬。', '狩人の足元を冬じゅう駆ける。'),
             'en': ('Sirius leads the great hound.', "It runs at Orion's winter heels.")},
     'LYR': {'ja': ('小さな竪琴にベガが鳴る。', '夏の高空へ澄んだ光を放つ。'),
             'en': ('Vega rings from a tiny lyre.', 'Clear light spills through summer.')},
     'AQL': {'ja': ('アルタイルを胸に広げた鷲。', '天の川を横切り翼を伸ばす。'),
             'en': ("Altair marks the eagle's breast.", 'Wide wings cross the Milky Way.')},
     'BOO': {'ja': ('北斗の柄をたどる星の番人。', '橙のアークトゥルスが目印。'),
             'en': ("Follow the Dipper's handle to him.", 'Arcturus glows amber nearby.')},
     'CRU': {'ja': ('四つの星が刻む南の十字。', '旅人に方角を教えた小さな印。'),
             'en': ('Four stars carve a southern cross.', 'A small sign once guided voyagers.')},
     'CEN': {'ja': ('半人半馬の賢者が南を守る。', '明るい二星が十字を導く。'),
             'en': ('A wise centaur guards the south.', 'Two bright stars point to Crux.')},
     'CAR': {'ja': ('失われた大船の竜骨の部分。', 'カノープスが南海を照らす。'),
             'en': ("The keel remains from Argo's ship.", 'Canopus lights the southern sea.')},
     'VIR': {'ja': ('麦穂を手にした大地の乙女。', 'スピカが春の実りを青く示す。'),
             'en': ('A maiden carries an ear of wheat.', 'Blue Spica signals spring harvest.')},
     'PEG': {'ja': ('四辺形から翼ある馬が駆け出す。', '秋空に大きな窓を開く。'),
             'en': ('A great square opens into wings.', 'Pegasus leaps across autumn.')},
     'AND': {'ja': ('鎖につながれた王女の姿。', '秋の空から銀河の隣人を望む。'),
             'en': ('A chained princess spans autumn.', 'Her realm holds a nearby galaxy.')},
     'PER': {'ja': ('剣を掲げ怪物へ向かう英雄。', '秋には流星の放射点も宿す。'),
             'en': ("The hero raises a monster's head.", 'Autumn meteors stream from here.')},
     'AUR': {'ja': ('五角形の車を操る御者。', '黄金のカペラが冬路を照らす。'),
             'en': ('A five-sided chariot rolls high.', 'Capella lights the winter road.')},
     'DRA': {'ja': ('北極を囲み長くうねる竜。', '古い星座の間を静かに守る。'),
             'en': ('The dragon coils around the pole.', 'It guards the old northern stars.')},
     'CEP': {'ja': ('とがった屋根を持つ北の王。', '星々の回転を玉座から眺める。'),
             'en': ('A peaked roof crowns the sky king.', 'He watches the stars turn below.')},
     'AQR': {'ja': ('壺から水を注ぐ青年。', '秋の空へ淡い星の流れをほどく。'),
             'en': ('A youth pours water from a jar.', 'Faint streams loosen through fall.')},
     'CAP': {'ja': ('山羊の頭と魚の尾を持つ。', '夏から秋の低い空を泳ぐ。'),
             'en': ('Goat above, fish below.', 'It swims low from summer to fall.')},
     'UMI': {'ja': ('小さなひしゃくの先に北極星。', '北の軸をそっと指し続ける。'),
             'en': ('Polaris tips the Little Dipper.', 'Its quiet point fixes the north.')},
     'CMI': {'ja': ('プロキオンを先頭に走る小犬。', '冬の大三角の一角を担う。'),
             'en': ('Procyon leads the little hound.', "It joins winter's great triangle.")},
     'ERI': {'ja': ('オリオンの足元から流れる川。', '南へ曲がりながら長く続く。'),
             'en': ('A river starts beneath Orion.', 'It bends far south across the sky.')},
     'CET': {'ja': ('海原から浮かぶ巨大な怪物。', 'ミラは明るさを大きく変える。'),
             'en': ('A sea monster rises from the deep.', 'Mira swells and fades with time.')},
     'PSC': {'ja': ('一本のひもで結ばれた二匹。', '秋の暗い海を別々に泳ぐ。'),
             'en': ('Two fish share one knotted cord.', 'They swim apart through autumn.')},
     'ARI': {'ja': ('黄金の毛皮へ続く牡羊。', '秋の東空に小さな角を向ける。'),
             'en': ('The ram begins the fleece legend.', 'Small horns face the autumn east.')},
     'DEL': {'ja': ('四つの星が小さな菱形を作る。', '天の川近くでイルカが跳ねる。'),
             'en': ('Four stars make a tiny diamond.', 'A dolphin leaps by the Milky Way.')},
     'SGE': {'ja': ('夜空を横切る一本の矢。', '小さくても形は驚くほど鋭い。'),
             'en': ('One arrow flies across the night.', 'Tiny, yet sharply drawn.')},
     'VUL': {'ja': ('白鳥と矢の間に潜む小狐。', '淡い星野へ静かな気配を残す。'),
             'en': ('A fox hides by the Swan and Arrow.', 'A faint trail slips through stars.')},
     'SGR': {'ja': ('弓を引く半人半馬の射手。', '天の川銀河の中心を指し示す。'),
             'en': ('The centaur archer draws his bow.', 'Its arrow marks the galaxy core.')},
     'OPH': {'ja': ('両腕で大蛇を支える医神。', '夏空で黄道をまたいで立つ。'),
             'en': ('A healer grips the great serpent.', 'He straddles the summer zodiac.')},
     'HER': {'ja': ('ひざをつく怪力の英雄。', '頭上の四辺形が胴を形作る。'),
             'en': ('The strongman kneels overhead.', 'Four stars square his broad torso.')},
     'CRB': {'ja': ('半円の星が宝冠を描く。', '夏の空に小さな飾りを掛ける。'),
             'en': ('Half-ring stars make a crown.', 'Summer wears a small bright jewel.')},
     'LIB': {'ja': ('二つの皿を釣り合わせる秤。', '黄道の上で静かに均衡を取る。'),
             'en': ('Two pans balance on the zodiac.', 'The scales hold measured silence.')},
     'CRV': {'ja': ('四角い胴を持つ黒い鳥。', '春の南空でうみへびに乗る。'),
             'en': ('Four stars shape a black bird.', 'The crow rides Hydra in spring.')},
     'HYA': {'ja': ('星座一長い蛇が空を這う。', '頭から尾まで春の夜を横切る。'),
             'en': ("The sky's longest serpent crawls.", 'Its body crosses the spring night.')},
     'MON': {'ja': ('冬の天の川に立つ一角獣。', '淡い星の森へ角を向ける。'),
             'en': ("A unicorn waits in winter's river.", 'Its horn enters a faint star wood.')},
     'PUP': {'ja': ('大船アルゴーの船尾の名残。', '南の星海で航跡を引く。'),
             'en': ("Argo's stern survives among stars.", 'A wake trails in southern sky.')},
     'VEL': {'ja': ('大船アルゴーの帆を受け継ぐ。', '南風をはらみ星海を進む。'),
             'en': ("Argo's ancient sail fills again.", 'South wind drives the sail onward.')},
     'LUP': {'ja': ('ケンタウルスに捧げられた獣。', '南天で多くの青い星を抱く。'),
             'en': ('A wild beast lies by Centaurus.', 'Blue stars fill its southern hide.')},
     'LEP': {'ja': ('オリオンの足元を逃げる兎。', '冬の南空に耳を伏せる。'),
             'en': ('A hare flees beneath Orion.', "Its ears fold into winter's south.")},
     'CNC': {'ja': ('淡い甲羅の内に星団を抱く蟹。', '春の黄道で静かに横歩きする。'),
             'en': ('A faint crab shelters a star hive.', 'It sidesteps along the zodiac.')},
     'SER': {'ja': ('医神の腕を二つに分ける蛇。', '頭と尾が別の空域を進む。'),
             'en': ('One serpent is split by a bearer.', 'Head and tail cross two skies.')},
     'CVN': {'ja': ('熊を追う二匹の猟犬。', '春の北空を主人と駆ける。'),
             'en': ('Two hunting dogs pursue the Bear.', 'They race through northern spring.')},
     'COM': {'ja': ('王妃が捧げた髪の房。', '無数の淡い星が春風にほどける。'),
             'en': ("A queen's hair became the stars.", 'Soft clusters loosen in spring.')},
     'TRI': {'ja': ('三つの星だけで結ぶ三角。', '秋空に最小級の図形を置く。'),
             'en': ('Three stars form a clean triangle.', 'A small clean shape marks autumn.')},
     'LAC': {'ja': ('稲妻形の星が描く小さな蜥蜴。', '北の秋空で岩陰に潜む。'),
             'en': ('A jagged line sketches a lizard.', 'It hides among the northern rocks.')},
     'LYN': {'ja': ('目を凝らして探す山猫。', '北の淡い星々を長くつなぐ。'),
             'en': ('Only sharp eyes find the lynx.', 'Its faint chain crosses the north.')},
     'PAV': {'ja': ('尾羽を大きく広げる孔雀。', '南天に青白い飾りを並べる。'),
             'en': ('The peacock fans a jeweled tail.', 'Pale plumes fill the southern sky.')},
     'ARA': {'ja': ('神々へ煙を捧げる祭壇。', 'さそりの尾の南で火を灯す。'),
             'en': ('An altar burns below Scorpius.', 'Smoke rises for the ancient gods.')},
     'GRU': {'ja': ('首を伸ばし南へ渡る鶴。', '秋の南天に細い姿を描く。'),
             'en': ('A crane stretches its long neck.', 'It flies across the southern dark.')},
     'PHE': {'ja': ('炎からよみがえる不死鳥。', '南天の星野へ翼を広げる。'),
             'en': ('The phoenix rises out of flame.', 'Its wings open over southern sky.')},
     'COL': {'ja': ('洪水の先を探した白い鳩。', '冬の南空に小さく羽ばたく。'),
             'en': ('A dove searches beyond the flood.', 'Small wings beat in winter sky.')}}
from src.data.sky_features import ASTERISMS, SKY_PATHS, Asterism, SkyPath
from src.sky.capture import ScreenPoint, SkyCapture
from src.sky.camera import SkyCamera
from src.sky.letters import ExchangeLog, PresetLetter, display_letter_text
from src.sky.meteors import MeteorEventView
from src.sky.simulation import SimulationClock
from src.ui.localization import Language, city_name, constellation_name, country_name, sky_event_name, sky_feature_name

SCALE = 2
GLYPH_W = 3
GLYPH_H = 5
CHAR_STEP = 8
LINE_STEP = 13
BODY_TEXT_SCALE = 1
DESKTOP_JAPANESE_BODY_TEXT_SCALE = 2
BODY_LINE_STEP = 15
BODY_COMPACT_LINE_STEP = 13
LETTER_ORIGINAL_SECTION_GAP = BODY_LINE_STEP
JAPANESE_CONSTELLATION_LABEL_LIMIT = 8
FEATURE_COLOR = 11
LETTER_LACE_COLOR = 13
LETTER_LACE_DIM_COLOR = 1
_desktop_letter_text_mode = False
_display_width_cache: dict[str, int] = {}
_glyph_locations: dict[int, tuple[int, int, int, int]] = {}
_font_atlas_next_index = 0
FONT_CELL_WIDTH = 10
FONT_CELL_HEIGHT = 13
FONT_COLUMNS = 25
FONT_IMAGE_BANKS = (0, 1, 2)
GLYPHS: dict[int, tuple[int, tuple[str, ...]]] | None = None

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
    try:
        color = max(0, min(15, int(col)))
    except (TypeError, ValueError, OverflowError):
        color = 7
    try:
        pixel_scale = max(1, int(scale))
    except (TypeError, ValueError, OverflowError):
        pixel_scale = SCALE
    try:
        cursor_x = int(x)
        base_y = int(y)
    except (TypeError, ValueError, OverflowError):
        return
    for char in text.upper():
        glyph = FONT.get(char, FONT[" "])
        for row, bits in enumerate(glyph):
            for column, bit in enumerate(bits):
                if bit == "1":
                    draw_x = cursor_x + column * pixel_scale
                    draw_y = base_y + row * pixel_scale
                    if draw_x < 0 or draw_y < 0 or draw_x >= pyxel.width or draw_y >= pyxel.height:
                        continue
                    pyxel.rect(draw_x, draw_y, pixel_scale, pixel_scale, color)
        cursor_x += GLYPH_W * pixel_scale + 2


def draw_big_text(x: int, y: int, text: str, col: int) -> None:
    draw_text_scaled(x, y, text, col, SCALE)


def set_desktop_letter_text_mode(enabled: bool) -> None:
    global _desktop_letter_text_mode
    _desktop_letter_text_mode = enabled


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


def _ensure_japanese_font_loaded() -> dict[int, tuple[int, tuple[str, ...]]]:
    global GLYPHS
    if GLYPHS is None:
        from src.data.font_jp import GLYPHS as loaded_glyphs

        GLYPHS = loaded_glyphs
    return GLYPHS


def _glyph_advance(char: str) -> int:
    glyphs = _ensure_japanese_font_loaded()
    glyph = glyphs.get(ord(char)) or glyphs.get(ord("?"))
    if glyph is None:
        return FONT_CELL_WIDTH
    return glyph[0]


def _font_atlas_capacity() -> int:
    return FONT_COLUMNS * (256 // FONT_CELL_HEIGHT) * len(FONT_IMAGE_BANKS)


def _glyph_location_for(codepoint: int) -> tuple[int, int, int, int] | None:
    global _font_atlas_next_index
    location = _glyph_locations.get(codepoint)
    if location is not None:
        return location

    glyphs = _ensure_japanese_font_loaded()
    glyph = glyphs.get(codepoint) or glyphs.get(ord("?"))
    if glyph is None:
        return None
    if _font_atlas_next_index >= _font_atlas_capacity():
        _glyph_locations.clear()
        _font_atlas_next_index = 0

    glyphs_per_bank = FONT_COLUMNS * (256 // FONT_CELL_HEIGHT)
    bank_index = _font_atlas_next_index // glyphs_per_bank
    local_index = _font_atlas_next_index % glyphs_per_bank
    bank = FONT_IMAGE_BANKS[bank_index]
    x = local_index % FONT_COLUMNS * FONT_CELL_WIDTH
    y = local_index // FONT_COLUMNS * FONT_CELL_HEIGHT
    advance, rows = glyph
    pyxel.image(bank).set(x, y, list(rows))
    location = (bank, x, y, advance)
    _glyph_locations[codepoint] = location
    _font_atlas_next_index += 1
    return location


def _draw_bitmap_text(x: int, y: int, text: str, col: int, scale: int = 1) -> None:
    try:
        color = max(0, min(15, int(col)))
    except (TypeError, ValueError, OverflowError):
        color = 7
    try:
        cursor_x = int(x)
        base_y = int(y)
    except (TypeError, ValueError, OverflowError):
        return
    glyphs = _ensure_japanese_font_loaded()
    for char in text:
        glyph = glyphs.get(ord(char)) or glyphs.get(ord("?"))
        if glyph is None:
            cursor_x += FONT_CELL_WIDTH * scale
            continue
        advance, rows = glyph
        for row_index, row in enumerate(rows):
            for column_index, value in enumerate(row):
                if value == "0":
                    continue
                draw_x = cursor_x + column_index * scale
                draw_y = base_y + row_index * scale
                if draw_x < 0 or draw_y < 0 or draw_x >= pyxel.width or draw_y >= pyxel.height:
                    continue
                if scale == 1:
                    pyxel.pset(draw_x, draw_y, color)
                else:
                    pyxel.rect(draw_x, draw_y, scale, scale, color)
        cursor_x += advance * scale


def draw_bold_text_scaled(x: int, y: int, text: str, col: int, scale: int) -> None:
    draw_text_scaled(x + 1, y, text, 0, scale)
    draw_text_scaled(x, y, text, col, scale)


def menu_button_rect(width: int, height: int) -> tuple[int, int, int, int]:
    button_w = 70
    button_h = 22
    main_top = main_button_rects(width, height)["letter"][1]
    return ((width - button_w) // 2, main_top - button_h - 8, button_w, button_h)


def location_badge_rect(width: int, height: int) -> tuple[int, int, int, int]:
    log_x, _log_y, log_w, _log_h = main_button_rects(width, height)["log"]
    _menu_x, menu_y, _menu_w, _menu_h = menu_button_rect(width, height)
    panel_h = 34
    return (log_x, menu_y - panel_h - 6, log_w, panel_h)


def rotate_speed_control_rects(width: int, height: int) -> dict[str, tuple[int, int, int, int]]:
    capture_x, capture_y, capture_w, _capture_h = main_button_rects(width, height)["capture"]
    panel_w = capture_w
    panel_h = 44
    x = capture_x
    y = max(8, capture_y - panel_h - 8)
    return {
        "panel": (x, y, panel_w, panel_h),
        "down": (x + 6, y + 20, 24, 20),
        "up": (x + panel_w - 30, y + 20, 24, 20),
    }


def rotate_camera_speed_control_rects(width: int, height: int) -> dict[str, tuple[int, int, int, int]]:
    letter_x, letter_y, letter_w, _letter_h = main_button_rects(width, height)["letter"]
    panel_w = letter_w
    panel_h = 44
    x = letter_x
    y = max(8, letter_y - panel_h - 8)
    return {
        "panel": (x, y, panel_w, panel_h),
        "down": (x + 6, y + 20, 24, 20),
        "up": (x + panel_w - 30, y + 20, 24, 20),
    }


def main_button_rects(width: int, height: int) -> dict[str, tuple[int, int, int, int]]:
    gap = 6
    side = 8
    button_h = 38
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
    x = 8 if width <= 430 else 14
    w = width - x * 2
    h = 260 if height >= 520 else 220
    y = max(42 if height >= 520 else 38, (height - h) // 2)
    return (x, y, w, h)


def letter_view_panel_rect(width: int, height: int, letter: PresetLetter, language: Language) -> tuple[int, int, int, int]:
    x = 8 if width <= 430 else 14
    w = width - x * 2
    primary, original = display_letter_text(letter, language)
    h = _letter_panel_height_for_text(primary, original, w - 20, height)
    y = max(42 if height >= 520 else 38, (height - h) // 2)
    return (x, y, w, h)


def letter_close_rect(
    width: int,
    height: int,
    panel_rect: tuple[int, int, int, int] | None = None,
) -> tuple[int, int, int, int]:
    x, y, w, _ = panel_rect or letter_panel_rect(width, height)
    return (x + w - 38, y + 8, 30, 30)


def log_panel_rect(width: int, height: int) -> tuple[int, int, int, int]:
    return (18, 52, width - 36, height - 96)


def menu_panel_rect(width: int, height: int) -> tuple[int, int, int, int]:
    panel_w = min(width - 16, 244)
    panel_h = 222
    button_x, button_y, _, _ = menu_button_rect(width, height)
    x = max(8, min(width - panel_w - 8, button_x + 35 - panel_w // 2))
    return (x, max(8, button_y - panel_h - 6), panel_w, panel_h)


def menu_close_rect(width: int, height: int) -> tuple[int, int, int, int]:
    x, y, w, _ = menu_panel_rect(width, height)
    return (x + w - 30, y + 6, 22, 22)


def panel_toggle_rects(width: int, height: int) -> dict[str, tuple[int, int, int, int]]:
    x, y, w, _ = menu_panel_rect(width, height)
    button_w = max(68, (w - 32) // 3)
    row_button_x = x + 104
    row_button_w = w - 112
    return {
        "info": (x + 8, y + 34, button_w, 24),
        "guides": (x + 12 + button_w, y + 34, button_w, 24),
        "constellations": (x + 16 + button_w * 2, y + 34, button_w, 24),
        "side": (row_button_x, y + 72, row_button_w, 24),
        "location": (row_button_x, y + 104, row_button_w, 24),
        "language": (x + 8, y + 190, 72, 24),
        "sound": (x + 90, y + 190, 62, 24),
        "bgm": (x + 162, y + 190, 62, 24),
    }


def setup_restart_confirm_rects(width: int, height: int) -> dict[str, tuple[int, int, int, int]]:
    panel_w = min(width - 32, 332)
    panel_h = 144
    x = (width - panel_w) // 2
    y = (height - panel_h) // 2
    button_w = (panel_w - 30) // 2
    return {
        "panel": (x, y, panel_w, panel_h),
        "no": (x + 10, y + panel_h - 42, button_w, 30),
        "yes": (x + panel_w - button_w - 10, y + panel_h - 42, button_w, 30),
    }


def draw_button_colored(rect: tuple[int, int, int, int], label: str, fill: int, edge: int, text_col: int) -> None:
    x, y, w, h = rect
    pyxel.rect(x, y, w, h, fill)
    pyxel.rectb(x, y, w, h, edge)
    text_y = y + max(4, (h - GLYPH_H * SCALE) // 2)
    label_width = display_text_width(label)
    if not label.isascii():
        text_y = y + max(3, (h - FONT_CELL_HEIGHT) // 2)
    draw_display_text(x + max(4, (w - label_width) // 2), text_y, label, text_col)


def draw_button(rect: tuple[int, int, int, int], label: str, active: bool) -> None:
    fill = 5 if active else 1
    edge = 10 if active else 13
    draw_button_colored(rect, label, fill, edge, 7)


def draw_icon_search_button(rect: tuple[int, int, int, int], active: bool = False) -> None:
    x, y, w, h = rect
    fill = 5 if active else 1
    edge = 10 if active else 13
    pyxel.rect(x, y, w, h, fill)
    pyxel.rectb(x, y, w, h, edge)
    center_x = x + w // 2 - 4
    center_y = y + h // 2 - 2
    pyxel.circb(center_x, center_y, 5, 7)
    pyxel.line(center_x + 4, center_y + 4, center_x + 10, center_y + 10, 7)
    pyxel.pset(center_x - 2, center_y - 2, 7)


def draw_checkbox(rect: tuple[int, int, int, int], label: str, checked: bool) -> None:
    x, y, _, h = rect
    box = min(14, h - 8)
    box_y = y + (h - box) // 2
    pyxel.rectb(x, box_y, box, box, 10 if checked else 13)
    if checked:
        pyxel.line(x + 3, box_y + box // 2, x + 6, box_y + box - 4, 7)
        pyxel.line(x + 6, box_y + box - 4, x + box - 3, box_y + 3, 7)
    draw_big_text(x + box + 6, y + max(4, (h - GLYPH_H * SCALE) // 2), label, 7)


def draw_main_buttons(has_unread: bool, capture_pending: bool) -> None:
    rects = main_button_rects(pyxel.width, pyxel.height)
    draw_button(rects["letter"], "LETTER ." if has_unread else "LETTER", has_unread)
    draw_button(rects["log"], "LOG", False)
    if capture_pending:
        draw_button_colored(rects["capture"], "WAIT", 13, 7, 0)
    else:
        draw_button(rects["capture"], "CAPTURE", False)


def draw_back_button() -> None:
    draw_button(back_button_rect(pyxel.width, pyxel.height), "BACK", False)


def draw_cut_in(message: str, frame_age: int, duration_frames: int) -> None:
    if frame_age < 0 or frame_age >= duration_frames:
        return
    width = display_text_width(message)
    x = max(12, min(pyxel.width - width - 12, (pyxel.width - width) // 2))
    y = 42
    box_x = max(0, x - 16)
    box_w = min(pyxel.width - box_x, width + 32)
    pyxel.rect(box_x, y - 12, box_w, 38, 3)
    pyxel.rectb(box_x, y - 12, box_w, 38, 11)
    draw_display_bold_text(x, y, message, 7)


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


def draw_compact_time(
    clock: SimulationClock,
    highlight_date: bool = False,
    highlight_time: bool = False,
) -> None:
    scale = 3
    draw_bold_text_scaled(8, 8, clock.current_time.strftime("%b %d"), 10 if highlight_date else 7, scale)
    draw_bold_text_scaled(8, 27, clock.current_time.strftime("%H:%M"), 10 if highlight_time else 7, scale)


def draw_selected_constellation_summary(
    constellation: Constellation,
    language: Language,
    anchor_star_label: str | None,
    panel_summary: tuple[str, tuple[str, str], int] | None = None,
    animation_age: int | None = None,
    highlight_color: int | None = None,
) -> None:
    tool_left = tool_button_rects(pyxel.width, pyxel.height)["time"][0]
    x = 8
    y = 50
    w = tool_left - x - 8
    h = 49
    if w < 140:
        return
    if animation_age is not None and animation_age < 24:
        progress = max(0.0, min(1.0, animation_age / 23.0))
        y -= int((1.0 - progress) * (1.0 - progress) * 7)
    if highlight_color is not None:
        pyxel.rectb(x - 1, y - 1, w + 2, h + 2, highlight_color)
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 1)
    if panel_summary is not None:
        title, lines, title_color = panel_summary
    else:
        name = constellation_name(constellation, language)
        title = f"{constellation.id}  {name.upper() if language == 'en' else name}"
        lines = _constellation_summary_lines(constellation, language, anchor_star_label)
        title_color = 10
    draw_display_text(x + 7, y + 5, _clip_display_text(title, w - 14), title_color)
    for index, line in enumerate(lines):
        draw_display_text(x + 7, y + 19 + index * 13, _clip_display_text(line, w - 14), 13)
    if animation_age is not None and animation_age < 24:
        _draw_summary_panel_sparkles((x, y, w, h), animation_age, highlight_color)


def _draw_summary_panel_sparkles(rect: tuple[int, int, int, int], age: int, highlight_color: int | None) -> None:
    x, y, w, h = rect
    progress = max(0.0, min(1.0, age / 23.0))
    colors = _summary_sparkle_colors(highlight_color)
    main_color = colors[age % len(colors)]
    accent_color = colors[(age // 3 + 1) % len(colors)]
    seeds = (
        (0.08, 0.05, -5, -4),
        (0.24, 0.00, 0, -7),
        (0.48, 0.02, 3, -6),
        (0.73, 0.06, 5, -3),
        (0.92, 0.18, 6, 0),
        (0.98, 0.72, 7, 4),
        (0.68, 0.96, 3, 6),
        (0.36, 1.00, -2, 7),
        (0.06, 0.82, -6, 4),
        (0.00, 0.38, -7, -1),
    )
    for index, (rx, ry, dx, dy) in enumerate(seeds):
        drift = 1.0 + progress * 2.2
        px = int(x + rx * w + dx * drift)
        py = int(y + ry * h + dy * drift)
        if not (0 <= px < pyxel.width and 0 <= py < pyxel.height):
            continue
        dot_color = colors[(index + age // 2) % len(colors)]
        _sparkle_pset(px, py, dot_color)
        if index % 2 == 0:
            _sparkle_pset(px + (1 if index % 4 == 0 else -1), py + 1, accent_color)
        if (age + index) % 5 == 0:
            _draw_diagonal_sparkle(px, py, main_color)
        elif (age + index) % 3 == 0:
            _sparkle_pset(px, py, 7)
            _sparkle_pset(px - 1, py, accent_color)
            _sparkle_pset(px + 1, py, accent_color)
            _sparkle_pset(px, py - 1, accent_color)
            _sparkle_pset(px, py + 1, accent_color)


def _summary_sparkle_colors(highlight_color: int | None) -> tuple[int, ...]:
    if highlight_color == 8:
        return (8, 2, 7)
    if highlight_color == 11:
        return (11, 3, 7)
    if highlight_color == 10:
        return (10, 7)
    if highlight_color is not None:
        return (highlight_color, 7, 13)
    return (10, 7, 13)


def _sparkle_pset(x: int, y: int, color: int) -> None:
    if 0 <= x < pyxel.width and 0 <= y < pyxel.height:
        pyxel.pset(x, y, color)


def _draw_diagonal_sparkle(x: int, y: int, color: int) -> None:
    _sparkle_pset(x, y, 7)
    _sparkle_pset(x - 1, y - 1, color)
    _sparkle_pset(x + 1, y - 1, color)
    _sparkle_pset(x - 1, y + 1, color)
    _sparkle_pset(x + 1, y + 1, color)


def _constellation_summary_lines(
    constellation: Constellation,
    language: Language,
    anchor_star_label: str | None,
) -> tuple[str, str]:
    descriptions = CONSTELLATION_DESCRIPTIONS.get(constellation.id, {})
    lines = descriptions.get(language)
    if lines is not None:
        return lines
    line = "星座の説明を準備中" if language == "ja" else "constellation notes loading"
    return (line, "")


def draw_constellation_labels(
    constellations: tuple[Constellation, ...],
    selected_constellation: Constellation,
    points: dict[int, ScreenPoint],
    language: Language,
) -> None:
    for index, constellation, center in _visible_constellation_label_entries(
        constellations,
        selected_constellation,
        points,
        language,
    ):
        selected = constellation.id == selected_constellation.id
        draw_constellation_label(
            constellation,
            center,
            10 if selected else 13,
            index,
            language,
            selected,
        )


def constellation_label_hit_rects(
    constellations: tuple[Constellation, ...],
    selected_constellation: Constellation,
    points: dict[int, ScreenPoint],
    language: Language,
) -> list[tuple[int, tuple[int, int, int, int]]]:
    rects: list[tuple[int, tuple[int, int, int, int]]] = []
    for index, constellation, center in _visible_constellation_label_entries(
        constellations,
        selected_constellation,
        points,
        language,
    ):
        label_x, label_y, width = _constellation_label_layout(constellation, center, index, language)
        rects.append((index, (label_x - 6, label_y - 5, width + 12, 22)))
    return rects


def _visible_constellation_label_entries(
    constellations: tuple[Constellation, ...],
    selected_constellation: Constellation,
    points: dict[int, ScreenPoint],
    language: Language,
) -> list[tuple[int, Constellation, tuple[int, int]]]:
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
    return visible


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
    label_x, label_y, width = _constellation_label_layout(constellation, center, index, language)
    label = constellation_name(constellation, language)
    pyxel.line(center_x, center_y, label_x - 3, label_y + 6, color)
    if selected:
        draw_display_bold_text(label_x, label_y, label, color)
    else:
        draw_display_text(label_x, label_y, label, color)


def _constellation_label_layout(
    constellation: Constellation,
    center: tuple[int, int],
    index: int,
    language: Language,
) -> tuple[int, int, int]:
    center_x, center_y = center
    label = constellation_name(constellation, language)
    width = display_text_width(label)
    label_x = max(4, min(pyxel.width - width - 4, center_x + 10))
    label_y = max(88, min(pyxel.height - 76, center_y - 18 + (index % 3) * 12))
    return label_x, label_y, width


def draw_sky_features(
    points: dict[int, ScreenPoint],
    sky_paths: dict[str, list[tuple[float, float] | None]],
    language: Language,
    moon_light: float = 0.0,
) -> None:
    color = 5 if moon_light > 0.65 else FEATURE_COLOR
    for path in SKY_PATHS:
        draw_sky_path(path, sky_paths.get(path.id, []), language, color)
    for index, asterism in enumerate(ASTERISMS):
        draw_asterism(asterism, points, index, language, color)


def draw_asterism(
    asterism: Asterism,
    points: dict[int, ScreenPoint],
    index: int,
    language: Language,
    color: int = FEATURE_COLOR,
) -> None:
    visible = [points[star_id] for star_id in asterism.star_ids if star_id in points]
    if len(visible) < 2:
        return
    for a_id, b_id in asterism.edges:
        a = points.get(a_id)
        b = points.get(b_id)
        if a is None or b is None:
            continue
        pyxel.line(int(a.x), int(a.y), int(b.x), int(b.y), color)
    label = sky_feature_name(asterism, language)
    center_x, center_y, label_x, label_y, width = _asterism_label_layout(asterism, points, index, language)
    pyxel.line(center_x, center_y, label_x - 3, label_y + 6, color)
    draw_display_text(label_x, label_y, label, color)


def draw_sky_path(
    path: SkyPath,
    points: list[tuple[float, float] | None],
    language: Language,
    color: int = FEATURE_COLOR,
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
            pyxel.line(int(last[0]), int(last[1]), int(x), int(y), color)
        elif index % 2 == 1:
            pyxel.pset(int(x), int(y), color)
        last = point
    if len(visible_points) < 2:
        return
    label = sky_feature_name(path, language)
    x, y, _ = _sky_path_label_layout(path, visible_points, language)
    draw_display_text(x, y, label, color)


def sky_feature_label_hit_rects(
    points: dict[int, ScreenPoint],
    sky_paths: dict[str, list[tuple[float, float] | None]],
    language: Language,
) -> list[tuple[str, tuple[int, int, int, int]]]:
    rects: list[tuple[str, tuple[int, int, int, int]]] = []
    for path in SKY_PATHS:
        visible_points = [point for point in sky_paths.get(path.id, []) if point is not None and 0 <= point[0] < pyxel.width and 0 <= point[1] < pyxel.height]
        if len(visible_points) < 2:
            continue
        x, y, width = _sky_path_label_layout(path, visible_points, language)
        rects.append((path.id, (x - 6, y - 5, width + 12, 22)))
    for index, asterism in enumerate(ASTERISMS):
        visible = [points[star_id] for star_id in asterism.star_ids if star_id in points]
        if len(visible) < 2:
            continue
        _center_x, _center_y, label_x, label_y, width = _asterism_label_layout(asterism, points, index, language)
        rects.append((asterism.id, (label_x - 6, label_y - 5, width + 12, 22)))
    return rects


def _asterism_label_layout(
    asterism: Asterism,
    points: dict[int, ScreenPoint],
    index: int,
    language: Language,
) -> tuple[int, int, int, int, int]:
    visible = [points[star_id] for star_id in asterism.star_ids if star_id in points]
    center_x = int(sum(point.x for point in visible) / len(visible))
    center_y = int(sum(point.y for point in visible) / len(visible))
    label = sky_feature_name(asterism, language)
    width = display_text_width(label)
    label_x = max(4, min(pyxel.width - width - 4, center_x + 8))
    label_y = max(58, min(pyxel.height - 76, center_y - 22 + (index % 2) * 12))
    return (center_x, center_y, label_x, label_y, width)


def _sky_path_label_layout(
    path: SkyPath,
    visible_points: list[tuple[float, float]],
    language: Language,
) -> tuple[int, int, int]:
    label_x, label_y = visible_points[len(visible_points) // 2]
    label = sky_feature_name(path, language)
    width = display_text_width(label)
    x = max(4, min(pyxel.width - width - 4, int(label_x) + 8))
    y = max(58, min(pyxel.height - 76, int(label_y) - 10))
    return (x, y, width)


def draw_focused_star(point: ScreenPoint, name: str) -> None:
    x = int(point.x)
    y = int(point.y)
    pyxel.rectb(x - 5, y - 5, 11, 11, 8)
    pyxel.rectb(x - 6, y - 6, 13, 13, 8)
    label_x, label_y, width = _focused_star_label_layout(point, name)
    line_x = label_x - 3 if label_x > x else label_x + width + 3
    pyxel.line(x + 7 if label_x > x else x - 7, y, line_x, label_y + 6, 8)
    draw_display_bold_text(label_x, label_y, name, 8)


def focused_star_hit_rect(point: ScreenPoint, name: str) -> tuple[int, int, int, int]:
    label_x, label_y, width = _focused_star_label_layout(point, name)
    star_x = int(point.x)
    star_y = int(point.y)
    x1 = min(label_x - 6, star_x - 10)
    y1 = min(label_y - 6, star_y - 10)
    x2 = max(label_x + width + 6, star_x + 10)
    y2 = max(label_y + 20, star_y + 10)
    return (x1, y1, x2 - x1, y2 - y1)


def _focused_star_label_layout(point: ScreenPoint, name: str) -> tuple[int, int, int]:
    x = int(point.x)
    y = int(point.y)
    width = display_text_width(name)
    label_x = x + 12
    if label_x + width > pyxel.width - 4:
        label_x = x - width - 12
    label_x = max(4, min(pyxel.width - width - 4, label_x))
    label_y = max(4, min(pyxel.height - 18, y - 7))
    return (label_x, label_y, width)


def draw_focused_moon(point: tuple[float, float], moon: MoonState, language: Language) -> None:
    x = int(point[0])
    y = int(point[1])
    pyxel.rectb(x - 8, y - 8, 17, 17, 10)
    pyxel.rectb(x - 9, y - 9, 19, 19, 7)
    phase = int(round(moon.illumination * 100.0))
    label = f"月 {phase}%" if language == "ja" else f"MOON {phase}%"
    width = display_text_width(label)
    label_x = x + 14
    if label_x + width > pyxel.width - 4:
        label_x = x - width - 14
    label_x = max(4, min(pyxel.width - width - 4, label_x))
    label_y = max(4, min(pyxel.height - 18, y - 7))
    line_x = label_x - 3 if label_x > x else label_x + width + 3
    pyxel.line(x + 9 if label_x > x else x - 9, y, line_x, label_y + 6, 10)
    draw_display_text(label_x, label_y, label, 10)


def focused_moon_hit_rect(point: tuple[float, float], moon: MoonState, language: Language) -> tuple[int, int, int, int]:
    x = int(point[0])
    y = int(point[1])
    phase = int(round(moon.illumination * 100.0))
    label = f"月 {phase}%" if language == "ja" else f"MOON {phase}%"
    width = display_text_width(label)
    label_x = x + 14
    if label_x + width > pyxel.width - 4:
        label_x = x - width - 14
    label_x = max(4, min(pyxel.width - width - 4, label_x))
    label_y = max(4, min(pyxel.height - 18, y - 7))
    x1 = min(label_x - 6, x - 12)
    y1 = min(label_y - 6, y - 12)
    x2 = max(label_x + width + 6, x + 12)
    y2 = max(label_y + 20, y + 12)
    return (x1, y1, x2 - x1, y2 - y1)


def draw_meteor_event(event_view: MeteorEventView, language: Language) -> None:
    if not isinstance(event_view.event, MeteorShowerEvent):
        return
    if event_view.radiant_screen is None:
        return
    radiant_x, radiant_y = event_view.radiant_screen
    label = sky_event_name(event_view.event, language)
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
    heading = "【天体イベント】" if language == "ja" else "CELESTIAL EVENT"
    heading_width = display_text_width(heading)
    heading_x = max(4, min(pyxel.width - heading_width - 4, (pyxel.width - heading_width) // 2))
    draw_display_bold_text(heading_x, 4, heading, 10)

    label = sky_event_name(event_view.event, language)
    width = display_text_width(label)
    x = max(4, min(pyxel.width - width - 4, (pyxel.width - width) // 2))
    draw_display_bold_text(x, 17, label, 10)

    period = _event_period_label(event_view, language)
    period_x = max(4, min(pyxel.width - text_width(period) - 4, (pyxel.width - text_width(period)) // 2))
    draw_bold_text(period_x, 30, period, 10)


def _event_period_label(event_view: MeteorEventView, language: Language) -> str:
    if isinstance(event_view.event, LunarEclipseEvent):
        event_date = event_view.event.display_start
        return f"( {event_date:%Y/%m/%d} PEAK )"
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


def _draw_centered_display_text(text: str, x: int, y: int, w: int, col: int) -> None:
    draw_display_text(x + max(3, (w - display_text_width(text)) // 2), y, text, col)


def draw_location_badge(country_code: str | None, city: str | None, language: Language) -> None:
    _ = language
    country = country_name(country_code, "en")
    city_label = city_name(city, "en")
    if not country and not city_label:
        return

    x, y, w, h = location_badge_rect(pyxel.width, pyxel.height)
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 10)
    pyxel.rectb(x + 2, y + 2, w - 4, h - 4, 1)

    # Small framed corners keep the badge distinct without competing with controls.
    for corner_x, corner_y, sx, sy in (
        (x + 3, y + 3, 1, 1),
        (x + w - 4, y + 3, -1, 1),
        (x + 3, y + h - 4, 1, -1),
        (x + w - 4, y + h - 4, -1, -1),
    ):
        pyxel.pset(corner_x, corner_y, 10)
        pyxel.pset(corner_x + sx, corner_y, 7)
        pyxel.pset(corner_x, corner_y + sy, 7)

    if country and city_label:
        _draw_centered_display_text(country, x, y + 6, w, 10)
        _draw_centered_display_text(city_label, x, y + 19, w, 7)
    else:
        _draw_centered_display_text(country or city_label, x, y + 13, w, 10)


def draw_rotate_speed_control(speed_level: int) -> None:
    _draw_rotation_speed_control(rotate_speed_control_rects(pyxel.width, pyxel.height), "ROT-T", speed_level)


def draw_rotate_camera_speed_control(speed_level: int) -> None:
    _draw_rotation_speed_control(rotate_camera_speed_control_rects(pyxel.width, pyxel.height), "ROT-C", speed_level)


def _draw_rotation_speed_control(rects: dict[str, tuple[int, int, int, int]], label: str, speed_level: int) -> None:
    x, y, w, h = rects["panel"]
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 10)
    draw_big_text(x + (w - text_width(label)) // 2, y + 3, label, 10)
    draw_button(rects["down"], "-", False)
    clamped_level = max(-3, min(3, speed_level))
    sign = "+" if clamped_level > 0 else ""
    value = f"SPD{sign}{clamped_level}"
    draw_big_text(x + (w - text_width(value)) // 2, y + 27, value, 7)
    draw_button(rects["up"], "+", False)


def draw_menu_panel(
    show_info: bool,
    show_guides: bool,
    show_constellations: bool,
    sound_enabled: bool,
    bgm_enabled: bool,
    slider_side: str,
    event_source_label: str,
    event_count: int,
    language: Language,
) -> None:
    x, y, w, h = menu_panel_rect(pyxel.width, pyxel.height)
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 13)
    draw_display_text(x + 8, y + 8, _menu_text(language, "DISPLAY", "表示"), 7)
    draw_button(menu_close_rect(pyxel.width, pyxel.height), "X", False)
    toggle_rects = panel_toggle_rects(pyxel.width, pyxel.height)
    draw_button(toggle_rects["info"], _menu_text(language, "INFO", "情報"), show_info)
    draw_button(toggle_rects["guides"], _menu_text(language, "GUIDE", "補助"), show_guides)
    draw_button(toggle_rects["constellations"], _menu_text(language, "CONST", "星座"), show_constellations)
    draw_display_text(x + 8, y + 77, _menu_text(language, "SLIDER", "スライダー"), 7)
    side_label = slider_side.upper() if language == "en" else "左" if slider_side == "left" else "右"
    draw_button(toggle_rects["side"], side_label, True)
    draw_display_text(x + 8, y + 109, _menu_text(language, "LOCATION", "場所"), 7)
    draw_button(toggle_rects["location"], _menu_text(language, "CHANGE", "変更"), False)
    draw_display_text(x + 8, y + 136, _menu_text(language, f"EVENT SRC {event_source_label}", f"イベント情報 {event_source_label}"), 13)
    draw_display_text(x + 8, y + 150, _menu_text(language, f"EVENTS {event_count}", f"イベント {event_count}"), 13)
    draw_display_text(x + 8, y + 174, _menu_text(language, "LANGUAGE", "言語"), 7)
    language_label = "JA" if language == "en" else "EN"
    draw_button(toggle_rects["language"], language_label, True)
    sound_rect = toggle_rects["sound"]
    draw_display_text(sound_rect[0], y + 174, "SE", 7)
    draw_button(sound_rect, "ON" if sound_enabled else "OFF", sound_enabled)
    bgm_rect = toggle_rects["bgm"]
    draw_display_text(bgm_rect[0], y + 174, "BGM", 7)
    draw_button(bgm_rect, "ON" if bgm_enabled else "OFF", bgm_enabled)


def draw_setup_restart_confirm(language: Language) -> None:
    rects = setup_restart_confirm_rects(pyxel.width, pyxel.height)
    x, y, w, h = rects["panel"]
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 10)
    pyxel.rectb(x + 2, y + 2, w - 4, h - 4, 1)
    title = _menu_text(language, "CHANGE SKY", "空の設定を変更")
    line1 = _menu_text(language, "RETURN TO LANGUAGE / COUNTRY / CITY.", "言語・国・都市の選択へ戻ります。")
    line2 = _menu_text(language, "CURRENT SKY VIEW WILL CLOSE.", "現在の星空表示は中断されます。")
    _draw_centered_display_text(title, x, y + 14, w, 10)
    _draw_centered_display_text(line1, x, y + 48, w, 7)
    _draw_centered_display_text(line2, x, y + 66, w, 13)
    draw_button(rects["no"], _menu_text(language, "NO", "いいえ"), False)
    draw_button(rects["yes"], _menu_text(language, "YES", "はい"), True)


def _menu_text(language: Language, english: str, japanese: str) -> str:
    return japanese if language == "ja" else english

def draw_letter_view(
    log: ExchangeLog,
    letter: PresetLetter,
    language: Language,
    animation_age: int | None = None,
    animation_direction: int = 1,
) -> None:
    panel_rect = letter_view_panel_rect(pyxel.width, pyxel.height, letter, language)
    if animation_age is not None:
        panel_rect = _animated_letter_panel_rect(panel_rect, animation_age, animation_direction)
    x, y, w, h = panel_rect
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 13)
    _draw_letter_lace_frame(panel_rect)
    draw_back_button()
    draw_big_text(x + 10, y + 10, "LETTER", 7)
    draw_button(letter_close_rect(pyxel.width, pyxel.height, panel_rect), "X", False)

    primary, original = display_letter_text(letter, language)
    body_width, primary_layout, original_layout = _fit_letter_body_lines(primary, original, w - 20, h - 66)
    primary_scale, primary_line_step, primary_lines = primary_layout
    original_scale, original_line_step, original_lines = original_layout
    cursor_y = y + 44
    for line in primary_lines:
        _draw_body_text(x + 10, cursor_y, line, 7, primary_scale)
        cursor_y += primary_line_step
    if original_lines:
        cursor_y += LETTER_ORIGINAL_SECTION_GAP
        draw_big_text(x + 10, cursor_y, "- ORIGINAL -", 13)
        cursor_y += 13
        for line in original_lines:
            _draw_body_text(x + 10, cursor_y, line, 13, original_scale)
            cursor_y += original_line_step

    location = _letter_location(letter)
    location_lines = _wrap_display_lines(f"FROM {location}", body_width)
    draw_display_text(x + 10, y + h - 24, location_lines[0], 13)
    if animation_age is not None:
        _draw_letter_fade_mask(panel_rect, animation_age, animation_direction)


def _animated_letter_panel_rect(
    rect: tuple[int, int, int, int],
    age: int,
    direction: int,
) -> tuple[int, int, int, int]:
    x, y, w, h = rect
    progress = max(0.0, min(1.0, age / 17.0))
    ease = 1.0 - (1.0 - progress) * (1.0 - progress)
    if direction < 0:
        return (x, y + int(ease * 18.0), w, h)
    return (x, y - int((1.0 - ease) * 18.0), w, h)


def _draw_letter_fade_mask(rect: tuple[int, int, int, int], age: int, direction: int) -> None:
    x, y, w, h = rect
    progress = max(0.0, min(1.0, age / 17.0))
    visible = 1.0 - progress if direction < 0 else progress
    if visible >= 1.0:
        return
    if visible < 0.18:
        pyxel.rect(x, y, w, h, 0)
        return
    step = 2 if visible < 0.48 else 3 if visible < 0.76 else 5
    phase = age % step
    for yy in range(y, y + h, step):
        for xx in range(x + ((yy + phase) % step), x + w, step):
            pyxel.pset(xx, yy, 0)


def _draw_letter_lace_frame(rect: tuple[int, int, int, int]) -> None:
    x, y, w, h = rect
    if w < 120 or h < 160:
        return
    pyxel.rectb(x + 2, y + 2, w - 4, h - 4, LETTER_LACE_DIM_COLOR)
    _draw_lace_stitches_horizontal(x + 92, x + w - 54, y + 5, 1)
    _draw_lace_stitches_horizontal(x + 92, x + w - 18, y + h - 6, -1)
    _draw_lace_flower(x + w - 52, y + 22)
    _draw_lace_flower(x + w - 22, y + h - 17)


def _draw_lace_stitches_horizontal(start_x: int, end_x: int, y: int, direction: int) -> None:
    if end_x - start_x < 14:
        return
    for x in range(start_x, end_x, 12):
        pyxel.line(x, y, x + 3, y + direction * 3, LETTER_LACE_DIM_COLOR)
        pyxel.line(x + 3, y + direction * 3, x + 6, y, LETTER_LACE_DIM_COLOR)
        pyxel.pset(x + 3, y + direction * 2, LETTER_LACE_COLOR)


def _draw_lace_flower(cx: int, cy: int) -> None:
    pyxel.pset(cx, cy, 7)
    for dx, dy in ((-3, 0), (3, 0), (0, -3), (0, 3), (-2, -2), (2, -2), (-2, 2), (2, 2)):
        pyxel.pset(cx + dx, cy + dy, LETTER_LACE_COLOR)
    pyxel.line(cx - 5, cy, cx - 2, cy, LETTER_LACE_DIM_COLOR)
    pyxel.line(cx + 2, cy, cx + 5, cy, LETTER_LACE_DIM_COLOR)
    pyxel.line(cx, cy - 5, cx, cy - 2, LETTER_LACE_DIM_COLOR)
    pyxel.line(cx, cy + 2, cx, cy + 5, LETTER_LACE_DIM_COLOR)


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


def _clip_display_text(text: str, max_width: int) -> str:
    if display_text_width(text) <= max_width:
        return text
    suffix = "..."
    clipped = text
    while clipped and display_text_width(clipped + suffix) > max_width:
        clipped = clipped[:-1]
    return clipped + suffix if clipped else suffix


def _wrap_body_lines(text: str, max_width: int, scale: int) -> list[str]:
    if not text:
        return [""]
    wrapped: list[str] = []
    for sentence in _sentence_chunks(text):
        wrapped.extend(_wrap_body_sentence(sentence, max_width, scale))
    return wrapped or [""]


def _fit_letter_body_lines(
    primary: str,
    original: str | None,
    max_width: int,
    available_height: int,
) -> tuple[int, tuple[int, int, list[str]], tuple[int, int, list[str]]]:
    primary_preferred_scale = _preferred_body_scale(primary)
    original_preferred_scale = _preferred_body_scale(original or "")
    scale_pairs = (
        (primary_preferred_scale, original_preferred_scale),
        (BODY_TEXT_SCALE, original_preferred_scale),
        (primary_preferred_scale, BODY_TEXT_SCALE),
        (BODY_TEXT_SCALE, BODY_TEXT_SCALE),
    )
    tried: set[tuple[int, int]] = set()
    for primary_scale, original_scale in scale_pairs:
        if (primary_scale, original_scale) in tried:
            continue
        tried.add((primary_scale, original_scale))
        primary_line_step = _body_line_step(primary_scale)
        original_line_step = _body_line_step(original_scale)
        primary_lines = _wrap_body_lines(primary, max_width, primary_scale)
        original_lines = _wrap_body_lines(original, max_width, original_scale) if original else []
        required = _letter_body_required_height(
            primary_line_step,
            primary_lines,
            original_line_step,
            original_lines,
        )
        if required <= available_height:
            return (
                max_width,
                (primary_scale, primary_line_step, primary_lines),
                (original_scale, original_line_step, original_lines),
            )
    primary_lines = _wrap_body_lines(primary, max_width, BODY_TEXT_SCALE)
    original_lines = _wrap_body_lines(original, max_width, BODY_TEXT_SCALE) if original else []
    return (
        max_width,
        (BODY_TEXT_SCALE, BODY_COMPACT_LINE_STEP, primary_lines),
        (BODY_TEXT_SCALE, BODY_COMPACT_LINE_STEP, original_lines),
    )


def _letter_panel_height_for_text(primary: str, original: str | None, max_width: int, screen_height: int) -> int:
    top_min = 42 if screen_height >= 520 else 38
    bottom_margin = 14 if screen_height >= 520 else 10
    max_height = max(220, screen_height - top_min - bottom_margin)
    stages = (240, 300, 380, 480, max_height) if screen_height >= 520 else (220, 260, max_height)
    for panel_height in stages:
        height = min(panel_height, max_height)
        _body_width, primary_layout, original_layout = _fit_letter_body_lines(
            primary,
            original,
            max_width,
            height - 66,
        )
        _primary_scale, primary_line_step, primary_lines = primary_layout
        _original_scale, original_line_step, original_lines = original_layout
        if (
            _letter_body_required_height(primary_line_step, primary_lines, original_line_step, original_lines)
            <= height - 66
        ):
            return height
    return max_height


def _letter_body_required_height(
    primary_line_step: int,
    primary_lines: list[str],
    original_line_step: int,
    original_lines: list[str],
) -> int:
    required = len(primary_lines) * primary_line_step
    if original_lines:
        required += LETTER_ORIGINAL_SECTION_GAP + 13 + len(original_lines) * original_line_step
    return required


def _sentence_chunks(text: str) -> list[str]:
    chunks: list[str] = []
    current = ""
    index = 0
    while index < len(text):
        char = text[index]
        current += char
        next_char = text[index + 1] if index + 1 < len(text) else ""
        if char in "。！？" or (char in ".!?" and (not next_char or next_char == " ")):
            chunks.append(current.strip())
            current = ""
            while index + 1 < len(text) and text[index + 1] == " ":
                index += 1
        index += 1
    if current.strip():
        chunks.append(current.strip())
    return chunks


def _wrap_body_sentence(text: str, max_width: int, scale: int) -> list[str]:
    lines: list[str] = []
    current = ""
    tokens = text.split(" ") if text.isascii() else list(text)
    separator = " " if text.isascii() else ""
    for token in tokens:
        candidate = token if not current else current + separator + token
        if current and _body_text_width(candidate, scale) > max_width:
            lines.append(current)
            current = token
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def _preferred_body_scale(text: str) -> int:
    if _desktop_letter_text_mode and text and not text.isascii():
        return DESKTOP_JAPANESE_BODY_TEXT_SCALE
    return BODY_TEXT_SCALE


def _body_line_step(scale: int) -> int:
    if scale <= BODY_TEXT_SCALE:
        return BODY_LINE_STEP
    return FONT_CELL_HEIGHT * scale + 3


def _body_text_width(text: str, scale: int) -> int:
    return sum(_glyph_advance(char) * scale for char in text)


def _draw_body_text(x: int, y: int, text: str, col: int, scale: int) -> None:
    _draw_bitmap_text(x, y, text, col, scale)


def tool_button_rects(width: int, _height: int) -> dict[str, tuple[int, int, int, int]]:
    button_w = 62
    button_h = 22
    x = max(6, width - button_w - 6)
    return {
        "month": (x, 8, button_w, button_h),
        "time": (x, 34, button_w, button_h),
        "event": (x, 60, button_w, button_h),
        "rotate": (x, 86, button_w, button_h),
        "rotate_camera": (x, 112, button_w, button_h),
        "features": (x, 138, button_w, button_h),
        "reset": (x, 164, button_w, button_h),
        "search": (x, 190, button_w, button_h),
    }


def draw_tool_buttons(
    show_time_slider: bool,
    show_month_slider: bool,
    show_event_slider: bool,
    rotate_time: bool,
    rotate_camera: bool,
    show_features: bool,
) -> None:
    rects = tool_button_rects(pyxel.width, pyxel.height)
    draw_button(rects["time"], "TIME", show_time_slider)
    draw_button(rects["month"], "DAY", show_month_slider)
    draw_button(rects["event"], "EVENT", show_event_slider)
    draw_button(rects["rotate"], "ROT-T", rotate_time)
    draw_button(rects["rotate_camera"], "ROT-C", rotate_camera)
    feature_fill = 11 if show_features else 3
    feature_text = 0 if show_features else 7
    draw_button_colored(rects["features"], "FEATURE", feature_fill, 11, feature_text)
    draw_button(rects["reset"], "RESET", False)
    draw_icon_search_button(rects["search"], False)


def slider_rects(width: int, height: int, side: str) -> dict[str, tuple[int, int, int, int]]:
    panel_w = 34
    x = width - panel_w - 6 if side == "right" else 6
    _search_x, search_y, _search_w, search_h = tool_button_rects(width, height)["search"]
    _rot_x, rot_y, _rot_w, _rot_h = rotate_speed_control_rects(width, height)["panel"]
    y = search_y + search_h + 14
    panel_bottom = rot_y - 8
    panel_h = max(180, panel_bottom - y)
    event_panel_h = 92
    event_y = y
    return {
        "time_minus": (x + 5, y + 8, 24, 22),
        "time_track": (x + 15, y + 34, 4, panel_h - 68),
        "time_knob": (x + 8, y + panel_h // 2 - 10, 18, 20),
        "time_plus": (x + 5, y + panel_h - 30, 24, 22),
        "month_minus": (x + 5, y + 8, 24, 22),
        "month_track": (x + 15, y + 34, 4, panel_h - 68),
        "month_knob": (x + 8, y + panel_h // 2 - 10, 18, 20),
        "month_plus": (x + 5, y + panel_h - 30, 24, 22),
        "event_minus": (x + 5, event_y + 13, 24, 22),
        "event_track": (x + 15, event_y + 40, 4, 12),
        "event_knob": (x + 8, event_y + 36, 18, 20),
        "event_plus": (x + 5, event_y + 57, 24, 22),
        "event_panel": (x, event_y, panel_w, event_panel_h),
        "panel": (x, y, panel_w, panel_h),
    }


def draw_slider(side: str, label: str, knob_ratio: float = 0.5, rect_key: str | None = None) -> None:
    rects = slider_rects(pyxel.width, pyxel.height, side)
    key = rect_key or label.lower()
    x, y, w, h = rects["event_panel"] if key == "event" else rects["panel"]
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 13)
    label_x = max(4, min(pyxel.width - text_width(label) - 4, x + 5))
    draw_big_text(label_x, y - 14, label, 7)
    draw_button(rects[f"{key}_minus"], "+", False)
    if key == "event":
        draw_button(rects[f"{key}_plus"], "-", False)
        return
    track = rects[f"{key}_track"]
    pyxel.rect(track[0], track[1], track[2], track[3], 13)
    knob = rects[f"{key}_knob"]
    knob_y = int(track[1] + max(0.0, min(1.0, knob_ratio)) * track[3] - knob[3] / 2)
    knob_y = max(track[1], min(track[1] + track[3] - knob[3], knob_y))
    pyxel.rect(knob[0], knob_y, knob[2], knob[3], 5)
    pyxel.rectb(knob[0], knob_y, knob[2], knob[3], 10)
    draw_button(rects[f"{key}_plus"], "-", False)


CONSTELLATION_LIST_COLUMNS = 4
CONSTELLATION_LIST_BUTTON_H = 34
CONSTELLATION_LIST_GAP = 4
CONSTELLATION_SINGLE_WORD_SPLITS = {
    "CAMELOPARDALIS": ("CAMELO", "PARDALIS"),
    "MICROSCOPIUM": ("MICRO", "SCOPIUM"),
    "TELESCOPIUM": ("TELE", "SCOPIUM"),
}
CONSTELLATION_JA_BUTTON_LINES = {
    "CRA": ("みなみの", "かんむり座"),
    "TRA": ("みなみの", "さんかく座"),
}
SEARCH_TAB_KEYS = ("constellation", "star", "group")


@dataclass(slots=True, frozen=True)
class SearchListItem:
    id: str
    label: str
    selected: bool
    available: bool
    label_lines: tuple[str, ...] | None = None


def constellation_list_panel_rect(width: int, height: int) -> tuple[int, int, int, int]:
    x = 8
    y = 44
    return (x, y, width - x * 2, height - y - 44)


def constellation_list_close_rect(width: int, height: int) -> tuple[int, int, int, int]:
    x, y, w, _h = constellation_list_panel_rect(width, height)
    return (x + w - 32, y + 8, 24, 24)


def constellation_list_tab_rects(width: int, height: int) -> dict[str, tuple[int, int, int, int]]:
    x, y, _w, _h = constellation_list_panel_rect(width, height)
    tab_w = 58
    tab_h = 24
    gap = 4
    tab_x = x + 78
    tab_y = y + 10
    return {
        key: (tab_x + index * (tab_w + gap), tab_y, tab_w, tab_h)
        for index, key in enumerate(SEARCH_TAB_KEYS)
    }


def constellation_list_view_rect(width: int, height: int) -> tuple[int, int, int, int]:
    x, y, w, h = constellation_list_panel_rect(width, height)
    return (x + 8, y + 74, w - 16, h - 88)


def constellation_list_max_scroll(width: int, height: int, count: int) -> int:
    _x, _y, _w, view_h = constellation_list_view_rect(width, height)
    rows = (count + CONSTELLATION_LIST_COLUMNS - 1) // CONSTELLATION_LIST_COLUMNS
    content_h = rows * CONSTELLATION_LIST_BUTTON_H + max(0, rows - 1) * CONSTELLATION_LIST_GAP
    return max(0, content_h - view_h)


def constellation_list_button_rects(
    width: int,
    height: int,
    count: int,
    scroll: int,
) -> list[tuple[int, int, int, int]]:
    view_x, view_y, view_w, _view_h = constellation_list_view_rect(width, height)
    button_w = (view_w - CONSTELLATION_LIST_GAP * (CONSTELLATION_LIST_COLUMNS - 1)) // CONSTELLATION_LIST_COLUMNS
    rects = []
    for index in range(count):
        column = index % CONSTELLATION_LIST_COLUMNS
        row = index // CONSTELLATION_LIST_COLUMNS
        x = view_x + column * (button_w + CONSTELLATION_LIST_GAP)
        y = view_y + row * (CONSTELLATION_LIST_BUTTON_H + CONSTELLATION_LIST_GAP) - scroll
        rects.append((x, y, button_w, CONSTELLATION_LIST_BUTTON_H))
    return rects


def draw_constellation_list(
    constellations: tuple[Constellation, ...],
    selected: Constellation,
    available_ids: set[str],
    language: Language,
    scroll: int,
) -> None:
    items = tuple(
        SearchListItem(
            constellation.id,
            constellation_name(constellation, language),
            constellation.id == selected.id,
            constellation.id in available_ids,
            CONSTELLATION_JA_BUTTON_LINES.get(constellation.id) if language == "ja" else None,
        )
        for constellation in constellations
    )
    draw_search_list(items, "constellation", language, scroll)


def draw_search_list(
    items: tuple[SearchListItem, ...],
    active_tab: str,
    language: Language,
    scroll: int,
) -> None:
    panel = constellation_list_panel_rect(pyxel.width, pyxel.height)
    x, y, w, h = panel
    pyxel.rect(x, y, w, h, 0)
    pyxel.rectb(x, y, w, h, 13)
    pyxel.rectb(x + 2, y + 2, w - 4, h - 4, 1)
    if language == "ja":
        title = "探す"
        note = {
            "constellation": "グレー表示は観測不可の星座です",
            "star": "グレー表示は観測不可の星です",
            "group": "グレー表示は観測不可の星群です",
        }.get(active_tab, "グレー表示は観測不可です")
    else:
        title = "SEARCH"
        note = {
            "constellation": "GRAY CONSTELLATIONS ARE BELOW YOUR SKY",
            "star": "GRAY STARS ARE BELOW YOUR SKY",
            "group": "GRAY GROUPS ARE BELOW YOUR SKY",
        }.get(active_tab, "GRAY BUTTONS ARE BELOW YOUR SKY")
    title_y = y + 14 if title.isascii() else y + 12
    draw_display_bold_text(x + 18, title_y, title, 7)
    _draw_constellation_search_tabs(language, active_tab)
    note_w = display_text_width(note)
    note_y = y + 42 if note.isascii() else y + 40
    draw_display_text(x + max(8, (w - note_w) // 2), note_y, note, 13)
    draw_button(constellation_list_close_rect(pyxel.width, pyxel.height), "X", False)

    view = constellation_list_view_rect(pyxel.width, pyxel.height)
    view_x, view_y, view_w, view_h = view
    rects = constellation_list_button_rects(pyxel.width, pyxel.height, len(items), scroll)
    for index, rect in enumerate(rects):
        rx, ry, _rw, rh = rect
        if ry < view_y or ry + rh > view_y + view_h:
            continue
        _draw_search_list_button(
            rect,
            items[index],
            language,
        )
    _draw_constellation_list_scrollbar(view_x + view_w - 3, view_y, view_h, scroll, constellation_list_max_scroll(pyxel.width, pyxel.height, len(items)))


def _draw_constellation_search_tabs(language: Language, active_tab: str) -> None:
    if language == "ja":
        labels = {
            "constellation": "星座",
            "star": "星",
            "group": "星群",
        }
    else:
        labels = {
            "constellation": "CONST",
            "star": "STAR",
            "group": "GROUP",
        }
    for key, rect in constellation_list_tab_rects(pyxel.width, pyxel.height).items():
        if key == active_tab:
            draw_button_colored(rect, labels[key], 5, 10, 7)
        else:
            draw_button_colored(rect, labels[key], 1, 13, 13)


def _draw_constellation_list_button(
    rect: tuple[int, int, int, int],
    constellation: Constellation,
    selected: bool,
    available: bool,
    language: Language,
) -> None:
    x, y, w, h = rect
    if selected:
        fill, edge, text_col = 5, 10, 7
    elif available:
        fill, edge, text_col = 1, 13, 7
    else:
        fill, edge, text_col = 0, 5, 13
    pyxel.rect(x, y, w, h, fill)
    pyxel.rectb(x, y, w, h, edge)
    if selected:
        pyxel.rectb(x + 2, y + 2, w - 4, h - 4, 10)

    name = constellation_name(constellation, language)
    if language == "en":
        lines = _constellation_button_label_lines(name.upper(), w - 8)
        total_h = len(lines) * (GLYPH_H * SCALE) + max(0, len(lines) - 1) * 2
        text_y = y + max(3, (h - total_h) // 2)
        for line in lines:
            line_w = text_width(line)
            draw_big_text(x + max(4, (w - line_w) // 2), text_y, line, text_col)
            text_y += GLYPH_H * SCALE + 2
        return

    ja_lines = CONSTELLATION_JA_BUTTON_LINES.get(constellation.id)
    if ja_lines is not None:
        total_h = len(ja_lines) * FONT_CELL_HEIGHT + max(0, len(ja_lines) - 1) * 2
        text_y = y + max(3, (h - total_h) // 2)
        for line in ja_lines:
            line_w = display_text_width(line)
            draw_display_text(x + max(4, (w - line_w) // 2), text_y, line, text_col)
            text_y += FONT_CELL_HEIGHT + 2
        return

    label_w = display_text_width(name)
    text_y = y + max(3, (h - FONT_CELL_HEIGHT) // 2)
    draw_display_text(x + max(4, (w - label_w) // 2), text_y, name, text_col)


def _draw_search_list_button(
    rect: tuple[int, int, int, int],
    item: SearchListItem,
    language: Language,
) -> None:
    x, y, w, h = rect
    if item.selected:
        fill, edge, text_col = 5, 10, 7
    elif item.available:
        fill, edge, text_col = 1, 13, 7
    else:
        fill, edge, text_col = 0, 5, 13
    pyxel.rect(x, y, w, h, fill)
    pyxel.rectb(x, y, w, h, edge)
    if item.selected:
        pyxel.rectb(x + 2, y + 2, w - 4, h - 4, 10)

    lines = item.label_lines or _search_button_label_lines(item.label, language, w - 8)
    if language == "en":
        total_h = len(lines) * (GLYPH_H * SCALE) + max(0, len(lines) - 1) * 2
        text_y = y + max(3, (h - total_h) // 2)
        for line in lines:
            line_w = text_width(line.upper())
            draw_big_text(x + max(4, (w - line_w) // 2), text_y, line, text_col)
            text_y += GLYPH_H * SCALE + 2
        return

    total_h = len(lines) * FONT_CELL_HEIGHT + max(0, len(lines) - 1) * 2
    text_y = y + max(3, (h - total_h) // 2)
    for line in lines:
        line_w = display_text_width(line)
        draw_display_text(x + max(4, (w - line_w) // 2), text_y, line, text_col)
        text_y += FONT_CELL_HEIGHT + 2


def _search_button_label_lines(label: str, language: Language, max_width: int) -> tuple[str, ...]:
    if language == "en":
        return _constellation_button_label_lines(label.upper(), max_width)
    if display_text_width(label) <= max_width:
        return (label,)
    separators = ("の", "・", " ")
    best: tuple[str, str] | None = None
    best_score = 999999
    for index in range(1, len(label)):
        bonus = -1000 if label[index - 1] in separators or label[index] in separators else 0
        left = label[:index]
        right = label[index:]
        widest = max(display_text_width(left), display_text_width(right))
        balance = abs(display_text_width(left) - display_text_width(right))
        score = widest * 10 + balance + bonus
        if widest <= max_width:
            score -= 10000
        if score < best_score:
            best = (left, right)
            best_score = score
    return best or (label,)


def _constellation_button_label_lines(text: str, max_width: int) -> tuple[str, ...]:
    if text_width(text) <= max_width:
        return (text,)
    words = text.split()
    if len(words) <= 1:
        return _split_long_constellation_word(text, max_width)
    best: tuple[str, str] | None = None
    best_score = 999999
    for split_at in range(1, len(words)):
        left = " ".join(words[:split_at])
        right = " ".join(words[split_at:])
        widest = max(text_width(left), text_width(right))
        balance = abs(text_width(left) - text_width(right))
        score = widest * 10 + balance
        if widest <= max_width:
            score -= 10000
        if score < best_score:
            best = (left, right)
            best_score = score
    return best or (text,)


def _split_long_constellation_word(text: str, max_width: int) -> tuple[str, ...]:
    preferred = CONSTELLATION_SINGLE_WORD_SPLITS.get(text)
    if preferred is not None and all(text_width(line) <= max_width for line in preferred):
        return preferred
    max_chars = max(4, (max_width + 2) // CHAR_STEP)
    if len(text) <= max_chars:
        return (text,)
    split_at = min(len(text) - 3, max(3, len(text) // 2))
    if text_width(text[:split_at]) > max_width:
        split_at = max(3, max_chars)
    return (text[:split_at], text[split_at:])


def _draw_constellation_list_scrollbar(x: int, y: int, h: int, scroll: int, max_scroll: int) -> None:
    if max_scroll <= 0:
        return
    pyxel.rect(x, y, 2, h, 1)
    knob_h = max(18, h * h // (h + max_scroll))
    knob_y = y + int((h - knob_h) * max(0.0, min(1.0, scroll / max_scroll)))
    pyxel.rect(x - 1, knob_y, 4, knob_h, 13)
