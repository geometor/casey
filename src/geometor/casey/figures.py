"""Exact symbolic 5-layer ``.euclid-graphic`` SVG figure builders for Casey's *Sequel to Euclid*.

Builds and exports all 21 interactive calibrated ``.g1.svg`` plates paired with
the 1888 archival bitmap plates across Books I, II, III, IV, VI, and the
Supplementary Chapter. Every point, line, circle, polygon, and intersection is
constructed strictly over exact SymPy rationals / closed-form expressions
(never ``float`` or ``sympy.Float``) using ``Model(..., auto_intersect=False)``.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, clean_expr

from geometor.casey.brocard import (
    construct_brocard_and_lemoine_circles,
    construct_symmedian_and_lemoine_circles,
)
from geometor.casey.coaxial import construct_radical_axis_and_coaxial_pencil
from geometor.casey.feuerbach import (
    construct_casey_feuerbach,
    construct_euler_nine_point,
)
from geometor.casey.invariants import (
    HERONIAN_VERTICES,
    barycentric_point,
    compass_midpoint,
    compass_perpendicular_line,
)
from geometor.casey.poles_polars import (
    construct_complete_quadrilateral_harmonic,
    construct_pole_and_polar,
)
from geometor.casey.render import export_svg

__all__ = [
    "FigureResult",
    "construct_centres_of_similitude",
    "construct_ceva",
    "construct_coaxal_intersecting_orth",
    "construct_cyclic_quad_perps",
    "construct_desargues",
    "construct_euler_concurrence",
    "construct_incircle_contacts",
    "construct_isogonal_conjugates",
    "construct_mean_centre",
    "construct_menelaus",
    "construct_parallelogram_diagonals",
    "construct_pascal_hexagon",
    "construct_simson_line",
    "construct_stewart",
    "generate_all_figures",
]

_DEFAULT_DOCSRC = Path(__file__).resolve().parents[3] / "docsrc"


@dataclass(frozen=True)
class FigureResult:
    """Constructed symbolic figure ready for SVG export."""

    model: Model
    graphic_id: str
    title: str
    subdir: str
    bbox: tuple[float, float, float, float] | None = None
    focus_points: tuple[spg.Point, ...] = ()
    highlight_point_ids: tuple[str, ...] = ()


def _pt(x: int | sp.Expr, y: int | sp.Expr) -> spg.Point:
    return spg.Point(clean_expr(sp.sympify(x)), clean_expr(sp.sympify(y)))


def _add_polygon(model: Model, pts: list[spg.Point], *, classes: list[str]) -> None:
    model.set_polygon(pts, classes=classes)


def construct_parallelogram_diagonals() -> FigureResult:
    """Book I, Prop. 1 (p. 2): Diagonals of a parallelogram bisect each other."""
    m = Model("I.1 Parallelogram Diagonals", auto_intersect=False)
    A = m.set_point(2, 5, ID="A", classes=["given-point"])
    B = m.set_point(10, 5, ID="B", classes=["given-point"])
    C = m.set_point(8, 0, ID="C", classes=["given-point"])
    D = m.set_point(0, 0, ID="D", classes=["given-point"])

    m.construct_line(A, B, ID="[A B]", classes=["carrier-line"])
    m.construct_line(B, C, ID="[B C]", classes=["carrier-line"])
    m.construct_line(C, D, ID="[C D]", classes=["carrier-line"])
    m.construct_line(D, A, ID="[D A]", classes=["carrier-line"])
    ac = m.construct_line(A, C, ID="[A C]", classes=["highlight-line"])
    bd = m.construct_line(B, D, ID="[B D]", classes=["highlight-line"])
    m.intersect(ac, bd, ID="O", classes=["center-point", "highlight-point"], by="I.1")
    _add_polygon(m, [A, B, C, D], classes=["primary-poly"])
    return FigureResult(
        m,
        "0028.g1",
        "Casey Book I Prop. 1 — Diagonals of a Parallelogram Bisect Each Other",
        "book_01",
        bbox=(-1.2, 11.2, -1.2, 6.4),
        highlight_point_ids=("O",),
    )


def construct_euler_concurrence() -> FigureResult:
    """Book I, Prop. 12 Cor. 1 (p. 9): Concurrence of Circumcentre O, Centroid G & Orthocentre H."""
    m = Model("I.12 Cor. 1 Concurrence", auto_intersect=False)
    B, C, A = (
        m.set_point(0, 0, ID="D", classes=["given-point"]),
        m.set_point(14, 0, ID="C", classes=["given-point"]),
        m.set_point(5, 12, ID="A", classes=["given-point"]),
    )
    m.construct_line(A, B, ID="[A D]", classes=["carrier-line"])
    m.construct_line(B, C, ID="[D C]", classes=["carrier-line"])
    m.construct_line(C, A, ID="[C A]", classes=["carrier-line"])
    _add_polygon(m, [A, B, C], classes=["primary-poly"])

    E = compass_midpoint(m, C, A, ID="E")
    F = compass_midpoint(m, A, B, ID="F")
    Mc = compass_midpoint(m, B, C, ID="Mc")

    med_be = m.construct_line(B, E, ID="[D E]", classes=["cross-line"])
    med_cf = m.construct_line(C, F, ID="[C F]", classes=["cross-line"])
    m.intersect(med_be, med_cf, ID="H", classes=["center-point", "highlight-point"], by="Centroid")

    alt_a = compass_perpendicular_line(m, B, C, A, ID="[A I_a]", classes=["cross-line"])
    alt_c = compass_perpendicular_line(m, A, B, C, ID="[C I_c]", classes=["cross-line"])
    pt_i = m.intersect(alt_a, alt_c, ID="I", classes=["center-point", "highlight-point"], by="Orthocentre")

    pb_a = compass_perpendicular_line(m, C, A, E, off_line_ref=B, ID="[E G]", classes=["polar-line"])
    pb_b = compass_perpendicular_line(m, B, C, Mc, off_line_ref=A, ID="[Mc G]", classes=["polar-line"])
    pt_g = m.intersect(pb_a, pb_b, ID="G", classes=["center-point", "highlight-point"], by="Circumcentre")
    m.construct_circle(pt_g, A, ID="(G A)", classes=["featured-circle"])
    m.construct_line(pt_g, pt_i, ID="[G I]", classes=["highlight-line"])
    return FigureResult(
        m,
        "0035.g1",
        "Casey Book I Prop. 12 Cor. 1 — Concurrence of Circumcentre G, Centroid H & Orthocentre I",
        "book_01",
        bbox=(-3.0, 17.0, -5.0, 13.6),
        highlight_point_ids=("G", "H", "I"),
    )


def construct_mean_centre() -> FigureResult:
    """Book I, Prop. 16 (p. 12): Mean centre perpendiculars (m+n)AH = m*BD + n*CE."""
    m = Model("I.16 Mean Centre", auto_intersect=False)
    A = m.set_point(1, 5, ID="A", classes=["given-point"])
    B = m.set_point(10, 8, ID="B", classes=["given-point"])
    C = m.set_point(4, 6, ID="C", classes=["highlight-point"])
    L1 = m.set_point(-1, 0, ID="D", classes=["given-point"])
    L2 = m.set_point(12, 0, ID="L", classes=["given-point"])
    m.construct_line(L1, L2, ID="[D L]", classes=["carrier-line"])
    m.construct_line(A, B, ID="[A B]", classes=["highlight-line"])

    perp_a = compass_perpendicular_line(m, L1, L2, A, ID="[A G_a]", classes=["cross-line"])
    perp_c = compass_perpendicular_line(m, L1, L2, C, ID="[C F]", classes=["polar-line"])
    perp_b = compass_perpendicular_line(m, L1, L2, B, ID="[B E]", classes=["cross-line"])
    base = m.elements[0] if False else m.construct_line(L1, L2, ID="[D L]_b", guide=True)
    m.intersect(perp_c, base, ID="F", classes=["harmonic-point"])
    m.intersect(perp_b, base, ID="E", classes=["given-point"])
    m.intersect(perp_a, base, ID="P", classes=["given-point"])
    return FigureResult(
        m,
        "0038.g1",
        "Casey Book I Prop. 16 — Centre of Mean Position & Weighted Perpendiculars",
        "book_01",
        bbox=(-1.5, 13.0, -1.2, 9.5),
        highlight_point_ids=("C", "F"),
    )


def construct_stewart() -> FigureResult:
    """Book II, Prop. 9 (p. 24): Stewart's Theorem m*AC^2 + n*BC^2 = m*AD^2 + n*BD^2 + (m+n)*CD^2."""
    m = Model("II.9 Stewart's Theorem", auto_intersect=False)
    A = m.set_point(0, 0, ID="A", classes=["given-point"])
    B = m.set_point(14, 0, ID="B", classes=["given-point"])
    C = m.set_point(9, 8, ID="C", classes=["given-point"])
    D = m.set_point(6, 0, ID="D", classes=["highlight-point"])
    m.construct_line(A, B, ID="[A B]", classes=["carrier-line"])
    m.construct_line(A, C, ID="[A C]", classes=["carrier-line"])
    m.construct_line(B, C, ID="[B C]", classes=["carrier-line"])
    m.construct_line(C, D, ID="[C D]", classes=["highlight-line"])
    base = m.construct_line(A, B, guide=True)
    alt = compass_perpendicular_line(m, A, B, C, ID="[C E]", classes=["cross-line"])
    m.intersect(alt, base, ID="E", classes=["harmonic-point"])
    _add_polygon(m, [A, B, C], classes=["primary-poly"])
    return FigureResult(
        m,
        "0050.g1",
        "Casey Book II Prop. 9 — Stewart's Theorem on a Triangle Cevian",
        "book_02",
        bbox=(-1.5, 15.5, -1.6, 9.5),
        highlight_point_ids=("C", "D", "E"),
    )


