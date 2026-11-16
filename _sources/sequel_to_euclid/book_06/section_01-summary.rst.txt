:title: Book VI, Section I Summary — Theory of Concurrent Lines & Transversals
:layout: book
:canonical_id: Book VI, Section I Summary
:order: 1
:tracks: English: section_01-en | Summary: section_01-summary | Notes: section_01-notes

.. _casey-book-06-sec-01-summary:
.. _sequel-unit-3-summary:

Book VI, Section I Summary: Concurrent Lines & Transversals
============================================================

.. rubric:: Mathematical Synthesis of Casey's Book VI, Section I (pp. 67–81)

1. Architectural Overview
-------------------------

Section I marks the fundamental transition in Casey's *Sequel* from metric Euclidean geometry to projective and transversal invariants:

* **Ceva vs. Menelaus Duality (Props. 2 & 4):** Both theorems evaluate the cyclic product of ratios $\frac{BA'}{A'C} \cdot \frac{CB'}{B'A} \cdot \frac{AC'}{C'B}$ along the sides of $\triangle ABC$: $+1$ characterizes **concurrency** of three lines from the vertices (Ceva, 1678), while $-1$ characterizes **collinearity** of three points on the sides (Menelaus).
* **Parallels & Harmonic Proportions (Prop. 3):** Concurrent transversals cut parallel lines into proportional segments; perpendicular distances from points on transversals maintain constant ratios.
* **Circumradius Area Formula (Prop. 5):** The rectangle contained by two sides equals the altitude times the circumdiameter ($bc = 2pR$), yielding the invariant area identity $\Delta = \frac{abc}{4R}$.
* **Inscribed Polygon Perpendicular Product (Prop. 6):** For any inscribed $2n$-gon, the product of perpendiculars from any circumference point to the odd sides equals the product to the even sides ($\prod \perp_{\text{odd}} = \prod \perp_{\text{even}}$).
* **Circle of Apollonius (Prop. 7):** The locus of a point whose distances from two fixed points have a constant ratio is a circle whose diameter is bounded by the internal and external harmonic division points.
* **Perspective Triangles (Prop. 14):** When three triangles are pairwise in perspective with the same centre of homology, their three axes of homology are concurrent.

----

2. Structured Decompositions
----------------------------

Ceva's Theorem (Prop. 2)
~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Triangle $\triangle ABC$ and concurrent cevians $AA', BB', CC'$ meeting at $O$.
* **Construct:** Base lines $AO, BO, CO$ meeting opposite sides in $A', B', C'$.
* **Demonstrate:** By Prop. 1, triangles on common base $AO$ satisfy $\frac{BA'}{A'C} = \frac{\triangle AOB}{\triangle AOC}$. Cyclically permuting vertices gives $\frac{CB'}{B'A} = \frac{\triangle BOC}{\triangle BOA}$ and $\frac{AC'}{C'B} = \frac{\triangle AOC}{\triangle BOC}$. Multiplying the three ratios cancels the triangle areas identically:

  $$
  \frac{BA'}{A'C} \cdot \frac{CB'}{B'A} \cdot \frac{AC'}{C'B} = \frac{\triangle AOB}{\triangle AOC} \cdot \frac{\triangle BOC}{\triangle BOA} \cdot \frac{\triangle AOC}{\triangle BOC} \equiv +1.
  $$

* **Invariants:** Concurrency of medians ($1 \cdot 1 \cdot 1 = 1$), internal angle bisectors ($\frac{c}{b} \cdot \frac{a}{c} \cdot \frac{b}{a} = 1$), altitudes, symmedians, Gergonne lines, and Nagel lines all follow as direct corollaries.

Menelaus's Theorem (Prop. 4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Triangle $\triangle ABC$ cut by transversal line $L$ in points $A', B', C'$ on sides $BC, CA, AB$.
* **Construct:** Drop perpendiculars $p', p'', p'''$ from vertices $A, B, C$ onto transversal $L$.
* **Demonstrate:** Right triangles give similar ratio identities $\frac{AB'}{B'C} = \frac{p'}{p'''}$, $\frac{BC'}{C'A} = \frac{p''}{p'}$, and $\frac{CA'}{A'B} = \frac{p'''}{p''}$. Taking directed segments introduces one or three negative signs, giving product $-1$. Conversely, if product is $-1$, the points are collinear.
* **Invariants:** External bisector collinearity (Cor. 2); Monge's axes of similitude (Section II); Desargues's axis of homology (Section VI).

----

3. Canonical Heronian Ledger on $\triangle ABC$ $(15, 13, 14)$
--------------------------------------------------------------

Verified in :mod:`geometor.casey.invariants`:

.. list-table:: Exact Rational Transversal Invariants for $(15, 13, 14)$
   :header-rows: 1
   :widths: 34 32 34

   * - Theorem / Object
     - Formulation
     - Exact Value on $(15, 13, 14)$
   * - Circumradius $R$
     - $R = \frac{abc}{4\Delta}$
     - $\frac{15 \cdot 13 \cdot 14}{4 \cdot 84} = \frac{65}{8}$
   * - Inradius $r$
     - $r = \frac{\Delta}{s}$
     - $\frac{84}{21} = 4$
   * - Area Identity
     - $\Delta = \frac{abc}{4R} = rs$
     - $84$
   * - Medians Ceva Ratio
     - $\frac{BA'}{A'C} \cdot \frac{CB'}{B'A} \cdot \frac{AC'}{C'B}$
     - $1 \cdot 1 \cdot 1 = +1$
   * - Bisectors Ceva Ratio
     - $\frac{c}{b} \cdot \frac{a}{c} \cdot \frac{b}{a}$
     - $\frac{14}{13} \cdot \frac{15}{14} \cdot \frac{13}{15} = +1$
   * - External Bisectors Menelaus
     - $\left(-\frac{c}{b}\right) \cdot \left(\frac{a}{c}\right) \cdot \left(\frac{b}{a}\right)$
     - $-1$
