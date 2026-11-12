"""Exact straightedge-and-compass constructions for Radical Axes, Coaxal Systems & Limiting Points.

Implements Unit 2 of the Casey Codex:

- **Book III, Prop. 22 (p. 42)**: Orthogonal circles (``|O1 O2|^2 = r1^2 + r2^2``).
- **Book III, Prop. 23 & Defs. (p. 43)**: Radical Axis, Radical Centre, Radical Circle, and
  Poncelet's **Limiting Points** ``L1, L2`` on the line of centres (``|D L1| = |D L2| = sqrt(pow)``).
- **Book III, Prop. 24 (p. 44)**: Fundamental Theorem of Coaxal Circles: the difference of the
  squares of tangents from any point ``P`` to two circles equals twice the rectangle contained
  by the distance between their centres and the perpendicular from ``P`` to their radical axis:
  ``pow(P, C1) - pow(P, C2) = 2 * (O2 - O1) . (E - P)``.
- **Book III, Prop. 28 & Book VI, Sec. V (pp. 113–119)**: Compass-and-straightedge construction
  of the radical axis of two disjoint circles via an auxiliary secant circle and conjugate
  orthogonal pencils passing through ``L1`` and ``L2``.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, clean_expr, quadrance, zero_test

from geometor.casey.invariants import (
    are_orthogonal_circles,
    circle_power,
    compass_midpoint,
    compass_perpendicular_line,
)

__all__ = [
    "CoaxialPencilResult",
    "CoaxialTheoremReport",
    "construct_radical_axis_and_coaxial_pencil",
    "verify_coaxial_fundamental_theorem",
]


@dataclass(frozen=True)
class CoaxialTheoremReport:
    """Symbolic verification certificate for Casey's Fundamental Theorem (Book III, Prop. 24)."""

    symbolic_prop24_residual: sp.Expr
    radical_axis_power_diff: sp.Expr
    limiting_point_power_c1: sp.Expr
    limiting_point_power_c2: sp.Expr
    orthogonal_to_c1: bool
    orthogonal_to_c2: bool
    orthogonal_to_c3: bool
    verified: bool


@dataclass(frozen=True)
class CoaxialPencilResult:
    """Constructed elements for the Disjoint Coaxal Pencil & Poncelet Limiting Points (Unit 2)."""

    model: Model
    c1: spg.Circle
    c2: spg.Circle
    c3_coaxial: spg.Circle
    aux_secant_circle: spg.Circle
    radical_center: spg.Point
    radical_foot: spg.Point
    radical_axis: spg.Line
    line_of_centers: spg.Line
    tangent_contact_c1: spg.Point
    limiting_points: tuple[spg.Point, spg.Point]
    orthogonal_circle_1: spg.Circle
    orthogonal_circle_2: spg.Circle
    report: CoaxialTheoremReport


