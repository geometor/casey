"""Exact straightedge-and-compass constructions for Harmonic Section, Poles, Polars & Reciprocity.

Implements:

- **Unit 3 (Book VI, Sec. III, Prop. 7, p. 91)**: Pure-straightedge Complete Quadrilateral
  harmonic ranges ``(A, C; M, N) = -1``.
- **Unit 4 (Book III, Def. & Props. 25, 27, pp. 44–47; Book VI, Sec. III, Prop. 4, p. 89;
  Book VI, Sec. VII, Props. 1–6, pp. 141–147)**:

  1. Universal symbolic proof of **La Hire's Reciprocity Theorem** (Prop. 25):
     ``Q in polar(P) <=> P in polar(Q)``.
  2. Pure-straightedge construction of ``polar(D)`` via an inscribed complete quadrangle
     ``G1 H1 H2 G2`` on ``x^2 + y^2 = 25``, producing the **Self-Conjugate Triangle** ``D U V``
     (Sec. VII, Prop. 2, p. 142).
  3. Verification of **Harmonic Secant Section** ``(G1, H1; J1, D) = -1`` and
     ``(G2, H2; J2, D) = -1`` (Sec. III, Prop. 4, p. 89).
  4. Compass-and-straightedge chord-of-contact construction of ``polar(Q)`` for ``Q = (4, -4)``
     lying on ``polar(D)``, confirming ``D in polar(Q)`` (Book III, Props. 25 & 27).
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, cross_ratio, is_harmonic, zero_test

from geometor.casey.invariants import compass_midpoint, polar_line, pole_of_line

__all__ = [
    "CompleteQuadrilateralResult",
    "LaHireSymbolicProof",
    "PolePolarResult",
    "construct_complete_quadrilateral_harmonic",
    "construct_pole_and_polar",
    "verify_lahire_reciprocity_symbolic",
]


@dataclass(frozen=True)
class LaHireSymbolicProof:
    """Universal symbolic proof certificate for La Hire's Reciprocity & Harmonic Secants."""

    reciprocity_bilinear_diff: sp.Expr
    secant_cross_ratio: sp.Expr
    verified: bool


@dataclass(frozen=True)
class CompleteQuadrilateralResult:
    """Constructed elements for Casey's Complete Quadrilateral Harmonic Section (Unit 3)."""

    model: Model
    quad_vertices: tuple[spg.Point, spg.Point, spg.Point, spg.Point]
    opposite_meets: tuple[spg.Point, spg.Point]
    diagonal_center: spg.Point
    third_diagonal_meets: tuple[spg.Point, spg.Point]
    cross_ratio_ac: sp.Expr
    cross_ratio_bd: sp.Expr


@dataclass(frozen=True)
class PolePolarResult:
    """Constructed elements for Pole, Polar, Harmonic Secants & La Hire Reciprocity (Unit 4)."""

    model: Model
    circle: spg.Circle
    center: spg.Point
    pole_d: spg.Point
    secant_1_pts: tuple[spg.Point, spg.Point]
    secant_2_pts: tuple[spg.Point, spg.Point]
    self_conjugate_triangle: tuple[spg.Point, spg.Point, spg.Point]
    polar_d: spg.Line
    harmonic_meets: tuple[spg.Point, spg.Point]
    reciprocal_pole_q: spg.Point
    polar_q: spg.Line
    cross_ratio_secant_1: sp.Expr
    cross_ratio_secant_2: sp.Expr
    lahire_verified: bool


