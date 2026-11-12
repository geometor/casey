geometor.casey.brocard
======================

.. py:module:: geometor.casey.brocard

.. autoapi-nested-parse::

   Exact symbolic constructions and proofs for Symmedians, Lemoine Circles & Brocard Geometry.

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



Classes
-------

.. autoapisummary::

   geometor.casey.brocard.BrocardLemoineReport
   geometor.casey.brocard.LemoineCirclesResult
   geometor.casey.brocard.BrocardLemoineResult


Functions
---------

.. autoapisummary::

   geometor.casey.brocard.verify_brocard_identities_symbolic
   geometor.casey.brocard.construct_symmedian_and_lemoine_circles
   geometor.casey.brocard.construct_brocard_and_lemoine_circles


Module Contents
---------------

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


.. py:function:: verify_brocard_identities_symbolic() -> dict[str, sympy.Expr]

   Verify Casey's universal algebraic identities for ``cot(omega)`` and ``K``'s minimum property.

   1. By the Law of Cosines, ``cot A + cot B + cot C = (b^2+c^2-a^2)/(4*Delta) +
      (c^2+a^2-b^2)/(4*Delta) + (a^2+b^2-c^2)/(4*Delta) = (a^2+b^2+c^2)/(4*Delta)``.
   2. By Lagrange's identity (Sec. I, Prop. 7, p. 171):
      ``(a^2+b^2+c^2)*(x^2+y^2+z^2) - (a*x+b*y+c*z)^2 =
      (b*z - c*y)^2 + (c*x - a*z)^2 + (a*y - b*x)^2``, proving that under ``a*x+b*y+c*z = 2*Delta``,
      ``x^2 + y^2 + z^2`` attains its unique minimum when ``x/a = y/b = z/c`` (at ``K = X(6)``).

   :returns: Dictionary of zero-verified symbolic residuals.


.. py:function:: construct_symmedian_and_lemoine_circles(model: geometor.model.Model | None = None) -> LemoineCirclesResult

   Construct Lemoine's Point ``K``, First Lemoine Circle & Cosine Circle (Unit 5).

   Follows Casey, Supplementary Chapter, Sec. I, Props. 5–6 (pp. 170–171) and Sec. III,
   Prop. 1 & Cor. 4 (pp. 179–183) on ``A=(0,0), B=(14,0), C=(5,12)``.

   :param model: Optional existing :class:`~geometor.model.Model`.

   :returns: Populated :class:`LemoineCirclesResult`.


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