def construct_cyclic_quad_perps() -> FigureResult:
    """Book III, Prop. 11 (p. 34): Product of perpendiculars on opposite sides equals diagonals."""
    m = Model("III.11 Cyclic Quad Perps", auto_intersect=False)
    origin = m.set_point(0, 0, ID="M", guide=True)
    A = m.set_point(-4, 3, ID="A", classes=["given-point"])
    B = m.set_point(-4, -3, ID="B", classes=["given-point"])
    C = m.set_point(3, -4, ID="C", classes=["given-point"])
    D = m.set_point(4, 3, ID="D", classes=["given-point"])
    pt_o = m.set_point(0, 5, ID="O", classes=["highlight-point"])
    m.construct_circle(origin, pt_o, ID="(M O)", classes=["featured-circle"])

    ab = m.construct_line(A, B, ID="[A B]", classes=["carrier-line"])
    cd = m.construct_line(C, D, ID="[C D]", classes=["carrier-line"])
    ac = m.construct_line(A, C, ID="[A C]", classes=["cross-line"])
    bd = m.construct_line(B, D, ID="[B D]", classes=["cross-line"])
    m.construct_line(B, C, ID="[B C]", classes=["carrier-line"])
    m.construct_line(D, A, ID="[D A]", classes=["carrier-line"])
    _add_polygon(m, [A, B, C, D], classes=["primary-poly"])

    pe = compass_perpendicular_line(m, A, B, pt_o, ID="[O E]", classes=["polar-line"])
    pf = compass_perpendicular_line(m, C, D, pt_o, ID="[O F]", classes=["polar-line"])
    pg = compass_perpendicular_line(m, A, C, pt_o, ID="[O G]", classes=["highlight-line"])
    ph = compass_perpendicular_line(m, B, D, pt_o, ID="[O H]", classes=["highlight-line"])
    m.intersect(pe, ab, ID="E", classes=["harmonic-point"])
    m.intersect(pf, cd, ID="F", classes=["harmonic-point"])
    m.intersect(pg, ac, ID="G", classes=["highlight-point"])
    m.intersect(ph, bd, ID="H", classes=["highlight-point"])
    return FigureResult(
        m,
        "0060.g1",
        "Casey Book III Prop. 11 — Perpendiculars from Circle Point to Sides & Diagonals (OE·OF = OG·OH)",
        "book_03",
        bbox=(-6.8, 6.8, -5.8, 6.4),
        highlight_point_ids=("O", "E", "F", "G", "H"),
    )


