:title: Book I, Section I Summary — Additional Propositions
:layout: book
:canonical_id: Book I, Section I Summary
:order: 1
:folio: 0027–0042 (p. 1–16)
:tracks: English: section_01-en | Summary: section_01-summary | Notes: section_01-notes

.. _casey-book-01-sec-01-summary:
.. _sequel-unit-1-summary:

Book I, Section I Summary: Additional Propositions
==================================================

.. rubric:: Structured Decomposition & Invariant Ledger for Casey's Book I Section I (pp. 1–16)

.. folio:: 0027
   :page: 1

1. Architectural Overview
-------------------------

Section I extends Euclid's Book I by deriving the classical triangle concurrencies and barycentric theory using strictly elementary methods (congruence and parallelograms, without appealing to Book III circle theorems or Book VI ratios):

* **Parallelogram & Midline Theorems (Props. 1–3):** Bisection of diagonals; midline parallel to base and equal to half the base ($DE = \frac{1}{2} BC$).
* **Locus of Vertex under Difference of Squares (Props. 9–10):** The locus of vertices of triangles on a given base with given difference of squares of sides is a straight line perpendicular to the base.
* **Concurrency of Perpendiculars / The Orthocentre (Prop. 10 Cor. 1):** Proved via the anticomplementary triangle $\triangle A'B'C'$ whose perpendicular bisectors coincide with the altitudes of $\triangle ABC$.
* **Concurrency of Medians / The Centroid (Prop. 11):** Proved via similar midline triangles; the centroid $G = X(2)$ trisects each median in ratio $2:1$.
* **Centres of Mean Position (Props. 16–17):** Synthetic construction of weighted barycentres $\bar{P} = (\sum m_i P_i)/(\sum m_i)$, establishing the foundation for barycentric coordinates.
* **Variational Extremes (Props. 20–22):** Isoperimetric properties of triangles and cyclic polygons.

----

2. Structured Decompositions
----------------------------

Orthocentre Concurrency (Prop. 10 Cor. 1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Arbitrary triangle $\triangle ABC$ with altitudes $A D_a, B D_b, C D_c$.
* **Construct:** Anticomplementary triangle $\triangle A'B'C'$ by drawing lines through $A, B, C$ parallel to $BC, CA, AB$ respectively.
* **Demonstrate:** Quadrilaterals $ABCB'$ and $ABA'C$ are parallelograms; hence $B'A = BC = AC'$, making $A$ the midpoint of $B'C'$. Similarly $B$ and $C$ are midpoints of $C'A'$ and $A'B'$. Since $A D_a \perp BC \parallel B'C'$, the altitude $A D_a$ is the perpendicular bisector of $B'C'$. By Euclid I, the perpendicular bisectors of $\triangle A'B'C'$ concur at a single point $H$.
* **Invariants:**
  - $AH = 2\,O M_a$, $BH = 2\,O M_b$, $CH = 2\,O M_c$ (where $O$ is circumcentre and $M_a, M_b, M_c$ side midpoints).
  - Exact rational locus on Heronian $\triangle ABC$ $(15, 13, 14)$: $H = \left(5, \frac{15}{4}\right)$.

Medians Concurrency & Trisection (Prop. 11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Triangle $\triangle ABC$ with midpoints $M_a, M_b, M_c$ on sides $BC, CA, AB$.
* **Construct:** Join $M_a M_b$; let medians $A M_a$ and $B M_b$ meet at $G$.
* **Demonstrate:** $M_a M_b \parallel AB$ and $M_a M_b = \frac{1}{2} AB$ (Props. 2, 3). The vertically opposite triangles $\triangle ABG$ and $\triangle M_a M_b G$ are equiangular; hence $AG = 2\,G M_a$ and $BG = 2\,G M_b$. The third median $C M_c$ likewise cuts $A M_a$ at the point trisecting it, so all three concur at $G$.
* **Invariants:**
  - Barycentric weights: $G = \frac{1}{3} A + \frac{1}{3} B + \frac{1}{3} C$.
  - Exact rational locus on Heronian $\triangle ABC$ $(15, 13, 14)$: $G = \left(\frac{19}{3}, 4\right)$.

----

3. Canonical Heronian Ledger on $\triangle ABC$ $(15, 13, 14)$
--------------------------------------------------------------

Verified symbolically in :func:`~geometor.casey.feuerbach.construct_euler_nine_point` on $A = (0, 0), B = (14, 0), C = (5, 12)$:

.. list-table:: Exact Rational Invariants for Book I Section I
   :header-rows: 1
   :widths: 30 35 35

   * - Geometric Object
     - Symbol
     - Value on $(15, 13, 14)$
   * - Side lengths $(a, b, c)$
     - $a, b, c$
     - $a = 15, \; b = 13, \; c = 14$
   * - Area & Semiperimeter
     - $\Delta, s$
     - $\Delta = 84, \; s = 21$
   * - Centroid
     - $G = X(2)$
     - $\left(\frac{19}{3}, 4\right)$
   * - Orthocentre
     - $H = X(4)$
     - $\left(5, \frac{15}{4}\right)$
   * - Circumcentre
     - $O = X(3)$
     - $\left(7, \frac{33}{8}\right)$
   * - Altitude feet $(D_a, D_b, D_c)$
     - $D_a, D_b, D_c$
     - $\left(\frac{224}{25}, \frac{168}{25}\right), \; \left(\frac{350}{169}, \frac{840}{169}\right), \; (5, 0)$
   * - Side midpoints $(M_a, M_b, M_c)$
     - $M_a, M_b, M_c$
     - $\left(\frac{19}{2}, 6\right), \; \left(\frac{5}{2}, 6\right), \; (7, 0)$
