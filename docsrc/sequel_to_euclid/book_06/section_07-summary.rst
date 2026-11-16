:title: Book VI, Section VII Summary — Poles, Polars & Reciprocation
:layout: book
:canonical_id: Book VI, Section VII Summary
:order: 7
:tracks: English: section_07-en | Summary: section_07-summary | Notes: section_07-notes

.. _casey-book-06-sec-07-summary:
.. _unit-4-poles-polars-summary:

Book VI, Section VII Summary: Poles, Polars & Reciprocation
===========================================================

.. rubric:: Mathematical Synthesis of Casey's Book VI, Section VII (pp. 141–147)

1. Key Theorems of Polar Duality & Reciprocation
------------------------------------------------

Section VII establishes the projective duality of poles and polars with respect to a circle:

* **Anharmonic Equivalence (Prop. 1):** The cross-ratio of four collinear points equals the cross-ratio of their four polars: $(A, B; C, D) = (a, b; c, d)$.
* **Self-Conjugate Triangles (Prop. 1.1):** If two triangles are self-conjugate with respect to a circle, any two sides are divided equianharmonically by the four remaining sides, and any two vertices are subtended equianharmonically by the four remaining vertices.
* **Perspective of Polar Triangles (Prop. 1.2):** If two triangles are such that the sides of one are the polars of the vertices of the other, they are in perspective (homologous).
* **Locus of Pole (Prop. 2):** If two variable points on fixed lines subtend a constant angle at the centre $O$ of circle $X$, the locus of the pole of their join is a circle.
* **Homographic Systems (Prop. 3):** For two homographic systems of points on two lines, there exist two points at each of which corresponding points subtend equal angles.
* **Harmonic Envelope and Tangent Invariance (Prop. 3.2):** Any four fixed tangents to a circle are cut by any fifth variable tangent in four points whose anharmonic ratio is constant.
* **Involution of Quadrilateral Rays (Prop. 3.3):** Lines drawn from any variable point in the plane of a quadrilateral to the six points of intersection of its four sides form a pencil in involution (dual of Section VI Prop. 9.1).
* **Brianchon's Theorem (Prop. 3.6):** If a hexagon be described about a circle, the three lines joining opposite angular points are concurrent (reciprocal of Pascal's Theorem).
* **Parallel Homologous Rays (Prop. 3.7):** In two homographic pencils of rays, there exist two pairs of homologous rays that are parallel to each other.

----

2. Verified Exact Symbolic Ledgers (:mod:`geometor.casey.poles_polars`)
-----------------------------------------------------------------------

.. list-table:: Exact Pole–Polar Coordinates Verified in ``geometor.casey``
   :header-rows: 1
   :widths: 34 32 34

   * - Theorem / Element
     - Symbol
     - Exact Symbolic Value
   * - Base Circle & Pole–Polar Pair (`0071.g1`)
     - $x^2 + y^2 = 25, \; D \leftrightarrow [UV]$
     - $D = \left(\frac{15}{2}, \frac{5}{4}\right), \; 6x + y - 20 = 0$
   * - Self-Conjugate Triangle & Reciprocal Pole
     - $\triangle DUV, \; Q \in [UV]$
     - $U = (3, 2), \; V = \left(\frac{5}{3}, 10\right), \; Q = (4, -4)$
   * - Tangent Cross-Ratio Invariance
     - $(T_1, T_2; T_3, T_4)$
     - Preserved across all variable transverse tangents
   * - Brianchon Concurrence
     - $AD \cap BE \cap CF$
     - Concurrent Brianchon point dual to Pascal line
