geometor.casey
==============

.. py:module:: geometor.casey

.. autoapi-nested-parse::

   Exact symbolic geometry constructions and Digital Scriptorium apparatus for John Casey's *Sequel*.

   Models the landmark theorems and straightedge-and-compass constructions of **John Casey's**
   *A Sequel to the First Six Books of the Elements of Euclid, Containing an Easy Introduction
   to Modern Geometry* (5th ed. 1888 / 6th ed. 1892):

   - **Euler Line & Nine-Points Circle** (:func:`construct_euler_nine_point`)
   - **Radical Axis, Coaxal Circles & Poncelet Limiting Points**
     (:func:`construct_radical_axis_and_coaxial_pencil`, :func:`verify_coaxial_fundamental_theorem`)
   - **Complete Quadrilateral Harmonic Division** (:func:`construct_complete_quadrilateral_harmonic`)
   - **Casey's Generalized Ptolemy Theorem & Feuerbach's Theorem**
     (:func:`prove_casey_theorem_symbolic`, :func:`prove_casey_feuerbach_heronian`,
     :func:`construct_casey_feuerbach`)
   - **Poles, Polars, Harmonic Secants & La Hire's Reciprocity**
     (:func:`construct_pole_and_polar`, :func:`verify_lahire_reciprocity_symbolic`)
   - **Symmedians, Lemoine Circles, Brocard Points, Brocard Circle, Steiner & Tarry Points**
     (:func:`construct_symmedian_and_lemoine_circles`, :func:`construct_brocard_and_lemoine_circles`)



Submodules
----------

.. toctree::
   :maxdepth: 1

   /modules/api/geometor/casey/__main__/index
   /modules/api/geometor/casey/brocard/index
   /modules/api/geometor/casey/coaxial/index
   /modules/api/geometor/casey/concordance/index
   /modules/api/geometor/casey/feuerbach/index
   /modules/api/geometor/casey/invariants/index
   /modules/api/geometor/casey/poles_polars/index
   /modules/api/geometor/casey/render/index


Attributes
----------

.. autoapisummary::

   geometor.casey.HERONIAN_VERTICES
   geometor.casey.EMBEDDED_SVG_STYLE
   geometor.casey.__version__


Classes
-------

.. autoapisummary::

   geometor.casey.BrocardLemoineReport
   geometor.casey.BrocardLemoineResult
   geometor.casey.LemoineCirclesResult
   geometor.casey.CoaxialPencilResult
   geometor.casey.CoaxialTheoremReport
   geometor.casey.ConcordanceEntry
   geometor.casey.SympyCircleGap
   geometor.casey.CaseyFeuerbachHeronianReport
   geometor.casey.CaseyFeuerbachResult
   geometor.casey.CaseySymbolicProof
   geometor.casey.EulerNinePointResult
   geometor.casey.CompleteQuadrilateralResult
   geometor.casey.LaHireSymbolicProof
   geometor.casey.PolePolarResult


Functions
---------

.. autoapisummary::

   geometor.casey.construct_brocard_and_lemoine_circles
   geometor.casey.construct_symmedian_and_lemoine_circles
   geometor.casey.verify_brocard_identities_symbolic
   geometor.casey.construct_radical_axis_and_coaxial_pencil
   geometor.casey.verify_coaxial_fundamental_theorem
   geometor.casey.audit_sympy_circle_gaps
   geometor.casey.get_resources_dir
   geometor.casey.load_apparatus_registry
   geometor.casey.load_concordance
   geometor.casey.compass_internal_angle_bisector
   geometor.casey.construct_casey_feuerbach
   geometor.casey.construct_euler_nine_point
   geometor.casey.prove_casey_feuerbach_heronian
   geometor.casey.prove_casey_theorem_symbolic
   geometor.casey.are_orthogonal_circles
   geometor.casey.barycentric_point
   geometor.casey.bitangent_length
   geometor.casey.bitangent_quadrance
   geometor.casey.circle_power
   geometor.casey.compass_midpoint
   geometor.casey.compass_parallel_line
   geometor.casey.compass_perp_bisector
   geometor.casey.compass_perpendicular_line
   geometor.casey.invert_point
   geometor.casey.polar_line
   geometor.casey.pole_of_line
   geometor.casey.radical_axis_line
   geometor.casey.signed_triangle_area
   geometor.casey.construct_complete_quadrilateral_harmonic
   geometor.casey.construct_pole_and_polar
   geometor.casey.verify_lahire_reciprocity_symbolic
   geometor.casey.export_svg
   geometor.casey.render_svg_string


