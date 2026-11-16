:title: Book VI, Section III Summary — Harmonic Section & Complete Quadrilateral
:tracks: section_03-en section_03-notes

.. _casey-book-06-sec-03-summary:

Book VI, Section III Summary: Harmonic Section & The Complete Quadrilateral
===========================================================================

.. rubric:: Modern Geometric & Invariant Analysis of Casey's Book VI, Section III (pp. 87–94)

1. Definitions & Metric Criteria
--------------------------------

* **Harmonic Conjugates:** Four collinear points $A, B, C, D$ satisfy $(A, B; C, D) = -1$ when:

  $$
  \frac{AC}{CB} = -\frac{AD}{DB} \iff \frac{2}{AB} = \frac{1}{AC} + \frac{1}{AD} \iff OC \cdot OD = OB^2,
  $$

  where $O = \operatorname{midpoint}(AB)$.
* **Harmonic Orthogonality:** The circle on diameter $AB$ cuts the circle on diameter $CD$ orthogonally if and only if $(A, B; C, D) = -1$.
* **Harmonic Pencil:** Four concurrent rays $O(A, B; C, D)$ cut every transversal in a harmonic range, and any transversal parallel to one ray is bisected by its conjugate ray.

----

2. The Complete Quadrilateral Harmonic Theorem (Prop. 7)
--------------------------------------------------------

* **Given:** Complete quadrilateral with four sides $[AB]$, $[BC]$, $[CD]$, $[DA]$, whose opposite pairs meet at $E = [AB]\cap[CD]$ and $F = [AD]\cap[BC]$.
* **Diagonals:** The three diagonals are $[AC]$, $[BD]$, and $[EF]$.
* **Intersections:**
  - $P = [AC] \cap [BD]$ (diagonal cross);
  - $Q_a = [AC] \cap [EF]$;
  - $Q_b = [BD] \cap [EF]$.
* **Harmonic Invariants:** Each diagonal is harmonically divided by the other two:

  $$
  (A, C; P, Q_a) = -1, \qquad (B, D; P, Q_b) = -1, \qquad (E, F; Q_a, Q_b) = -1.
  $$

----

3. Verified Exact Rational Ledger (:mod:`geometor.casey.poles_polars`)
----------------------------------------------------------------------

Constructed in :func:`~geometor.casey.poles_polars.construct_complete_quadrilateral_harmonic` (`0117.g1.svg`):

.. list-table:: Exact Rational Coordinates & Cross-Ratios of the Complete Quadrilateral
   :header-rows: 1
   :widths: 36 32 32

   * - Projective Element
     - Incidence Definition
     - Exact Rational Value
   * - Quadrangle Base Vertices
     - $A, B, C, D$
     - $(0, 0), \; (6, 0), \; (4, 2), \; (2, 3)$
   * - Opposite Side Intersections
     - $E = [AB]\cap[CD], \; F = [AD]\cap[BC]$
     - $E = (8, 0), \; F = \left(\frac{12}{5}, \frac{18}{5}\right)$
   * - Internal Diagonal Centre
     - $P = [AC]\cap[BD]$
     - $P = \left(\frac{18}{5}, \frac{9}{5}\right)$
   * - Third Diagonal Harmonic Meets
     - $Q_a = [AC]\cap[EF], \; Q_b = [BD]\cap[EF]$
     - $Q_a = \left(\frac{9}{2}, \frac{9}{4}\right), \; Q_b = (-6, 9)$
   * - Verified Cross-Ratios
     - $(A,C;P,Q_a), \; (B,D;P,Q_b), \; (E,F;Q_a,Q_b)$
     - $-1, \; -1, \; -1$
