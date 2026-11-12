"""Command-line interface for ``geometor-casey`` exact symbolic verifications & concordances."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from rich.console import Console
from rich.table import Table

from geometor.casey.brocard import construct_brocard_and_lemoine_circles
from geometor.casey.coaxial import construct_radical_axis_and_coaxial_pencil
from geometor.casey.concordance import audit_sympy_circle_gaps, load_concordance
from geometor.casey.feuerbach import prove_casey_feuerbach_heronian, prove_casey_theorem_symbolic
from geometor.casey.poles_polars import construct_pole_and_polar, verify_lahire_reciprocity_symbolic


def _print_summary(console: Console) -> None:
    """Print an executive Rich summary table of all verified theorems in Casey's *Sequel*."""
    sym_casey = prove_casey_theorem_symbolic()
    heron_fb = prove_casey_feuerbach_heronian()
    coax = construct_radical_axis_and_coaxial_pencil()
    lahire = verify_lahire_reciprocity_symbolic()
    polars = construct_pole_and_polar()
    brocard = construct_brocard_and_lemoine_circles()

    table = Table(title="GEOMETOR • John Casey — Sequel to Euclid Exact Symbolic Ledger")
    table.add_column("Codex Unit", style="cyan", no_wrap=True)
    table.add_column("Theorem / Construction", style="bold")
    table.add_column("Key Exact Invariant", style="green")
    table.add_column("Status", justify="center")

    table.add_row(
        "Unit 2 (III.23–28, VI.V)",
        "Disjoint Radical Axis & Poncelet Limiting Points",
        f"Rc={coax.radical_center}, L1={coax.limiting_points[0]}, L2={coax.limiting_points[1]}",
        "PASS" if coax.report.verified else "FAIL",
    )
    table.add_row(
        "Unit 4 (VI.IV.9–10)",
        "Casey's Generalized Ptolemy & Feuerbach X(11)",
        f"Fe={heron_fb.feuerbach_point}, |NI|={heron_fb.ni_distance}=R9-r",
        "PASS" if (sym_casey.verified and heron_fb.verified) else "FAIL",
    )
    table.add_row(
        "Unit 4 (III.25, VI.VII)",
        "Poles, Polars, Harmonic Secants & La Hire",
        f"D={polars.pole_d}, (G,H;J,D)={polars.cross_ratio_secant_1}",
        "PASS" if (lahire.verified and polars.lahire_verified) else "FAIL",
    )
    table.add_row(
        "Units 5–6 (Supp. I–VII)",
        "Symmedian K, Lemoine & Brocard Circles, X(98)/X(99)",
        f"K={brocard.symmedian_point}, cot(ω)={brocard.report.cot_omega}",
        "PASS" if brocard.report.verified else "FAIL",
    )
    console.print(table)

    gap_table = Table(title="sympy.geometry.Circle Capability Audit vs. geometor.casey")
    gap_table.add_column("Primitive", style="magenta")
    gap_table.add_column("sympy.Circle Native?", justify="center")
    gap_table.add_column("Casey Locus")
    gap_table.add_column("geometor.casey API", style="yellow")
    for gap in audit_sympy_circle_gaps():
        gap_table.add_row(
            gap.capability,
            "Yes" if gap.sympy_method_present else "No",
            gap.casey_locus,
            gap.geometor_casey_api,
        )
    console.print(gap_table)


def _print_concordance(console: Console) -> None:
    """Print the cross-repository concordance table."""
    entries = load_concordance()
    table = Table(title=f"Casey Sequel Cross-Repository Concordance ({len(entries)} Entries)")
    table.add_column("Unit", style="cyan", no_wrap=True)
    table.add_column("Casey Locus (1888)", style="bold")
    table.add_column("Folio / p.")
    table.add_column("Euclid")
    table.add_column("Altshiller-Court")
    table.add_column("ETC / Pappus", style="green")

    for entry in entries:
        etc_pappus = ", ".join([*entry.etc_centers, *entry.pappus_refs]) or "—"
        table.add_row(
            entry.unit,
            f"{entry.casey_locus}: {entry.title}",
            f"{entry.folio} (p. {entry.page})",
            ", ".join(entry.euclid_refs) or "—",
            ", ".join(entry.altshiller_court_refs) or "—",
            etc_pappus,
        )
    console.print(table)


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for the ``casey`` CLI command.

    Args:
        argv: Optional sequence of command-line arguments.

    Returns:
        Exit status code (``0`` on success).
    """
    parser = argparse.ArgumentParser(
        prog="casey",
        description="GEOMETOR • John Casey's Sequel to Euclid symbolic verifier and concordance.",
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="summary",
        choices=("summary", "concordance"),
        help="Subcommand to execute (default: summary).",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)
    console = Console()
    if args.command == "concordance":
        _print_concordance(console)
    else:
        _print_summary(console)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