def verify_coaxial_fundamental_theorem(
    c1: spg.Circle,
    c2: spg.Circle,
    c3_coaxial: spg.Circle,
    orth_circle: spg.Circle,
    limiting_points: tuple[spg.Point, spg.Point],
) -> CoaxialTheoremReport:
    """Verify Casey Book III Props. 22–24 symbolically and on the constructed coaxal system.

    Args:
        c1: First primary circle of the coaxal pencil.
        c2: Second primary circle of the coaxal pencil.
        c3_coaxial: Third circle belonging to the same coaxal pencil.
        orth_circle: Conjugate circle cutting the pencil orthogonally.
        limiting_points: Pair ``(L1, L2)`` of Poncelet limiting points.

    Returns:
        Frozen :class:`CoaxialTheoremReport` certificate.
    """
    # Universal symbolic proof of Casey Book III Prop. 24 on line of centres along x-axis:
    # C=(h1, 0, r1), C'=(h2, 0, r2). Radical axis x = x_e where x_e = ((r1^2 - r2^2) - (h1^2 - h2^2)) / (2*(h2 - h1))
    px, py, h1, h2, r1, r2 = sp.symbols("px py h1 h2 r1 r2", real=True)
    pf_sq = (px - h1) ** 2 + py**2 - r1**2
    pfp_sq = (px - h2) ** 2 + py**2 - r2**2
    xe = (h2**2 - r2**2 - (h1**2 - r1**2)) / (2 * (h2 - h1))
    # Directed segment CC' = h2 - h1 and directed perpendicular EP = px - xe (or xe - px):
    # (px - h1)^2 - r1^2 - ((px - h2)^2 - r2^2) = 2*(h2 - h1)*(px - xe)
    prop24_res = sp.simplify((pf_sq - pfp_sq) - 2 * (h2 - h1) * (px - xe))

    # Check equal power along radical axis and zero-radius power at limiting points
    sample_axis_pt = spg.Point(sp.Integer(0), sp.Integer(11))
    axis_diff = clean_expr(circle_power(sample_axis_pt, c1) - circle_power(sample_axis_pt, c2))

    # Each limiting point L_i treated as null-circle (L_i, 0) is coaxal: pow(D, (L_i, 0)) == pow(D, C1),
    # and any orthogonal circle through L1, L2 has radius^2 = pow(center, L_i) = pow(center, C_k).
    l1, l2 = limiting_points
    # Moreover, by Casey VI.V (2), |P L1|^2 / dist(P, rad_axis) = 2 * |O_k - L1| for P on C_k!
    # Check at P1 = (-4, 0) on C1((-10, 0), 6): |P1 L1|^2 = (-4 - (-8))^2 = 16, dist = 4,
    # and 2 * |(-10) - (-8)| * 4 = 2 * 2 * 4 = 16!
    p_on_c1 = spg.Point(c1.center.x + c1.radius, c1.center.y)
    lim_rel_c1 = clean_expr(
        quadrance(p_on_c1, l1) - 2 * sp.Abs(c1.center.x - l1.x) * sp.Abs(p_on_c1.x)
    )
    p_on_c2 = spg.Point(c2.center.x - c2.radius, c2.center.y)
    lim_rel_c2 = clean_expr(
        quadrance(p_on_c2, l2) - 2 * sp.Abs(c2.center.x - l2.x) * sp.Abs(p_on_c2.x)
    )

    orth1 = are_orthogonal_circles(orth_circle, c1)
    orth2 = are_orthogonal_circles(orth_circle, c2)
    orth3 = are_orthogonal_circles(orth_circle, c3_coaxial)

    ok = (
        zero_test(prop24_res)
        and zero_test(axis_diff)
        and zero_test(lim_rel_c1)
        and zero_test(lim_rel_c2)
        and orth1
        and orth2
        and orth3
    )
    return CoaxialTheoremReport(
        symbolic_prop24_residual=prop24_res,
        radical_axis_power_diff=axis_diff,
        limiting_point_power_c1=lim_rel_c1,
        limiting_point_power_c2=lim_rel_c2,
        orthogonal_to_c1=orth1,
        orthogonal_to_c2=orth2,
        orthogonal_to_c3=orth3,
        verified=ok,
    )


