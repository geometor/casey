geometor.casey.feuerbach
========================

.. py:module:: geometor.casey.feuerbach

.. autoapi-nested-parse::

   Exact symbolic proofs and compass-and-straightedge constructions of Casey's & Feuerbach's Theorems.

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



Classes
-------

.. autoapisummary::

   geometor.casey.feuerbach.CaseySymbolicProof
   geometor.casey.feuerbach.CaseyFeuerbachHeronianReport
   geometor.casey.feuerbach.EulerNinePointResult
   geometor.casey.feuerbach.CaseyFeuerbachResult


Functions
---------

.. autoapisummary::

   geometor.casey.feuerbach.compass_internal_angle_bisector
   geometor.casey.feuerbach.prove_casey_theorem_symbolic
   geometor.casey.feuerbach.prove_casey_feuerbach_heronian
   geometor.casey.feuerbach.construct_euler_nine_point
   geometor.casey.feuerbach.construct_casey_feuerbach


Module Contents
---------------

.. py:class:: CaseySymbolicProof

   Symbolic verification certificate for Casey's Generalized Ptolemy Theorem.


   .. py:attribute:: inversion_invariance_residual
      :type:  sympy.Expr


   .. py:attribute:: tangent_line_euler_residual
      :type:  sympy.Expr


   .. py:attribute:: incircle_casey_residual
      :type:  sympy.Expr


   .. py:attribute:: incircle_cor2_squares_residual
      :type:  sympy.Expr


   .. py:attribute:: excircle_a_casey_residual
      :type:  sympy.Expr


   .. py:attribute:: verified
      :type:  bool


.. py:class:: CaseyFeuerbachHeronianReport

   Exact rational invariant report for Casey's Theorem & Feuerbach tangency on ``(15, 13, 14)``.


   .. py:attribute:: sides
      :type:  tuple[sympy.Integer, sympy.Integer, sympy.Integer]


   .. py:attribute:: area
      :type:  sympy.Rational


   .. py:attribute:: inradius
      :type:  sympy.Rational


   .. py:attribute:: circumradius
      :type:  sympy.Rational


   .. py:attribute:: nine_point_radius
      :type:  sympy.Rational


   .. py:attribute:: exradii
      :type:  tuple[sympy.Rational, sympy.Rational, sympy.Rational]


   .. py:attribute:: midpoint_chords
      :type:  tuple[sympy.Rational, sympy.Rational, sympy.Rational]


   .. py:attribute:: incircle_midpoint_tangents
      :type:  tuple[sympy.Rational, sympy.Rational, sympy.Rational]


   .. py:attribute:: casey_signed_sum
      :type:  sympy.Expr


   .. py:attribute:: feuerbach_point
      :type:  sympy.geometry.Point


   .. py:attribute:: excircle_feuerbach_points
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: ni_distance
      :type:  sympy.Rational


   .. py:attribute:: inversion_circle_orthogonal_to_incircle
      :type:  bool


   .. py:attribute:: inversion_circle_orthogonal_to_excircle_a
      :type:  bool


   .. py:attribute:: verified
      :type:  bool


.. py:class:: EulerNinePointResult

   Constructed elements for the Euler Line and Nine-Points Circle (Unit 1).


   .. py:attribute:: model
      :type:  geometor.model.Model


   .. py:attribute:: vertices
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: midpoints
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: altitude_feet
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: euler_midpoints
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: centroid
      :type:  sympy.geometry.Point


   .. py:attribute:: circumcenter
      :type:  sympy.geometry.Point


   .. py:attribute:: orthocenter
      :type:  sympy.geometry.Point


   .. py:attribute:: nine_point_center
      :type:  sympy.geometry.Point


   .. py:attribute:: euler_line
      :type:  sympy.geometry.Line


   .. py:attribute:: circumcircle
      :type:  sympy.geometry.Circle


   .. py:attribute:: nine_point_circle
      :type:  sympy.geometry.Circle


