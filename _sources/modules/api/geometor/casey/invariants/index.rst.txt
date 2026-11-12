geometor.casey.invariants
=========================

.. py:module:: geometor.casey.invariants

.. autoapi-nested-parse::

   Exact symbolic circle, inversion, polar, and Euclidean helper invariants for Casey's *Sequel*.

   All algebraic predicates and compass-and-straightedge sub-constructions operate strictly over
   exact SymPy expressions (:class:`sympy.Rational`, :class:`sympy.Integer`, and closed-form
   radicals) without floating-point approximations.



Attributes
----------

.. autoapisummary::

   geometor.casey.invariants.HERONIAN_VERTICES


Functions
---------

.. autoapisummary::

   geometor.casey.invariants.signed_triangle_area
   geometor.casey.invariants.circle_power
   geometor.casey.invariants.are_orthogonal_circles
   geometor.casey.invariants.bitangent_quadrance
   geometor.casey.invariants.bitangent_length
   geometor.casey.invariants.invert_point
   geometor.casey.invariants.polar_line
   geometor.casey.invariants.pole_of_line
   geometor.casey.invariants.radical_axis_line
   geometor.casey.invariants.barycentric_point
   geometor.casey.invariants.compass_perp_bisector
   geometor.casey.invariants.compass_midpoint
   geometor.casey.invariants.compass_perpendicular_line
   geometor.casey.invariants.compass_parallel_line


Module Contents
---------------

.. py:data:: HERONIAN_VERTICES
   :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]

   Canonical Heronian ``(15, 13, 14)`` scalene triangle ``A=(0,0), B=(14,0), C=(5,12)``.

.. py:function:: signed_triangle_area(a_pt: sympy.geometry.Point, b_pt: sympy.geometry.Point, c_pt: sympy.geometry.Point) -> sympy.Expr

   Compute the exact signed area of oriented triangle ``ABC``.

   :param a_pt: First vertex ``A``.
   :param b_pt: Second vertex ``B``.
   :param c_pt: Third vertex ``C``.

   :returns: Exact symbolic signed area ``((B.x - A.x)*(C.y - A.y) - (B.y - A.y)*(C.x - A.x)) / 2``.


.. py:function:: circle_power(pt: sympy.geometry.Point, circ: sympy.geometry.Circle) -> sympy.Expr

   Compute the exact power ``|PO|^2 - r^2`` of point ``pt`` with respect to ``circ``.

   Corresponds to Casey, Book III, Props. 20–24 (pp. 41–44): for exterior points,
   equals the square of the tangent from ``pt`` to ``circ``.

   :param pt: Query point ``P``.
   :param circ: Reference circle ``(O, r)``.

   :returns: Exact symbolic expression ``(P.x - O.x)^2 + (P.y - O.y)^2 - r^2``.


.. py:function:: are_orthogonal_circles(c1: sympy.geometry.Circle, c2: sympy.geometry.Circle) -> bool

   Return ``True`` iff circles ``c1`` and ``c2`` cut orthogonally (Casey Book III, Prop. 22).

   Two circles cut orthogonally iff the square of the distance between their centres
   equals the sum of the squares of their radii: ``|O1 O2|^2 = r1^2 + r2^2``.

   :param c1: First circle ``(O1, r1)``.
   :param c2: Second circle ``(O2, r2)``.

   :returns: ``True`` if ``|O1 O2|^2 - r1^2 - r2^2 == 0`` symbolically.


.. py:function:: bitangent_quadrance(c1: sympy.geometry.Circle | sympy.geometry.Point, c2: sympy.geometry.Circle | sympy.geometry.Point, *, internal: bool = False) -> sympy.Expr

   Compute the exact squared common-tangent length ``t_12^2`` between circles or null-circles.

   In Casey's Generalized Ptolemy Theorem (Book VI, Sec. IV, Prop. 10, pp. 103–104), a point
   is treated as a circle of radius ``0``. For two circles soaked in the same sense (external
   common tangent), ``t_12^2 = |O1 O2|^2 - (r1 - r2)^2``; for transverse (internal) contact,
   ``t_12^2 = |O1 O2|^2 - (r1 + r2)^2``.

   :param c1: First :class:`sympy.geometry.Circle` or null-circle :class:`sympy.geometry.Point`.
   :param c2: Second :class:`sympy.geometry.Circle` or null-circle :class:`sympy.geometry.Point`.
   :param internal: If ``True``, use ``(r1 + r2)^2`` (internal bitangent); otherwise ``(r1 - r2)^2``.

   :returns: Exact symbolic squared bitangent length.


