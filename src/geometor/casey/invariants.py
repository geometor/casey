"""Exact symbolic circle, inversion, polar, and Euclidean helper invariants for Casey's *Sequel*.

All algebraic predicates and compass-and-straightedge sub-constructions operate strictly over
exact SymPy expressions (:class:`sympy.Rational`, :class:`sympy.Integer`, and closed-form
radicals) without floating-point approximations.
"""

from __future__ import annotations

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    clean_expr,
    cross_ratio,
    is_harmonic,
    line_spread,
    proposition,
    quadrance,
    zero_test,
)

__all__ = [
    "HERONIAN_VERTICES",
    "are_orthogonal_circles",
    "barycentric_point",
    "bitangent_length",
    "bitangent_quadrance",
    "circle_power",
    "compass_midpoint",
    "compass_parallel_line",
    "compass_perp_bisector",
    "compass_perpendicular_line",
    "cross_ratio",
    "invert_point",
    "is_harmonic",
    "line_spread",
    "polar_line",
    "pole_of_line",
    "quadrance",
    "radical_axis_line",
    "signed_triangle_area",
]

HERONIAN_VERTICES: tuple[spg.Point, spg.Point, spg.Point] = (
    spg.Point(0, 0),
    spg.Point(14, 0),
    spg.Point(5, 12),
)
"""Canonical Heronian ``(15, 13, 14)`` scalene triangle ``A=(0,0), B=(14,0), C=(5,12)``."""


def signed_triangle_area(a_pt: spg.Point, b_pt: spg.Point, c_pt: spg.Point) -> sp.Expr:
    """Compute the exact signed area of oriented triangle ``ABC``.

    Args:
        a_pt: First vertex ``A``.
        b_pt: Second vertex ``B``.
        c_pt: Third vertex ``C``.

    Returns:
        Exact symbolic signed area ``((B.x - A.x)*(C.y - A.y) - (B.y - A.y)*(C.x - A.x)) / 2``.
    """
    det = (b_pt.x - a_pt.x) * (c_pt.y - a_pt.y) - (b_pt.y - a_pt.y) * (c_pt.x - a_pt.x)
    return clean_expr(sp.Rational(1, 2) * det)


def circle_power(pt: spg.Point, circ: spg.Circle) -> sp.Expr:
    """Compute the exact power ``|PO|^2 - r^2`` of point ``pt`` with respect to ``circ``.

    Corresponds to Casey, Book III, Props. 20–24 (pp. 41–44): for exterior points,
    equals the square of the tangent from ``pt`` to ``circ``.

    Args:
        pt: Query point ``P``.
        circ: Reference circle ``(O, r)``.

    Returns:
        Exact symbolic expression ``(P.x - O.x)^2 + (P.y - O.y)^2 - r^2``.
    """
    return clean_expr(quadrance(pt, circ.center) - circ.radius**2)


def are_orthogonal_circles(c1: spg.Circle, c2: spg.Circle) -> bool:
    """Return ``True`` iff circles ``c1`` and ``c2`` cut orthogonally (Casey Book III, Prop. 22).

    Two circles cut orthogonally iff the square of the distance between their centres
    equals the sum of the squares of their radii: ``|O1 O2|^2 = r1^2 + r2^2``.

    Args:
        c1: First circle ``(O1, r1)``.
        c2: Second circle ``(O2, r2)``.

    Returns:
        ``True`` if ``|O1 O2|^2 - r1^2 - r2^2 == 0`` symbolically.
    """
    diff = quadrance(c1.center, c2.center) - c1.radius**2 - c2.radius**2
    return zero_test(diff)


def bitangent_quadrance(
    c1: spg.Circle | spg.Point,
    c2: spg.Circle | spg.Point,
    *,
    internal: bool = False,
) -> sp.Expr:
    """Compute the exact squared common-tangent length ``t_12^2`` between circles or null-circles.

    In Casey's Generalized Ptolemy Theorem (Book VI, Sec. IV, Prop. 10, pp. 103–104), a point
    is treated as a circle of radius ``0``. For two circles soaked in the same sense (external
    common tangent), ``t_12^2 = |O1 O2|^2 - (r1 - r2)^2``; for transverse (internal) contact,
    ``t_12^2 = |O1 O2|^2 - (r1 + r2)^2``.

    Args:
        c1: First :class:`sympy.geometry.Circle` or null-circle :class:`sympy.geometry.Point`.
        c2: Second :class:`sympy.geometry.Circle` or null-circle :class:`sympy.geometry.Point`.
        internal: If ``True``, use ``(r1 + r2)^2`` (internal bitangent); otherwise ``(r1 - r2)^2``.

    Returns:
        Exact symbolic squared bitangent length.
    """
    o1 = c1 if isinstance(c1, spg.Point) else c1.center
    r1 = sp.Integer(0) if isinstance(c1, spg.Point) else c1.radius
    o2 = c2 if isinstance(c2, spg.Point) else c2.center
    r2 = sp.Integer(0) if isinstance(c2, spg.Point) else c2.radius
    rad_term = (r1 + r2) ** 2 if internal else (r1 - r2) ** 2
    return clean_expr(quadrance(o1, o2) - rad_term)


