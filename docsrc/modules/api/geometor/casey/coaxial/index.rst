geometor.casey.coaxial
======================

.. py:module:: geometor.casey.coaxial

.. autoapi-nested-parse::

   Exact straightedge-and-compass constructions for Radical Axes, Coaxal Systems & Limiting Points.

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



Classes
-------

.. autoapisummary::

   geometor.casey.coaxial.CoaxialTheoremReport
   geometor.casey.coaxial.CoaxialPencilResult


Functions
---------

.. autoapisummary::

   geometor.casey.coaxial.verify_coaxial_fundamental_theorem
   geometor.casey.coaxial.construct_radical_axis_and_coaxial_pencil


Module Contents
---------------

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


.. py:function:: verify_coaxial_fundamental_theorem(c1: sympy.geometry.Circle, c2: sympy.geometry.Circle, c3_coaxial: sympy.geometry.Circle, orth_circle: sympy.geometry.Circle, limiting_points: tuple[sympy.geometry.Point, sympy.geometry.Point]) -> CoaxialTheoremReport

   Verify Casey Book III Props. 22–24 symbolically and on the constructed coaxal system.

   :param c1: First primary circle of the coaxal pencil.
   :param c2: Second primary circle of the coaxal pencil.
   :param c3_coaxial: Third circle belonging to the same coaxal pencil.
   :param orth_circle: Conjugate circle cutting the pencil orthogonally.
   :param limiting_points: Pair ``(L1, L2)`` of Poncelet limiting points.

   :returns: Frozen :class:`CoaxialTheoremReport` certificate.


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


