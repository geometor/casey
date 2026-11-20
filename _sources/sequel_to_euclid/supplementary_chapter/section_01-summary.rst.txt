:title: Supplementary Chapter, Section I Summary — Isogonal Conjugates & Symmedians
:layout: book
:canonical_id: Supplementary Chapter, Section I Summary
:order: 1
:folio: 0191–0199 (p. 165–173)
:tracks: English: section_01-en | Summary: section_01-summary | Notes: section_01-notes

.. _casey-supp-sec-01-summary:
.. _sequel-unit-5-summary:

Supplementary Chapter, Section I Summary: Isogonal Conjugates & Symmedians
==========================================================================

.. rubric:: Mathematical Synthesis of Casey's Supplementary Chapter, Section I (pp. 165–173)

.. folio:: 0191
   :page: 165

1. Core Algebraic & Geometric Structure
---------------------------------------

Section I opens Casey's *Supplementary Chapter on the Recent Elementary Geometry of the Triangle* with the projective-metric foundations of conjugates, antiparallels, and symmedians:

* **Isogonal Transformation (`0191.g1.svg`):** In homogeneous trilinear coordinates $(\alpha : \beta : \gamma)$, isogonal conjugation acts as componentwise inversion $(1/\alpha : 1/\beta : 1/\gamma)$; in barycentric coordinates $(u : v : w)$, it acts as $(a^2/u : b^2/v : c^2/w)$. Any point $P$ and its isogonal conjugate $Q$ share a single six-point **Pedal Circle** centered at $M_p = \frac{1}{2}(P + Q)$.
* **Isotomic Transformation (f. ``0193``):** Mapping $(u : v : w) \mapsto (1/u : 1/v : 1/w)$ swaps cevians symmetrically across side midpoints (pairing Gergonne $X(7)$ and Nagel $X(8)$).
* **Antiparallels & Symmedians (f. ``0195–0199``):** An antiparallel to $BC$ across $\angle A$ is parallel to the circumcircle tangent at $A$. The isogonal conjugate of median $AM_a$ bisects all antiparallels to $BC$ and divides $BC$ in ratio $c^2 : b^2$.
* **Lemoine's Symmedian Point $K = X(6)$:** Mapping the Centroid $G = (1 : 1 : 1)$ under isogonal conjugation yields $K = (a^2 : b^2 : c^2)$, whose trilinear distances $(x, y, z) = \frac{2\Delta}{a^2+b^2+c^2}(a, b, c)$ minimize $x^2 + y^2 + z^2$.

----

.. folio:: 0196
   :page: 170

2. Verified Exact Ledger on $\triangle ABC$ $(15, 13, 14)$ (:mod:`geometor.casey.brocard`)
------------------------------------------------------------------------------------------

Verified in :func:`~geometor.casey.brocard.construct_symmedian_and_lemoine_circles`:

.. list-table:: Exact Rational Symmedian & Conjugate Quantities on $(15, 13, 14)$
   :header-rows: 1
   :widths: 36 30 34

   * - Geometric Object
     - Symbol / ETC Index
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
   * - Centroid / Circumcentre / Orthocentre
     - $G = X(2), \; O = X(3), \; H = X(4)$
     - Isogonal pairs $(O, H)$ and $(G, K)$