def verify_lahire_reciprocity_symbolic() -> LaHireSymbolicProof:
    """Prove La Hire's Reciprocity (Book III, Prop. 25) and Harmonic Secant Section (VI.III.4).

    1. For circle ``(x - h)^2 + (y - k)^2 = r^2``, ``polar(P)`` has equation
       ``(x1 - h)(x - h) + (y1 - k)(y - k) - r^2 = 0``, which is symmetric in ``(x1, y1)``
       and ``(x2, y2)``.
    2. For exterior pole ``D = (d, 0)`` on diameter secant ``y = 0`` cutting ``x^2 + y^2 = r^2``
       at ``G = (-r, 0), H = (r, 0)`` with polar foot ``J = (r^2/d, 0)``, the anharmonic ratio
       ``(G, H; J, D)`` simplifies identically to ``-1``.

    Returns:
        Frozen :class:`LaHireSymbolicProof` certificate.
    """
    h, k, r, x1, y1, x2, y2, d = sp.symbols("h k r x1 y1 x2 y2 d", real=True, positive=True)
    q_on_polar_p = (x1 - h) * (x2 - h) + (y1 - k) * (y2 - k) - r**2
    p_on_polar_q = (x2 - h) * (x1 - h) + (y2 - k) * (y1 - k) - r**2
    rec_diff = sp.expand(q_on_polar_p - p_on_polar_q)

    # Cross ratio (G, H; J, D) along x-axis: ((G - J)*(H - D)) / ((G - D)*(H - J))
    g_x, h_x, j_x, d_x = -r, r, r**2 / d, d
    cr_secant = sp.simplify(((g_x - j_x) * (h_x - d_x)) / ((g_x - d_x) * (h_x - j_x)))

    ok = zero_test(rec_diff) and zero_test(cr_secant + 1)
    return LaHireSymbolicProof(
        reciprocity_bilinear_diff=rec_diff,
        secant_cross_ratio=cr_secant,
        verified=ok,
    )


def construct_complete_quadrilateral_harmonic(
    model: Model | None = None,
) -> CompleteQuadrilateralResult:
    """Construct Casey's Complete Quadrilateral and verify harmonic diagonal division (Unit 3).

    Follows Casey, Book VI, Sec. III, Prop. 7 (p. 91) using pure straightedge incidences on
    exact integer vertices ``A=(0, 0), B=(6, 0), C=(4, 2), D=(2, 3)``:

    - Opposite side meets: ``E = [AB] ∩ [CD] = (8, 0)`` and ``F = [AD] ∩ [BC] = (12/5, 18/5)``.
    - Internal diagonal meet: ``P = [AC] ∩ [BD] = (18/5, 9/5)``.
    - Third diagonal ``[EF]`` cuts ``[AC]`` at ``Qa = (9/2, 9/4)`` and ``[BD]`` at
      ``Qb = (-6, 9)`` such that ``(A, C; P, Qa) = -1`` and ``(B, D; P, Qb) = -1``.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`CompleteQuadrilateralResult`.
    """
    if model is None:
        model = Model("casey_complete_quadrilateral", auto_intersect=False, enable_logging=False)

    a_pt = model.given_point(0, 0, ID="A", classes=["given", "vertex"])
    b_pt = model.given_point(6, 0, ID="B", classes=["given", "vertex"])
    c_pt = model.given_point(4, 2, ID="C", classes=["given", "vertex"])
    d_pt = model.given_point(2, 3, ID="D", classes=["given", "vertex"])

    model.set_polygon([a_pt, b_pt, c_pt, d_pt], classes=["quadrilateral", "primary"], ID="< A B C D >")

    l_ab = model.construct_line(a_pt, b_pt, classes=["carrier", "quadrilateral"], ID="[ A B ]", by="Post.1")
    l_bc = model.construct_line(b_pt, c_pt, classes=["carrier", "quadrilateral"], ID="[ B C ]", by="Post.1")
    l_cd = model.construct_line(c_pt, d_pt, classes=["carrier", "quadrilateral"], ID="[ C D ]", by="Post.1")
    l_da = model.construct_line(d_pt, a_pt, classes=["carrier", "quadrilateral"], ID="[ D A ]", by="Post.1")

    e_pt = model.intersect(l_ab, l_cd, ID="E", classes=["meet", "vertex"], by="Casey.VI.III.7")
    f_pt = model.intersect(l_da, l_bc, ID="F", classes=["meet", "vertex"], by="Casey.VI.III.7")

    diag_ac = model.construct_line(a_pt, c_pt, classes=["diagonal"], ID="[ A C ]", by="Post.1")
    diag_bd = model.construct_line(b_pt, d_pt, classes=["diagonal"], ID="[ B D ]", by="Post.1")
    diag_ef = model.construct_line(
        e_pt, f_pt, classes=["harmonic", "diagonal", "highlight"], ID="[ E F ]", by="Casey.VI.III.7"
    )

    p_center = model.intersect(
        diag_ac, diag_bd, ID="P", classes=["harmonic", "meet"], by="Casey.VI.III.7"
    )
    q_ac = model.intersect(
        diag_ac, diag_ef, ID="Qa", classes=["harmonic", "highlight_point"], by="Casey.VI.III.7"
    )
    q_bd = model.intersect(
        diag_bd, diag_ef, ID="Qb", classes=["harmonic", "highlight_point"], by="Casey.VI.III.7"
    )

    cr_ac = cross_ratio(a_pt, c_pt, p_center, q_ac)
    cr_bd = cross_ratio(b_pt, d_pt, p_center, q_bd)
    if not (is_harmonic(a_pt, c_pt, p_center, q_ac) and is_harmonic(b_pt, d_pt, p_center, q_bd)):
        raise AssertionError(f"Expected harmonic ranges -1, got {cr_ac}, {cr_bd}")
    model.conclude("Complete quadrilateral diagonals divide harmonically: (A,C;P,Qa) = (B,D;P,Qb) = -1", by="Casey.VI.III.7")

    return CompleteQuadrilateralResult(
        model=model,
        quad_vertices=(a_pt, b_pt, c_pt, d_pt),
        opposite_meets=(e_pt, f_pt),
        diagonal_center=p_center,
        third_diagonal_meets=(q_ac, q_bd),
        cross_ratio_ac=cr_ac,
        cross_ratio_bd=cr_bd,
    )


