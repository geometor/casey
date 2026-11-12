"""Demo 2: Radical Axis, Coaxal System & Poncelet Limiting Points (Unit 2).

Constructs the radical axis of two disjoint circles ``C1=((-10,0), 6)`` and ``C2=((17,0), 15)``
via an auxiliary secant circle ``C_aux=((2,8), 10)`` (Casey Book III, Prop. 28), locates the
Radical Centre ``Rc=(0,-6)``, constructs Poncelet's Limiting Points ``L1=(-8,0), L2=(8,0)``,
and verifies Casey's Fundamental Theorem of Coaxal Circles (Book III, Prop. 24).
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
    circle_power,
    construct_radical_axis_and_coaxial_pencil,
    export_svg,
)


def run_demo(*, write_svgs: bool = True) -> None:
    """Execute the Coaxal Pencil & Limiting Points demo and optionally export SVGs."""
    console = Console()
    res = construct_radical_axis_and_coaxial_pencil()

    table = Table(title="Casey Book III Props. 22–28 & VI.V — Coaxal System & Limiting Points")
    table.add_column("Element / Invariant", style="cyan bold")
    table.add_column("Exact Symbolic Value", style="green")
    table.add_row("Primary Disjoint Circles C1, C2", f"C1=({res.c1.center}, r={res.c1.radius}), C2=({res.c2.center}, r={res.c2.radius})")
    table.add_row("Third Coaxal Circle C3", f"C3=({res.c3_coaxial.center}, r={res.c3_coaxial.radius})")
    table.add_row("Radical Centre Rc (via C_aux)", f"{res.radical_center}, pow(Rc, C1)={circle_power(res.radical_center, res.c1)}")
    table.add_row("Radical Axis [Rc D]", f"{res.radical_axis.equation()} = 0, foot D={res.radical_foot}")
    table.add_row("C1 Tangent Contact T1 from D", str(res.tangent_contact_c1))
    table.add_row("Poncelet Limiting Points (L1, L2)", f"{res.limiting_points[0]}, {res.limiting_points[1]}")
    table.add_row(
        "Orthogonal Circle (Rc, L1) Cuts C1, C2, C3",
        f"{res.report.orthogonal_to_c1}, {res.report.orthogonal_to_c2}, {res.report.orthogonal_to_c3}",
    )
    table.add_row("Book III Prop. 24 Symbolic Residual", str(res.report.symbolic_prop24_residual))
    console.print(table)

    if write_svgs:
        for out_path in (
            _REPO_ROOT / "docsrc" / "sequel_to_euclid" / "unit-2" / "0069.g1.svg",
            _REPO_ROOT / "docsrc" / "_static" / "figures" / "unit2_coaxial_limiting_points.svg",
        ):
            export_svg(
                res.model,
                out_path,
                graphic_id="0069.g1",
                title="Casey Book III Props. 23–28 — Disjoint Radical Axis, Orthogonal Pencil & Poncelet Limiting Points",
                bbox=(-18.0, 34.0, -17.5, 19.5),
                highlight_point_ids=("Rc", "L1", "L2"),
            )


if __name__ == "__main__":
    run_demo()
