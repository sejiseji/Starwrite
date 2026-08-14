from __future__ import annotations

from dataclasses import dataclass

import pyxel

DEFAULT_BASE_SOUND = 48
SOUND_SLOTS_REQUIRED = 4

DEFAULT_PRIMARY_CHANNEL = 3
DEFAULT_ACCENT_CHANNEL = 0

CONSTELLATION_OFFSET = 0
STAR_OFFSET = 1
FEATURE_PRIMARY_OFFSET = 2
FEATURE_ACCENT_OFFSET = 3


def _validate(base_sound: int, primary_channel: int, accent_channel: int) -> None:
    if not 0 <= base_sound <= 64 - SOUND_SLOTS_REQUIRED:
        raise ValueError(f"base_sound must be between 0 and {64 - SOUND_SLOTS_REQUIRED}")
    if not 0 <= primary_channel <= 3:
        raise ValueError("primary_channel must be between 0 and 3")
    if not 0 <= accent_channel <= 3:
        raise ValueError("accent_channel must be between 0 and 3")
    if primary_channel == accent_channel:
        raise ValueError("primary_channel and accent_channel must differ")


def install_starwrite_ui_sfx(*, base_sound: int = DEFAULT_BASE_SOUND) -> None:
    if not 0 <= base_sound <= 64 - SOUND_SLOTS_REQUIRED:
        raise ValueError(f"base_sound must be between 0 and {64 - SOUND_SLOTS_REQUIRED}")

    pyxel.sound(base_sound + CONSTELLATION_OFFSET).set(
        "c3 g3 c4",
        "t",
        "432",
        "f",
        8,
    )
    pyxel.sound(base_sound + STAR_OFFSET).set(
        "e4 b4",
        "p",
        "42",
        "f",
        6,
    )
    pyxel.sound(base_sound + FEATURE_PRIMARY_OFFSET).set(
        "c3 r e3 r g3 b3 r e4 r d4 c4 r",
        "t",
        "403032020210",
        "f",
        12,
    )
    pyxel.sound(base_sound + FEATURE_ACCENT_OFFSET).set(
        "r g3 r b3 r d4 g4 r e4 r e4 r",
        "p",
        "020202302010",
        "f",
        12,
    )


def play_constellation_select(*, base_sound: int = DEFAULT_BASE_SOUND, channel: int = DEFAULT_PRIMARY_CHANNEL) -> None:
    if not 0 <= channel <= 3:
        raise ValueError("channel must be between 0 and 3")
    pyxel.play(channel, base_sound + CONSTELLATION_OFFSET)


def play_star_select(*, base_sound: int = DEFAULT_BASE_SOUND, channel: int = DEFAULT_PRIMARY_CHANNEL) -> None:
    if not 0 <= channel <= 3:
        raise ValueError("channel must be between 0 and 3")
    pyxel.play(channel, base_sound + STAR_OFFSET)


def play_feature_select(
    *,
    base_sound: int = DEFAULT_BASE_SOUND,
    primary_channel: int = DEFAULT_PRIMARY_CHANNEL,
    accent_channel: int = DEFAULT_ACCENT_CHANNEL,
) -> None:
    _validate(base_sound, primary_channel, accent_channel)
    pyxel.play(primary_channel, base_sound + FEATURE_PRIMARY_OFFSET)
    try:
        pyxel.play(accent_channel, base_sound + FEATURE_ACCENT_OFFSET, resume=True)
    except TypeError:
        pass


@dataclass(slots=True)
class StarwriteUISfx:
    base_sound: int = DEFAULT_BASE_SOUND
    primary_channel: int = DEFAULT_PRIMARY_CHANNEL
    accent_channel: int = DEFAULT_ACCENT_CHANNEL

    def install(self) -> None:
        _validate(self.base_sound, self.primary_channel, self.accent_channel)
        install_starwrite_ui_sfx(base_sound=self.base_sound)

    def constellation(self) -> None:
        play_constellation_select(base_sound=self.base_sound, channel=self.primary_channel)

    def star(self) -> None:
        play_star_select(base_sound=self.base_sound, channel=self.primary_channel)

    def feature(self) -> None:
        play_feature_select(
            base_sound=self.base_sound,
            primary_channel=self.primary_channel,
            accent_channel=self.accent_channel,
        )