def construct_simson_line() -> FigureResult:
    """Book III, Prop. 12 (pp. 34–35): Simson's Pedal Line of triangle ABC from circumcircle point P."""
    m = Model("III.12 Simson's Line", auto_intersect=False)
    origin = m.set_point(0, 0, ID="O", classes=["center-point"])
    A = m.set_point(3, 4, ID="A", classes=["given-point"])
    B = m.set_point(-4, -3, ID="B", classes=["given-point"])
    C = m.set_point(5, 0, ID="C", classes=["given-point"])
    P = m.set_point(-4, 3, ID="P", classes=["highlight-point"])
    m.construct_circle(origin, A, ID="(O A)", classes=["featured-circle"])

    bc = m.construct_line(B, C, ID="[B C]", classes=["carrier-line"])
    ca = m.construct_line(C, A, ID="[C A]", classes=["carrier-line"])
    ab = m.construct_line(A, B, ID="[A B]", classes=["carrier-line"])
    _add_polygon(m, [A, B, C], classes=["primary-poly"])

    pd = compass_perpendicular_line(m, B, C, P, ID="[P D]", classes=["cross-line"])
    pe = compass_perpendicular_line(m, C, A, P, ID="[P E]", classes=["cross-line"])
    pf = compass_perpendicular_line(m, A, B, P, ID="[P F]", classes=["cross-line"])

    D = m.intersect(pd, bc, ID="D", classes=["harmonic-point"], by="III.12")
    E = m.intersect(pe, ca, ID="E", classes=["harmonic-point"], by="III.12")
    m.intersect(pf, ab, ID="F", classes=["harmonic-point"], by="III.12")
    m.construct_line(D, E, ID="[D F E]", classes=["highlight-line"], by="Simson")
    return FigureResult(
        m,
        "0061.g1",
        "Casey Book III Prop. 12 — Simson's Pedal Line (Collinearity of Feet D, F, E)",
        "book_03",
        bbox=(-6.6, 6.6, -5.8, 5.8),
        highlight_point_ids=("P", "D", "E", "F"),
    )