.. py:function:: bitangent_length(c1: sympy.geometry.Circle | sympy.geometry.Point, c2: sympy.geometry.Circle | sympy.geometry.Point, *, internal: bool = False) -> sympy.Expr

   Compute the exact common-tangent length ``t_12`` between two circles or points.

   :param c1: First circle or null-circle point.
   :param c2: Second circle or null-circle point.
   :param internal: If ``True``, return the internal common-tangent length; else external.

   :returns: Exact symbolic principal square root ``sqrt(bitangent_quadrance(c1, c2))``.


.. py:function:: invert_point(pt: sympy.geometry.Point, center: sympy.geometry.Point, radius_sq: sympy.Expr) -> sympy.geometry.Point

   Compute the exact circular inverse of ``pt`` with respect to ``(center, sqrt(radius_sq))``.

   Implements Casey, Book III, Def. (p. 41) & Book VI, Sec. IV, Def. (p. 95):
   collinear with ``center`` and ``pt`` on the same ray such that ``|O P| * |O P'| = k^2``.

   :param pt: Point ``P`` distinct from ``center``.
   :param center: Centre of inversion ``O``.
   :param radius_sq: Square ``k^2`` of the radius of inversion.

   :returns: Exact inverted :class:`sympy.geometry.Point` ``P'``.

   :raises ValueError: If ``pt`` coincides with ``center``.


.. py:function:: polar_line(pt: sympy.geometry.Point, circ: sympy.geometry.Circle) -> sympy.geometry.Line

   Compute the exact polar line of ``pt`` with respect to ``circ`` (Casey Book III, Def. p. 44).

   By Casey's definition, the polar of ``P`` with respect to ``(O, r)`` is the perpendicular
   to ray ``OP`` erected at the inverse point ``P'`` of ``P``. Note that ``sympy.geometry.Circle``
   natively lacks ``polar_line`` and ``pole_of_line`` methods.

   :param pt: Pole ``P`` distinct from ``circ.center``.
   :param circ: Reference circle ``(O, r)``.

   :returns: Exact :class:`sympy.geometry.Line` representing ``polar(P)``.

   :raises ValueError: If ``pt`` coincides with ``circ.center``.


.. py:function:: pole_of_line(line: sympy.geometry.Line, circ: sympy.geometry.Circle) -> sympy.geometry.Point

   Compute the exact pole of ``line`` with respect to ``circ`` (Casey Book III, Def. p. 44).

   Constructed algebraically as the circular inverse of the orthogonal foot of ``circ.center``
   upon ``line``.

   :param line: Non-diametral :class:`sympy.geometry.Line`.
   :param circ: Reference circle ``(O, r)``.

   :returns: Exact :class:`sympy.geometry.Point` whose polar with respect to ``circ`` is ``line``.

   :raises ValueError: If ``line`` passes through ``circ.center`` (pole is at infinity).


.. py:function:: radical_axis_line(c1: sympy.geometry.Circle, c2: sympy.geometry.Circle) -> sympy.geometry.Line

   Compute the exact radical axis of two non-concentric circles (Casey Book III, Prop. 23).

   :param c1: First circle ``(O1, r1)``.
   :param c2: Second circle ``(O2, r2)``.

   :returns: Exact :class:`sympy.geometry.Line` locus of equal circle powers.

   :raises ValueError: If ``c1`` and ``c2`` are concentric.


.. py:function:: barycentric_point(a_pt: sympy.geometry.Point, b_pt: sympy.geometry.Point, c_pt: sympy.geometry.Point, w_a: sympy.Expr, w_b: sympy.Expr, w_c: sympy.Expr) -> sympy.geometry.Point

   Compute the exact homogeneous barycentric point ``(w_a : w_b : w_c)`` on ``ABC``.

   Implements Casey's Centre of Mean Position (Book I, Props. 17–18, pp. 12–13) and
   symmedian/Brocard weights (Supplementary Chapter, Secs. I–II).

   :param a_pt: First vertex ``A``.
   :param b_pt: Second vertex ``B``.
   :param c_pt: Third vertex ``C``.
   :param w_a: Weight attached to ``A``.
   :param w_b: Weight attached to ``B``.
   :param w_c: Weight attached to ``C``.

   :returns: Exact :class:`sympy.geometry.Point` ``(w_a*A + w_b*B + w_c*C) / (w_a + w_b + w_c)``.

   :raises ValueError: If ``w_a + w_b + w_c == 0``.


