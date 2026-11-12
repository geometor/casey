"""Demo 1: Casey's Generalized Ptolemy Theorem & Feuerbach's Nine-Point Tangency (Units 1 & 4).

Verifies:
1. Universal polynomial proof of Casey's bitangent relation ``t_12*t_34 + t_14*t_23 = t_13*t_24``
   under circular inversion (Book VI, Sec. IV, Props. 9–10, pp. 102–104).
2. Universal ``(a, b, c)`` bitangent identities for both the incircle and the excircles
   (Prop. 10, Cor. 2, pp. 104–105).
3. Exact compass-and-straightedge construction on the Heronian ``(15, 13, 14)`` triangle,
   confirming Casey's 1861 orthogonal inversion circle ``(Ma, 1/2)`` and tangency at the
   Feuerbach point ``Fe = X(11) = (6, 8)``.
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
    construct_casey_feuerbach,
    construct_euler_nine_point,
    export_svg,
    prove_casey_feuerbach_heronian,
    prove_casey_theorem_symbolic,
)


def run_demo(*, write_svgs: bool = True) -> None:
    """Execute the Casey–Feuerbach symbolic demonstration and optionally export interactive SVGs."""
    console = Console()
    sym_proof = prove_casey_theorem_symbolic()
    heron = prove_casey_feuerbach_heronian()
    unit1_res = construct_euler_nine_point()
    unit4_res = construct_casey_feuerbach()

    tbl_sym = Table(title="Casey's Generalized Ptolemy Theorem — Symbolic Verification (VI.IV.9–10)")
    tbl_sym.add_column("Algebraic Identity", style="cyan bold")
    tbl_sym.add_column("Residual", style="green")
    tbl_sym.add_row("Inversion invariance of t_12^2 / (r_1 r_2) (Prop. 9)", str(sym_proof.inversion_invariance_residual))
    tbl_sym.add_row("Collinear contact Euler identity (Prop. 10)", str(sym_proof.tangent_line_euler_residual))
    tbl_sym.add_row("Incircle bitangent sum a(c-b)+b(a-c)-c(a-b) (Cor. 2)", str(sym_proof.incircle_casey_residual))
    tbl_sym.add_row("Casey Cor. 2 squared difference sum", str(sym_proof.incircle_cor2_squares_residual))
    tbl_sym.add_row("A-Excircle bitangent sum a(c-b)+c(a+b)-b(a+c)", str(sym_proof.excircle_a_casey_residual))
    console.print(tbl_sym)

    tbl_heron = Table(title="Heronian (15, 13, 14) Exact Feuerbach & Bitangent Ledger")
    tbl_heron.add_column("Quantity", style="cyan bold")
    tbl_heron.add_column("Exact Symbolic Value", style="green")
    tbl_heron.add_row("Sides (a, b, c) & Area Δ", f"{heron.sides}, Δ = {heron.area}")
    tbl_heron.add_row("Radii (r, R, R_9)", f"r = {heron.inradius}, R = {heron.circumradius}, R_9 = {heron.nine_point_radius}")
    tbl_heron.add_row("Exradii (r_a, r_b, r_c)", str(heron.exradii))
    tbl_heron.add_row("Midpoint chords (t_23, t_31, t_12)", str(heron.midpoint_chords))
    tbl_heron.add_row("Midpoint-to-incircle bitangents (|MaTa|, |MbTb|, |McTc|)", str(heron.incircle_midpoint_tangents))
    tbl_heron.add_row("Casey bitangent relation t_23*t_14 + t_31*t_24 - t_12*t_34", str(heron.casey_signed_sum))
    tbl_heron.add_row("Centre distance |N I| = R_9 - r", str(heron.ni_distance))
    tbl_heron.add_row("Feuerbach Point Fe = X(11)", f"{unit4_res.feuerbach_point} (steps={len(unit4_res.model.steps)})")
    tbl_heron.add_row("Excircle Feuerbach Touch Points", str(heron.excircle_feuerbach_points))
    tbl_heron.add_row(
        "Casey 1861 Circle (Ma, 1/2) Orthogonal to I & I_a",
        f"{heron.inversion_circle_orthogonal_to_incircle} & {heron.inversion_circle_orthogonal_to_excircle_a}",
    )
    console.print(tbl_heron)

    if write_svgs:
        u1_focus = [
            *unit1_res.vertices,
            *unit1_res.midpoints,
            unit1_res.circumcenter,
            unit1_res.orthocenter,
        ]
        for out_u1 in (
            _REPO_ROOT / "docsrc" / "sequel_to_euclid" / "unit-1" / "0083.g1.svg",
            _REPO_ROOT / "docsrc" / "_static" / "figures" / "unit1_euler_nine_point.svg",
        ):
            export_svg(
                unit1_res.model,
                out_u1,
                graphic_id="0083.g1",
                title="Casey Book IV Prop. 5 — Euler Line & Nine-Points Circle",
                bbox=(-2.5, 16.5, -4.6, 13.4),
                focus_points=u1_focus,
                highlight_point_ids=("O", "G", "N", "H"),
            )

        for out_u4 in (
            _REPO_ROOT / "docsrc" / "sequel_to_euclid" / "unit-4" / "0130.g1.svg",
            _REPO_ROOT / "docsrc" / "_static" / "figures" / "unit4_casey_feuerbach.svg",
        ):
            export_svg(
                unit4_res.model,
                out_u4,
                graphic_id="0130.g1",
                title="Casey Book VI Sec. IV Prop. 10 Cor. 2 — Casey's Inversion & Feuerbach Tangency at X(11)",
                bbox=(-2.5, 16.5, -4.6, 13.4),
                highlight_point_ids=("Fe", "Ma", "I", "N"),
            )


if __name__ == "__main__":
    run_demo()