def bitangent_length(
    c1: spg.Circle | spg.Point,
    c2: spg.Circle | spg.Point,
    *,
    internal: bool = False,
) -> sp.Expr:
    """Compute the exact common-tangent length ``t_12`` between two circles or points.

    Args:
        c1: First circle or null-circle point.
        c2: Second circle or null-circle point.
        internal: If ``True``, return the internal common-tangent length; else external.

    Returns:
        Exact symbolic principal square root ``sqrt(bitangent_quadrance(c1, c2))``.
    """
    return clean_expr(sp.sqrt(bitangent_quadrance(c1, c2, internal=internal)))


def invert_point(pt: spg.Point, center: spg.Point, radius_sq: sp.Expr) -> spg.Point:
    """Compute the exact circular inverse of ``pt`` with respect to ``(center, sqrt(radius_sq))``.

    Implements Casey, Book III, Def. (p. 41) & Book VI, Sec. IV, Def. (p. 95):
    collinear with ``center`` and ``pt`` on the same ray such that ``|O P| * |O P'| = k^2``.

    Args:
        pt: Point ``P`` distinct from ``center``.
        center: Centre of inversion ``O``.
        radius_sq: Square ``k^2`` of the radius of inversion.

    Returns:
        Exact inverted :class:`sympy.geometry.Point` ``P'``.

    Raises:
        ValueError: If ``pt`` coincides with ``center``.
    """
    q_op = quadrance(center, pt)
    if zero_test(q_op):
        raise ValueError("Centre of inversion has no finite inverse point.")
    scale = sp.sympify(radius_sq) / q_op
    return spg.Point(
        clean_expr(center.x + scale * (pt.x - center.x)),
        clean_expr(center.y + scale * (pt.y - center.y)),
    )


def polar_line(pt: spg.Point, circ: spg.Circle) -> spg.Line:
    """Compute the exact polar line of ``pt`` with respect to ``circ`` (Casey Book III, Def. p. 44).

    By Casey's definition, the polar of ``P`` with respect to ``(O, r)`` is the perpendicular
    to ray ``OP`` erected at the inverse point ``P'`` of ``P``. Note that ``sympy.geometry.Circle``
    natively lacks ``polar_line`` and ``pole_of_line`` methods.

    Args:
        pt: Pole ``P`` distinct from ``circ.center``.
        circ: Reference circle ``(O, r)``.

    Returns:
        Exact :class:`sympy.geometry.Line` representing ``polar(P)``.

    Raises:
        ValueError: If ``pt`` coincides with ``circ.center``.
    """
    inv_pt = invert_point(pt, circ.center, circ.radius**2)
    dx = pt.x - circ.center.x
    dy = pt.y - circ.center.y
    second_pt = spg.Point(clean_expr(inv_pt.x - dy), clean_expr(inv_pt.y + dx))
    return spg.Line(inv_pt, second_pt)


def pole_of_line(line: spg.Line, circ: spg.Circle) -> spg.Point:
    """Compute the exact pole of ``line`` with respect to ``circ`` (Casey Book III, Def. p. 44).

    Constructed algebraically as the circular inverse of the orthogonal foot of ``circ.center``
    upon ``line``.

    Args:
        line: Non-diametral :class:`sympy.geometry.Line`.
        circ: Reference circle ``(O, r)``.

    Returns:
        Exact :class:`sympy.geometry.Point` whose polar with respect to ``circ`` is ``line``.

    Raises:
        ValueError: If ``line`` passes through ``circ.center`` (pole is at infinity).
    """
    a_coeff, b_coeff, c_coeff = line.coefficients
    h_val, k_val = circ.center.x, circ.center.y
    s_val = clean_expr(a_coeff * h_val + b_coeff * k_val + c_coeff)
    if zero_test(s_val):
        raise ValueError("A diameter of the circle has its pole at infinity.")
    n2 = a_coeff**2 + b_coeff**2
    foot = spg.Point(
        clean_expr(h_val - a_coeff * s_val / n2),
        clean_expr(k_val - b_coeff * s_val / n2),
    )
    return invert_point(foot, circ.center, circ.radius**2)