Package Contents
----------------

.. py:class:: BrocardLemoineReport

   Exact rational invariant summary for Symmedian, Lemoine & Brocard geometry on ``(15,13,14)``.


   .. py:attribute:: cot_omega
      :type:  sympy.Rational


   .. py:attribute:: sin_sq_omega
      :type:  sympy.Rational


   .. py:attribute:: symmedian_point
      :type:  sympy.geometry.Point


   .. py:attribute:: brocard_center
      :type:  sympy.geometry.Point


   .. py:attribute:: brocard_1
      :type:  sympy.geometry.Point


   .. py:attribute:: brocard_2
      :type:  sympy.geometry.Point


   .. py:attribute:: brocard_first_triangle
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: steiner_point
      :type:  sympy.geometry.Point


   .. py:attribute:: tarry_point
      :type:  sympy.geometry.Point


   .. py:attribute:: longchamps_point
      :type:  sympy.geometry.Point


   .. py:attribute:: lemoine_intercept_ratios
      :type:  tuple[sympy.Rational, sympy.Rational]


   .. py:attribute:: min_perp_squares_sum
      :type:  sympy.Rational


   .. py:attribute:: verified
      :type:  bool


.. py:class:: BrocardLemoineResult

   Constructed elements for Brocard Points, Brocard Circle, Lemoine Circle, Steiner & Tarry.


   .. py:attribute:: model
      :type:  geometor.model.Model


   .. py:attribute:: vertices
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: circumcenter
      :type:  sympy.geometry.Point


   .. py:attribute:: circumcircle
      :type:  sympy.geometry.Circle


   .. py:attribute:: symmedian_point
      :type:  sympy.geometry.Point


   .. py:attribute:: brocard_center
      :type:  sympy.geometry.Point


   .. py:attribute:: brocard_1
      :type:  sympy.geometry.Point


   .. py:attribute:: brocard_2
      :type:  sympy.geometry.Point


   .. py:attribute:: brocard_first_triangle
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: brocard_circle
      :type:  sympy.geometry.Circle


   .. py:attribute:: lemoine_hexagon
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: first_lemoine_circle
      :type:  sympy.geometry.Circle


   .. py:attribute:: steiner_point
      :type:  sympy.geometry.Point


   .. py:attribute:: tarry_point
      :type:  sympy.geometry.Point


   .. py:attribute:: longchamps_point
      :type:  sympy.geometry.Point


   .. py:attribute:: report
      :type:  BrocardLemoineReport


.. py:class:: LemoineCirclesResult

   Constructed elements for Symmedians, First Lemoine Circle & Cosine Circle (Unit 5).


   .. py:attribute:: model
      :type:  geometor.model.Model


   .. py:attribute:: vertices
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: circumcenter
      :type:  sympy.geometry.Point


   .. py:attribute:: circumcircle
      :type:  sympy.geometry.Circle


   .. py:attribute:: tangential_vertices
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: symmedian_point
      :type:  sympy.geometry.Point


   .. py:attribute:: lemoine_center
      :type:  sympy.geometry.Point


   .. py:attribute:: lemoine_hexagon
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: first_lemoine_circle
      :type:  sympy.geometry.Circle


   .. py:attribute:: cosine_hexagon
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: cosine_circle
      :type:  sympy.geometry.Circle


.. py:function:: construct_brocard_and_lemoine_circles(model: geometor.model.Model | None = None) -> BrocardLemoineResult

   Construct the Brocard Points, Brocard Circle, First Lemoine Circle, Steiner & Tarry Points.

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

   :param model: Optional existing :class:`~geometor.model.Model`.

   :returns: Populated :class:`BrocardLemoineResult` with full exact symbolic report.