def construct_incircle_contacts() -> FigureResult:
    """Book IV, Prop. 1 (p. 53): Incircle contact segments s-a, s-b, s-c."""
    m = Model("IV.1 Incircle Contacts", auto_intersect=False)
    B = m.set_point(0, 0, ID="B", classes=["given-point"])
    C = m.set_point(14, 0, ID="C", classes=["given-point"])
    A = m.set_point(5, 12, ID="A", classes=["given-point"])
    pt_o = m.set_point(6, 4, ID="O", classes=["center-point", "highlight-point"])
    D = m.set_point(6, 0, ID="D", classes=["harmonic-point"])

    m.construct_line(A, B, ID="[A B]", classes=["carrier-line"])
    m.construct_line(B, C, ID="[B C]", classes=["carrier-line"])
    m.construct_line(C, A, ID="[C A]", classes=["carrier-line"])
    _add_polygon(m, [A, B, C], classes=["primary-poly"])
    m.construct_circle(pt_o, D, ID="(O D)", classes=["featured-circle"])

    m.set_point(sp.Rational(30, 13), sp.Rational(72, 13), ID="F", classes=["harmonic-point"])
    m.set_point(sp.Rational(46, 5), sp.Rational(32, 5), ID="E", classes=["harmonic-point"])
    m.construct_line(pt_o, A, ID="[O A]", classes=["cross-line"])
    m.construct_line(pt_o, B, ID="[O B]", classes=["cross-line"])
    m.construct_line(pt_o, C, ID="[O C]", classes=["cross-line"])
    return FigureResult(
        m,
        "0079.g1",
        "Casey Book IV Prop. 1 — Incircle Contact Segments s - a, s - b, s - c",
        "book_04",
        bbox=(-1.5, 15.5, -1.6, 13.4),
        highlight_point_ids=("O", "D", "E", "F"),
    )


def construct_ceva() -> FigureResult:
    """Book VI, Prop. 2 (p. 67): Ceva's Theorem on concurrent triangle cevians."""
    m = Model("VI.2 Ceva's Theorem", auto_intersect=False)
    b0, c0, a0 = HERONIAN_VERTICES
    B = m.set_point(b0.x, b0.y, ID="B", classes=["given-point"])
    C = m.set_point(c0.x, c0.y, ID="C", classes=["given-point"])
    A = m.set_point(a0.x, a0.y, ID="A", classes=["given-point"])
    pt_o = m.set_point(6, 4, ID="O", classes=["highlight-point"])

    bc = m.construct_line(B, C, ID="[B C]", classes=["carrier-line"])
    ca = m.construct_line(C, A, ID="[C A]", classes=["carrier-line"])
    ab = m.construct_line(A, B, ID="[A B]", classes=["carrier-line"])
    _add_polygon(m, [A, B, C], classes=["primary-poly"])

    ao = m.construct_line(A, pt_o, ID="[A O]", classes=["highlight-line"])
    bo = m.construct_line(B, pt_o, ID="[B O]", classes=["highlight-line"])
    co = m.construct_line(C, pt_o, ID="[C O]", classes=["highlight-line"])
    m.intersect(ao, bc, ID="A'", classes=["harmonic-point"], by="Ceva")
    m.intersect(bo, ca, ID="B'", classes=["harmonic-point"], by="Ceva")
    m.intersect(co, ab, ID="C'", classes=["harmonic-point"], by="Ceva")
    return FigureResult(
        m,
        "0093.g1",
        "Casey Book VI Prop. 2 — Ceva's Theorem (BA'·CB'·AC' = A'C·B'A·C'B)",
        "book_06",
        bbox=(-1.5, 15.5, -1.6, 13.4),
        highlight_point_ids=("O", "A'", "B'", "C'"),
    )


