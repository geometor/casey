:layout: book
:title: Unit 2 Summary — Circle Power, Radical Axis & Coaxal Pencils

.. _sequel-unit-2-summary:

Unit 2 Summary: Power of a Point, Orthogonal Circles & Coaxal Pencils
=====================================================================

.. rubric:: Mathematical Synthesis of Casey's Book III (Props. 20–24, 28) & Book VI, Section V

1. Algebraic & Synthetic Invariants
-----------------------------------

Unit 2 develops the quadratic algebra of circles over the Euclidean plane:

* **Power of a Point:** $\operatorname{pow}(P, C) = (x_P - h)^2 + (y_P - k)^2 - r^2$. Positive outside $C$ ($= |PT|^2$), zero on $C$, negative inside $C$ ($= -PA \cdot PB$).
* **Orthogonality Criterion:** $C_1 \perp C_2 \iff |O_1 O_2|^2 = r_1^2 + r_2^2 \iff \operatorname{pow}(O_1, C_2) = r_1^2$.
* **Radical Axis as Linear Difference:** Subtracting $C_2(x, y) = 0$ from $C_1(x, y) = 0$ eliminates $x^2 + y^2$, yielding the linear radical axis $2(h_2 - h_1)x + 2(k_2 - k_1)y + (h_1^2 + k_1^2 - r_1^2) - (h_2^2 + k_2^2 - r_2^2) = 0$.
* **Casey's Difference-of-Powers Identity (III.24):** Choosing coordinates with line of centres along the $x$-axis and radical axis at $x = 0$, every circle in the coaxal pencil takes the canonical form

  $$
  x^2 + y^2 - 2\lambda x + \delta = 0,
  $$

  where $\operatorname{pow}(P, C_\lambda) - \operatorname{pow}(P, C_\mu) = 2(\mu - \lambda)x_P = 2\,|O_\mu O_\lambda|\cdot PN$. When $\delta = \ell^2 > 0$, the pencil is non-intersecting with real **Poncelet Limiting Points** $L_1 = (-\ell, 0)$ and $L_2 = (+\ell, 0)$ at $\lambda = \mp\ell$, and every circle $x^2 + y^2 - 2\eta y - \ell^2 = 0$ centered on $x = 0$ passes through $L_1, L_2$ and cuts every $C_\lambda$ orthogonally!

----

2. Verified Exact Construction Ledger (:mod:`geometor.casey.coaxial`)
---------------------------------------------------------------------

Constructed in :func:`~geometor.casey.coaxial.construct_radical_axis_and_coaxial_pencil` (`0069.g1.svg`):

.. list-table:: Exact Coaxal Pencil & Limiting-Point Parameters
   :header-rows: 1
   :widths: 34 33 33

   * - Geometric Element
     - Symbol / Equation
     - Exact Rational Coordinates
   * - Given Non-Intersecting Circles
     - $C_1 = (O_1, 6), \; C_2 = (O_2, 15)$
     - $O_1 = (-10, 0), \; O_2 = (17, 0)$ ($\delta = 64$)
   * - Third Pencil Member
     - $C_3 = (O_3, 6)$
     - $O_3 = (10, 0)$ ($10^2 - 6^2 = 64$)
   * - Auxiliary Secant Circle
     - $C_{\text{aux}} = ((2, 8), 10)$
     - Meets $C_1, C_2$ in rational chords concurring at $R_c$
   * - Radical Centre & Radical Axis
     - $R_c, \; [D R_c]$
     - $R_c = (0, -6), \; x = 0, \; D = (0, 0)$
   * - Tangent Contact on $C_1$ from $D$
     - $T_1, \; H$
     - $T_1 = \left(-\frac{32}{5}, \frac{24}{5}\right), \; H = \left(-\frac{32}{5}, 0\right), \; |DT_1| = 8$
   * - Poncelet Limiting Points
     - $L_1, \; L_2$
     - $L_1 = (-8, 0), \; L_2 = (8, 0)$
   * - Conjugate Orthogonal Circle
     - $(R_c, L_1)$
     - Centre $(0, -6)$, radius $10$ ($C_{\perp} \perp C_1, C_2, C_3$)