.. py:function:: construct_symmedian_and_lemoine_circles(model: geometor.model.Model | None = None) -> LemoineCirclesResult

   Construct Lemoine's Point ``K``, First Lemoine Circle & Cosine Circle (Unit 5).

   Follows Casey, Supplementary Chapter, Sec. I, Props. 5–6 (pp. 170–171) and Sec. III,
   Prop. 1 & Cor. 4 (pp. 179–183) on ``A=(0,0), B=(14,0), C=(5,12)``.

   :param model: Optional existing :class:`~geometor.model.Model`.

   :returns: Populated :class:`LemoineCirclesResult`.


.. py:function:: verify_brocard_identities_symbolic() -> dict[str, sympy.Expr]

   Verify Casey's universal algebraic identities for ``cot(omega)`` and ``K``'s minimum property.

   1. By the Law of Cosines, ``cot A + cot B + cot C = (b^2+c^2-a^2)/(4*Delta) +
      (c^2+a^2-b^2)/(4*Delta) + (a^2+b^2-c^2)/(4*Delta) = (a^2+b^2+c^2)/(4*Delta)``.
   2. By Lagrange's identity (Sec. I, Prop. 7, p. 171):
      ``(a^2+b^2+c^2)*(x^2+y^2+z^2) - (a*x+b*y+c*z)^2 =
      (b*z - c*y)^2 + (c*x - a*z)^2 + (a*y - b*x)^2``, proving that under ``a*x+b*y+c*z = 2*Delta``,
      ``x^2 + y^2 + z^2`` attains its unique minimum when ``x/a = y/b = z/c`` (at ``K = X(6)``).

   :returns: Dictionary of zero-verified symbolic residuals.


.. py:class:: CoaxialPencilResult

   Constructed elements for the Disjoint Coaxal Pencil & Poncelet Limiting Points (Unit 2).


   .. py:attribute:: model
      :type:  geometor.model.Model


   .. py:attribute:: c1
      :type:  sympy.geometry.Circle


   .. py:attribute:: c2
      :type:  sympy.geometry.Circle


   .. py:attribute:: c3_coaxial
      :type:  sympy.geometry.Circle


   .. py:attribute:: aux_secant_circle
      :type:  sympy.geometry.Circle


   .. py:attribute:: radical_center
      :type:  sympy.geometry.Point


   .. py:attribute:: radical_foot
      :type:  sympy.geometry.Point


   .. py:attribute:: radical_axis
      :type:  sympy.geometry.Line


   .. py:attribute:: line_of_centers
      :type:  sympy.geometry.Line


   .. py:attribute:: tangent_contact_c1
      :type:  sympy.geometry.Point


   .. py:attribute:: limiting_points
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: orthogonal_circle_1
      :type:  sympy.geometry.Circle


   .. py:attribute:: orthogonal_circle_2
      :type:  sympy.geometry.Circle


   .. py:attribute:: report
      :type:  CoaxialTheoremReport


.. py:class:: CoaxialTheoremReport

   Symbolic verification certificate for Casey's Fundamental Theorem (Book III, Prop. 24).


   .. py:attribute:: symbolic_prop24_residual
      :type:  sympy.Expr


   .. py:attribute:: radical_axis_power_diff
      :type:  sympy.Expr


   .. py:attribute:: limiting_point_power_c1
      :type:  sympy.Expr


   .. py:attribute:: limiting_point_power_c2
      :type:  sympy.Expr


   .. py:attribute:: orthogonal_to_c1
      :type:  bool


   .. py:attribute:: orthogonal_to_c2
      :type:  bool


   .. py:attribute:: orthogonal_to_c3
      :type:  bool


   .. py:attribute:: verified
      :type:  bool


.. py:function:: construct_radical_axis_and_coaxial_pencil(model: geometor.model.Model | None = None) -> CoaxialPencilResult

   Construct the radical axis, coaxal system, orthogonal pencil, and limiting points.

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

   :param model: Optional existing :class:`~geometor.model.Model`.

   :returns: Populated :class:`CoaxialPencilResult` with exact coordinates and verification report.


