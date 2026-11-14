:title: Unit 4 Summary — Inversion, Casey's Theorem, Feuerbach & Polar Duality

.. _sequel-unit-4-summary:

Unit 4 Summary: Inversion, Casey's Theorem, Feuerbach & Polar Reciprocity
=========================================================================

.. rubric:: Mathematical Synthesis of Casey's Book VI, Sections IV & VII and Book III Props. 25, 27

1. Crown Jewels of Casey's *Sequel*
-----------------------------------

Unit 4 contains the mathematical climax of Casey's treatise:

* **Conformal Circle Inversion:** $P \mapsto O + \frac{k^2}{|OP|^2}(P - O)$ linearizes circles through $O$, fixes orthogonal circles globally, preserves angles and cross-ratios, and leaves normalized bitangent quadrances $t_{12}^2 / (r_1 r_2)$ invariant.
* **Casey's Generalized Ptolemy Theorem (1866):** Four circles tangent to a fifth satisfy $t_{12} t_{34} \pm t_{14} t_{23} \pm t_{13} t_{24} = 0$, proved in six lines by inverting from a contact point on the fifth circle into Euler's collinear four-point identity!
* **Feuerbach's Theorem at $F_e = X(11)$:** Proved both algebraically (as the point-circle midpoint specialization $\frac{1}{4}[a(c-b) + b(a-c) - c(a-b)] = 0$ of Casey's Theorem) and synthetically (via Casey's 1861 orthogonal circle $(M_a, \frac{1}{2}|b-c|)$ inverting the fourth common tangent $[C T_s]$ of $(I)$ and $(I_a)$ onto the Nine-Points Circle!).
* **Pole–Polar Bilinear Duality:** $(x_0 - h)(x - h) + (y_0 - k)(y - k) = r^2$ is symmetric in $(x_0, y_0) \leftrightarrow (x, y)$, immediately establishing La Hire's Reciprocity, self-conjugate triangles $\triangle DUV$, and polar reciprocation (Pascal $\leftrightarrow$ Brianchon).

----

2. Verified Exact Symbolic Ledgers (:mod:`geometor.casey.feuerbach` & :mod:`geometor.casey.poles_polars`)
---------------------------------------------------------------------------------------------------------

.. list-table:: Exact Feuerbach & Pole–Polar Coordinates Verified in ``geometor.casey``
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
   * - Base Circle & Pole–Polar Pair (`0071.g1`)
     - $x^2 + y^2 = 25, \; D \leftrightarrow [UV]$
     - $D = \left(\frac{15}{2}, \frac{5}{4}\right), \; 6x + y - 20 = 0$
   * - Self-Conjugate Triangle & Reciprocal Pole
     - $\triangle DUV, \; Q \in [UV]$
     - $U = (3, 2), \; V = \left(\frac{5}{3}, 10\right), \; Q = (4, -4)$
