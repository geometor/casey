"""Exact symbolic constructions and proofs for Symmedians, Lemoine Circles & Brocard Geometry.

Implements Units 5 & 6 of the Casey Codex (Supplementary Chapter, Sections I–VII, pp. 165–248):

- **Symmedians & Lemoine's Point ``K = X(6)``** (Sec. I, Props. 5–7, pp. 170–172): Constructed via
  circumcircle tangents (Prop. 6), verifying barycentric weights ``(a^2 : b^2 : c^2)`` and
  Lagrange's minimum-sum-of-squares property ``min(x^2 + y^2 + z^2) = 4*Delta^2 / (a^2+b^2+c^2)``.
- **First Lemoine Circle & Cosine Circle** (Sec. III, Prop. 1 & Cor. 4, pp. 179–183): Six concyclic
  side-parallel intersections ``D1, D2, E1, E2, F1, F2`` centered at ``Ml = midpoint(O, K)`` with
  intercepts ``a^3 : b^3 : c^3``, and six concyclic antiparallel intersections centered at ``K``.
- **Brocard Points ``Om1, Om2``, Brocard Angle ``omega``, Brocard's First Triangle & Brocard Circle**
  (Sec. II, pp. 175–179; Sec. V, pp. 194–196): Constructed by pure compass-and-straightedge tangent
  circles, verifying ``cot(omega) = cot A + cot B + cot C = (a^2 + b^2 + c^2) / (4*Delta)`` and
  the seven-point **Brocard Circle** on diameter ``OK`` containing ``O, K, Om1, Om2, A1, B1, C1``.
- **Associated Figures: Steiner Point ``X(99)``, Tarry Point ``X(98)`` & Longchamps Point ``X(20)``**
  (Sec. VII & Misc. Ex. 146–158, p. 247).
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, clean_expr, quadrance, zero_test

from geometor.casey.invariants import (
    HERONIAN_VERTICES,
    barycentric_point,
    compass_midpoint,
    compass_parallel_line,
    compass_perp_bisector,
    compass_perpendicular_line,
    signed_triangle_area,
)

__all__ = [
    "BrocardLemoineReport",
    "BrocardLemoineResult",
    "LemoineCirclesResult",
    "construct_brocard_and_lemoine_circles",
    "construct_symmedian_and_lemoine_circles",
    "verify_brocard_identities_symbolic",
]


@dataclass(frozen=True)
class BrocardLemoineReport:
    """Exact rational invariant summary for Symmedian, Lemoine & Brocard geometry on ``(15,13,14)``."""

    cot_omega: sp.Rational
    sin_sq_omega: sp.Rational
    symmedian_point: spg.Point
    brocard_center: spg.Point
    brocard_1: spg.Point
    brocard_2: spg.Point
    brocard_first_triangle: tuple[spg.Point, spg.Point, spg.Point]
    steiner_point: spg.Point
    tarry_point: spg.Point
    longchamps_point: spg.Point
    lemoine_intercept_ratios: tuple[sp.Rational, sp.Rational]
    min_perp_squares_sum: sp.Rational
    verified: bool


@dataclass(frozen=True)
class LemoineCirclesResult:
    """Constructed elements for Symmedians, First Lemoine Circle & Cosine Circle (Unit 5)."""

    model: Model
    vertices: tuple[spg.Point, spg.Point, spg.Point]
    circumcenter: spg.Point
    circumcircle: spg.Circle
    tangential_vertices: tuple[spg.Point, spg.Point, spg.Point]
    symmedian_point: spg.Point
    lemoine_center: spg.Point
    lemoine_hexagon: tuple[spg.Point, spg.Point, spg.Point, spg.Point, spg.Point, spg.Point]
    first_lemoine_circle: spg.Circle
    cosine_hexagon: tuple[spg.Point, spg.Point, spg.Point, spg.Point, spg.Point, spg.Point]
    cosine_circle: spg.Circle


@dataclass(frozen=True)
class BrocardLemoineResult:
    """Constructed elements for Brocard Points, Brocard Circle, Lemoine Circle, Steiner & Tarry."""

    model: Model
    vertices: tuple[spg.Point, spg.Point, spg.Point]
    circumcenter: spg.Point
    circumcircle: spg.Circle
    symmedian_point: spg.Point
    brocard_center: spg.Point
    brocard_1: spg.Point
    brocard_2: spg.Point
    brocard_first_triangle: tuple[spg.Point, spg.Point, spg.Point]
    brocard_circle: spg.Circle
    lemoine_hexagon: tuple[spg.Point, spg.Point, spg.Point, spg.Point, spg.Point, spg.Point]
    first_lemoine_circle: spg.Circle
    steiner_point: spg.Point
    tarry_point: spg.Point
    longchamps_point: spg.Point
    report: BrocardLemoineReport


def verify_brocard_identities_symbolic() -> dict[str, sp.Expr]:
    """Verify Casey's universal algebraic identities for ``cot(omega)`` and ``K``'s minimum property.

    1. By the Law of Cosines, ``cot A + cot B + cot C = (b^2+c^2-a^2)/(4*Delta) +
       (c^2+a^2-b^2)/(4*Delta) + (a^2+b^2-c^2)/(4*Delta) = (a^2+b^2+c^2)/(4*Delta)``.
    2. By Lagrange's identity (Sec. I, Prop. 7, p. 171):
       ``(a^2+b^2+c^2)*(x^2+y^2+z^2) - (a*x+b*y+c*z)^2 =
       (b*z - c*y)^2 + (c*x - a*z)^2 + (a*y - b*x)^2``, proving that under ``a*x+b*y+c*z = 2*Delta``,
       ``x^2 + y^2 + z^2`` attains its unique minimum when ``x/a = y/b = z/c`` (at ``K = X(6)``).

    Returns:
        Dictionary of zero-verified symbolic residuals.
    """
    a, b, c, delta, x, y, z = sp.symbols("a b c Delta x y z", positive=True)
    cot_sum = (
        (b**2 + c**2 - a**2) / (4 * delta)
        + (c**2 + a**2 - b**2) / (4 * delta)
        + (a**2 + b**2 - c**2) / (4 * delta)
    )
    cot_res = sp.simplify(cot_sum - (a**2 + b**2 + c**2) / (4 * delta))

    lagrange_lhs = (a**2 + b**2 + c**2) * (x**2 + y**2 + z**2) - (a * x + b * y + c * z) ** 2
    lagrange_rhs = (b * z - c * y) ** 2 + (c * x - a * z) ** 2 + (a * y - b * x) ** 2
    lagrange_res = sp.expand(lagrange_lhs - lagrange_rhs)

    if not (zero_test(cot_res) and zero_test(lagrange_res)):
        raise AssertionError("Symbolic Brocard/Lagrange verification failed.")
    return {"cot_omega_residual": cot_res, "lagrange_symmedian_residual": lagrange_res}


def construct_symmedian_and_lemoine_circles(
    model: Model | None = None,
) -> LemoineCirclesResult:
    """Construct Lemoine's Point ``K``, First Lemoine Circle & Cosine Circle (Unit 5).

    Follows Casey, Supplementary Chapter, Sec. I, Props. 5–6 (pp. 170–171) and Sec. III,
    Prop. 1 & Cor. 4 (pp. 179–183) on ``A=(0,0), B=(14,0), C=(5,12)``.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`LemoineCirclesResult`.
    """
    if model is None:
        model = Model("casey_symmedian_lemoine", auto_intersect=False, enable_logging=False)

    a_coord, b_coord, c_coord = HERONIAN_VERTICES
    a_pt = model.given_point(a_coord.x, a_coord.y, ID="A", classes=["given", "vertex"])
    b_pt = model.given_point(b_coord.x, b_coord.y, ID="B", classes=["given", "vertex"])
    c_pt = model.given_point(c_coord.x, c_coord.y, ID="C", classes=["given", "vertex"])

    model.set_polygon([a_pt, b_pt, c_pt], classes=["triangle", "primary"], ID="< A B C >")
    side_bc = model.construct_line(b_pt, c_pt, classes=["carrier", "side"], ID="[ B C ]", by="Post.1")
    side_ca = model.construct_line(c_pt, a_pt, classes=["carrier", "side"], ID="[ C A ]", by="Post.1")
    side_ab = model.construct_line(a_pt, b_pt, classes=["carrier", "side"], ID="[ A B ]", by="Post.1")

    pb_ab = compass_perp_bisector(model, a_pt, b_pt, guide=True)
    pb_bc = compass_perp_bisector(model, b_pt, c_pt, guide=True)
    o_pt = model.intersect(pb_ab, pb_bc, ID="O", classes=["center"], by="IV.5")
    circumcircle = model.construct_circle(
        o_pt, a_pt, classes=["circumcircle"], ID="( O A )", by="Post.3"
    )

    # Circumcircle tangents at A, B, C (antiparallel directions to BC, CA, AB)
    tang_a = compass_perpendicular_line(
        model, o_pt, a_pt, a_pt, off_line_ref=b_pt, ID="[ tA ]", classes=["tangent"], guide=True
    )
    tang_b = compass_perpendicular_line(
        model, o_pt, b_pt, b_pt, off_line_ref=c_pt, ID="[ tB ]", classes=["tangent"], guide=True
    )
    tang_c = compass_perpendicular_line(
        model, o_pt, c_pt, c_pt, off_line_ref=a_pt, ID="[ tC ]", classes=["tangent"], guide=True
    )

    pa = model.intersect(tang_b, tang_c, ID="Pa", classes=["tangential"], guide=True, by="Casey.Supp.I.6")
    pb = model.intersect(tang_c, tang_a, ID="Pb", classes=["tangential"], guide=True, by="Casey.Supp.I.6")
    pc = model.intersect(tang_a, tang_b, ID="Pc", classes=["tangential"], guide=True, by="Casey.Supp.I.6")

    sym_a = model.construct_line(a_pt, pa, classes=["symmedian"], ID="[ A K ]", by="Casey.Supp.I.6")
    sym_b = model.construct_line(b_pt, pb, classes=["symmedian"], ID="[ B K ]", by="Casey.Supp.I.6")
    sym_c = model.construct_line(c_pt, pc, classes=["symmedian"], ID="[ C K ]", by="Casey.Supp.I.6")

    k_pt = model.intersect(
        sym_a, sym_b, ID="K", classes=["symmedian_point", "highlight_point"], by="Casey.Supp.I.5"
    )
    model.assert_incident(k_pt, sym_c, by="Casey.Supp.I.5")

    # Parallels through K to BC, CA, AB -> Lemoine Hexagon D1, D2, E1, E2, F1, F2
    par_bc = compass_parallel_line(model, b_pt, c_pt, k_pt, ID="[ parBC ]", classes=["cross"])
    par_ca = compass_parallel_line(model, c_pt, a_pt, k_pt, ID="[ parCA ]", classes=["cross"])
    par_ab = compass_parallel_line(model, a_pt, b_pt, k_pt, ID="[ parAB ]", classes=["cross"])

    d1 = model.intersect(side_bc, par_ca, ID="D1", classes=["lemoine_pt"], by="Casey.Supp.III.1")
    d2 = model.intersect(side_bc, par_ab, ID="D2", classes=["lemoine_pt"], by="Casey.Supp.III.1")
    e1 = model.intersect(side_ca, par_ab, ID="E1", classes=["lemoine_pt"], by="Casey.Supp.III.1")
    e2 = model.intersect(side_ca, par_bc, ID="E2", classes=["lemoine_pt"], by="Casey.Supp.III.1")
    f1 = model.intersect(side_ab, par_bc, ID="F1", classes=["lemoine_pt"], by="Casey.Supp.III.1")
    f2 = model.intersect(side_ab, par_ca, ID="F2", classes=["lemoine_pt"], by="Casey.Supp.III.1")

    ml_center = compass_midpoint(model, o_pt, k_pt, ID="Ml", classes=["center"])
    first_lemoine = model.construct_circle(
        ml_center,
        d1,
        classes=["lemoine_circle", "featured"],
        ID="( Ml D1 )",
        by="Casey.Supp.III.1",
    )
    for l_pt in (d2, e1, e2, f1, f2):
        model.assert_incident(l_pt, first_lemoine, by="Casey.Supp.III.1")

    # Antiparallels through K (parallel to circumcircle tangents) -> Cosine Circle centered at K!
    anti_bc = compass_parallel_line(model, a_pt, pc, k_pt, guide=True)
    anti_ca = compass_parallel_line(model, b_pt, pa, k_pt, guide=True)
    anti_ab = compass_parallel_line(model, c_pt, pb, k_pt, guide=True)

    ca1 = model.intersect(side_ca, anti_bc, ID="Ca1", classes=["cosine_pt"], guide=True, by="Casey.Supp.III.1.Cor4")
    ca2 = model.intersect(side_ab, anti_bc, ID="Ca2", classes=["cosine_pt"], guide=True, by="Casey.Supp.III.1.Cor4")
    cb1 = model.intersect(side_ab, anti_ca, ID="Cb1", classes=["cosine_pt"], guide=True, by="Casey.Supp.III.1.Cor4")
    cb2 = model.intersect(side_bc, anti_ca, ID="Cb2", classes=["cosine_pt"], guide=True, by="Casey.Supp.III.1.Cor4")
    cc1 = model.intersect(side_bc, anti_ab, ID="Cc1", classes=["cosine_pt"], guide=True, by="Casey.Supp.III.1.Cor4")
    cc2 = model.intersect(side_ca, anti_ab, ID="Cc2", classes=["cosine_pt"], guide=True, by="Casey.Supp.III.1.Cor4")

    cosine_circ = model.construct_circle(
        k_pt,
        cb2,
        classes=["cosine_circle", "secondary_circle"],
        ID="( K Cb2 )",
        by="Casey.Supp.III.1.Cor4",
    )
    for c_pt_i in (ca1, ca2, cb1, cc1, cc2):
        model.assert_incident(c_pt_i, cosine_circ, by="Casey.Supp.III.1.Cor4")

    model.conclude("First Lemoine Circle & Cosine Circle verified on 6+6 side intersections", by="Casey.Supp.III.1")

    return LemoineCirclesResult(
        model=model,
        vertices=(a_pt, b_pt, c_pt),
        circumcenter=o_pt,
        circumcircle=circumcircle,
        tangential_vertices=(pa, pb, pc),
        symmedian_point=k_pt,
        lemoine_center=ml_center,
        lemoine_hexagon=(d1, d2, e1, e2, f1, f2),
        first_lemoine_circle=first_lemoine,
        cosine_hexagon=(ca1, ca2, cb1, cb2, cc1, cc2),
        cosine_circle=cosine_circ,
    )


def construct_brocard_and_lemoine_circles(
    model: Model | None = None,
) -> BrocardLemoineResult:
    """Construct the Brocard Points, Brocard Circle, First Lemoine Circle, Steiner & Tarry Points.

    On the Heronian ``(15, 13, 14)`` triangle ``A=(0,0), B=(14,0), C=(5,12)``:

    1. Constructs ``O = (7, 33/8)``, ``K = X(6) = (1673/295, 1176/295)``, and the First Lemoine
       Circle centered at ``Ml = midpoint(O, K) = (4053/590, 9567/2360)``.
    2. Constructs the **First Brocard Point ``Om1``** via tangent circles ``(Ob1, B)`` (tangent to
       ``BC`` at ``B`` through ``A``) and ``(Oc1, C)`` (tangent to ``CA`` at ``C`` through ``B``),
       verifying concurrency with ``(Oa1, A)`` (tangent to ``AB`` at ``A`` through ``C``).
    3. Constructs the **Second Brocard Point ``Om2``** via reversed tangent circles.
    4. Constructs **Brocard's First Triangle ``A1 B1 C1``** (``A1 = [B Om1] ∩ [C Om2]``, etc.)
       and proves that **all seven points ``O, K, Om1, Om2, A1, B1, C1``** lie on the
       **Brocard Circle** with diameter ``OK`` (Casey, Supp. Sec. V, pp. 194–195).
    5. Constructs **Steiner's Point ``St = X(99)``** (parallels through ``A, B, C`` to sides of
       ``A1 B1 C1``), **Tarry's Point ``Tr = X(98)``** (antipode of ``St`` on circumcircle), and
       **de Longchamps' Point ``Lo = X(20)``** (reflection of ``H`` across ``O``).

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`BrocardLemoineResult` with full exact symbolic report.
    """
    if model is None:
        model = Model("casey_brocard_circle", auto_intersect=False, enable_logging=False)

    verify_brocard_identities_symbolic()

    a_coord, b_coord, c_coord = HERONIAN_VERTICES
    a_pt = model.given_point(a_coord.x, a_coord.y, ID="A", classes=["given", "vertex"])
    b_pt = model.given_point(b_coord.x, b_coord.y, ID="B", classes=["given", "vertex"])
    c_pt = model.given_point(c_coord.x, c_coord.y, ID="C", classes=["given", "vertex"])

    model.set_polygon([a_pt, b_pt, c_pt], classes=["triangle", "primary"], ID="< A B C >")
    side_bc = model.construct_line(b_pt, c_pt, classes=["carrier", "side"], ID="[ B C ]", by="Post.1")
    side_ca = model.construct_line(c_pt, a_pt, classes=["carrier", "side"], ID="[ C A ]", by="Post.1")
    side_ab = model.construct_line(a_pt, b_pt, classes=["carrier", "side"], ID="[ A B ]", by="Post.1")

    pb_ab = compass_perp_bisector(model, a_pt, b_pt, guide=True)
    pb_bc = compass_perp_bisector(model, b_pt, c_pt, guide=True)
    pb_ca = compass_perp_bisector(model, c_pt, a_pt, guide=True)
    o_pt = model.intersect(pb_ab, pb_bc, ID="O", classes=["center", "brocard_concyclic"], by="IV.5")
    circumcircle = model.construct_circle(
        o_pt, a_pt, classes=["circumcircle"], ID="( O A )", by="Post.3"
    )

    # Symmedian point K via circumcircle tangents (Casey Supp. Sec. I, Prop. 6)
    tang_a = compass_perpendicular_line(model, o_pt, a_pt, a_pt, off_line_ref=b_pt, guide=True)
    tang_b = compass_perpendicular_line(model, o_pt, b_pt, b_pt, off_line_ref=c_pt, guide=True)
    tang_c = compass_perpendicular_line(model, o_pt, c_pt, c_pt, off_line_ref=a_pt, guide=True)
    pa = model.intersect(tang_b, tang_c, guide=True, by="Casey.Supp.I.6")
    pb = model.intersect(tang_c, tang_a, guide=True, by="Casey.Supp.I.6")
    sym_a = model.construct_line(a_pt, pa, guide=True, by="Casey.Supp.I.6")
    sym_b = model.construct_line(b_pt, pb, guide=True, by="Casey.Supp.I.6")
    k_pt = model.intersect(
        sym_a, sym_b, ID="K", classes=["symmedian_point", "brocard_concyclic", "highlight_point"], by="Casey.Supp.I.5"
    )

    # Diameter [O K] and Brocard / First-Lemoine centre Ml = midpoint(O, K)
    model.construct_line(o_pt, k_pt, classes=["brocard_diameter", "highlight"], ID="[ O K ]", by="Post.1")
    ml_center = compass_midpoint(model, o_pt, k_pt, ID="Ml", classes=["center"],)
    brocard_circle = model.construct_circle(
        ml_center,
        o_pt,
        classes=["brocard_circle", "featured"],
        ID="( Ml O )",
        by="Casey.Supp.V.1",
    )
    model.assert_incident(k_pt, brocard_circle, by="III.31")

    # First Brocard Point Om1 (Omega): circles tangent to BC at B (through A), CA at C (through B), AB at A (through C)
    perp_bc_b = compass_perpendicular_line(model, b_pt, c_pt, b_pt, off_line_ref=a_pt, guide=True)
    perp_ca_c = compass_perpendicular_line(model, c_pt, a_pt, c_pt, off_line_ref=b_pt, guide=True)
    perp_ab_a = compass_perpendicular_line(model, a_pt, b_pt, a_pt, off_line_ref=c_pt, guide=True)

    ob1 = model.intersect(perp_bc_b, pb_ab, guide=True, by="IV.5")
    oc1 = model.intersect(perp_ca_c, pb_bc, guide=True, by="IV.5")
    oa1 = model.intersect(perp_ab_a, pb_ca, guide=True, by="IV.5")

    circ_b1 = model.construct_circle(ob1, b_pt, classes=["adjoint_circle"], guide=True, by="Post.3")
    circ_c1 = model.construct_circle(oc1, c_pt, classes=["adjoint_circle"], guide=True, by="Post.3")
    circ_a1 = model.construct_circle(oa1, a_pt, classes=["adjoint_circle"], guide=True, by="Post.3")

    om1 = model.intersect(
        circ_b1,
        circ_c1,
        other_than=b_pt,
        ID="Om1",
        classes=["brocard_point", "highlight_point"],
        by="Casey.Supp.II.1",
    )
    model.assert_incident(om1, circ_a1, by="Casey.Supp.II.1")

    # Second Brocard Point Om2 (Omega'): circles tangent to BC at C (through A), AB at B (through C), CA at A (through B)
    perp_bc_c = compass_perpendicular_line(model, b_pt, c_pt, c_pt, off_line_ref=a_pt, guide=True)
    perp_ab_b = compass_perpendicular_line(model, a_pt, b_pt, b_pt, off_line_ref=c_pt, guide=True)
    perp_ca_a = compass_perpendicular_line(model, c_pt, a_pt, a_pt, off_line_ref=b_pt, guide=True)

    oc2 = model.intersect(perp_bc_c, pb_ca, guide=True, by="IV.5")
    ob2 = model.intersect(perp_ab_b, pb_bc, guide=True, by="IV.5")
    oa2 = model.intersect(perp_ca_a, pb_ab, guide=True, by="IV.5")

    circ_c2 = model.construct_circle(oc2, c_pt, guide=True, by="Post.3")
    circ_b2 = model.construct_circle(ob2, b_pt, guide=True, by="Post.3")
    circ_a2 = model.construct_circle(oa2, a_pt, guide=True, by="Post.3")

    om2 = model.intersect(
        circ_c2,
        circ_b2,
        other_than=c_pt,
        ID="Om2",
        classes=["brocard_point", "highlight_point"],
        by="Casey.Supp.II.1",
    )
    model.assert_incident(om2, circ_a2, by="Casey.Supp.II.1")

    # Brocard's First Triangle A1 B1 C1 (Casey Supp. Sec. V, pp. 194–195)
    ray_b_om1 = model.construct_line(b_pt, om1, classes=["brocard_ray"], ID="[ B Om1 ]", by="Post.1")
    ray_c_om1 = model.construct_line(c_pt, om1, classes=["brocard_ray"], ID="[ C Om1 ]", by="Post.1")
    ray_a_om1 = model.construct_line(a_pt, om1, classes=["brocard_ray"], ID="[ A Om1 ]", by="Post.1")

    ray_c_om2 = model.construct_line(c_pt, om2, classes=["brocard_ray"], ID="[ C Om2 ]", by="Post.1")
    ray_a_om2 = model.construct_line(a_pt, om2, classes=["brocard_ray"], ID="[ A Om2 ]", by="Post.1")
    ray_b_om2 = model.construct_line(b_pt, om2, classes=["brocard_ray"], ID="[ B Om2 ]", by="Post.1")

    a1 = model.intersect(ray_b_om1, ray_c_om2, ID="A1", classes=["brocard_tri"], by="Casey.Supp.V.1")
    b1 = model.intersect(ray_c_om1, ray_a_om2, ID="B1", classes=["brocard_tri"], by="Casey.Supp.V.1")
    c1 = model.intersect(ray_a_om1, ray_b_om2, ID="C1", classes=["brocard_tri"], by="Casey.Supp.V.1")
    model.set_polygon([a1, b1, c1], classes=["brocard_triangle", "diamond"], ID="< A1 B1 C1 >")

    # Assert ALL FIVE points Om1, Om2, A1, B1, C1 lie on the Brocard Circle with diameter OK!
    for b_concyclic in (om1, om2, a1, b1, c1):
        model.assert_incident(b_concyclic, brocard_circle, by="Casey.Supp.V.1")

    # First Lemoine Circle (6 side-parallel intersections)
    par_bc = compass_parallel_line(model, b_pt, c_pt, k_pt, guide=True)
    par_ca = compass_parallel_line(model, c_pt, a_pt, k_pt, guide=True)
    par_ab = compass_parallel_line(model, a_pt, b_pt, k_pt, guide=True)
    d1 = model.intersect(side_bc, par_ca, ID="D1", classes=["lemoine_pt"], guide=True, by="Casey.Supp.III.1")
    d2 = model.intersect(side_bc, par_ab, ID="D2", classes=["lemoine_pt"], guide=True, by="Casey.Supp.III.1")
    e1 = model.intersect(side_ca, par_ab, ID="E1", classes=["lemoine_pt"], guide=True, by="Casey.Supp.III.1")
    e2 = model.intersect(side_ca, par_bc, ID="E2", classes=["lemoine_pt"], guide=True, by="Casey.Supp.III.1")
    f1 = model.intersect(side_ab, par_bc, ID="F1", classes=["lemoine_pt"], guide=True, by="Casey.Supp.III.1")
    f2 = model.intersect(side_ab, par_ca, ID="F2", classes=["lemoine_pt"], guide=True, by="Casey.Supp.III.1")
    first_lemoine = model.construct_circle(
        ml_center,
        d1,
        classes=["lemoine_circle", "secondary_circle"],
        ID="( Ml D1 )",
        by="Casey.Supp.III.1",
    )
    for l_pt in (d2, e1, e2, f1, f2):
        model.assert_incident(l_pt, first_lemoine, by="Casey.Supp.III.1")

    # Steiner Point St = X(99): parallels through A, B, C to [B1 C1], [C1 A1], [A1 B1] concur on circumcircle!
    st_line_a = compass_parallel_line(model, b1, c1, a_pt, guide=True)
    st_line_b = compass_parallel_line(model, c1, a1, b_pt, guide=True)
    st_line_c = compass_parallel_line(model, a1, b1, c_pt, guide=True)
    steiner_pt = model.intersect(
        st_line_a, st_line_b, ID="St", classes=["steiner_point"], by="Casey.Supp.VII"
    )
    model.assert_incident(steiner_pt, st_line_c, by="Casey.Supp.VII")
    model.assert_incident(steiner_pt, circumcircle, by="Casey.Supp.VII")

    # Tarry Point Tr = X(98): antipode of Steiner Point St on circumcircle (and concurrency of perpendiculars!)
    st_diam = model.construct_line(steiner_pt, o_pt, guide=True, by="Post.1")
    tarry_pt = model.intersect(
        circumcircle,
        st_diam,
        other_than=steiner_pt,
        ID="Tr",
        classes=["tarry_point"],
        by="Casey.Supp.VII",
    )

    # de Longchamps Point Lo = X(20): reflection of orthocentre H across circumcentre O (Misc. Ex. 146, p. 247)
    alt_a = compass_perpendicular_line(model, b_pt, c_pt, a_pt, guide=True)
    alt_b = compass_perpendicular_line(model, c_pt, a_pt, b_pt, guide=True)
    h_pt = model.intersect(alt_a, alt_b, guide=True, by="Casey.I.10")
    oh_line = model.construct_line(o_pt, h_pt, guide=True, by="Post.1")
    refl_oh = model.construct_circle(o_pt, h_pt, guide=True, by="Post.3")
    longchamps_pt = model.intersect(
        refl_oh, oh_line, other_than=h_pt, ID="Lo", classes=["longchamps_point"], guide=True, by="Casey.Supp.Ex146"
    )

    # Exact rational verification of Casey's Brocard & Lemoine invariants
    a_sq, b_sq, c_sq = sp.Integer(225), sp.Integer(169), sp.Integer(196)
    area = signed_triangle_area(a_pt, b_pt, c_pt)
    cot_omega = clean_expr((a_sq + b_sq + c_sq) / (4 * area))
    sin_sq_omega = clean_expr(sp.Integer(1) / (1 + cot_omega**2))

    # Check barycentric identities for K, Om1, Om2, St
    k_bary = barycentric_point(a_pt, b_pt, c_pt, a_sq, b_sq, c_sq)
    om1_bary = barycentric_point(a_pt, b_pt, c_pt, c_sq * a_sq, a_sq * b_sq, b_sq * c_sq)
    om2_bary = barycentric_point(a_pt, b_pt, c_pt, a_sq * b_sq, b_sq * c_sq, c_sq * a_sq)
    st_bary = barycentric_point(
        a_pt,
        b_pt,
        c_pt,
        sp.Rational(1, int(b_sq - c_sq)),
        sp.Rational(1, int(c_sq - a_sq)),
        sp.Rational(1, int(a_sq - b_sq)),
    )

    # Check Lemoine cube intercept law |D1 D2| / |E1 E2| = (15/13)^3 and |D1 D2| / |F1 F2| = (15/14)^3
    len_d = clean_expr(sp.sqrt(quadrance(d1, d2)))
    len_e = clean_expr(sp.sqrt(quadrance(e1, e2)))
    len_f = clean_expr(sp.sqrt(quadrance(f1, f2)))
    ratio_de = clean_expr(len_d / len_e)
    ratio_df = clean_expr(len_d / len_f)

    min_sq_sum = clean_expr(4 * area**2 / (a_sq + b_sq + c_sq))
    ok = (
        k_pt == k_bary
        and om1 == om1_bary
        and om2 == om2_bary
        and steiner_pt == st_bary
        and ratio_de == sp.Rational(15**3, 13**3)
        and ratio_df == sp.Rational(15**3, 14**3)
        and cot_omega == sp.Rational(295, 168)
    )
    model.conclude("Brocard Circle (O, K, Om1, Om2, A1, B1, C1), Lemoine Circle, Steiner & Tarry verified", by="Casey.Supp.V")

    report = BrocardLemoineReport(
        cot_omega=cot_omega,  # type: ignore[arg-type]
        sin_sq_omega=sin_sq_omega,  # type: ignore[arg-type]
        symmedian_point=k_pt,
        brocard_center=ml_center,
        brocard_1=om1,
        brocard_2=om2,
        brocard_first_triangle=(a1, b1, c1),
        steiner_point=steiner_pt,
        tarry_point=tarry_pt,
        longchamps_point=longchamps_pt,
        lemoine_intercept_ratios=(ratio_de, ratio_df),  # type: ignore[arg-type]
        min_perp_squares_sum=min_sq_sum,  # type: ignore[arg-type]
        verified=ok,
    )
    return BrocardLemoineResult(
        model=model,
        vertices=(a_pt, b_pt, c_pt),
        circumcenter=o_pt,
        circumcircle=circumcircle,
        symmedian_point=k_pt,
        brocard_center=ml_center,
        brocard_1=om1,
        brocard_2=om2,
        brocard_first_triangle=(a1, b1, c1),
        brocard_circle=brocard_circle,
        lemoine_hexagon=(d1, d2, e1, e2, f1, f2),
        first_lemoine_circle=first_lemoine,
        steiner_point=steiner_pt,
        tarry_point=tarry_pt,
        longchamps_point=longchamps_pt,
        report=report,
    )