.. py:function:: verify_coaxial_fundamental_theorem(c1: sympy.geometry.Circle, c2: sympy.geometry.Circle, c3_coaxial: sympy.geometry.Circle, orth_circle: sympy.geometry.Circle, limiting_points: tuple[sympy.geometry.Point, sympy.geometry.Point]) -> CoaxialTheoremReport

   Verify Casey Book III Props. 22–24 symbolically and on the constructed coaxal system.

   :param c1: First primary circle of the coaxal pencil.
   :param c2: Second primary circle of the coaxal pencil.
   :param c3_coaxial: Third circle belonging to the same coaxal pencil.
   :param orth_circle: Conjugate circle cutting the pencil orthogonally.
   :param limiting_points: Pair ``(L1, L2)`` of Poncelet limiting points.

   :returns: Frozen :class:`CoaxialTheoremReport` certificate.


.. py:class:: ConcordanceEntry

   Single proposition/topic concordance mapping across the GEOMETOR canon.


   .. py:attribute:: id
      :type:  str


   .. py:attribute:: unit
      :type:  str


   .. py:attribute:: casey_locus
      :type:  str


   .. py:attribute:: folio
      :type:  str


   .. py:attribute:: page
      :type:  str


   .. py:attribute:: title
      :type:  str


   .. py:attribute:: euclid_refs
      :type:  tuple[str, ...]


   .. py:attribute:: altshiller_court_refs
      :type:  tuple[str, ...]


   .. py:attribute:: etc_centers
      :type:  tuple[str, ...]


   .. py:attribute:: pappus_refs
      :type:  tuple[str, ...]


   .. py:attribute:: casey_symbol
      :type:  str


.. py:class:: SympyCircleGap

   Audit record comparing ``sympy.geometry.Circle`` against :mod:`geometor.casey`.


   .. py:attribute:: capability
      :type:  str


   .. py:attribute:: sympy_method_present
      :type:  bool


   .. py:attribute:: casey_locus
      :type:  str


   .. py:attribute:: geometor_casey_api
      :type:  str


.. py:function:: audit_sympy_circle_gaps() -> list[SympyCircleGap]

   Inspect :class:`sympy.geometry.Circle` for modern-circle-geometry primitives in Casey.

   :returns: List of :class:`SympyCircleGap` entries documenting native presence vs.
             :mod:`geometor.casey` exact symbolic implementations.


.. py:function:: get_resources_dir() -> pathlib.Path

   Return the path to ``resources/sequel_to_euclid/`` inside the repository.


.. py:function:: load_apparatus_registry(name: str) -> dict[str, Any]

   Load a JSON apparatus file (``persons``, ``citations``, ``glossary``, ``sources_manifest``).

   :param name: Filename stem without ``.json`` extension.

   :returns: Parsed JSON dictionary.


.. py:function:: load_concordance() -> list[ConcordanceEntry]

   Load all cross-repository concordance entries from ``concordance.json``.

   :returns: List of :class:`ConcordanceEntry` records in codex order.


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


.. py:function:: construct_casey_feuerbach(model: geometor.model.Model | None = None) -> CaseyFeuerbachResult

   Construct Casey's Inversion Proof & Feuerbach's Tangency Theorem on ``(15, 13, 14)``.

   Builds the Nine-Points Circle, constructs the Incentre ``I`` and Incircle ``(I, Ta)`` by
   pure compass-and-straightedge (Euclid IV.4), erects Casey's 1861 orthogonal inversion
   circle ``(Ma, Ta)`` (Book VI, Sec. IV, p. 106), constructs the fourth common internal
   tangent of ``(I, r)`` and ``(Ia, r_a)`` via reflection across line of centres ``AI``, and
   discovers the exact Feuerbach point ``Fe = X(11) = (6, 8)`` as ``(N, Ma) ∩ (I, Ta)``.

   :param model: Optional existing :class:`~geometor.model.Model`.

   :returns: Populated :class:`CaseyFeuerbachResult`.