def construct_menelaus() -> FigureResult:
    """Book VI, Prop. 4 (p. 69): Menelaus's Theorem on a transversal line."""
    m = Model("VI.4 Menelaus's Theorem", auto_intersect=False)
    B = m.set_point(0, 0, ID="B", classes=["given-point"])
    C = m.set_point(8, 0, ID="C", classes=["given-point"])
    A = m.set_point(3, 9, ID="A", classes=["given-point"])
    Bp = m.set_point(sp.Rational(19, 3), 3, ID="B'", classes=["harmonic-point"])
    Cp = m.set_point(sp.Rational(3, 2), sp.Rational(9, 2), ID="C'", classes=["harmonic-point"])

    bc = m.construct_line(B, C, ID="[B C]", classes=["carrier-line"])
    m.construct_line(C, A, ID="[C A]", classes=["carrier-line"])
    m.construct_line(A, B, ID="[A B]", classes=["carrier-line"])
    _add_polygon(m, [A, B, C], classes=["primary-poly"])

    trans = m.construct_line(Cp, Bp, ID="[C' B' A']", classes=["highlight-line"], by="Menelaus")
    m.intersect(trans, bc, ID="A'", classes=["highlight-point"], by="Menelaus")
    return FigureResult(
        m,
        "0095.g1",
        "Casey Book VI Prop. 4 — Menelaus's Transversal Theorem",
        "book_06",
        bbox=(-1.5, 13.5, -1.8, 10.5),
        highlight_point_ids=("A'", "B'", "C'"),
    )


def construct_centres_of_similitude() -> FigureResult:
    """Book VI, Sec. III (p. 83): External Centre of Similitude & Common Tangent."""
    m = Model("VI.III Centres of Similitude", auto_intersect=False)
    pt_o = m.set_point(0, 0, ID="O", classes=["center-point"])
    Op = m.set_point(10, 0, ID="O'", classes=["center-point"])
    P = m.set_point(sp.Rational(27, 5), sp.Rational(36, 5), ID="P", classes=["harmonic-point"])
    Pp = m.set_point(sp.Rational(59, 5), sp.Rational(12, 5), ID="P'", classes=["harmonic-point"])
    T = m.set_point(15, 0, ID="T", classes=["highlight-point"])
    m.set_point(sp.Rational(15, 2), 0, ID="S", classes=["highlight-point"])

    m.construct_circle(pt_o, P, ID="(O P)", classes=["featured-circle"])
    m.construct_circle(Op, Pp, ID="(O' P')", classes=["secondary-circle"])
    m.construct_line(pt_o, T, ID="[O T]", classes=["carrier-line"])
    m.construct_line(P, T, ID="[P P' T]", classes=["highlight-line"])
    m.construct_line(pt_o, P, ID="[O P]", classes=["cross-line"])
    m.construct_line(Op, Pp, ID="[O' P']", classes=["cross-line"])
    return FigureResult(
        m,
        "0109.g1",
        "Casey Book VI Sec. III — External & Internal Centres of Similitude T, S",
        "book_06",
        bbox=(-10.2, 16.5, -10.2, 10.2),
        highlight_point_ids=("T", "S", "P", "P'"),
    )


def construct_coaxal_intersecting_orth() -> FigureResult:
    """Book VI, Sec. IV Prop. 15 (p. 114): Intersecting Coaxal Circles & Orthogonal Circle."""
    m = Model("VI.IV Coaxal Circles", auto_intersect=False)
    X = m.set_point(-3, 0, ID="X", classes=["center-point"])
    Y = m.set_point(3, 0, ID="Y", classes=["center-point"])
    Z = m.set_point(0, 5, ID="Z", classes=["highlight-point"])
    C = m.set_point(0, 4, ID="C", classes=["harmonic-point"])
    B = m.set_point(0, -4, ID="B", classes=["harmonic-point"])
    A = m.set_point(0, 8, ID="A", classes=["given-point"])
    E = m.set_point(0, 2, ID="E", classes=["given-point"])

    m.construct_circle(X, C, ID="(X C)", classes=["geom-circle"])
    m.construct_circle(Y, C, ID="(Y C)", classes=["secondary-circle"])
    m.construct_circle(Z, E, ID="(Z E)", classes=["orth-circle"])
    m.construct_line(A, B, ID="[A B]", classes=["highlight-line"])
    m.construct_line(X, Y, ID="[X Y]", classes=["carrier-line"])
    return FigureResult(
        m,
        "0140.g1",
        "Casey Book VI Sec. IV Prop. 15 — Coaxal Circles & Orthogonal Circle on Radical Axis",
        "book_06",
        bbox=(-9.2, 9.2, -6.2, 9.2),
        highlight_point_ids=("Z", "C", "B"),
    )