def construct_pole_and_polar(model: Model | None = None) -> PolePolarResult:
    """Construct the Polar of ``D`` by straightedge and verify La Hire's Reciprocity (Unit 4).

    On circle ``(O, R0)`` with ``O = (0, 0)`` and ``R0 = (5, 0)`` (``x^2 + y^2 = 25``):

    1. Draws two rational secants cutting the circle in ``G1=(0, 5), H1=(4, 3)`` and
       ``G2=(-3, -4), H2=(5, 0)``, meeting at exterior pole ``D = (15/2, 5/4)``.
    2. Constructs the remaining diagonal vertices ``U = [G1 H2] ∩ [G2 H1] = (3, 2)`` and
       ``V = [G1 G2] ∩ [H1 H2] = (5/3, 10)`` of the inscribed quadrangle; their join ``[U V]``
       is ``polar(D): 6x + y - 20 = 0``, and ``D U V`` is a **Self-Conjugate Triangle**
       (Casey, Book VI, Sec. VII, Prop. 2, p. 142).
    3. Intersects ``polar(D)`` with both secants at ``J1, J2`` and verifies Casey's Harmonic
       Secant Theorem ``(G1, H1; J1, D) = (G2, H2; J2, D) = -1`` (Sec. III, Prop. 4, p. 89).
    4. Selects exterior point ``Q = (4, -4)`` on ``polar(D)``, constructs its two tangents to
       ``(O, 5)`` by Thales semicircle on ``OQ``, draws chord of contact ``polar(Q)`` (Book III,
       Prop. 27, p. 47), and asserts **La Hire's Reciprocity** ``D in polar(Q)`` (Book III,
       Prop. 25, p. 45).

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`PolePolarResult`.
    """
    if model is None:
        model = Model("casey_poles_polars", auto_intersect=False, enable_logging=False)

    o_center = model.given_point(0, 0, ID="O", classes=["given", "center"])
    g1 = model.given_point(0, 5, ID="G1", classes=["given", "conic_pt"])
    h1 = model.given_point(4, 3, ID="H1", classes=["given", "conic_pt"])
    g2 = model.given_point(-3, -4, ID="G2", classes=["given", "conic_pt"])
    h2 = model.given_point(5, 0, ID="H2", classes=["given", "conic_pt"])

    base_circle = model.construct_circle(
        o_center, h2, classes=["primary_circle", "featured"], ID="( O H2 )", by="Post.3"
    )
    for pt_c in (g1, h1, g2):
        model.assert_incident(pt_c, base_circle, by="I.def.15")

    sec_1 = model.construct_line(g1, h1, classes=["carrier", "secant"], ID="[ G1 H1 ]", by="Post.1")
    sec_2 = model.construct_line(g2, h2, classes=["carrier", "secant"], ID="[ G2 H2 ]", by="Post.1")
    pole_d = model.intersect(
        sec_1, sec_2, ID="D", classes=["pole", "highlight_point"], by="Casey.VI.VII.2"
    )

    ch_g1_h2 = model.construct_line(g1, h2, classes=["cross"], ID="[ G1 H2 ]", by="Post.1")
    ch_g2_h1 = model.construct_line(g2, h1, classes=["cross"], ID="[ G2 H1 ]", by="Post.1")
    u_pt = model.intersect(ch_g1_h2, ch_g2_h1, ID="U", classes=["conjugate"], by="Casey.VI.VII.2")

    ch_g1_g2 = model.construct_line(g1, g2, classes=["cross"], ID="[ G1 G2 ]", by="Post.1")
    ch_h1_h2 = model.construct_line(h1, h2, classes=["cross"], ID="[ H1 H2 ]", by="Post.1")
    v_pt = model.intersect(ch_g1_g2, ch_h1_h2, ID="V", classes=["conjugate"], by="Casey.VI.VII.2")

    polar_d = model.construct_line(
        u_pt, v_pt, classes=["polar_line", "highlight"], ID="[ U V ]", by="Casey.III.27"
    )

    # Confirm algebraic polar_line and pole_of_line match exact synthetic construction
    alg_polar_d = polar_line(pole_d, base_circle)
    if not (alg_polar_d.contains(u_pt) and alg_polar_d.contains(v_pt)):
        raise AssertionError("Synthetic quadrangle polar does not coincide with algebraic polar.")
    if pole_of_line(polar_d, base_circle) != pole_d:
        raise AssertionError("pole_of_line(polar(D)) failed to recover D.")

    # Harmonic secant divisions (Casey Book VI, Sec. III, Prop. 4, p. 89)
    j1 = model.intersect(sec_1, polar_d, ID="J1", classes=["harmonic"], by="Casey.VI.III.4")
    j2 = model.intersect(sec_2, polar_d, ID="J2", classes=["harmonic"], by="Casey.VI.III.4")
    cr1 = cross_ratio(g1, h1, j1, pole_d)
    cr2 = cross_ratio(g2, h2, j2, pole_d)
    if not (is_harmonic(g1, h1, j1, pole_d) and is_harmonic(g2, h2, j2, pole_d)):
        raise AssertionError(f"Expected harmonic secants -1, got {cr1}, {cr2}")

    # La Hire's Reciprocity (Casey Book III, Prop. 25, p. 45):
    # Choose Q = (4, -4) on polar(D): 6*4 + (-4) = 20, construct polar(Q) as chord of contact!
    q_pt = model.given_point(4, -4, ID="Q", classes=["pole", "reciprocal"])
    model.assert_incident(q_pt, polar_d, by="Casey.III.25")

    mid_oq = compass_midpoint(model, o_center, q_pt)
    thales_oq = model.construct_circle(mid_oq, o_center, guide=True, by="III.17")
    k1, k2 = model.intersect_all(base_circle, thales_oq, classes=["contact"], guide=True, by="III.17")
    polar_q = model.construct_line(
        k1, k2, classes=["reciprocal_polar", "diagonal"], ID="[ polarQ ]", by="Casey.III.27"
    )
    model.assert_incident(pole_d, polar_q, by="Casey.III.25")

    # Also verify D U V is a self-conjugate triangle: polar(U) = [D V] and polar(V) = [D U]
    alg_polar_u = polar_line(u_pt, base_circle)
    alg_polar_v = polar_line(v_pt, base_circle)
    self_conj_ok = (
        alg_polar_u.contains(pole_d)
        and alg_polar_u.contains(v_pt)
        and alg_polar_v.contains(pole_d)
        and alg_polar_v.contains(u_pt)
    )
    lahire_ok = bool(polar_q.contains(pole_d) and self_conj_ok)
    model.conclude("La Hire reciprocity Q in polar(D) <=> D in polar(Q) & harmonic secants verified", by="Casey.III.25")

    return PolePolarResult(
        model=model,
        circle=base_circle,
        center=o_center,
        pole_d=pole_d,
        secant_1_pts=(g1, h1),
        secant_2_pts=(g2, h2),
        self_conjugate_triangle=(pole_d, u_pt, v_pt),
        polar_d=polar_d,
        harmonic_meets=(j1, j2),
        reciprocal_pole_q=q_pt,
        polar_q=polar_q,
        cross_ratio_secant_1=cr1,
        cross_ratio_secant_2=cr2,
        lahire_verified=lahire_ok,
    )
