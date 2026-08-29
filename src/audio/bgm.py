from __future__ import annotations

import pyxel

TRACK_TITLE_JA = "星の余白"
TRACK_TITLE_EN = "Between the Stars"

SOUND_TICKS_PER_SECOND = 120
SECTION_COUNT = 4

# BGMは2chだけ使用する。
# ch2/ch3を空けることで、UI効果音を鳴らした時の同時発音負荷と競合を抑える。
BGM_CHANNELS = (0, 1)
SOUND_SLOTS_REQUIRED = 8

DEFAULT_BASE_SOUND = 52
DEFAULT_MUSIC_ID = 7

# 元のリードで実際に鳴っていた32音を維持し、
# 「音 + 休符」の64ステップを32ステップへ畳み込む。
# speedを56 -> 112へ倍化するため、ループ長は約29.9秒のまま。
_LEAD_NOTES = [
    "c4", "g3", "e3", "d3",
    "e3", "g3", "a3", "e3",
    "c4", "a3", "g3", "e3",
    "d4", "a3", "g3", "d3",
    "b3", "g3", "e3", "d3",
    "e4", "a3", "g3", "e3",
    "c4", "f3", "e3", "d3",
    "d4", "f3", "g3", "b3",
]

_LEAD_VOLUMES = [2, 2, 2, 1] * 8

# 旧アルペジオとベースを、低密度の1本の伴奏へ統合する。
# コード進行と上下のきらめきは残しつつ、常時発音を3ch -> 2chへ削減。
_HARMONY_NOTES = [
    "c2", "g2", "e3", "g2",
    "a1", "e2", "c3", "e2",
    "f1", "c2", "a2", "c3",
    "g1", "d2", "a2", "d3",
    "e1", "b1", "g2", "b2",
    "a1", "e2", "c3", "e2",
    "d1", "a1", "f2", "a2",
    "g1", "d2", "g2", "b2",
]

# 伴奏は常に1。リードと重なった時のピークを抑え、割れにくくする。
_HARMONY_VOLUMES = [1] * len(_HARMONY_NOTES)

_CHANNEL_SPECS = (
    {
        "notes": _LEAD_NOTES,
        "volumes": _LEAD_VOLUMES,
        "tone": "p",
        # リードのみ長めのFadeOutを残し、元の星屑感を維持する。
        "effect": "f",
        "speed": 112,
    },
    {
        "notes": _HARMONY_NOTES,
        "volumes": _HARMONY_VOLUMES,
        "tone": "t",
        # 伴奏の全音FadeOutは外す。短音FadeOut由来の途切れ感を避ける。
        "effect": "n",
        "speed": 112,
    },
)


def _chunks(values: list[str] | list[int], count: int) -> list[list[str] | list[int]]:
    if len(values) % count != 0:
        raise ValueError("Channel data must divide evenly into sections")
    size = len(values) // count
    return [values[index * size : (index + 1) * size] for index in range(count)]


def _validate_channel_specs() -> None:
    durations: set[int] = set()
    for spec in _CHANNEL_SPECS:
        notes = spec["notes"]
        volumes = spec["volumes"]
        speed = spec["speed"]

        if len(notes) != len(volumes):
            raise ValueError("Each channel must have one volume value per note")
        if len(notes) % SECTION_COUNT != 0:
            raise ValueError("Each channel must divide evenly into sections")

        durations.add(len(notes) * speed)

    if len(durations) != 1:
        raise ValueError("All BGM channels must have the same loop duration")


def install_starwrite_bgm(
    *,
    base_sound: int = DEFAULT_BASE_SOUND,
    music_id: int = DEFAULT_MUSIC_ID,
) -> None:
    _validate_channel_specs()

    if not 0 <= base_sound <= 64 - SOUND_SLOTS_REQUIRED:
        raise ValueError(f"base_sound must be between 0 and {64 - SOUND_SLOTS_REQUIRED}")
    if not 0 <= music_id < 8:
        raise ValueError("music_id must be between 0 and 7")

    music_sequences: list[list[int]] = []
    for channel_index, spec in enumerate(_CHANNEL_SPECS):
        note_sections = _chunks(spec["notes"], SECTION_COUNT)
        volume_sections = _chunks(spec["volumes"], SECTION_COUNT)
        sound_ids: list[int] = []

        for section_index, (notes, volumes) in enumerate(
            zip(note_sections, volume_sections, strict=True)
        ):
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
        [],
        [],
    )


def play_starwrite_bgm(*, music_id: int = DEFAULT_MUSIC_ID, loop: bool = True) -> None:
    pyxel.playm(music_id, loop=loop)


def stop_starwrite_bgm() -> None:
    for channel in BGM_CHANNELS:
        pyxel.stop(channel)


def loop_seconds() -> float:
    spec = _CHANNEL_SPECS[0]
    return len(spec["notes"]) * spec["speed"] / SOUND_TICKS_PER_SECOND
