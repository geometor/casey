:title: Book II, Section II Summary — Exercises
:layout: book
:canonical_id: Book II, Section II Summary
:order: 2
:folio: 0053–0054 (p. 27–28)
:tracks: English: section_02-en | Summary: section_02-summary | Notes: section_02-notes

.. _casey-book-02-sec-02-summary:

Book II, Section II Summary: Exercises
======================================

.. rubric:: Structured Decomposition & Invariant Ledger for Casey's Book II Section II Exercises (pp. 27–28)

.. folio:: 0053
   :page: 27

1. Architectural Overview
-------------------------

The exercises of Book II explore quadratic identities, algebraic Law of Cosines specializations, and locus problems:

* **Law of Cosines Specializations (Ex. 4–5):** Exact Euclidean evaluations for $c^2 = a^2 + b^2 - 2ab\cos C$ when $C = 60^\circ$ ($\cos C = \frac{1}{2}$, giving $c^2 = a^2 + b^2 - ab$) and $C = 120^\circ$ ($\cos C = -\frac{1}{2}$, giving $c^2 = a^2 + b^2 + ab$).
* **Quadrilateral Midpoint Relations (Ex. 6):** Quadratic relations connecting opposite sides and diagonals.
* **Golden Section Identities (Ex. 10):** Metric relations for the extreme and mean ratio ($AB \cdot BC = AC^2$), proving $AB^2 + BC^2 = 3 AC^2$ and $(AB + BC)^2 = 5 AC^2$.
* **Flank Triangles of Vecten-Style Outer Squares (Ex. 13):** The sum of the squares of the outer lines connecting the adjacent vertices of squares described on the three sides of a triangle equals three times the sum of the squares of the sides ($d_a^2 + d_b^2 + d_c^2 = 3(a^2 + b^2 + c^2)$).
* **Weighted Distance Loci (Ex. 14):** The locus of points whose weighted difference of squared distances $m AC^2 - n BC^2$ is constant is an Apollonian circle or straight line.

----

2. Structured Decompositions
----------------------------

Outer Squares Flank Identity (Ex. 13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Arbitrary triangle $\triangle ABC$ with squares erected on sides $BC, CA, AB$.
* **Construct:** Join the adjacent outer corners to form the three flank segments $d_a, d_b, d_c$.
* **Demonstrate:** In flank triangle at vertex $C$, the angle is $180^\circ - C$. By the generalized Law of Cosines (Euclid II.12), $d_c^2 = a^2 + b^2 + 2ab\cos C$. Since $c^2 = a^2 + b^2 - 2ab\cos C$ (Euclid II.13), we have $d_c^2 + c^2 = 2(a^2 + b^2)$, or $d_c^2 = 2a^2 + 2b^2 - c^2$. Summing cyclically over all three vertices:
  $$
  d_a^2 + d_b^2 + d_c^2 = (2b^2 + 2c^2 - a^2) + (2c^2 + 2a^2 - b^2) + (2a^2 + 2b^2 - c^2) = 3(a^2 + b^2 + c^2).
  $$
* **Invariants:**
  - Ratio $(d_a^2 + d_b^2 + d_c^2) / (a^2 + b^2 + c^2) \equiv 3$ for every planar triangle.
  - On canonical Heronian $(15, 13, 14)$: $a^2 + b^2 + c^2 = 225 + 169 + 196 = 590$, so $d_a^2 + d_b^2 + d_c^2 = 1770$.