.. py:class:: CaseyFeuerbachResult

   Constructed elements for Casey's & Feuerbach's Theorem on ``(15, 13, 14)`` (Unit 4).


   .. py:attribute:: model
      :type:  geometor.model.Model


   .. py:attribute:: euler_nine_point
      :type:  EulerNinePointResult


   .. py:attribute:: incenter
      :type:  sympy.geometry.Point


   .. py:attribute:: incircle_contacts
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: incircle
      :type:  sympy.geometry.Circle


   .. py:attribute:: feuerbach_point
      :type:  sympy.geometry.Point


   .. py:attribute:: casey_inversion_circle
      :type:  sympy.geometry.Circle


   .. py:attribute:: fourth_common_tangent
      :type:  sympy.geometry.Line


.. py:function:: compass_internal_angle_bisector(model: geometor.model.Model, vertex: sympy.geometry.Point, arm_p1: sympy.geometry.Point, arm_p2: sympy.geometry.Point, *, ID: str = '', classes: list[str] | None = None, guide: bool = False) -> sympy.geometry.Line

   Construct the internal bisector of ``< arm_p1 vertex arm_p2 )`` by Euclid I.9.

   Transfers ``|vertex arm_p1|`` onto ray ``vertex arm_p2`` via circle ``(vertex, arm_p1)``
   and bisects the resulting isosceles base chord.

   :param model: Target :class:`~geometor.model.Model`.
   :param vertex: Angle vertex.
   :param arm_p1: Point on the first ray.
   :param arm_p2: Point on the second ray.
   :param ID: Optional explicit line identifier.
   :param classes: Optional semantic CSS classes.
   :param guide: Whether the angle bisector should remain a guide.

   :returns: Exact internal angle bisector :class:`sympy.geometry.Line`.


.. py:function:: prove_casey_theorem_symbolic() -> CaseySymbolicProof

   Prove Casey's Generalized Ptolemy Theorem & Feuerbach's Corollary symbolically.

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

   :returns: Frozen :class:`CaseySymbolicProof` certificate with zero residuals.


.. py:function:: prove_casey_feuerbach_heronian() -> CaseyFeuerbachHeronianReport

   Verify Casey's bitangent equation and all 4 Feuerbach tangencies on Heronian ``(15, 13, 14)``.

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

   :returns: Frozen :class:`CaseyFeuerbachHeronianReport` with exact rational values.


.. py:function:: construct_euler_nine_point(model: geometor.model.Model | None = None) -> EulerNinePointResult

   Construct the Euler Line and Nine-Points Circle by straightedge and compass (Unit 1).

   Follows Casey, Book I, Misc. Ex. 42–46 (p. 20) and Book IV, Prop. 5 (pp. 57–58) on
   ``A=(0,0), B=(14,0), C=(5,12)``, verifying exact incidence of all nine classical points
   and Euler trisection ``|HG|^2 = 4*|GO|^2``.

   :param model: Optional existing :class:`~geometor.model.Model`. Created with
                 ``auto_intersect=False`` when ``None``.

   :returns: Populated :class:`EulerNinePointResult`.


.. py:function:: construct_casey_feuerbach(model: geometor.model.Model | None = None) -> CaseyFeuerbachResult

   Construct Casey's Inversion Proof & Feuerbach's Tangency Theorem on ``(15, 13, 14)``.

   Builds the Nine-Points Circle, constructs the Incentre ``I`` and Incircle ``(I, Ta)`` by
   pure compass-and-straightedge (Euclid IV.4), erects Casey's 1861 orthogonal inversion
   circle ``(Ma, Ta)`` (Book VI, Sec. IV, p. 106), constructs the fourth common internal
   tangent of ``(I, r)`` and ``(Ia, r_a)`` via reflection across line of centres ``AI``, and
   discovers the exact Feuerbach point ``Fe = X(11) = (6, 8)`` as ``(N, Ma) ∩ (I, Ta)``.

   :param model: Optional existing :class:`~geometor.model.Model`.

   :returns: Populated :class:`CaseyFeuerbachResult`.


