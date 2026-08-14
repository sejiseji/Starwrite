from __future__ import annotations

import pyxel

TRACK_TITLE_JA = "星の余白"
TRACK_TITLE_EN = "Between the Stars"

SOUND_TICKS_PER_SECOND = 120
SECTION_COUNT = 4
BGM_CHANNELS = (0, 1, 2)
SOUND_SLOTS_REQUIRED = 12

DEFAULT_BASE_SOUND = 52
DEFAULT_MUSIC_ID = 7

_LEAD_NOTES = [
    "c4", "r", "r", "g3", "r", "e3", "r", "d3",
    "r", "e3", "r", "g3", "r", "a3", "r", "e3",
    "c4", "r", "a3", "r", "r", "g3", "r", "e3",
    "r", "d4", "r", "a3", "r", "g3", "r", "d3",
    "b3", "r", "r", "g3", "r", "e3", "r", "d3",
    "r", "e4", "r", "a3", "r", "g3", "r", "e3",
    "c4", "r", "f3", "r", "e3", "r", "d3", "r",
    "r", "d4", "r", "f3", "r", "g3", "r", "b3",
]

_LEAD_VOLUMES = [
    2, 0, 0, 2, 0, 2, 0, 1,
    0, 2, 0, 2, 0, 2, 0, 1,
    2, 0, 2, 0, 0, 2, 0, 1,
    0, 2, 0, 2, 0, 2, 0, 1,
    2, 0, 0, 2, 0, 2, 0, 1,
    0, 2, 0, 2, 0, 2, 0, 1,
    2, 0, 2, 0, 2, 0, 1, 0,
    0, 2, 0, 2, 0, 2, 0, 1,
]

_ARP_NOTES = [
    "c2", "g2", "e3", "g2", "d3", "g2", "e3", "g2",
    "a1", "e2", "c3", "e2", "g2", "e2", "c3", "e2",
    "f1", "c2", "a2", "c3", "e3", "c3", "a2", "c3",
    "g1", "d2", "a2", "d3", "g2", "d3", "a2", "d3",
    "e1", "b1", "e2", "g2", "b2", "d3", "b2", "g2",
    "a1", "e2", "c3", "e2", "g2", "e2", "c3", "e2",
    "d1", "a1", "f2", "a2", "e3", "a2", "f2", "a2",
    "g1", "d2", "g2", "c3", "d3", "c3", "g2", "b1",
]

_ARP_VOLUMES = [2, 1, 2, 1, 2, 1, 2, 1] * 8

_BASS_NOTES = [
    "c1", "g0", "a0", "e1", "f0", "c1", "g0", "d1",
    "e0", "b0", "a0", "e1", "d1", "a0", "g0", "b0",
]

_BASS_VOLUMES = [2, 1] * 8

_CHANNEL_SPECS = (
    {
        "notes": _LEAD_NOTES,
        "volumes": _LEAD_VOLUMES,
        "tone": "p",
        "effect": "f",
        "speed": 56,
    },
    {
        "notes": _ARP_NOTES,
        "volumes": _ARP_VOLUMES,
        "tone": "t",
        "effect": "f",
        "speed": 56,
    },
    {
        "notes": _BASS_NOTES,
        "volumes": _BASS_VOLUMES,
        "tone": "t",
        "effect": "f",
        "speed": 224,
    },
)


def _chunks(values: list[str] | list[int], count: int) -> list[list[str] | list[int]]:
    if len(values) % count != 0:
        raise ValueError("Channel data must divide evenly into sections")
    size = len(values) // count
    return [values[index * size : (index + 1) * size] for index in range(count)]


def install_starwrite_bgm(
    *,
    base_sound: int = DEFAULT_BASE_SOUND,
    music_id: int = DEFAULT_MUSIC_ID,
) -> None:
    if not 0 <= base_sound <= 64 - SOUND_SLOTS_REQUIRED:
        raise ValueError(f"base_sound must be between 0 and {64 - SOUND_SLOTS_REQUIRED}")
    if not 0 <= music_id < 8:
        raise ValueError("music_id must be between 0 and 7")

    music_sequences: list[list[int]] = []
    for channel_index, spec in enumerate(_CHANNEL_SPECS):
        note_sections = _chunks(spec["notes"], SECTION_COUNT)
        volume_sections = _chunks(spec["volumes"], SECTION_COUNT)
        sound_ids: list[int] = []
        for section_index, (notes, volumes) in enumerate(zip(note_sections, volume_sections, strict=True)):
            sound_id = base_sound + channel_index * SECTION_COUNT + section_index
            pyxel.sound(sound_id).set(
                " ".join(notes),
                spec["tone"],
                "".join(str(volume) for volume in volumes),
                spec["effect"],
                spec["speed"],
            )
            sound_ids.append(sound_id)
        music_sequences.append(sound_ids)

    pyxel.music(music_id).set(
        music_sequences[0],
        music_sequences[1],
        music_sequences[2],
        [],
    )


def play_starwrite_bgm(*, music_id: int = DEFAULT_MUSIC_ID, loop: bool = True) -> None:
    pyxel.playm(music_id, loop=loop)


def stop_starwrite_bgm() -> None:
    for channel in BGM_CHANNELS:
        pyxel.stop(channel)


def loop_seconds() -> float:
    return 64 * 56 / SOUND_TICKS_PER_SECOND
