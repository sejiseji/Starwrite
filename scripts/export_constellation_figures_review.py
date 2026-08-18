from __future__ import annotations

import json
import math
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.data.constellation_line_reference_88 import (  # noqa: E402
    CONSTELLATION_LINE_EDGES_HIP,
    CONSTELLATION_LINE_POLYLINES_HIP,
    REFERENCE_ATTRIBUTION,
)
from src.data.constellations import CONSTELLATIONS  # noqa: E402
from src.data.star_descriptions import STAR_DESCRIPTIONS  # noqa: E402
from src.data.stars import STAR_NAMES, STARS_BY_ID  # noqa: E402
from src.ui.localization import CONSTELLATION_NAMES_JA, STAR_NAMES_JA  # noqa: E402


OUTPUT_JSON = ROOT / "exports" / "starwrite_constellation_figures_review.json"
OUTPUT_MD = ROOT / "exports" / "starwrite_constellation_figures_review.md"


def _git_short_sha() -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception:
        return None
    return result.stdout.strip() or None


def _star_record(star_id: int) -> dict[str, Any]:
    star = STARS_BY_ID[star_id]
    english_name = STAR_NAMES.get(star_id)
    japanese_name = STAR_NAMES_JA.get(star_id)
    return {
        "hip": star_id,
        "label_en": english_name or f"HIP {star_id}",
        "label_ja": japanese_name or english_name or f"HIP {star_id}",
        "has_display_name": english_name is not None,
        "has_description": star_id in STAR_DESCRIPTIONS,
        "ra_hours": round(math.degrees(star.ra_rad) / 15.0, 6),
        "dec_deg": round(math.degrees(star.dec_rad), 6),
        "magnitude": star.magnitude,
        "color_index": star.color_index,
    }


def _edge_record(edge: tuple[int, int]) -> dict[str, Any]:
    a_id, b_id = edge
    return {
        "from": _star_record(a_id),
        "to": _star_record(b_id),
        "hip_pair": [a_id, b_id],
        "label_en": f"{_star_record(a_id)['label_en']} -- {_star_record(b_id)['label_en']}",
        "label_ja": f"{_star_record(a_id)['label_ja']} -- {_star_record(b_id)['label_ja']}",
    }


def _polyline_record(index: int, path: tuple[int, ...]) -> dict[str, Any]:
    segments = [[path[i], path[i + 1]] for i in range(len(path) - 1)]
    return {
        "index": index,
        "hip_ids": list(path),
        "labels_en": [_star_record(star_id)["label_en"] for star_id in path],
        "labels_ja": [_star_record(star_id)["label_ja"] for star_id in path],
        "segments": segments,
        "path_en": " -> ".join(_star_record(star_id)["label_en"] for star_id in path),
        "path_ja": " -> ".join(_star_record(star_id)["label_ja"] for star_id in path),
    }


def _branch_points(edges: tuple[tuple[int, int], ...]) -> list[dict[str, Any]]:
    degree = Counter()
    for a_id, b_id in edges:
        degree[a_id] += 1
        degree[b_id] += 1
    return [
        {
            "hip": star_id,
            "degree": count,
            "label_en": _star_record(star_id)["label_en"],
            "label_ja": _star_record(star_id)["label_ja"],
        }
        for star_id, count in sorted(degree.items())
        if count > 2
    ]


def _constellation_record(order: int, constellation) -> dict[str, Any]:
    edges = CONSTELLATION_LINE_EDGES_HIP[constellation.id]
    polylines = CONSTELLATION_LINE_POLYLINES_HIP[constellation.id]
    star_ids = tuple(sorted({star_id for edge in edges for star_id in edge}))
    named_count = sum(1 for star_id in star_ids if star_id in STAR_NAMES)
    described_count = sum(1 for star_id in star_ids if star_id in STAR_DESCRIPTIONS)
    return {
        "id": constellation.id,
        "app_order": order,
        "name_en": constellation.name,
        "name_ja": CONSTELLATION_NAMES_JA.get(constellation.id, constellation.name),
        "anchor_star_id": constellation.anchor_star_id,
        "counts": {
            "stars": len(star_ids),
            "named_stars": named_count,
            "stars_with_descriptions": described_count,
            "stars_without_display_name": len(star_ids) - named_count,
            "edges": len(edges),
            "polylines": len(polylines),
            "branch_points": len(_branch_points(edges)),
        },
        "review_priority_hint": constellation.id in {"CET", "LAC", "LUP"},
        "branch_points": _branch_points(edges),
        "polylines": [_polyline_record(i + 1, path) for i, path in enumerate(polylines)],
        "edges": [_edge_record(edge) for edge in edges],
        "stars": [_star_record(star_id) for star_id in star_ids],
    }


