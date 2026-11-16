:title: Book VI, Section IV Summary — Theory of Inversion
:layout: book
:canonical_id: Book VI, Section IV Summary
:order: 4
:tracks: English: section_04-en | Summary: section_04-summary | Notes: section_04-notes

.. _casey-book-06-sec-04-summary:
.. _sequel-unit-4-summary:

Book VI, Section IV Summary: Theory of Inversion
================================================

.. rubric:: Mathematical Synthesis of Casey's Book VI, Section IV (pp. 95–112)

1. Crown Jewels of Casey's Theory of Inversion
----------------------------------------------

Section IV contains the mathematical climax of Casey's treatise:

* **Conformal Circle Inversion (Props. 1–3):** $P \mapsto O + \frac{k^2}{|OP|^2}(P - O)$ linearizes circles through $O$, fixes orthogonal circles globally, preserves angles and cross-ratios, and transforms circles not through $O$ into circles with $O$ as a centre of similitude.
* **Invariant Bitangent Quadrances (Prop. 9):** If two circles invert into two circles, their direct common tangents satisfy $\frac{t_{12}^2}{r_1 r_2} = \frac{t_{12}'^{\,2}}{r_1' r_2'}$.
* **Pappus's Ancient Arbelos Chain (Prop. 9 Cor. 1):** In the shoemaker's knife, inverting from the common cusp straightens the boundary semicircles into parallel lines, proving that the height of the $n$-th inscribed circle equals $2n$ times its radius ($h_n = 2 n r_n$).
* **Casey's Generalized Ptolemy Theorem (1866, Prop. 10):** Four circles tangent to a fifth satisfy $\overline{12} \cdot \overline{34} + \overline{14} \cdot \overline{23} = \overline{13} \cdot \overline{24}$, proved in six lines by inverting from a contact point on the fifth circle into Euler's collinear four-point identity!
* **Feuerbach's Theorem at $F_e = X(11)$ (Prop. 10 Cor. 2):** Proved both algebraically (as the point-circle midpoint specialization $\frac{1}{4}[a(c-b) + b(a-c) - c(a-b)] = 0$ of Casey's Theorem) and synthetically (via Casey's 1861 orthogonal circle $(M_a, \frac{1}{2}|b-c|)$ inverting the fourth common tangent $[C T_s]$ of $(I)$ and $(I_a)$ onto the Nine-Points Circle!).
* **Hart's Extension (Prop. 11):** Any circular triangle has four Apollonius circles touched by a fourth circle—Hart's Circle.
* **Bicentric Quadrilateral Relation (Prop. 14):** Inscribed in radius $R$ and circumscribed about $r$ with centre distance $\delta$, $\frac{1}{(R+\delta)^2} + \frac{1}{(R-\delta)^2} = \frac{1}{r^2}$ (Durège / R. F. Davis).
* **Four Mutually Orthogonal Circles (Props. 15–16):** Successive inversions in four mutually orthogonal circles return any figure to itself, reducing bicircular quartics to elliptic integrals.

----

2. Verified Exact Symbolic Ledgers (:mod:`geometor.casey.feuerbach`)
---------------------------------------------------------------------

.. list-table:: Exact Feuerbach Coordinates Verified in ``geometor.casey``
   :header-rows: 1
   :widths: 34 32 34

   * - Theorem / Element
     - Symbol
     - Exact Symbolic Value
   * - Incentre & Inradius on $(15, 13, 14)$
     - $I = X(1), \; r$
     - $I = (6, 4), \; r = 4$
   * - Nine-Points Centre & Radius
     - $N = X(5), \; R_9$
     - $N = \left(6, \frac{63}{16}\right), \; R_9 = \frac{65}{16}$
   * - Internal Centre Distance
     - $|N I| = R_9 - r$
     - $\frac{1}{16} = \frac{65}{16} - 4$
   * - **Feuerbach Point**
     - $F_e = X(11)$
     - $F_e = (6, 8)$
   * - Three Excircle Feuerbach Touch Points
     - $F_a, \; F_b, \; F_c$
     - $\left(\frac{2709}{289}, \frac{1792}{289}\right), \; \left(\frac{553}{233}, \frac{1344}{233}\right), \; \left(\frac{1672}{257}, -\frac{24}{257}\right)$
   * - Casey Orthogonal Circle & Contact Inverse
     - $(M_a, T_a), \; T_s \mapsto F_e$
     - Centre $\left(\frac{19}{2}, 6\right)$, radius $\frac{1}{2}$; $T_s = \left(\frac{614}{65}, \frac{392}{65}\right) \mapsto (6, 8)$
