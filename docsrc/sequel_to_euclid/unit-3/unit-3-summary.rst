:title: Unit 3 Summary — Projective Ratios, Similitude & Complete Quadrilaterals

.. _sequel-unit-3-summary:

Unit 3 Summary: Ceva, Menelaus, Similitude & Anharmonic Projectivity
====================================================================

.. rubric:: Mathematical Synthesis of Casey's Book VI, Sections I–III & VI

1. Directed Ratios & Projective Duality Inside Euclidean Geometry
-----------------------------------------------------------------

Unit 3 marks the transition in Casey's *Sequel* from metric Euclidean geometry to projective invariants:

* **Ceva vs. Menelaus Duality:** Both theorems evaluate the identical cyclic product $\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB}$ on $\triangle ABC$: $+1$ characterizes **concurrency** of three lines (Ceva), while $-1$ characterizes **collinearity** of three points (Menelaus).
* **Homothecy & Monge's Theorem:** Two circles possess external and internal centres of similitude $S_e, S_i$ dividing $O_1 O_2$ harmonically in ratio $\pm r_1 : r_2$; Menelaus's theorem immediately forces the six centres of similitude of three circles onto Monge's four axes of similitude.
* **Complete Quadrilateral Harmonic Invariance:** Pure linear incidence alone—without compass or metric measurement—constructs the fourth harmonic conjugate of three collinear points via the third diagonal $[EF]$ of a complete quadrilateral (`0117.g1.svg`).
* **Anharmonic Pencils on a Circle:** Inscribed angle equality (Euclid ``III.21``) makes the cross-ratio $P(ABCD)$ invariant on a circle, unlocking short synthetic proofs of **Desargues's Homology Theorem** and **Pascal's Hexagrammum Mysticum**.

----

2. Verified Exact Quadrilateral Ledger (:mod:`geometor.casey.poles_polars`)
---------------------------------------------------------------------------

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