def construct_pascal_hexagon() -> FigureResult:
    """Book VI, Sec. VI Prop. 3 (p. 130): Pascal's Hexagrammum Mysticum in a Circle."""
    m = Model("VI.VI Pascal's Theorem", auto_intersect=False)
    origin = m.set_point(0, 0, ID="O", guide=True)
    A = m.set_point(-4, -3, ID="A", classes=["given-point"])
    B = m.set_point(0, 5, ID="B", classes=["given-point"])
    C = m.set_point(5, 0, ID="C", classes=["given-point"])
    D = m.set_point(3, -4, ID="D", classes=["given-point"])
    E = m.set_point(-3, 4, ID="E", classes=["given-point"])
    F = m.set_point(4, 3, ID="F", classes=["given-point"])
    m.construct_circle(origin, B, ID="(O B)", classes=["featured-circle"])

    ab = m.construct_line(A, B, ID="[A B]", classes=["carrier-line"])
    bc = m.construct_line(B, C, ID="[B C]", classes=["carrier-line"])
    cd = m.construct_line(C, D, ID="[C D]", classes=["carrier-line"])
    de = m.construct_line(D, E, ID="[D E]", classes=["carrier-line"])
    ef = m.construct_line(E, F, ID="[E F]", classes=["carrier-line"])
    fa = m.construct_line(F, A, ID="[F A]", classes=["carrier-line"])

    L = m.intersect(ab, de, ID="L", classes=["highlight-point"], by="Pascal")
    m.intersect(bc, ef, ID="M", classes=["highlight-point"], by="Pascal")
    N = m.intersect(cd, fa, ID="N", classes=["highlight-point"], by="Pascal")
    m.construct_line(L, N, ID="[L M N]", classes=["highlight-line"], by="Pascal")
    return FigureResult(
        m,
        "0156.g1",
        "Casey Book VI Sec. VI Prop. 3 — Pascal's Hexagrammum Mysticum & Pascal Line",
        "book_06",
        bbox=(-6.2, 9.4, -5.8, 7.2),
        highlight_point_ids=("L", "M", "N"),
    )


def construct_desargues() -> FigureResult:
    """Book VI, Sec. VI Prop. 4 Cor. 2 (p. 131): Desargues's Perspective Triangles."""
    m = Model("VI.VI Desargues's Theorem", auto_intersect=False)
    P = m.set_point(0, 9, ID="P", classes=["highlight-point"])
    A = m.set_point(-3, 4, ID="A", classes=["given-point"])
    B = m.set_point(-1, 5, ID="B", classes=["given-point"])
    C = m.set_point(sp.Rational(5, 2), 4, ID="C", classes=["given-point"])

    Ap = _pt(P.x + 2 * (A.x - P.x), P.y + 2 * (A.y - P.y))
    Bp = _pt(P.x + sp.Rational(3, 2) * (B.x - P.x), P.y + sp.Rational(3, 2) * (B.y - P.y))
    Cp = _pt(P.x + sp.Rational(5, 3) * (C.x - P.x), P.y + sp.Rational(5, 3) * (C.y - P.y))
    Ap = m.set_point(Ap.x, Ap.y, ID="A'", classes=["given-point"])
    Bp = m.set_point(Bp.x, Bp.y, ID="B'", classes=["given-point"])
    Cp = m.set_point(Cp.x, Cp.y, ID="C'", classes=["given-point"])

    m.construct_line(P, Ap, ID="[P A']", classes=["cross-line"])
    m.construct_line(P, Bp, ID="[P B']", classes=["cross-line"])
    m.construct_line(P, Cp, ID="[P C']", classes=["cross-line"])

    ab = m.construct_line(A, B, ID="[A B]", classes=["carrier-line"])
    bc = m.construct_line(B, C, ID="[B C]", classes=["carrier-line"])
    ca = m.construct_line(C, A, ID="[C A]", classes=["carrier-line"])
    abp = m.construct_line(Ap, Bp, ID="[A' B']", classes=["carrier-line"])
    bcp = m.construct_line(Bp, Cp, ID="[B' C']", classes=["carrier-line"])
    cap = m.construct_line(Cp, Ap, ID="[C' A']", classes=["carrier-line"])

    _add_polygon(m, [A, B, C], classes=["primary-poly"])
    _add_polygon(m, [Ap, Bp, Cp], classes=["brocard-poly"])

    L = m.intersect(bc, bcp, ID="L", classes=["harmonic-point"], by="Desargues")
    M = m.intersect(ca, cap, ID="M", classes=["harmonic-point"], by="Desargues")
    m.intersect(ab, abp, ID="N", classes=["harmonic-point"], by="Desargues")
    m.construct_line(L, M, ID="[L M N]", classes=["highlight-line"], by="Desargues")
    return FigureResult(
        m,
        "0157.g1",
        "Casey Book VI Sec. VI Prop. 4 Cor. 2 — Desargues's Two Perspective Triangles",
        "book_06",
        bbox=(-9.5, 9.5, -2.5, 10.2),
        highlight_point_ids=("P", "L", "M", "N"),
    )