.. py:function:: construct_euler_nine_point(model: geometor.model.Model | None = None) -> EulerNinePointResult

   Construct the Euler Line and Nine-Points Circle by straightedge and compass (Unit 1).

   Follows Casey, Book I, Misc. Ex. 42–46 (p. 20) and Book IV, Prop. 5 (pp. 57–58) on
   ``A=(0,0), B=(14,0), C=(5,12)``, verifying exact incidence of all nine classical points
   and Euler trisection ``|HG|^2 = 4*|GO|^2``.

   :param model: Optional existing :class:`~geometor.model.Model`. Created with
                 ``auto_intersect=False`` when ``None``.

   :returns: Populated :class:`EulerNinePointResult`.


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


.. py:data:: HERONIAN_VERTICES
   :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]

   Canonical Heronian ``(15, 13, 14)`` scalene triangle ``A=(0,0), B=(14,0), C=(5,12)``.

.. py:function:: are_orthogonal_circles(c1: sympy.geometry.Circle, c2: sympy.geometry.Circle) -> bool

   Return ``True`` iff circles ``c1`` and ``c2`` cut orthogonally (Casey Book III, Prop. 22).

   Two circles cut orthogonally iff the square of the distance between their centres
   equals the sum of the squares of their radii: ``|O1 O2|^2 = r1^2 + r2^2``.

   :param c1: First circle ``(O1, r1)``.
   :param c2: Second circle ``(O2, r2)``.

   :returns: ``True`` if ``|O1 O2|^2 - r1^2 - r2^2 == 0`` symbolically.


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


.. py:function:: bitangent_length(c1: sympy.geometry.Circle | sympy.geometry.Point, c2: sympy.geometry.Circle | sympy.geometry.Point, *, internal: bool = False) -> sympy.Expr

   Compute the exact common-tangent length ``t_12`` between two circles or points.

   :param c1: First circle or null-circle point.
   :param c2: Second circle or null-circle point.
   :param internal: If ``True``, return the internal common-tangent length; else external.

   :returns: Exact symbolic principal square root ``sqrt(bitangent_quadrance(c1, c2))``.


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


.. py:function:: circle_power(pt: sympy.geometry.Point, circ: sympy.geometry.Circle) -> sympy.Expr

   Compute the exact power ``|PO|^2 - r^2`` of point ``pt`` with respect to ``circ``.

   Corresponds to Casey, Book III, Props. 20–24 (pp. 41–44): for exterior points,
   equals the square of the tangent from ``pt`` to ``circ``.

   :param pt: Query point ``P``.
   :param circ: Reference circle ``(O, r)``.

   :returns: Exact symbolic expression ``(P.x - O.x)^2 + (P.y - O.y)^2 - r^2``.


.. py:function:: compass_midpoint(model: geometor.model.Model, p1: sympy.geometry.Point, p2: sympy.geometry.Point, *, ID: str = '', classes: list[str] | None = None) -> sympy.geometry.Point

   Construct the exact midpoint of ``p1 p2`` by straightedge and compass (Euclid I.10).

   :param model: Target :class:`~geometor.model.Model`.
   :param p1: First endpoint.
   :param p2: Second endpoint.
   :param ID: Optional explicit point identifier.
   :param classes: Optional semantic CSS classes.

   :returns: Exact midpoint :class:`sympy.geometry.Point`.


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


.. py:function:: compass_perp_bisector(model: geometor.model.Model, p1: sympy.geometry.Point, p2: sympy.geometry.Point, *, ID: str = '', classes: list[str] | None = None, guide: bool = False) -> sympy.geometry.Line

   Construct the perpendicular bisector of ``p1 p2`` by Euclid I.10 symmetric circles.

   :param model: Target :class:`~geometor.model.Model`.
   :param p1: First endpoint.
   :param p2: Second endpoint.
   :param ID: Optional explicit line identifier.
   :param classes: Optional semantic CSS classes.
   :param guide: Whether the resulting bisector should remain a guide.

   :returns: Exact perpendicular bisector :class:`sympy.geometry.Line`.


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


