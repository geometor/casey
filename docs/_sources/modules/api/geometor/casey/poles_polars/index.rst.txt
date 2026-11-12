geometor.casey.poles_polars
===========================

.. py:module:: geometor.casey.poles_polars

.. autoapi-nested-parse::

   Exact straightedge-and-compass constructions for Harmonic Section, Poles, Polars & Reciprocity.

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



Classes
-------

.. autoapisummary::

   geometor.casey.poles_polars.LaHireSymbolicProof
   geometor.casey.poles_polars.CompleteQuadrilateralResult
   geometor.casey.poles_polars.PolePolarResult


Functions
---------

.. autoapisummary::

   geometor.casey.poles_polars.verify_lahire_reciprocity_symbolic
   geometor.casey.poles_polars.construct_complete_quadrilateral_harmonic
   geometor.casey.poles_polars.construct_pole_and_polar


Module Contents
---------------

.. py:class:: LaHireSymbolicProof

   Universal symbolic proof certificate for La Hire's Reciprocity & Harmonic Secants.


   .. py:attribute:: reciprocity_bilinear_diff
      :type:  sympy.Expr


   .. py:attribute:: secant_cross_ratio
      :type:  sympy.Expr


   .. py:attribute:: verified
      :type:  bool


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


.. py:function:: verify_lahire_reciprocity_symbolic() -> LaHireSymbolicProof

   Prove La Hire's Reciprocity (Book III, Prop. 25) and Harmonic Secant Section (VI.III.4).

   1. For circle ``(x - h)^2 + (y - k)^2 = r^2``, ``polar(P)`` has equation
      ``(x1 - h)(x - h) + (y1 - k)(y - k) - r^2 = 0``, which is symmetric in ``(x1, y1)``
      and ``(x2, y2)``.
   2. For exterior pole ``D = (d, 0)`` on diameter secant ``y = 0`` cutting ``x^2 + y^2 = r^2``
      at ``G = (-r, 0), H = (r, 0)`` with polar foot ``J = (r^2/d, 0)``, the anharmonic ratio
      ``(G, H; J, D)`` simplifies identically to ``-1``.

   :returns: Frozen :class:`LaHireSymbolicProof` certificate.


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


