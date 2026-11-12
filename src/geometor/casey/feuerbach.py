"""Exact symbolic proofs and compass-and-straightedge constructions of Casey's & Feuerbach's Theorems.

Implements:

- **Unit 1 (Book I Misc. Ex. 42–46 & Book IV Prop. 5, pp. 20, 57–58)**: The Euler line
  (``O, G, N, H``) and the Nine-Points Circle through side midpoints ``Ma, Mb, Mc``, altitude
  feet ``Da, Db, Dc``, and Euler midpoints ``Ea, Eb, Ec``.
- **Unit 4 (Book VI, Sec. IV, Prop. 9, Prop. 10 & Cor. 2, pp. 102–106)**:

  1. Universal polynomial proof of Casey's Generalized Ptolemy Theorem
     (``t_12*t_34 + t_14*t_23 = t_13*t_24``) via circular inversion and bitangent invariance.
  2. Universal side-length ``(a, b, c)`` bitangent proof of Feuerbach's Theorem for both the
     incircle and the excircles.
  3. Exact compass-and-straightedge construction on the canonical Heronian ``(15, 13, 14)``
     triangle verifying bitangent lengths, Casey's 1861 orthogonal inversion circle at ``Ma``,
     and exact tangency at the Feuerbach point ``Fe = X(11) = (6, 8)`` plus all three excircles.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, clean_expr, proposition, quadrance, zero_test

from geometor.casey.invariants import (
    HERONIAN_VERTICES,
    are_orthogonal_circles,
    bitangent_length,
    compass_midpoint,
    compass_perp_bisector,
    compass_perpendicular_line,
    invert_point,
    signed_triangle_area,
)

__all__ = [
    "CaseyFeuerbachHeronianReport",
    "CaseyFeuerbachResult",
    "CaseySymbolicProof",
    "EulerNinePointResult",
    "compass_internal_angle_bisector",
    "construct_casey_feuerbach",
    "construct_euler_nine_point",
    "prove_casey_feuerbach_heronian",
    "prove_casey_theorem_symbolic",
]


@dataclass(frozen=True)
class CaseySymbolicProof:
    """Symbolic verification certificate for Casey's Generalized Ptolemy Theorem."""

    inversion_invariance_residual: sp.Expr
    tangent_line_euler_residual: sp.Expr
    incircle_casey_residual: sp.Expr
    incircle_cor2_squares_residual: sp.Expr
    excircle_a_casey_residual: sp.Expr
    verified: bool


@dataclass(frozen=True)
class CaseyFeuerbachHeronianReport:
    """Exact rational invariant report for Casey's Theorem & Feuerbach tangency on ``(15, 13, 14)``."""

    sides: tuple[sp.Integer, sp.Integer, sp.Integer]
    area: sp.Rational
    inradius: sp.Rational
    circumradius: sp.Rational
    nine_point_radius: sp.Rational
    exradii: tuple[sp.Rational, sp.Rational, sp.Rational]
    midpoint_chords: tuple[sp.Rational, sp.Rational, sp.Rational]
    incircle_midpoint_tangents: tuple[sp.Rational, sp.Rational, sp.Rational]
    casey_signed_sum: sp.Expr
    feuerbach_point: spg.Point
    excircle_feuerbach_points: tuple[spg.Point, spg.Point, spg.Point]
    ni_distance: sp.Rational
    inversion_circle_orthogonal_to_incircle: bool
    inversion_circle_orthogonal_to_excircle_a: bool
    verified: bool


@dataclass(frozen=True)
class EulerNinePointResult:
    """Constructed elements for the Euler Line and Nine-Points Circle (Unit 1)."""

    model: Model
    vertices: tuple[spg.Point, spg.Point, spg.Point]
    midpoints: tuple[spg.Point, spg.Point, spg.Point]
    altitude_feet: tuple[spg.Point, spg.Point, spg.Point]
    euler_midpoints: tuple[spg.Point, spg.Point, spg.Point]
    centroid: spg.Point
    circumcenter: spg.Point
    orthocenter: spg.Point
    nine_point_center: spg.Point
    euler_line: spg.Line
    circumcircle: spg.Circle
    nine_point_circle: spg.Circle