def radical_axis_line(c1: spg.Circle, c2: spg.Circle) -> spg.Line:
    """Compute the exact radical axis of two non-concentric circles (Casey Book III, Prop. 23).

    Args:
        c1: First circle ``(O1, r1)``.
        c2: Second circle ``(O2, r2)``.

    Returns:
        Exact :class:`sympy.geometry.Line` locus of equal circle powers.

    Raises:
        ValueError: If ``c1`` and ``c2`` are concentric.
    """
    h1, k1, r1 = c1.center.x, c1.center.y, c1.radius
    h2, k2, r2 = c2.center.x, c2.center.y, c2.radius
    dx = clean_expr(h2 - h1)
    dy = clean_expr(k2 - k1)
    if zero_test(dx**2 + dy**2):
        raise ValueError("Concentric circles have no finite radical axis.")
    # 2*(h2 - h1)*x + 2*(k2 - k1)*y + (h1^2 + k1^2 - r1^2 - (h2^2 + k2^2 - r2^2)) = 0
    a_val = 2 * dx
    b_val = 2 * dy
    c_val = clean_expr((h1**2 + k1**2 - r1**2) - (h2**2 + k2**2 - r2**2))
    if not zero_test(b_val):
        p1 = spg.Point(sp.Integer(0), clean_expr(-c_val / b_val))
        p2 = spg.Point(sp.Integer(1), clean_expr(-(a_val + c_val) / b_val))
    else:
        x0 = clean_expr(-c_val / a_val)
        p1 = spg.Point(x0, sp.Integer(0))
        p2 = spg.Point(x0, sp.Integer(1))
    return spg.Line(p1, p2)


def barycentric_point(
    a_pt: spg.Point,
    b_pt: spg.Point,
    c_pt: spg.Point,
    w_a: sp.Expr,
    w_b: sp.Expr,
    w_c: sp.Expr,
) -> spg.Point:
    """Compute the exact homogeneous barycentric point ``(w_a : w_b : w_c)`` on ``ABC``.

    Implements Casey's Centre of Mean Position (Book I, Props. 17–18, pp. 12–13) and
    symmedian/Brocard weights (Supplementary Chapter, Secs. I–II).

    Args:
        a_pt: First vertex ``A``.
        b_pt: Second vertex ``B``.
        c_pt: Third vertex ``C``.
        w_a: Weight attached to ``A``.
        w_b: Weight attached to ``B``.
        w_c: Weight attached to ``C``.

    Returns:
        Exact :class:`sympy.geometry.Point` ``(w_a*A + w_b*B + w_c*C) / (w_a + w_b + w_c)``.

    Raises:
        ValueError: If ``w_a + w_b + w_c == 0``.
    """
    total = clean_expr(sp.sympify(w_a) + sp.sympify(w_b) + sp.sympify(w_c))
    if zero_test(total):
        raise ValueError("Homogeneous barycentric weights sum to zero (point at infinity).")
    x_val = clean_expr((w_a * a_pt.x + w_b * b_pt.x + w_c * c_pt.x) / total)
    y_val = clean_expr((w_a * a_pt.y + w_b * b_pt.y + w_c * c_pt.y) / total)
    return spg.Point(x_val, y_val)


