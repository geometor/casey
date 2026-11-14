:title: Unit 5 Summary — Symmedians, Lemoine's Point & Lemoine Circles

.. _sequel-unit-5-summary:

Unit 5 Summary: Symmedian Geometry, Lemoine's Point & Lemoine Circles
=====================================================================

.. rubric:: Mathematical Synthesis of Casey's Supplementary Chapter, Sections I & III (Part 1)

1. Core Algebraic & Geometric Structure
---------------------------------------

Unit 5 opens Casey's celebrated *Supplementary Chapter on the Recent Elementary Geometry of the Triangle*:

* **Isogonal Transformation:** In homogeneous trilinear coordinates $(\alpha : \beta : \gamma)$, isogonal conjugation acts as componentwise inversion $(1/\alpha : 1/\beta : 1/\gamma)$; in barycentric coordinates $(u : v : w)$, it acts as $(a^2/u : b^2/v : c^2/w)$.
* **Lemoine's Symmedian Point $K = X(6)$:** Mapping the Centroid $G = (1 : 1 : 1)$ under isogonal conjugation yields $K = (a^2 : b^2 : c^2)$, whose trilinear distances $(x, y, z) = \frac{2\Delta}{a^2+b^2+c^2}(a, b, c)$ minimize $x^2 + y^2 + z^2$.
* **Lemoine's Two Six-Point Circles:**
  - **First Lemoine Circle (`(Ml D1)`):** Cut by the three **parallels** to the sides through $K$; centered at $M_L = X(182) = \operatorname{midpoint}(O, K)$ with side chords $\frac{a^3}{a^2+b^2+c^2}, \frac{b^3}{a^2+b^2+c^2}, \frac{c^3}{a^2+b^2+c^2}$ in triplicate ratio $a^3 : b^3 : c^3$.
  - **Cosine (Second Lemoine) Circle (`(K Cb2)`):** Cut by the three **antiparallels** to the sides through $K$; centered at $K$ itself with radius $R\tan\omega = \frac{abc}{a^2+b^2+c^2}$ and side chords proportional to $\cos A : \cos B : \cos C$.

----

2. Verified Exact Ledger on $\triangle ABC$ $(15, 13, 14)$ (:mod:`geometor.casey.brocard`)
------------------------------------------------------------------------------------------

Constructed in :func:`~geometor.casey.brocard.construct_symmedian_and_lemoine_circles` (`0205.g1.svg`):

.. list-table:: Exact Rational Symmedian & Lemoine Circle Quantities on $(15, 13, 14)$
   :header-rows: 1
   :widths: 36 30 34

   * - Geometric Object
     - Symbol
     - Exact Symbolic Value
   * - Sum of Squares of Sides
     - $a^2 + b^2 + c^2$
     - $15^2 + 13^2 + 14^2 = 590$
   * - **Lemoine / Symmedian Point**
     - $K = X(6)$
     - $\left(\frac{1673}{295}, \frac{1176}{295}\right)$
   * - Minimum Squared-Distance Sum
     - $d_a^2 + d_b^2 + d_c^2$
     - $\frac{4\Delta^2}{a^2+b^2+c^2} = \frac{14112}{295}$
   * - **First Lemoine Circle Centre**
     - $M_L = X(182)$
     - $\left(\frac{1869}{295}, \frac{19143}{4720}\right)$
   * - First Lemoine Squared Radius
     - $R_{L_1}^2$
     - $\frac{19477081}{891136}$
   * - Triplicate-Ratio Chords
     - $|D_1 D_2| : |E_1 E_2| : |F_1 F_2|$
     - $3375 : 2197 : 2744 = 15^3 : 13^3 : 14^3$
   * - **Cosine Circle Squared Radius**
     - $R_{\cos}^2 = R^2 \tan^2\omega$
     - $\left(\frac{273}{59}\right)^2 = \frac{74529}{3481}$
