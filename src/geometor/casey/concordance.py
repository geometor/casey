"""Cross-repository concordance and SymPy capability audit for Casey's *Sequel to Euclid*.

Provides structured access to ``resources/sequel_to_euclid/concordance.json`` mapping Casey's
propositions across ``euclid``, ``elements``, ``altshiller-court``, ``etc``, and ``pappus``,
alongside an empirical audit of ``sympy.geometry.Circle`` capability gaps filled by
:mod:`geometor.casey`.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy.geometry as spg

__all__ = [
    "ConcordanceEntry",
    "SympyCircleGap",
    "audit_sympy_circle_gaps",
    "get_resources_dir",
    "load_apparatus_registry",
    "load_concordance",
]


@dataclass(frozen=True)
class ConcordanceEntry:
    """Single proposition/topic concordance mapping across the GEOMETOR canon."""

    id: str
    unit: str
    casey_locus: str
    folio: str
    page: str
    title: str
    euclid_refs: tuple[str, ...]
    altshiller_court_refs: tuple[str, ...]
    etc_centers: tuple[str, ...]
    pappus_refs: tuple[str, ...]
    casey_symbol: str


@dataclass(frozen=True)
class SympyCircleGap:
    """Audit record comparing ``sympy.geometry.Circle`` against :mod:`geometor.casey`."""

    capability: str
    sympy_method_present: bool
    casey_locus: str
    geometor_casey_api: str


def get_resources_dir() -> Path:
    """Return the path to ``resources/sequel_to_euclid/`` inside the repository."""
    return Path(__file__).resolve().parents[3] / "resources" / "sequel_to_euclid"


def load_apparatus_registry(name: str) -> dict[str, Any]:
    """Load a JSON apparatus file (``persons``, ``citations``, ``glossary``, ``sources_manifest``).

    Args:
        name: Filename stem without ``.json`` extension.

    Returns:
        Parsed JSON dictionary.
    """
    path = get_resources_dir() / f"{name}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def load_concordance() -> list[ConcordanceEntry]:
    """Load all cross-repository concordance entries from ``concordance.json``.

    Returns:
        List of :class:`ConcordanceEntry` records in codex order.
    """
    raw = json.loads((get_resources_dir() / "concordance.json").read_text(encoding="utf-8"))
    entries: list[ConcordanceEntry] = []
    for item in raw.get("entries", []):
        entries.append(
            ConcordanceEntry(
                id=str(item["id"]),
                unit=str(item["unit"]),
                casey_locus=str(item["casey_locus"]),
                folio=str(item["folio"]),
                page=str(item["page"]),
                title=str(item["title"]),
                euclid_refs=tuple(item.get("euclid_refs", [])),
                altshiller_court_refs=tuple(item.get("altshiller_court_refs", [])),
                etc_centers=tuple(item.get("etc_centers", [])),
                pappus_refs=tuple(item.get("pappus_refs", [])),
                casey_symbol=str(item.get("casey_symbol", "")),
            )
        )
    return entries


def audit_sympy_circle_gaps() -> list[SympyCircleGap]:
    """Inspect :class:`sympy.geometry.Circle` for modern-circle-geometry primitives in Casey.

    Returns:
        List of :class:`SympyCircleGap` entries documenting native presence vs.
        :mod:`geometor.casey` exact symbolic implementations.
    """
    specs = (
        ("power_of_point", "Book III, Props. 20–24 (pp. 41–44)", "circle_power(pt, circ)"),
        ("is_orthogonal", "Book III, Prop. 22 (p. 42)", "are_orthogonal_circles(c1, c2)"),
        ("radical_axis", "Book III, Prop. 23 & Prop. 28 (p. 43)", "radical_axis_line(c1, c2)"),
        ("limiting_points", "Book III, Prop. 23 Def. & VI.V (pp. 43, 113)", "construct_radical_axis_and_coaxial_pencil()"),
        ("invert", "Book III, Def. (p. 41) & VI.IV (pp. 95–106)", "invert_point(pt, center, radius_sq)"),
        ("bitangent_distance", "Book VI, Sec. IV, Prop. 10 (pp. 103–104)", "bitangent_length(c1, c2, internal=...)"),
        ("polar_line", "Book III, Def. & Prop. 25 (pp. 44–45)", "polar_line(pt, circ)"),
        ("pole_of_line", "Book III, Def. & VI.VII (pp. 44, 141)", "pole_of_line(line, circ)"),
    )
    return [
        SympyCircleGap(
            capability=cap,
            sympy_method_present=hasattr(spg.Circle, cap),
            casey_locus=locus,
            geometor_casey_api=api,
        )
        for cap, locus, api in specs
    ]