def build_review_data() -> dict[str, Any]:
    constellation_records = [
        _constellation_record(order, constellation)
        for order, constellation in enumerate(CONSTELLATIONS, start=1)
    ]
    all_edge_star_ids = {
        star_id
        for edges in CONSTELLATION_LINE_EDGES_HIP.values()
        for edge in edges
        for star_id in edge
    }
    return {
        "schema_version": 1,
        "generated_from_commit": _git_short_sha(),
        "purpose": (
            "GPT-readable review data for the constellation stick figures currently implemented in Starwrite."
        ),
        "review_instruction": (
            "For each constellation, compare the listed polylines/edges with common modern star-chart stick figures. "
            "Flag likely_wrong or questionable shapes, especially if branches, torso/limb outlines, or main outlines "
            "differ substantially from common references. If suggesting corrections, use HIP ids from the included "
            "stars list whenever possible."
        ),
        "notes": [
            "IAU standardizes constellation names, abbreviations, and sky boundaries, not a unique stick-figure line art.",
            "Feature/asterism lines such as seasonal triangles, Pleiades, Hyades, and the Big Dipper are not included here.",
            "stars_without_display_name means the endpoint is drawn as a star but does not currently have a display label or description.",
            "polylines preserve the source traversal order, including repeated HIP ids where a branch returns through the same star.",
        ],
        "attribution": REFERENCE_ATTRIBUTION,
        "counts": {
            "constellations": len(constellation_records),
            "edges": sum(len(edges) for edges in CONSTELLATION_LINE_EDGES_HIP.values()),
            "endpoint_stars": len(all_edge_star_ids),
            "named_endpoint_stars": len(all_edge_star_ids & set(STAR_NAMES)),
            "described_endpoint_stars": len(all_edge_star_ids & set(STAR_DESCRIPTIONS)),
            "unnamed_endpoint_stars": len(all_edge_star_ids - set(STAR_NAMES)),
        },
        "constellations": sorted(constellation_records, key=lambda item: item["name_en"]),
    }


def _markdown_star_label(star_id: int) -> str:
    record = _star_record(star_id)
    suffix = ""
    if not record["has_display_name"]:
        suffix = " [no display name]"
    return (
        f"{record['label_en']} / {record['label_ja']} "
        f"(HIP {star_id}, mag {record['magnitude']:.2f}, "
        f"RA {record['ra_hours']:.4f}h, Dec {record['dec_deg']:.4f}deg){suffix}"
    )


def build_markdown(data: dict[str, Any]) -> str:
    lines: list[str] = [
        "# Starwrite Constellation Figure Review",
        "",
        "This file lists the constellation stick figures currently implemented in Starwrite.",
        "Use it to compare each figure against common modern star-chart patterns.",
        "",
        "## Review Checklist",
        "",
        "- Mark each constellation as `acceptable`, `questionable`, or `likely_wrong`.",
        "- Check whether the main outline matches common references closely enough for Starwrite.",
        "- Check whether branches or repeated path points create odd shapes.",
        "- If a correction is needed, propose replacement polylines or edges using HIP ids.",
        "- Do not mix feature/asterism lines into constellation body lines.",
        "",
        "## Data Notes",
        "",
        f"- Generated from commit: `{data['generated_from_commit']}`",
        f"- Constellations: {data['counts']['constellations']}",
        f"- Edges: {data['counts']['edges']}",
        f"- Endpoint stars: {data['counts']['endpoint_stars']}",
        f"- Endpoint stars without display names: {data['counts']['unnamed_endpoint_stars']}",
        "",
    ]
    for item in data["constellations"]:
        priority = " REVIEW PRIORITY" if item["review_priority_hint"] else ""
        lines.extend(
            [
                f"## {item['id']} -- {item['name_en']} / {item['name_ja']}{priority}",
                "",
                (
                    f"Counts: stars {item['counts']['stars']}, edges {item['counts']['edges']}, "
                    f"polylines {item['counts']['polylines']}, branch points {item['counts']['branch_points']}, "
                    f"stars without display names {item['counts']['stars_without_display_name']}"
                ),
                "",
                "### Polylines",
                "",
            ]
        )
        for polyline in item["polylines"]:
            lines.append(f"{polyline['index']}. {polyline['path_en']}")
        lines.extend(["", "### Edges", ""])
        for edge in item["edges"]:
            lines.append(f"- {edge['label_en']}  |  {edge['label_ja']}")
        if item["branch_points"]:
            lines.extend(["", "### Branch Points", ""])
            for branch in item["branch_points"]:
                lines.append(
                    f"- {branch['label_en']} / {branch['label_ja']} "
                    f"(HIP {branch['hip']}): degree {branch['degree']}"
                )
        lines.extend(["", "### Stars", ""])
        for star in item["stars"]:
            lines.append(f"- {_markdown_star_label(star['hip'])}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    data = build_review_data()
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(build_markdown(data) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT_JSON}")
    print(f"wrote {OUTPUT_MD}")


if __name__ == "__main__":
    main()
