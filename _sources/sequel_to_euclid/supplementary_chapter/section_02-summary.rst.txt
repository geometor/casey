:title: Supplementary Chapter, Section II Summary — Spiral Similarity & Brocard Points
:layout: book
:canonical_id: Supplementary Chapter, Section II Summary
:order: 2
:folio: 0199–0204 (p. 173–178)
:tracks: English: section_02-en | Summary: section_02-summary | Notes: section_02-notes

.. _casey-supp-sec-02-summary:
.. _sequel-unit-6-summary:

Supplementary Chapter, Section II Summary: Two Figures Directly Similar & Brocard Points
========================================================================================

.. rubric:: Mathematical Synthesis of Casey's Supplementary Chapter, Section II (pp. 173–178)

.. folio:: 0199
   :page: 173

1. Spiral Similarity & The Brocard Invariants
---------------------------------------------

Section II establishes the synthetic theory of **two directly similar plane figures** and derives the **Brocard Points** $(\Omega, \Omega')$ as canonical double points:

* **Brocard Angle $\omega$:** Governed purely by rational quadratic invariants via $\cot\omega = \frac{a^2 + b^2 + c^2}{4\Delta}$ and Heron's identity $(a^2+b^2+c^2)^2 + 16\Delta^2 = 4(a^2 b^2 + b^2 c^2 + c^2 a^2)$:

  $$
  \sin^2\omega = \frac{4\Delta^2}{a^2 b^2 + b^2 c^2 + c^2 a^2}, \qquad \csc^2\omega = \frac{1}{\sin^2 A} + \frac{1}{\sin^2 B} + \frac{1}{\sin^2 C}.
  $$

* **Bicentric Brocard Pair $(\Omega, \Omega')$ (f. ``0203``):** Homogeneous barycentrics $\Omega = \left(\frac{1}{b^2} : \frac{1}{c^2} : \frac{1}{a^2}\right)$ and $\Omega' = \left(\frac{1}{c^2} : \frac{1}{a^2} : \frac{1}{b^2}\right)$, whose midpoint $X(39)$ lies on diameter $[OK]$.

----

.. folio:: 0203
   :page: 177

2. Verified Exact Ledger on $\triangle ABC$ $(15, 13, 14)$ (:mod:`geometor.casey.brocard`)
------------------------------------------------------------------------------------------

Constructed in :func:`~geometor.casey.brocard.construct_brocard_and_lemoine_circles`:

.. list-table:: Exact Rational Brocard Pair & Angle Invariants on $(15, 13, 14)$
   :header-rows: 1
   :widths: 34 26 40

   * - Geometric Object
     - Symbol
     - Exact Symbolic Value
   * - Brocard Cotangent & Sine-Squared
     - $\cot\omega, \; \sin^2\omega$
     - $\cot\omega = \frac{295}{168}, \quad \sin^2\omega = \frac{28224}{115249}$
   * - **First Brocard Point**
     - $\Omega$
     - $\left(\frac{697970}{115249}, \frac{397488}{115249}\right)$
   * - **Second Brocard Point**
     - $\Omega'$
     - $\left(\frac{684236}{115249}, \frac{529200}{115249}\right)$
   * - Brocard Midpoint
     - $X(39) = \frac{1}{2}(\Omega + \Omega')$
     - Midpoint of the bicentric pair on $[OK]$