.. py:function:: compass_perp_bisector(model: geometor.model.Model, p1: sympy.geometry.Point, p2: sympy.geometry.Point, *, ID: str = '', classes: list[str] | None = None, guide: bool = False) -> sympy.geometry.Line

   Construct the perpendicular bisector of ``p1 p2`` by Euclid I.10 symmetric circles.

   :param model: Target :class:`~geometor.model.Model`.
   :param p1: First endpoint.
   :param p2: Second endpoint.
   :param ID: Optional explicit line identifier.
   :param classes: Optional semantic CSS classes.
   :param guide: Whether the resulting bisector should remain a guide.

   :returns: Exact perpendicular bisector :class:`sympy.geometry.Line`.


.. py:function:: compass_midpoint(model: geometor.model.Model, p1: sympy.geometry.Point, p2: sympy.geometry.Point, *, ID: str = '', classes: list[str] | None = None) -> sympy.geometry.Point

   Construct the exact midpoint of ``p1 p2`` by straightedge and compass (Euclid I.10).

   :param model: Target :class:`~geometor.model.Model`.
   :param p1: First endpoint.
   :param p2: Second endpoint.
   :param ID: Optional explicit point identifier.
   :param classes: Optional semantic CSS classes.

   :returns: Exact midpoint :class:`sympy.geometry.Point`.


.. py:function:: compass_perpendicular_line(model: geometor.model.Model, line_p1: sympy.geometry.Point, line_p2: sympy.geometry.Point, through: sympy.geometry.Point, *, off_line_ref: sympy.geometry.Point | None = None, ID: str = '', classes: list[str] | None = None, guide: bool = False) -> sympy.geometry.Line

   Construct the perpendicular to line ``line_p1 line_p2`` through ``through``.

   Uses rational circle reflection (Euclid I.12) when ``through`` lies off the line, and
   Thales's semicircle construction (Euclid III.31) via ``off_line_ref`` (or equilateral
   fallback) when ``through`` lies on the line—preserving rational fields without extraneous
   nested radicals whenever ``off_line_ref`` is provided.

   :param model: Target :class:`~geometor.model.Model`.
   :param line_p1: First point defining the base line.
   :param line_p2: Second point defining the base line.
   :param through: Point through which the perpendicular is drawn.
   :param off_line_ref: Optional known point not lying on ``line_p1 line_p2`` for Thales III.31.
   :param ID: Optional explicit line identifier.
   :param classes: Optional semantic CSS classes.
   :param guide: Whether the perpendicular line should remain a guide.

   :returns: Exact perpendicular :class:`sympy.geometry.Line` passing through ``through``.


.. py:function:: compass_parallel_line(model: geometor.model.Model, line_p1: sympy.geometry.Point, line_p2: sympy.geometry.Point, through: sympy.geometry.Point, *, ID: str = '', classes: list[str] | None = None, guide: bool = False) -> sympy.geometry.Line

   Construct the line through ``through`` parallel to ``line_p1 line_p2`` (Euclid I.31).

   Constructs the fourth vertex ``Q = line_p2 + through - line_p1`` of parallelogram
   ``line_p1 line_p2 Q through`` by bisecting diagonal ``line_p2 through`` at ``M`` and
   doubling ``line_p1 M`` via circle ``(M, line_p1)``.

   :param model: Target :class:`~geometor.model.Model`.
   :param line_p1: First point on the reference line.
   :param line_p2: Second point on the reference line.
   :param through: Exterior point through which the parallel is drawn.
   :param ID: Optional explicit line identifier.
   :param classes: Optional semantic CSS classes.
   :param guide: Whether the parallel line should remain a guide.

   :returns: Exact parallel :class:`sympy.geometry.Line` passing through ``through``.


