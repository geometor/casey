:title: Book VI, Section V Summary — Coaxal Circles
:layout: book
:canonical_id: Book VI, Section V Summary
:order: 5
:tracks: English: section_05-en | Summary: section_05-summary | Notes: section_05-notes

.. _casey-book-06-sec-05-summary:
.. _sequel-unit-2-summary:

Book VI, Section V Summary: Coaxal Circles
==========================================

.. rubric:: Mathematical Synthesis of Casey's Book VI, Section V (pp. 113–126)

1. Synthetic & Projective Foundations of Coaxal Systems
-------------------------------------------------------

Section V investigates systems of circles having a common radical axis and their profound connections to inversion, projectivity, and closure theorems:

* **Classification of Coaxal Systems (Props. 1–2):** Two circles $A, B$ determine an entire coaxial pencil. The system is intersecting (real common chord), touching (parabolic pencil), or non-intersecting (hyperbolic pencil) possessing two real **limiting points** $L, L'$ (Poncelet's *points limites*), which are point-circles (zero radius) of the system.
* **Conjugate Orthogonal Pencils (Prop. 3):** Every circle passing through the limiting points $L, L'$ cuts every circle of the coaxal system orthogonally. The coaxal system of intersecting circles through $L, L'$ is orthogonal and conjugate to the coaxal system of non-intersecting circles with limiting points $L, L'$.
* **Concurrency of Radical Axes (Prop. 4):** The radical axes of any three systems of coaxal circles, taken in pairs, are concurrent at a radical centre.
* **Line of Centres & Radical Axis (Prop. 5):** The line connecting the centres of two circles is perpendicular to their radical axis; the distance from the radical axis to the centre of any circle of the system is proportional to the difference of squares of its radius and tangent from the origin.
* **Inversion into Concentric Circles (Prop. 6):** Inverting a non-intersecting coaxal pencil from either of its limiting points $L$ transforms the entire coaxal system into a family of **concentric circles** centered at $L'$ (the inverse of the other limiting point)! Orthogonal circles passing through $L, L'$ invert into concurrent straight lines through the concentric centre.
* **Envelope of Circles Touching Two Fixed Circles (Props. 7–8):** A variable circle touching two fixed circles cuts their coaxal pencil at constant angles, and its chord of contact subtends a right angle at either limiting point.
* **Proportional Chord Division (Prop. 9):** Any line cuts the circles of a coaxal pencil in segments whose chords are divided harmonically and proportionally.
* **Apollonius' Problem of the Three Circles (Prop. 10):** Casey provides a direct, synthetic solution to Apollonius' ancient problem: the chords of contact of the tangent circles pass through the radical centres and poles of similitude, reducible by inversion or Newton's 16th Lemma.
* **Bitangent Ratio Invariance (Prop. 11):** The tangents $AA', BB'$ from variable points to two fixed circles of a coaxal system maintain a constant ratio depending only on their powers.
* **Poncelet's Closure Theorem (Prop. 12):** If a variable polygon of $n$ sides is inscribed in one circle of a coaxal system while $n-1$ of its sides touch other fixed circles of the system, its $n$-th side also touches a fixed circle of the system (proved via Jacobi's elliptic functions and Hart's celebrated elementary synthetic proof).

----

2. Verified Invariant Ledger (:mod:`geometor.casey.coaxial`)
------------------------------------------------------------

.. list-table:: Invariants of Coaxal Pencils & Limiting Points
   :header-rows: 1
   :widths: 35 30 35

   * - Geometric Element
     - Symbol / Formula
     - Analytical Invariant
   * - Canonical Pencil Equation
     - $x^2 + y^2 - 2\lambda x + \delta = 0$
     - Line of centres $y = 0$, Radical axis $x = 0$
   * - Limiting Points ($\delta > 0$)
     - $L_1, L_2 = (\mp \sqrt{\delta}, 0)$
     - Real point-circles ($r = 0$)
   * - Conjugate Orthogonal System
     - $x^2 + y^2 - 2\mu y - \delta = 0$
     - Pass through $L_1, L_2$, centres on $x = 0$
   * - Power Difference
     - $\operatorname{pow}(P, C_\lambda) - \operatorname{pow}(P, C_\mu)$
     - $2(\mu - \lambda)x_P$
   * - Inversion Centre
     - $L_1$
     - Maps pencil to concentric circles at $L_2'$