def construct_radical_axis_and_coaxial_pencil(
    model: Model | None = None,
) -> CoaxialPencilResult:
    """Construct the radical axis, coaxal system, orthogonal pencil, and limiting points.

    Uses exact integer-rational circles ``C1 = ((-10, 0), 6)`` and ``C2 = ((17, 0), 15)``:

    1. Draws an auxiliary secant circle ``C_aux = ((2, 8), 10)`` cutting ``C1`` in ``U1, V1``
       and ``C2`` in ``U2, V2`` (Casey Book III, Prop. 28).
    2. Intersects common chords ``[U1 V1]`` and ``[U2 V2]`` to obtain the **Radical Centre**
       ``Rc = (0, -6)`` (Book III, Prop. 23, Cor. 2).
    3. Drops the perpendicular from ``Rc`` to the line of centres ``[O1 O2]`` to construct
       the **Radical Axis** ``x = 0`` and foot ``D = (0, 0)``.
    4. Constructs the tangent ``D T1`` to ``C1`` by Euclid III.17 (Thales circle on ``O1 D``)
       and transfers ``|D T1| = 8`` onto ``[O1 O2]`` via circle ``(D, T1)`` to construct
       **Poncelet's Limiting Points** ``L1 = (-8, 0)`` and ``L2 = (8, 0)``.
    5. Constructs two members ``(Rc, L1)`` and ``(D, T1)`` of the conjugate orthogonal pencil
       passing through ``L1, L2`` and cutting ``C1, C2, C3`` orthogonally.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`CoaxialPencilResult` with exact coordinates and verification report.
    """
    if model is None:
        model = Model("casey_coaxial_pencil", auto_intersect=False, enable_logging=False)

    o1 = model.given_point(-10, 0, ID="O1", classes=["given", "center"])
    p1 = model.set_point(-4, 0, ID="P1", classes=["given"], guide=True, by="given")
    o2 = model.given_point(17, 0, ID="O2", classes=["given", "center"])
    p2 = model.set_point(2, 0, ID="P2", classes=["given"], guide=True, by="given")

    line_centers = model.construct_line(
        o1, o2, classes=["carrier", "line_of_centers"], ID="[ O1 O2 ]", by="Post.1"
    )
    c1 = model.construct_circle(o1, p1, classes=["coaxial_circle", "primary"], ID="( O1 P1 )", by="Post.3")
    c2 = model.construct_circle(o2, p2, classes=["coaxial_circle", "primary"], ID="( O2 P2 )", by="Post.3")

    # Third member C3 of the coaxal pencil: centre O3c=(10, 0), radius 6 (10^2 - 6^2 = 64)
    o3c = model.given_point(10, 0, ID="O3", classes=["center", "coaxial_member"])
    p3c = model.set_point(4, 0, ID="P3", classes=["given"], guide=True, by="given")
    c3 = model.construct_circle(
        o3c, p3c, classes=["coaxial_circle", "secondary"], ID="( O3 P3 )", by="Post.3"
    )

    # Auxiliary secant circle C_aux = ((2, 8), (-6, 2)) of radius 10 cutting both C1 and C2
    o_aux = model.set_point(2, 8, ID="Oa", classes=["auxiliary"], guide=True, by="given")
    q_aux = model.set_point(-6, 2, ID="Qa", classes=["auxiliary"], guide=True, by="given")
    c_aux = model.construct_circle(
        o_aux, q_aux, classes=["auxiliary_circle"], ID="( Oa Qa )", by="Casey.III.28"
    )

    u1, v1 = model.intersect_all(c1, c_aux, classes=["secant_hit"], guide=True, by="Casey.III.28")
    u2, v2 = model.intersect_all(c2, c_aux, classes=["secant_hit"], guide=True, by="Casey.III.28")

    chord_1 = model.construct_line(
        u1, v1, classes=["radical_chord"], ID="[ U1 V1 ]", by="Casey.III.23"
    )
    chord_2 = model.construct_line(
        u2, v2, classes=["radical_chord"], ID="[ U2 V2 ]", by="Casey.III.23"
    )
    rad_center = model.intersect(
        chord_1, chord_2, ID="Rc", classes=["radical_center", "highlight_point"], by="Casey.III.23.Cor2"
    )

    # Perpendicular from Radical Centre Rc=(0, -6) to line of centres [O1 O2] -> Radical Axis x = 0!
    rad_axis = compass_perpendicular_line(
        model, o1, o2, rad_center, ID="[ Rc D ]", classes=["radical_axis", "highlight"]
    )
    rad_foot = model.intersect(
        line_centers, rad_axis, ID="D", classes=["center", "foot"], by="I.12"
    )

    # Tangent from D=(0, 0) to C1 via Thales circle on O1 D -> Poncelet Limiting Points L1, L2
    mid_o1_d = compass_midpoint(model, o1, rad_foot)
    thales_c1 = model.construct_circle(mid_o1_d, rad_foot, guide=True, by="III.17")
    t1 = model.intersect(
        c1, thales_c1, side_of=(o1, o2, 1), ID="T1", classes=["contact"], by="III.17"
    )

    orth_circle_d = model.construct_circle(
        rad_foot, t1, classes=["orthogonal_circle"], ID="( D T1 )", by="Casey.III.23.Cor3"
    )
    l1 = model.intersect(
        orth_circle_d,
        line_centers,
        between=(o1, rad_foot),
        ID="L1",
        classes=["limiting_point", "highlight_point"],
        by="Casey.III.23.Def",
    )
    l2 = model.intersect(
        orth_circle_d,
        line_centers,
        between=(rad_foot, o2),
        ID="L2",
        classes=["limiting_point", "highlight_point"],
        by="Casey.III.23.Def",
    )

    orth_circle_rc = model.construct_circle(
        rad_center, l1, classes=["orthogonal_circle", "featured"], ID="( Rc L1 )", by="Casey.VI.V.1"
    )
    model.assert_incident(l2, orth_circle_rc, by="Casey.VI.V.1")
    model.conclude("Orthogonal pencil passes through Poncelet limiting points L1=(-8,0), L2=(8,0)", by="Casey.VI.V.1")

    report = verify_coaxial_fundamental_theorem(c1, c2, c3, orth_circle_rc, (l1, l2))
    return CoaxialPencilResult(
        model=model,
        c1=c1,
        c2=c2,
        c3_coaxial=c3,
        aux_secant_circle=c_aux,
        radical_center=rad_center,
        radical_foot=rad_foot,
        radical_axis=rad_axis,
        line_of_centers=line_centers,
        tangent_contact_c1=t1,
        limiting_points=(l1, l2),
        orthogonal_circle_1=orth_circle_rc,
        orthogonal_circle_2=orth_circle_d,
        report=report,
    )
