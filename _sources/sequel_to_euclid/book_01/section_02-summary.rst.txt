:title: Book I, Section II Summary — Exercises
:layout: book
:canonical_id: Book I, Section II Summary
:order: 2
:tracks: English: section_02-en | Summary: section_02-summary | Notes: section_02-notes

.. _casey-book-01-sec-02-summary:

Book I, Section II Summary: Exercises
=====================================

.. rubric:: Structured Decomposition & Invariant Ledger for Casey's Book I Section II Exercises (pp. 17–20)

1. Architectural Overview
-------------------------

The exercises of Book I extend the core propositions to key geometric configurations:

* **Angle Bisectors & Incentre / Excentres (Ex. 8–10):** The concurrency of the three internal angle bisectors at the Incentre $I = X(1)$, and of two external bisectors with the third internal bisector at each Excentre ($I_a, I_b, I_c$).
* **Orthic Triangle Perimeter Extremum (Ex. 31):** The orthic triangle formed by joining the feet of the altitudes $D_a, D_b, D_c$ has the minimum perimeter of all triangles inscribed in an acute triangle (Fagnano's problem).
* **Mean Centre Vector Sums & Projections (Ex. 33–34, 45–46):** Summation identities for unweighted and weighted collinear systems, establishing the linear projection invariance of barycentres.

----

2. Structured Decompositions
----------------------------

Incentre & Excentres Concurrency (Ex. 8–9)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Arbitrary triangle $\triangle ABC$ with internal angle bisectors and external angle bisectors.
* **Construct:** Let the internal bisectors of $\angle A$ and $\angle B$ meet at $I$. Drop perpendiculars $I P_a, I P_b, I P_c$ to $BC, CA, AB$.
* **Demonstrate:** By Euclid ``I.26``, triangles $\triangle I P_c A \cong \triangle I P_b A$ and $\triangle I P_c B \cong \triangle I P_a B$; hence $I P_a = I P_b = I P_c$. The right triangles $\triangle I P_a C$ and $\triangle I P_b C$ share hypotenuse $IC$ and have equal legs; therefore $\angle I C P_a = \angle I C P_b$, so $IC$ bisects $\angle C$. For excentres, taking one internal and two external bisectors yields equal distances to the three sides outside the triangle.
* **Invariants:**
  - Inradius $r = \Delta / s$; exradii $r_a = \Delta / (s - a)$, etc.
  - On canonical Heronian $(15, 13, 14)$: Incentre $I = (6, 4), r = 4$.
