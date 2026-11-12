"""Demo 4: Symmedians, Lemoine Circles, Brocard Points, Brocard Circle & Associated Points (Units 5 & 6).

Constructs on the Heronian ``(15, 13, 14)`` triangle ``A=(0,0), B=(14,0), C=(5,12)``:
1. Lemoine's Symmedian Point ``K = X(6) = (1673/295, 1176/295)`` via circumcircle tangents.
2. First Lemoine Circle (6 side-parallel intersections centered at ``Ml = midpoint(O, K)``)
   and Cosine Circle (6 antiparallel intersections centered at ``K``).
3. First & Second Brocard Points ``Ω, Ω'``, Brocard Angle ``cot(ω) = 295/168``, Brocard's First
   Triangle ``A1 B1 C1``, and the seven-point **Brocard Circle** on diameter ``OK``.
4. Steiner's Point ``X(99)``, Tarry's Point ``X(98)``, and de Longchamps' Point ``X(20)``.
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
for _extra in (_REPO_ROOT / "src", _REPO_ROOT.parent / "model" / "src"):
    if _extra.exists() and str(_extra) not in sys.path:
        sys.path.insert(0, str(_extra))

from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.casey import (  # noqa: E402
    construct_brocard_and_lemoine_circles,
    construct_symmedian_and_lemoine_circles,
    export_svg,
)


def run_demo(*, write_svgs: bool = True) -> None:
    """Execute the Symmedian, Lemoine & Brocard geometry demo and export SVGs."""
    console = Console()
    lem = construct_symmedian_and_lemoine_circles()
    bro = construct_brocard_and_lemoine_circles()
    rep = bro.report

    table = Table(title="Casey Supplementary Chapter — Exact Rational Lemoine & Brocard Ledger")
    table.add_column("Center / Invariant", style="cyan bold")
    table.add_column("Exact Rational Expression on (15, 13, 14)", style="green")
    table.add_row("Circumcentre O = X(3)", str(bro.circumcenter))
    table.add_row("Symmedian Point K = X(6)", str(rep.symmedian_point))
    table.add_row("Brocard / First Lemoine Centre Ml = X(182)", str(rep.brocard_center))
    table.add_row("Brocard Angle cot(ω) & sin²(ω)", f"cot(ω) = {rep.cot_omega}, sin²(ω) = {rep.sin_sq_omega}")
    table.add_row("First Brocard Point Ω (c²a² : a²b² : b²c²)", str(rep.brocard_1))
    table.add_row("Second Brocard Point Ω′ (a²b² : b²c² : c²a²)", str(rep.brocard_2))
    table.add_row("Brocard's First Triangle (A1, B1, C1)", str(rep.brocard_first_triangle))
    table.add_row("Lemoine Intercept Cube Ratios (a³/b³, a³/c³)", str(rep.lemoine_intercept_ratios))
    table.add_row("Lagrange Minimum Σ dist² at K (Supp. I.7)", str(rep.min_perp_squares_sum))
    table.add_row("Steiner Point X(99) on Circumcircle", str(rep.steiner_point))
    table.add_row("Tarry Point X(98) (Antipode of X(99))", str(rep.tarry_point))
    table.add_row("de Longchamps Point X(20) = 2O - H", str(rep.longchamps_point))
    console.print(table)

    if write_svgs:
        for out_u5 in (
            _REPO_ROOT / "docsrc" / "sequel_to_euclid" / "unit-5" / "0205.g1.svg",
            _REPO_ROOT / "docsrc" / "_static" / "figures" / "unit5_symmedian_lemoine_circle.svg",
        ):
            export_svg(
                lem.model,
                out_u5,
                graphic_id="0205.g1",
                title="Casey Supp. Ch. Secs. I & III — Symmedian Point K, First Lemoine Circle & Cosine Circle",
                bbox=(-2.2, 16.2, -4.4, 13.2),
                highlight_point_ids=("K", "O", "Ml"),
            )

        for out_u6 in (
            _REPO_ROOT / "docsrc" / "sequel_to_euclid" / "unit-6" / "0220.g1.svg",
            _REPO_ROOT / "docsrc" / "_static" / "figures" / "unit6_brocard_circle.svg",
        ):
            export_svg(
                bro.model,
                out_u6,
                graphic_id="0220.g1",
                title="Casey Supp. Ch. Secs. II, V & VII — Brocard Points Ω, Ω′, Brocard Circle, Steiner X(99) & Tarry X(98)",
                bbox=(-2.2, 16.2, -4.5, 13.2),
                highlight_point_ids=("K", "Om1", "Om2", "St", "Tr"),
            )


if __name__ == "__main__":
    run_demo()