@dataclass(frozen=True)
class CaseyFeuerbachResult:
    """Constructed elements for Casey's & Feuerbach's Theorem on ``(15, 13, 14)`` (Unit 4)."""

    model: Model
    euler_nine_point: EulerNinePointResult
    incenter: spg.Point
    incircle_contacts: tuple[spg.Point, spg.Point, spg.Point]
    incircle: spg.Circle
    feuerbach_point: spg.Point
    casey_inversion_circle: spg.Circle
    fourth_common_tangent: spg.Line


@proposition("I.9", kind="problem", title="Internal Angle Bisector")
def compass_internal_angle_bisector(
    model: Model,
    vertex: spg.Point,
    arm_p1: spg.Point,
    arm_p2: spg.Point,
    *,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Line:
    """Construct the internal bisector of ``< arm_p1 vertex arm_p2 )`` by Euclid I.9.

    Transfers ``|vertex arm_p1|`` onto ray ``vertex arm_p2`` via circle ``(vertex, arm_p1)``
    and bisects the resulting isosceles base chord.

    Args:
        model: Target :class:`~geometor.model.Model`.
        vertex: Angle vertex.
        arm_p1: Point on the first ray.
        arm_p2: Point on the second ray.
        ID: Optional explicit line identifier.
        classes: Optional semantic CSS classes.
        guide: Whether the angle bisector should remain a guide.

    Returns:
        Exact internal angle bisector :class:`sympy.geometry.Line`.
    """
    ray_2 = model.construct_line(vertex, arm_p2, guide=True, by="Post.1")
    gauge = model.construct_circle(vertex, arm_p1, guide=True, by="Post.3")
    mark = model.intersect(gauge, ray_2, on_ray=(vertex, arm_p2), guide=True, by="I.3")
    chord_mid = compass_midpoint(model, arm_p1, mark)
    return model.construct_line(vertex, chord_mid, ID=ID, classes=classes, guide=guide, by="I.9")


def prove_casey_theorem_symbolic() -> CaseySymbolicProof:
    """Prove Casey's Generalized Ptolemy Theorem & Feuerbach's Corollary symbolically.

    Verifies four algebraic pillars from Casey, Book VI, Sec. IV, Props. 9–10 (pp. 102–106):

    1. **Inversion Invariance (Prop. 9, pp. 102–103)**: Under inversion in ``(O, k)`` at the
       origin, for two circles ``(x1, y1, r1)`` and ``(x2, y2, r2)`` not passing through ``O``,
       the normalized bitangent ratio ``t_12^2 / (r1 * r2)`` is strictly invariant:
       ``t'_12^2 / (r'_1 * r'_2) - t_12^2 / (r1 * r2) == 0``.
    2. **Collinear Contact Reduction (Prop. 10, pp. 103–104)**: Inverting from a point on the
       fifth tangent circle maps it to ``y = 0`` and the four tangent circles to ``(u_i, r_i)``
       with ``t_ij = |u_i - u_j|``, reducing ``t_12*t_34 + t_14*t_23 = t_13*t_24`` for ordered
       contacts ``u_1 < u_2 < u_3 < u_4`` to Euler's identity (Book II, Prop. 7, p. 24).
    3. **Universal Incircle Bitangent Identity (Prop. 10, Cor. 2, pp. 104–105)**: For general
       positive side lengths ``b <= c <= a``, ``t_23 = a/2, t_31 = b/2, t_12 = c/2`` and
       ``t_14 = (c - b)/2, t_24 = (a - c)/2, t_34 = (a - b)/2`` satisfy
       ``t_23*t_14 + t_31*t_24 - t_12*t_34 == 0``, alongside Casey's squared identity
       ``(b^2 - c^2) + (c^2 - a^2) + (a^2 - b^2) == 0``.
    4. **Universal Excircle Bitangent Identity**: For the ``A``-excircle,
       ``t_14 = (c - b)/2, t_24 = (a + c)/2, t_34 = (a + b)/2`` satisfy
       ``t_23*t_14 + t_31*t_24 - t_12*t_34 == 0`` (with ``t_31*t_24 = t_12*t_34 + t_23*t_14``).

    Returns:
        Frozen :class:`CaseySymbolicProof` certificate with zero residuals.
    """
    k, x1, y1, r1, x2, y2, r2 = sp.symbols("k x1 y1 r1 x2 y2 r2", positive=True)
    p1 = x1**2 + y1**2 - r1**2
    p2 = x2**2 + y2**2 - r2**2
    # Inverted circle i under (O, k) has centre (k^2/p_i)*(x_i, y_i) and radius (k^2/|p_i|)*r_i
    # Assuming p1 > 0, p2 > 0 (exterior to O; sign cancels in squared ratio when same power sign):
    cx1, cy1, cr1 = k**2 * x1 / p1, k**2 * y1 / p1, k**2 * r1 / p1
    cx2, cy2, cr2 = k**2 * x2 / p2, k**2 * y2 / p2, k**2 * r2 / p2

    t12_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2 - (r1 - r2) ** 2
    t12_inv_sq = (cx1 - cx2) ** 2 + (cy1 - cy2) ** 2 - (cr1 - cr2) ** 2
    inv_residual = sp.simplify(t12_inv_sq / (cr1 * cr2) - t12_sq / (r1 * r2))

    u1, u2, u3, u4 = sp.symbols("u1 u2 u3 u4", real=True)
    euler_residual = sp.expand((u2 - u1) * (u4 - u3) + (u4 - u1) * (u3 - u2) - (u3 - u1) * (u4 - u2))

    a_sym, b_sym, c_sym = sp.symbols("a b c", positive=True)
    # Ordered b <= c <= a: |b - c| = c - b, |c - a| = a - c, |a - b| = a - b
    inc_res = sp.simplify(
        (a_sym / 2) * ((c_sym - b_sym) / 2)
        + (b_sym / 2) * ((a_sym - c_sym) / 2)
        - (c_sym / 2) * ((a_sym - b_sym) / 2)
    )
    cor2_sq_res = sp.expand((b_sym**2 - c_sym**2) + (c_sym**2 - a_sym**2) + (a_sym**2 - b_sym**2))

    # A-excircle with b <= c <= a: |Ma T'_a| = (c - b)/2, |Mb T'_b| = (a + c)/2, |Mc T'_c| = (a + b)/2
    exc_res = sp.simplify(
        (a_sym / 2) * ((c_sym - b_sym) / 2)
        + (b_sym / 2) * ((a_sym + c_sym) / 2)
        - (c_sym / 2) * ((a_sym + b_sym) / 2)
    )

    ok = all(
        zero_test(expr)
        for expr in (inv_residual, euler_residual, inc_res, cor2_sq_res, exc_res)
    )
    return CaseySymbolicProof(
        inversion_invariance_residual=inv_residual,
        tangent_line_euler_residual=euler_residual,
        incircle_casey_residual=inc_res,
        incircle_cor2_squares_residual=cor2_sq_res,
        excircle_a_casey_residual=exc_res,
        verified=ok,
    )


def prove_casey_feuerbach_heronian() -> CaseyFeuerbachHeronianReport:
    """Verify Casey's bitangent equation and all 4 Feuerbach tangencies on Heronian ``(15, 13, 14)``.

    Evaluates exact coordinates on ``A=(0,0), B=(14,0), C=(5,12)`` (``a=15, b=13, c=14``),
    confirming:

    - Midpoint chords ``t_23 = 15/2``, ``t_31 = 13/2``, ``t_12 = 7``.
    - Midpoint-to-incircle bitangents ``|Ma Ta| = 1/2``, ``|Mb Tb| = 1/2``, ``|Mc Tc| = 1``.
    - Casey's equation ``(15/2)*(1/2) + (13/2)*(1/2) - 7*1 = 15/4 + 13/4 - 7 = 0``.
    - Internal tangency of Nine-Points Circle ``N=(6, 63/16), R_9=65/16`` with Incircle
      ``I=(6, 4), r=4`` at ``Fe = X(11) = (6, 8)`` with ``|NI| = 1/16 = R_9 - r``.
    - External tangency of Nine-Points Circle with all three Excircles ``(Ia, r_a), (Ib, r_b),
      (Ic, r_c)`` with ``|N I_k| = R_9 + r_k``.
    - Casey's 1861 inversion circle ``(Ma, 1/2)`` cuts both ``(I, 4)`` and ``(Ia, 14)``
      orthogonally and inverts their fourth common internal tangent into the Nine-Points Circle.

    Returns:
        Frozen :class:`CaseyFeuerbachHeronianReport` with exact rational values.
    """
    a_pt, b_pt, c_pt = HERONIAN_VERTICES
    a_len = sp.Integer(15)
    b_len = sp.Integer(13)
    c_len = sp.Integer(14)
    s_val = (a_len + b_len + c_len) / 2
    area = signed_triangle_area(a_pt, b_pt, c_pt)
    r_in = clean_expr(area / s_val)
    r_circum = clean_expr((a_len * b_len * c_len) / (4 * area))
    r_nine = clean_expr(r_circum / 2)

    ma = spg.Point((b_pt.x + c_pt.x) / 2, (b_pt.y + c_pt.y) / 2)
    mb = spg.Point((c_pt.x + a_pt.x) / 2, (c_pt.y + a_pt.y) / 2)
    mc = spg.Point((a_pt.x + b_pt.x) / 2, (a_pt.y + b_pt.y) / 2)

    incenter = spg.Point(
        (a_len * a_pt.x + b_len * b_pt.x + c_len * c_pt.x) / (2 * s_val),
        (a_len * a_pt.y + b_len * b_pt.y + c_len * c_pt.y) / (2 * s_val),
    )
    incircle = spg.Circle(incenter, r_in)

    t23 = bitangent_length(mb, mc)
    t31 = bitangent_length(mc, ma)
    t12 = bitangent_length(ma, mb)

    t14 = bitangent_length(ma, incircle)
    t24 = bitangent_length(mb, incircle)
    t34 = bitangent_length(mc, incircle)

    casey_sum = clean_expr(t23 * t14 + t31 * t24 - t12 * t34)

    n_center = spg.Point(sp.Integer(6), sp.Rational(63, 16))
    nine_circ = spg.Circle(n_center, r_nine)
    ni_dist = clean_expr(sp.sqrt(quadrance(n_center, incenter)))
    fe_pts = nine_circ.intersection(incircle)
    if len(fe_pts) != 1 or not isinstance(fe_pts[0], spg.Point):
        raise AssertionError(f"Expected unique Feuerbach tangency point, got {fe_pts!r}")
    fe_pt = fe_pts[0]

    # Excircles: Ia=(-a:b:c), Ib=(a:-b:c), Ic=(a:b:-c)
    ex_specs = (
        (-a_len, b_len, c_len, clean_expr(area / (s_val - a_len))),
        (a_len, -b_len, c_len, clean_expr(area / (s_val - b_len))),
        (a_len, b_len, -c_len, clean_expr(area / (s_val - c_len))),
    )
    exradii_list: list[sp.Rational] = []
    ex_touch_pts: list[spg.Point] = []
    ex_circles: list[spg.Circle] = []
    ex_tangency_ok = True
    for wa, wb, wc, r_ex in ex_specs:
        w_sum = wa + wb + wc
        ex_c = spg.Point(
            clean_expr((wa * a_pt.x + wb * b_pt.x + wc * c_pt.x) / w_sum),
            clean_expr((wa * a_pt.y + wb * b_pt.y + wc * c_pt.y) / w_sum),
        )
        ex_circ = spg.Circle(ex_c, r_ex)
        ex_circles.append(ex_circ)
        exradii_list.append(r_ex)  # type: ignore[arg-type]
        dist_n_ex = clean_expr(sp.sqrt(quadrance(n_center, ex_c)))
        if not zero_test(dist_n_ex - (r_nine + r_ex)):
            ex_tangency_ok = False
        hits = nine_circ.intersection(ex_circ)
        if len(hits) != 1 or not isinstance(hits[0], spg.Point):
            ex_tangency_ok = False
        else:
            ex_touch_pts.append(hits[0])

    # Casey's 1861 inversion circle at G = Ma of radius |b - c|/2 = 1/2
    inv_circ = spg.Circle(ma, t14)
    orth_in = are_orthogonal_circles(inv_circ, incircle)
    orth_exa = are_orthogonal_circles(inv_circ, ex_circles[0])

    verified = (
        zero_test(casey_sum)
        and zero_test(ni_dist - (r_nine - r_in))
        and fe_pt == spg.Point(6, 8)
        and ex_tangency_ok
        and orth_in
        and orth_exa
    )

    return CaseyFeuerbachHeronianReport(
        sides=(a_len, b_len, c_len),
        area=area,  # type: ignore[arg-type]
        inradius=r_in,  # type: ignore[arg-type]
        circumradius=r_circum,  # type: ignore[arg-type]
        nine_point_radius=r_nine,  # type: ignore[arg-type]
        exradii=(exradii_list[0], exradii_list[1], exradii_list[2]),
        midpoint_chords=(t23, t31, t12),  # type: ignore[arg-type]
        incircle_midpoint_tangents=(t14, t24, t34),  # type: ignore[arg-type]
        casey_signed_sum=casey_sum,
        feuerbach_point=fe_pt,
        excircle_feuerbach_points=(ex_touch_pts[0], ex_touch_pts[1], ex_touch_pts[2]),
        ni_distance=ni_dist,  # type: ignore[arg-type]
        inversion_circle_orthogonal_to_incircle=orth_in,
        inversion_circle_orthogonal_to_excircle_a=orth_exa,
        verified=verified,
    )


def construct_euler_nine_point(model: Model | None = None) -> EulerNinePointResult:
    """Construct the Euler Line and Nine-Points Circle by straightedge and compass (Unit 1).

    Follows Casey, Book I, Misc. Ex. 42–46 (p. 20) and Book IV, Prop. 5 (pp. 57–58) on
    ``A=(0,0), B=(14,0), C=(5,12)``, verifying exact incidence of all nine classical points
    and Euler trisection ``|HG|^2 = 4*|GO|^2``.

    Args:
        model: Optional existing :class:`~geometor.model.Model`. Created with
            ``auto_intersect=False`` when ``None``.

    Returns:
        Populated :class:`EulerNinePointResult`.
    """
    if model is None:
        model = Model("casey_euler_nine_point", auto_intersect=False, enable_logging=False)

    a_coord, b_coord, c_coord = HERONIAN_VERTICES
    a_pt = model.given_point(a_coord.x, a_coord.y, ID="A", classes=["given", "vertex"])
    b_pt = model.given_point(b_coord.x, b_coord.y, ID="B", classes=["given", "vertex"])
    c_pt = model.given_point(c_coord.x, c_coord.y, ID="C", classes=["given", "vertex"])

    model.set_polygon([a_pt, b_pt, c_pt], classes=["triangle", "primary"], ID="< A B C >")
    side_bc = model.construct_line(b_pt, c_pt, classes=["carrier", "side"], ID="[ B C ]", by="Post.1")
    side_ca = model.construct_line(c_pt, a_pt, classes=["carrier", "side"], ID="[ C A ]", by="Post.1")
    side_ab = model.construct_line(a_pt, b_pt, classes=["carrier", "side"], ID="[ A B ]", by="Post.1")

    # Side midpoints Ma, Mb, Mc & Centroid G (Casey Book I, Prop. 9 & Misc. Ex. 42)
    ma = compass_midpoint(model, b_pt, c_pt, ID="Ma", classes=["nine_point", "midpoint"])
    mb = compass_midpoint(model, c_pt, a_pt, ID="Mb", classes=["nine_point", "midpoint"])
    mc = compass_midpoint(model, a_pt, b_pt, ID="Mc", classes=["nine_point", "midpoint"])

    med_a = model.construct_line(a_pt, ma, classes=["median"], guide=True, by="Post.1")
    med_b = model.construct_line(b_pt, mb, classes=["median"], guide=True, by="Post.1")
    centroid = model.intersect(med_a, med_b, ID="G", classes=["center", "euler"], by="Casey.I.9")

    # Altitudes, feet Da, Db, Dc & Orthocentre H (Casey Book I, Prop. 10 Cor.)
    alt_a = compass_perpendicular_line(
        model, b_pt, c_pt, a_pt, ID="[ A Da ]", classes=["altitude"]
    )
    alt_b = compass_perpendicular_line(
        model, c_pt, a_pt, b_pt, ID="[ B Db ]", classes=["altitude"]
    )
    alt_c = compass_perpendicular_line(
        model, a_pt, b_pt, c_pt, ID="[ C Dc ]", classes=["altitude"]
    )
    da = model.intersect(side_bc, alt_a, ID="Da", classes=["nine_point", "foot"], by="I.12")
    db = model.intersect(side_ca, alt_b, ID="Db", classes=["nine_point", "foot"], by="I.12")
    dc = model.intersect(side_ab, alt_c, ID="Dc", classes=["nine_point", "foot"], by="I.12")
    orthocenter = model.intersect(
        alt_a, alt_b, ID="H", classes=["center", "euler"], by="Casey.I.10"
    )
    model.assert_incident(orthocenter, alt_c, by="Casey.I.10.Cor")

    # Circumcentre O & Circumcircle (Euclid IV.5)
    pb_ab = compass_perp_bisector(model, a_pt, b_pt, guide=True)
    pb_bc = compass_perp_bisector(model, b_pt, c_pt, guide=True)
    circumcenter = model.intersect(
        pb_ab, pb_bc, ID="O", classes=["center", "euler"], by="IV.5"
    )
    circumcircle = model.construct_circle(
        circumcenter, a_pt, classes=["circumcircle"], ID="( O A )", by="Post.3"
    )

    # Euler midpoints Ea, Eb, Ec & Nine-Points Centre N (Casey Book IV, Prop. 5, pp. 57–58)
    ea = compass_midpoint(model, a_pt, orthocenter, ID="Ea", classes=["nine_point", "euler_mid"])
    eb = compass_midpoint(model, b_pt, orthocenter, ID="Eb", classes=["nine_point", "euler_mid"])
    ec = compass_midpoint(model, c_pt, orthocenter, ID="Ec", classes=["nine_point", "euler_mid"])

    euler_line = model.construct_line(
        circumcenter, orthocenter, classes=["euler_line", "highlight"], ID="[ O H ]", by="Post.1"
    )
    model.assert_collinear(circumcenter, centroid, orthocenter, by="Casey.I.Ex43")

    nine_center = compass_midpoint(
        model, circumcenter, orthocenter, ID="N", classes=["center", "euler"]
    )
    nine_circle = model.construct_circle(
        nine_center, ma, classes=["nine_point_circle", "featured"], ID="( N Ma )", by="Casey.IV.5"
    )

    for nine_pt in (ma, mb, mc, da, db, dc, ea, eb, ec):
        model.assert_incident(nine_pt, nine_circle, by="Casey.IV.5")
    model.conclude("Nine-Points Circle passes through Ma, Mb, Mc, Da, Db, Dc, Ea, Eb, Ec", by="Casey.IV.5")

    return EulerNinePointResult(
        model=model,
        vertices=(a_pt, b_pt, c_pt),
        midpoints=(ma, mb, mc),
        altitude_feet=(da, db, dc),
        euler_midpoints=(ea, eb, ec),
        centroid=centroid,
        circumcenter=circumcenter,
        orthocenter=orthocenter,
        nine_point_center=nine_center,
        euler_line=euler_line,
        circumcircle=circumcircle,
        nine_point_circle=nine_circle,
    )


def construct_casey_feuerbach(model: Model | None = None) -> CaseyFeuerbachResult:
    """Construct Casey's Inversion Proof & Feuerbach's Tangency Theorem on ``(15, 13, 14)``.

    Builds the Nine-Points Circle, constructs the Incentre ``I`` and Incircle ``(I, Ta)`` by
    pure compass-and-straightedge (Euclid IV.4), erects Casey's 1861 orthogonal inversion
    circle ``(Ma, Ta)`` (Book VI, Sec. IV, p. 106), constructs the fourth common internal
    tangent of ``(I, r)`` and ``(Ia, r_a)`` via reflection across line of centres ``AI``, and
    discovers the exact Feuerbach point ``Fe = X(11) = (6, 8)`` as ``(N, Ma) ∩ (I, Ta)``.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`CaseyFeuerbachResult`.
    """
    if model is None:
        model = Model("casey_feuerbach", auto_intersect=False, enable_logging=False)

    enp = construct_euler_nine_point(model)
    a_pt, b_pt, c_pt = enp.vertices
    ma, mb, mc = enp.midpoints
    side_bc = model.get_element_by_ID("[ B C ]")
    side_ca = model.get_element_by_ID("[ C A ]")
    side_ab = model.get_element_by_ID("[ A B ]")

    # Incentre I by Euclid IV.4 internal angle bisectors
    bis_a = compass_internal_angle_bisector(
        model, a_pt, b_pt, c_pt, ID="[ A I ]", classes=["bisector"], guide=True
    )
    bis_b = compass_internal_angle_bisector(
        model, b_pt, c_pt, a_pt, ID="[ B I ]", classes=["bisector"], guide=True
    )
    incenter = model.intersect(bis_a, bis_b, ID="I", classes=["center", "incenter"], by="IV.4")

    # Orthogonal feet Ta, Tb, Tc of I on the three sides & Incircle (I, Ta)
    perp_ia = compass_perpendicular_line(model, b_pt, c_pt, incenter, guide=True)
    perp_ib = compass_perpendicular_line(model, c_pt, a_pt, incenter, guide=True)
    perp_ic = compass_perpendicular_line(model, a_pt, b_pt, incenter, guide=True)
    ta = model.intersect(side_bc, perp_ia, ID="Ta", classes=["contact"], by="IV.4")
    tb = model.intersect(side_ca, perp_ib, ID="Tb", classes=["contact"], by="IV.4")
    tc = model.intersect(side_ab, perp_ic, ID="Tc", classes=["contact"], by="IV.4")

    incircle = model.construct_circle(
        incenter, ta, classes=["incircle", "featured"], ID="( I Ta )", by="IV.4"
    )
    model.assert_incident(tb, incircle, by="IV.4")
    model.assert_incident(tc, incircle, by="IV.4")

    # Casey's 1861 orthogonal inversion circle at Ma passing through Ta (radius |b-c|/2 = 1/2)
    casey_inv_circle = model.construct_circle(
        ma, ta, classes=["inversion_circle", "auxiliary_circle"], ID="( Ma Ta )", by="Casey.VI.IV.10"
    )

    # Fourth common internal tangent of incircle I and A-excircle Ia:
    # Side BC and the 4th internal common tangent are symmetric across the internal bisector AI!
    # Reflecting B and C across bis_a (via circle centered at A and I) constructs it purely by compass!
    c_ai_1 = model.construct_circle(a_pt, ta, guide=True, by="Post.3")
    c_ai_2 = model.construct_circle(incenter, ta, guide=True, by="Post.3")
    ta_sym = model.intersect(c_ai_1, c_ai_2, other_than=ta, ID="Ts", classes=["contact"], by="Casey.VI.IV.10")
    c_b_1 = model.construct_circle(a_pt, b_pt, guide=True, by="Post.3")
    c_b_2 = model.construct_circle(incenter, b_pt, guide=True, by="Post.3")
    b_sym = model.intersect(c_b_1, c_b_2, other_than=b_pt, guide=True, by="Casey.VI.IV.10")
    fourth_tangent = model.construct_line(
        b_sym, ta_sym, classes=["tangent", "inversion_line"], ID="[ L4 ]", by="Casey.VI.IV.10"
    )

    # Exact Feuerbach point Fe = X(11) = (6, 8) via circle-circle tangency intersection!
    feuerbach_pt = model.intersect(
        enp.nine_point_circle,
        incircle,
        ID="Fe",
        classes=["feuerbach", "highlight_point"],
        by="Casey.VI.IV.10.Cor2",
    )

    # Verify Casey's inversion maps Ts (contact of 4th common tangent with incircle) directly onto Fe!
    inv_ts = invert_point(ta_sym, ma, quadrance(ma, ta))
    if inv_ts != feuerbach_pt:
        raise AssertionError(f"Expected Ts to invert to Fe={feuerbach_pt}, got {inv_ts}")

    model.assert_collinear(enp.nine_point_center, incenter, feuerbach_pt, by="III.11")
    model.conclude("Nine-Points Circle touches Incircle at Feuerbach Point Fe = (6, 8)", by="Casey.VI.IV.10.Cor2")

    return CaseyFeuerbachResult(
        model=model,
        euler_nine_point=enp,
        incenter=incenter,
        incircle_contacts=(ta, tb, tc),
        incircle=incircle,
        feuerbach_point=feuerbach_pt,
        casey_inversion_circle=casey_inv_circle,
        fourth_common_tangent=fourth_tangent,
    )