def construct_isogonal_conjugates() -> FigureResult:
    """Supplementary Chapter, Sec. I Prop. 1 (p. 165): Isogonal Conjugates P, Q & Pedal Circle."""
    m = Model("Supp. I.1 Isogonal Conjugates", auto_intersect=False)
    b0, c0, a0 = HERONIAN_VERTICES
    B = m.set_point(b0.x, b0.y, ID="B", classes=["given-point"])
    C = m.set_point(c0.x, c0.y, ID="C", classes=["given-point"])
    A = m.set_point(a0.x, a0.y, ID="A", classes=["given-point"])
    a_len, b_len, c_len = sp.Integer(14), sp.Integer(15), sp.Integer(13)

    p_raw = barycentric_point(A, B, C, sp.Integer(2), sp.Integer(3), sp.Integer(4))
    q_raw = barycentric_point(A, B, C, a_len**2 / 2, b_len**2 / 3, c_len**2 / 4)
    P = m.set_point(p_raw.x, p_raw.y, ID="P", classes=["highlight-point"])
    Q = m.set_point(q_raw.x, q_raw.y, ID="Q", classes=["highlight-point"])
    Mp = m.set_point(
        clean_expr((P.x + Q.x) / 2),
        clean_expr((P.y + Q.y) / 2),
        ID="Mp",
        classes=["center-point"],
    )

    bc = m.construct_line(B, C, ID="[B C]", classes=["carrier-line"])
    ca = m.construct_line(C, A, ID="[C A]", classes=["carrier-line"])
    ab = m.construct_line(A, B, ID="[A B]", classes=["carrier-line"])
    _add_polygon(m, [A, B, C], classes=["primary-poly"])

    for ray_t in (P, Q):
        for vtx, vname in ((A, "A"), (B, "B"), (C, "C")):
            m.construct_line(vtx, ray_t, ID=f"[{vname} {ray_t.x == P.x and 'P' or 'Q'}]", classes=["cross-line"])

    px = compass_perpendicular_line(m, B, C, P, ID="[P X]", classes=["polar-line"])
    py = compass_perpendicular_line(m, C, A, P, ID="[P Y]", classes=["polar-line"])
    pz = compass_perpendicular_line(m, A, B, P, ID="[P Z]", classes=["polar-line"])
    X = m.intersect(px, bc, ID="X", classes=["harmonic-point"])
    m.intersect(py, ca, ID="Y", classes=["harmonic-point"])
    m.intersect(pz, ab, ID="Z", classes=["harmonic-point"])

    qx = compass_perpendicular_line(m, B, C, Q, ID="[Q X']", classes=["cross-line"])
    qy = compass_perpendicular_line(m, C, A, Q, ID="[Q Y']", classes=["cross-line"])
    qz = compass_perpendicular_line(m, A, B, Q, ID="[Q Z']", classes=["cross-line"])
    m.intersect(qx, bc, ID="X'", classes=["harmonic-point"])
    m.intersect(qy, ca, ID="Y'", classes=["harmonic-point"])
    m.intersect(qz, ab, ID="Z'", classes=["harmonic-point"])

    m.construct_circle(Mp, X, ID="(Mp X)", classes=["featured-circle"])
    return FigureResult(
        m,
        "0191.g1",
        "Casey Supp. Ch. Sec. I Prop. 1 — Isogonal Conjugates P, Q & Six-Point Pedal Circle",
        "supplementary_chapter",
        bbox=(-1.5, 15.5, -2.5, 13.4),
        highlight_point_ids=("P", "Q", "Mp"),
    )


