"""Demo 3: Complete Quadrilateral Harmonic Section, Poles & Polars, and La Hire Reciprocity (Units 3 & 4).

Constructs:
1. Casey Book VI, Sec. III, Prop. 7 (p. 91): Complete Quadrilateral harmonic diagonal ranges.
2. Casey Book III, Props. 25, 27 & Book VI, Sec. VII, Prop. 2: Pure-straightedge inscribed
   quadrangle polar construction, Self-Conjugate Triangle ``D U V``, harmonic secant section
   ``(G, H; J, D) = -1``, and La Hire's Reciprocity ``Q in polar(D) <=> D in polar(Q)``.
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
    construct_complete_quadrilateral_harmonic,
    construct_pole_and_polar,
    export_svg,
    verify_lahire_reciprocity_symbolic,
)


def run_demo(*, write_svgs: bool = True) -> None:
    """Execute the Complete Quadrilateral & Pole–Polar Reciprocity demo and export SVGs."""
    console = Console()
    quad = construct_complete_quadrilateral_harmonic()
    sym_lh = verify_lahire_reciprocity_symbolic()
    pol = construct_pole_and_polar()

    tbl_q = Table(title="Casey Book VI Sec. III Prop. 7 — Complete Quadrilateral Harmonic Ranges")
    tbl_q.add_column("Element / Cross-Ratio", style="cyan bold")
    tbl_q.add_column("Exact Symbolic Value", style="green")
    tbl_q.add_row("Opposite Side Meets (E, F)", f"E={quad.opposite_meets[0]}, F={quad.opposite_meets[1]}")
    tbl_q.add_row("Internal Diagonal Meet P", str(quad.diagonal_center))
    tbl_q.add_row("Third Diagonal Meets (Qa, Qb)", f"Qa={quad.third_diagonal_meets[0]}, Qb={quad.third_diagonal_meets[1]}")
    tbl_q.add_row("Cross-Ratios (A,C;P,Qa) & (B,D;P,Qb)", f"{quad.cross_ratio_ac} & {quad.cross_ratio_bd}")
    console.print(tbl_q)

    tbl_p = Table(title="Casey Book III Prop. 25 & VI.VII — Poles, Polars & La Hire Reciprocity")
    tbl_p.add_column("Element / Invariant", style="cyan bold")
    tbl_p.add_column("Exact Symbolic Value", style="green")
    tbl_p.add_row("Symbolic Bilinear Reciprocity Residual", str(sym_lh.reciprocity_bilinear_diff))
    tbl_p.add_row("Pole D & Polar [U V]", f"D={pol.pole_d}, {pol.polar_d.equation()} = 0")
    tbl_p.add_row("Self-Conjugate Triangle (D, U, V)", f"{pol.self_conjugate_triangle}")
    tbl_p.add_row("Harmonic Secant Cross-Ratios", f"(G1,H1;J1,D)={pol.cross_ratio_secant_1}, (G2,H2;J2,D)={pol.cross_ratio_secant_2}")
    tbl_p.add_row("Reciprocal Pole Q on polar(D)", f"Q={pol.reciprocal_pole_q}, polar(Q): {pol.polar_q.equation()} = 0")
    tbl_p.add_row("La Hire Reciprocity D in polar(Q)", str(pol.lahire_verified))
    console.print(tbl_p)

    if write_svgs:
        for out_u3 in (
            _REPO_ROOT / "docsrc" / "sequel_to_euclid" / "unit-3" / "0117.g1.svg",
            _REPO_ROOT / "docsrc" / "_static" / "figures" / "unit3_complete_quadrilateral_harmonic.svg",
        ):
            export_svg(
                quad.model,
                out_u3,
                graphic_id="0117.g1",
                title="Casey Book VI Sec. III Prop. 7 — Complete Quadrilateral Harmonic Section",
                bbox=(-7.2, 9.2, -1.2, 10.2),
                highlight_point_ids=("P", "Qa", "Qb"),
            )

        for out_u4 in (
            _REPO_ROOT / "docsrc" / "sequel_to_euclid" / "unit-4" / "0071.g1.svg",
            _REPO_ROOT / "docsrc" / "_static" / "figures" / "unit4_poles_polars_lahire.svg",
        ):
            export_svg(
                pol.model,
                out_u4,
                graphic_id="0071.g1",
                title="Casey Book III Prop. 25 & VI.VII — Pole, Polar, Self-Conjugate Triangle & La Hire Reciprocity",
                bbox=(-6.5, 9.5, -6.5, 11.5),
                highlight_point_ids=("D", "Q", "U", "V"),
            )


if __name__ == "__main__":
    run_demo()
