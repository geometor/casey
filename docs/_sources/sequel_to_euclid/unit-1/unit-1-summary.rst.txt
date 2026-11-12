:layout: book
:title: Unit 1 Summary — Triangles, Euler Line & Nine-Points Circle

.. _sequel-unit-1-summary:

Unit 1 Summary: Triangle Concurrency, Mean Centres, Medians & the Nine-Points Circle
====================================================================================

.. rubric:: Mathematical Synthesis of Casey's Books I, II & IV Extensions (pp. 1–63)

1. Architectural Overview
-------------------------

Unit 1 gathers :person:`John Casey's <casey>` foundational extensions to Euclid's Books I, II, and IV before circle-power and projective methods enter in Units 2–4:

* **Four Classical Triangle Concurrencies (Book I, Props. 9–11):** Internal/external angle bisectors meet at the Incentre $I = X(1)$ and Excentres $I_a, I_b, I_c$; perpendicular bisectors meet at the Circumcentre $O = X(3)$; altitudes meet at the Orthocentre $H = X(4)$ (proved via the circumscribed anticomplementary triangle); medians meet at the Centroid $G = X(2)$ in ratio $2:1$.
* **Weighted Mean Centres & Variational Extremes (Book I, Props. 17–22):** Casey introduces weighted barycentres $G = (\sum m_i P_i)/(\sum m_i)$ synthetically and proves Heron's reflection principle and the cyclic maximum-area property for polygons of given sides.
* **Quadratic Segment Identities (Book II, Props. 1–2, 7, 10):** :person:`Apollonius's <apollonius>` median theorem, :person:`Euler's <euler>` quadrilateral midpoint identity, Euler's collinear four-point identity $AB\cdot CD + BC\cdot AD = AC\cdot BD$, and :person:`Stewart's <stewart>` theorem $b^2 m + c^2 n = a(d^2 + mn)$.
* **The Euler Line & Nine-Points Circle (Book I Ex. 43; Book IV, Prop. 5):** Collinearity of $O, G, N, H$ with $HG = 2\,GO$ and $HN = NO$, and concyclicity of the nine remarkable points on $(N, R/2)$.

----

2. Canonical Heronian Ledger on $\triangle ABC$ $(15, 13, 14)$
--------------------------------------------------------------

Verified symbolically in :func:`~geometor.casey.feuerbach.construct_euler_nine_point` on $A = (0, 0), B = (14, 0), C = (5, 12)$:

.. list-table:: Exact Rational Coordinates & Radii on $(15, 13, 14)$
   :header-rows: 1
   :widths: 30 35 35

   * - Geometric Object
     - Kimberling / Casey Symbol
     - Exact Rational Value
   * - Area $\Delta$ & Semiperimeter $s$
     - $\Delta, s$
     - $\Delta = 84, \; s = 21$
   * - Circumcentre & Circumradius
     - $O = X(3), \; R$
     - $O = \left(7, \frac{33}{8}\right), \; R = \frac{65}{8}$
   * - Centroid
     - $G = X(2)$
     - $G = \left(\frac{19}{3}, 4\right)$
   * - Orthocentre
     - $H = X(4)$
     - $H = \left(5, \frac{15}{4}\right)$
   * - Nine-Points Centre & Radius
     - $N = X(5), \; R_9$
     - $N = \left(6, \frac{63}{16}\right), \; R_9 = \frac{65}{16}$
   * - Euler Line Equation
     - $[O H]$
     - $3x - 16y + 45 = 0$
   * - Side Midpoints
     - $M_a, M_b, M_c$
     - $\left(\frac{19}{2}, 6\right), \; \left(\frac{5}{2}, 6\right), \; (7, 0)$
   * - Altitude Feet
     - $D_a, D_b, D_c$
     - $\left(\frac{224}{25}, \frac{168}{25}\right), \; \left(\frac{350}{169}, \frac{840}{169}\right), \; (5, 0)$
   * - Euler Midpoints
     - $E_a, E_b, E_c$
     - $\left(\frac{5}{2}, \frac{15}{8}\right), \; \left(\frac{19}{2}, \frac{15}{8}\right), \; \left(5, \frac{63}{8}\right)$