def generate_all_figures(docsrc_root: Path | None = None) -> list[Path]:
    """Build and export all 21 exact symbolic 5-layer ``.euclid-graphic`` SVGs.

    Args:
        docsrc_root: Path to ``docsrc`` (defaults to repository ``docsrc/``).

    Returns:
        List of all written SVG file paths.
    """
    docsrc = docsrc_root or _DEFAULT_DOCSRC
    seq = docsrc / "sequel_to_euclid"
    fig = docsrc / "_static" / "figures"
    written: list[Path] = []

    builders = [
        construct_parallelogram_diagonals(),
        construct_euler_concurrence(),
        construct_mean_centre(),
        construct_stewart(),
        construct_cyclic_quad_perps(),
        construct_simson_line(),
        construct_incircle_contacts(),
        construct_ceva(),
        construct_menelaus(),
        construct_centres_of_similitude(),
        construct_coaxal_intersecting_orth(),
        construct_pascal_hexagon(),
        construct_desargues(),
        construct_isogonal_conjugates(),
    ]
    for res in builders:
        out = seq / res.subdir / f"{res.graphic_id}.svg"
        export_svg(
            res.model,
            out,
            graphic_id=res.graphic_id,
            title=res.title,
            bbox=res.bbox,
            focus_points=res.focus_points or None,
            highlight_point_ids=res.highlight_point_ids,
        )
        written.append(out)

    # Also regenerate the 7 canonical theorem suite plates + _static/figures mirrors
    u1 = construct_euler_nine_point()
    u4 = construct_casey_feuerbach()
    coax = construct_radical_axis_and_coaxial_pencil()
    quad = construct_complete_quadrilateral_harmonic()
    pol = construct_pole_and_polar()
    lem = construct_symmedian_and_lemoine_circles()
    bro = construct_brocard_and_lemoine_circles()

    u1_focus = [*u1.vertices, *u1.midpoints, u1.circumcenter, u1.orthocenter]
    legacy_specs = [
        (u1.model, (seq / "book_04" / "0083.g1.svg", fig / "unit1_euler_nine_point.svg"), "0083.g1",
         "Casey Book IV Prop. 5 — Euler Line & Nine-Points Circle", (-2.5, 16.5, -4.6, 13.4), u1_focus, ("O", "G", "N", "H")),
        (u4.model, (seq / "book_06" / "0130.g1.svg", fig / "unit4_casey_feuerbach.svg"), "0130.g1",
         "Casey Book VI Sec. IV Prop. 10 Cor. 2 — Casey's Inversion & Feuerbach Tangency at X(11)", (-2.5, 16.5, -4.6, 13.4), None, ("Fe", "Ma", "I", "N")),
        (coax.model, (seq / "book_03" / "0069.g1.svg", fig / "unit2_coaxial_limiting_points.svg"), "0069.g1",
         "Casey Book III Props. 23–28 — Disjoint Radical Axis, Orthogonal Pencil & Poncelet Limiting Points", (-18.0, 34.0, -17.5, 19.5), None, ("Rc", "L1", "L2")),
        (quad.model, (seq / "book_06" / "0117.g1.svg", fig / "unit3_complete_quadrilateral_harmonic.svg"), "0117.g1",
         "Casey Book VI Sec. III Prop. 7 — Complete Quadrilateral Harmonic Section", (-7.2, 9.2, -1.2, 10.2), None, ("P", "Qa", "Qb")),
        (pol.model, (seq / "book_03" / "0071.g1.svg", fig / "unit4_poles_polars_lahire.svg"), "0071.g1",
         "Casey Book III Prop. 25 & VI.VII — Pole, Polar, Self-Conjugate Triangle & La Hire Reciprocity", (-6.5, 9.5, -6.5, 11.5), None, ("D", "Q", "U", "V")),
        (lem.model, (seq / "supplementary_chapter" / "0205.g1.svg", fig / "unit5_symmedian_lemoine_circle.svg"), "0205.g1",
         "Casey Supp. Ch. Secs. I & III — Symmedian Point K, First Lemoine Circle & Cosine Circle", (-2.2, 16.2, -4.4, 13.2), None, ("K", "O", "Ml")),
        (bro.model, (seq / "supplementary_chapter" / "0220.g1.svg", fig / "unit6_brocard_circle.svg"), "0220.g1",
         "Casey Supp. Ch. Secs. II, V & VII — Brocard Points Ω, Ω′, Brocard Circle, Steiner X(99) & Tarry X(98)", (-2.2, 16.2, -4.5, 13.2), None, ("K", "Om1", "Om2", "St", "Tr")),
    ]
    for model, targets, gid, title, bbox, focus, hl in legacy_specs:
        for out in targets:
            export_svg(
                model,
                out,
                graphic_id=gid,
                title=title,
                bbox=bbox,
                focus_points=focus,
                highlight_point_ids=hl,
            )
            written.append(out)
    return written