@proposition("I.10.bisector", kind="problem", title="Perpendicular Bisector of a Segment")
def compass_perp_bisector(
    model: Model,
    p1: spg.Point,
    p2: spg.Point,
    *,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Line:
    """Construct the perpendicular bisector of ``p1 p2`` by Euclid I.10 symmetric circles.

    Args:
        model: Target :class:`~geometor.model.Model`.
        p1: First endpoint.
        p2: Second endpoint.
        ID: Optional explicit line identifier.
        classes: Optional semantic CSS classes.
        guide: Whether the resulting bisector should remain a guide.

    Returns:
        Exact perpendicular bisector :class:`sympy.geometry.Line`.
    """
    c1 = model.construct_circle(p1, p2, guide=True, by="Post.3")
    c2 = model.construct_circle(p2, p1, guide=True, by="Post.3")
    q1, q2 = model.intersect_all(c1, c2, guide=True, by="I.1")
    return model.construct_line(q1, q2, ID=ID, classes=classes, guide=guide, by="Post.1")


@proposition("I.10", kind="problem", title="Midpoint of a Segment")
def compass_midpoint(
    model: Model,
    p1: spg.Point,
    p2: spg.Point,
    *,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the exact midpoint of ``p1 p2`` by straightedge and compass (Euclid I.10).

    Args:
        model: Target :class:`~geometor.model.Model`.
        p1: First endpoint.
        p2: Second endpoint.
        ID: Optional explicit point identifier.
        classes: Optional semantic CSS classes.

    Returns:
        Exact midpoint :class:`sympy.geometry.Point`.
    """
    c1 = model.construct_circle(p1, p2, guide=True, by="Post.3")
    c2 = model.construct_circle(p2, p1, guide=True, by="Post.3")
    q1, q2 = model.intersect_all(c1, c2, guide=True, by="I.1")
    bis = model.construct_line(q1, q2, guide=True, by="Post.1")
    carrier = model.construct_line(p1, p2, guide=True, by="Post.1")
    return model.intersect(carrier, bis, ID=ID, classes=classes, by="I.10")


@proposition("I.11_12", kind="problem", title="Perpendicular Line Through a Given Point")
def compass_perpendicular_line(
    model: Model,
    line_p1: spg.Point,
    line_p2: spg.Point,
    through: spg.Point,
    *,
    off_line_ref: spg.Point | None = None,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Line:
    """Construct the perpendicular to line ``line_p1 line_p2`` through ``through``.

    Uses rational circle reflection (Euclid I.12) when ``through`` lies off the line, and
    Thales's semicircle construction (Euclid III.31) via ``off_line_ref`` (or equilateral
    fallback) when ``through`` lies on the line—preserving rational fields without extraneous
    nested radicals whenever ``off_line_ref`` is provided.

    Args:
        model: Target :class:`~geometor.model.Model`.
        line_p1: First point defining the base line.
        line_p2: Second point defining the base line.
        through: Point through which the perpendicular is drawn.
        off_line_ref: Optional known point not lying on ``line_p1 line_p2`` for Thales III.31.
        ID: Optional explicit line identifier.
        classes: Optional semantic CSS classes.
        guide: Whether the perpendicular line should remain a guide.

    Returns:
        Exact perpendicular :class:`sympy.geometry.Line` passing through ``through``.
    """
    base_line = model.construct_line(line_p1, line_p2, guide=True, by="Post.1")
    if not base_line.contains(through):
        c1 = model.construct_circle(line_p1, through, guide=True, by="Post.3")
        c2 = model.construct_circle(line_p2, through, guide=True, by="Post.3")
        refl = model.intersect(c1, c2, other_than=through, guide=True, by="I.12")
        return model.construct_line(through, refl, ID=ID, classes=classes, guide=guide, by="Post.1")

    if off_line_ref is not None and not base_line.contains(off_line_ref):
        dx_line = line_p2.x - line_p1.x
        dy_line = line_p2.y - line_p1.y
        dot_val = dx_line * (off_line_ref.x - through.x) + dy_line * (off_line_ref.y - through.y)
        if zero_test(dot_val):
            return model.construct_line(
                through, off_line_ref, ID=ID, classes=classes, guide=guide, by="Post.1"
            )
        thales_circ = model.construct_circle(off_line_ref, through, guide=True, by="Post.3")
        sec_pt = model.intersect(thales_circ, base_line, other_than=through, guide=True, by="III.31")
        diam_line = model.construct_line(sec_pt, off_line_ref, guide=True, by="Post.1")
        anti_pt = model.intersect(
            thales_circ, diam_line, other_than=sec_pt, guide=True, by="III.31"
        )
        return model.construct_line(
            through, anti_pt, ID=ID, classes=classes, guide=guide, by="III.31"
        )

    other_on_line = line_p2 if through == line_p1 else line_p1
    step_circ = model.construct_circle(through, other_on_line, guide=True, by="Post.3")
    q_a, q_b = model.intersect_all(step_circ, base_line, guide=True, by="I.11")
    return compass_perp_bisector(model, q_a, q_b, ID=ID, classes=classes, guide=guide)


@proposition("I.31", kind="problem", title="Parallel Line Through a Given Point")
def compass_parallel_line(
    model: Model,
    line_p1: spg.Point,
    line_p2: spg.Point,
    through: spg.Point,
    *,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Line:
    """Construct the line through ``through`` parallel to ``line_p1 line_p2`` (Euclid I.31).

    Constructs the fourth vertex ``Q = line_p2 + through - line_p1`` of parallelogram
    ``line_p1 line_p2 Q through`` by bisecting diagonal ``line_p2 through`` at ``M`` and
    doubling ``line_p1 M`` via circle ``(M, line_p1)``.

    Args:
        model: Target :class:`~geometor.model.Model`.
        line_p1: First point on the reference line.
        line_p2: Second point on the reference line.
        through: Exterior point through which the parallel is drawn.
        ID: Optional explicit line identifier.
        classes: Optional semantic CSS classes.
        guide: Whether the parallel line should remain a guide.

    Returns:
        Exact parallel :class:`sympy.geometry.Line` passing through ``through``.
    """
    diag_mid = compass_midpoint(model, line_p2, through)
    diag_line = model.construct_line(line_p1, diag_mid, guide=True, by="Post.1")
    transfer_circ = model.construct_circle(diag_mid, line_p1, guide=True, by="Post.3")
    fourth_vertex = model.intersect(
        transfer_circ, diag_line, other_than=line_p1, guide=True, by="I.31"
    )
    return model.construct_line(
        through, fourth_vertex, ID=ID, classes=classes, guide=guide, by="I.31"
    )