.. py:function:: signed_triangle_area(a_pt: sympy.geometry.Point, b_pt: sympy.geometry.Point, c_pt: sympy.geometry.Point) -> sympy.Expr

   Compute the exact signed area of oriented triangle ``ABC``.

   :param a_pt: First vertex ``A``.
   :param b_pt: Second vertex ``B``.
   :param c_pt: Third vertex ``C``.

   :returns: Exact symbolic signed area ``((B.x - A.x)*(C.y - A.y) - (B.y - A.y)*(C.x - A.x)) / 2``.


.. py:class:: CompleteQuadrilateralResult

   Constructed elements for Casey's Complete Quadrilateral Harmonic Section (Unit 3).


   .. py:attribute:: model
      :type:  geometor.model.Model


   .. py:attribute:: quad_vertices
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: opposite_meets
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: diagonal_center
      :type:  sympy.geometry.Point


   .. py:attribute:: third_diagonal_meets
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: cross_ratio_ac
      :type:  sympy.Expr


   .. py:attribute:: cross_ratio_bd
      :type:  sympy.Expr


.. py:class:: LaHireSymbolicProof

   Universal symbolic proof certificate for La Hire's Reciprocity & Harmonic Secants.


   .. py:attribute:: reciprocity_bilinear_diff
      :type:  sympy.Expr


   .. py:attribute:: secant_cross_ratio
      :type:  sympy.Expr


   .. py:attribute:: verified
      :type:  bool


.. py:class:: PolePolarResult

   Constructed elements for Pole, Polar, Harmonic Secants & La Hire Reciprocity (Unit 4).


   .. py:attribute:: model
      :type:  geometor.model.Model


   .. py:attribute:: circle
      :type:  sympy.geometry.Circle


   .. py:attribute:: center
      :type:  sympy.geometry.Point


   .. py:attribute:: pole_d
      :type:  sympy.geometry.Point


   .. py:attribute:: secant_1_pts
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: secant_2_pts
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: self_conjugate_triangle
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: polar_d
      :type:  sympy.geometry.Line


   .. py:attribute:: harmonic_meets
      :type:  tuple[sympy.geometry.Point, sympy.geometry.Point]


   .. py:attribute:: reciprocal_pole_q
      :type:  sympy.geometry.Point


   .. py:attribute:: polar_q
      :type:  sympy.geometry.Line


   .. py:attribute:: cross_ratio_secant_1
      :type:  sympy.Expr


   .. py:attribute:: cross_ratio_secant_2
      :type:  sympy.Expr


   .. py:attribute:: lahire_verified
      :type:  bool


.. py:function:: construct_complete_quadrilateral_harmonic(model: geometor.model.Model | None = None) -> CompleteQuadrilateralResult

   Construct Casey's Complete Quadrilateral and verify harmonic diagonal division (Unit 3).

   Follows Casey, Book VI, Sec. III, Prop. 7 (p. 91) using pure straightedge incidences on
   exact integer vertices ``A=(0, 0), B=(6, 0), C=(4, 2), D=(2, 3)``:

   - Opposite side meets: ``E = [AB] ∩ [CD] = (8, 0)`` and ``F = [AD] ∩ [BC] = (12/5, 18/5)``.
   - Internal diagonal meet: ``P = [AC] ∩ [BD] = (18/5, 9/5)``.
   - Third diagonal ``[EF]`` cuts ``[AC]`` at ``Qa = (9/2, 9/4)`` and ``[BD]`` at
     ``Qb = (-6, 9)`` such that ``(A, C; P, Qa) = -1`` and ``(B, D; P, Qb) = -1``.

   :param model: Optional existing :class:`~geometor.model.Model`.

   :returns: Populated :class:`CompleteQuadrilateralResult`.


.. py:function:: construct_pole_and_polar(model: geometor.model.Model | None = None) -> PolePolarResult

   Construct the Polar of ``D`` by straightedge and verify La Hire's Reciprocity (Unit 4).

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

   :param model: Optional existing :class:`~geometor.model.Model`.

   :returns: Populated :class:`PolePolarResult`.


.. py:function:: verify_lahire_reciprocity_symbolic() -> LaHireSymbolicProof

   Prove La Hire's Reciprocity (Book III, Prop. 25) and Harmonic Secant Section (VI.III.4).

   1. For circle ``(x - h)^2 + (y - k)^2 = r^2``, ``polar(P)`` has equation
      ``(x1 - h)(x - h) + (y1 - k)(y - k) - r^2 = 0``, which is symmetric in ``(x1, y1)``
      and ``(x2, y2)``.
   2. For exterior pole ``D = (d, 0)`` on diameter secant ``y = 0`` cutting ``x^2 + y^2 = r^2``
      at ``G = (-r, 0), H = (r, 0)`` with polar foot ``J = (r^2/d, 0)``, the anharmonic ratio
      ``(G, H; J, D)`` simplifies identically to ``-1``.

   :returns: Frozen :class:`LaHireSymbolicProof` certificate.


.. py:data:: EMBEDDED_SVG_STYLE
   :type:  str
   :value: ''


.. py:function:: export_svg(model: geometor.model.Model, output_path: str | pathlib.Path, *, graphic_id: str = 'g1', title: str = 'Casey Euclidean Circle Construction', width: int = 680, height: int = 480, margin: float = 42.0, bbox: tuple[float, float, float, float] | None = None, focus_points: collections.abc.Sequence[sympy.geometry.Point] | None = None, include_guides: bool = False, show_labels: bool = True, label_overrides: dict[str, tuple[str, str]] | None = None, highlight_point_ids: collections.abc.Sequence[str] | None = None) -> pathlib.Path

   Write an interactive ``.euclid-graphic`` SVG rendering of ``model`` to ``output_path``.

   :param model: Populated :class:`~geometor.model.Model`.
   :param output_path: Destination ``.svg`` file path.
   :param graphic_id: ``data-graphic-id`` identifier for ``geometor_interactive.js``.
   :param title: Accessible SVG title string.
   :param width: Pixel width of the SVG ``viewBox``.
   :param height: Pixel height of the SVG ``viewBox``.
   :param margin: Outer pixel margin around the framed viewport.
   :param bbox: Optional explicit math viewport ``(xmin, xmax, ymin, ymax)``.
   :param focus_points: Optional subset of points used to compute auto-framing bounds.
   :param include_guides: If ``True``, also render elements marked ``guide=True``.
   :param show_labels: Master toggle for point text labels.
   :param label_overrides: Optional mapping ``pt_id -> (base, subscript)``.
   :param highlight_point_ids: Optional point IDs to emphasize with an outer halo ring.

   :returns: Resolved :class:`pathlib.Path` of the written SVG file.


.. py:function:: render_svg_string(model: geometor.model.Model, *, graphic_id: str = 'g1', title: str = 'Casey Euclidean Circle Construction', width: int = 680, height: int = 480, margin: float = 42.0, bbox: tuple[float, float, float, float] | None = None, focus_points: collections.abc.Sequence[sympy.geometry.Point] | None = None, include_guides: bool = False, show_labels: bool = True, label_overrides: dict[str, tuple[str, str]] | None = None, highlight_point_ids: collections.abc.Sequence[str] | None = None) -> str

   Render a :class:`~geometor.model.Model` into a complete ``.euclid-graphic`` SVG string.

   :param model: Populated :class:`~geometor.model.Model`.
   :param graphic_id: ``data-graphic-id`` identifier for ``geometor_interactive.js``.
   :param title: Accessible SVG title string.
   :param width: Pixel width of the SVG ``viewBox``.
   :param height: Pixel height of the SVG ``viewBox``.
   :param margin: Outer pixel margin around the framed viewport.
   :param bbox: Optional explicit math viewport ``(xmin, xmax, ymin, ymax)``.
   :param focus_points: Optional subset of points used to compute auto-framing bounds.
   :param include_guides: If ``True``, also render elements marked ``guide=True``.
   :param show_labels: Master toggle for point text labels.
   :param label_overrides: Optional mapping ``pt_id -> (base, subscript)``.
   :param highlight_point_ids: Optional point IDs to emphasize with an outer halo ring.

   :returns: UTF-8 XML/SVG string.


.. py:data:: __version__
   :value: '0.1.0'


