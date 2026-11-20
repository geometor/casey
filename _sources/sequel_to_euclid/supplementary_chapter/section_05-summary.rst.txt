:title: Supplementary Chapter, Section V Summary — Brocard's Circle & Feuerbach's Theorem
:layout: book
:canonical_id: Supplementary Chapter, Section V Summary
:order: 5
:folio: 0220–0230 (p. 194–204)
:tracks: English: section_05-en | Summary: section_05-summary | Notes: section_05-notes

.. _casey-supp-sec-05-summary:

Supplementary Chapter, Section V Summary: Brocard's Circle & Feuerbach's Theorem
================================================================================

.. rubric:: Mathematical Synthesis of Casey's Supplementary Chapter, Section V (pp. 194–204)

.. folio:: 0220
   :page: 194

1. Seven-Point Brocard Circle & Similar-Figures Feuerbach Synthesis
-------------------------------------------------------------------

Section V applies the abstract machinery of Section IV to prove the two crowning circle-concurrency theorems of modern triangle geometry:

* **Seven-Point Brocard Circle (`(Ml O)` in `0220.g1.svg`):** Circle on diameter $[OK]$ passing through $O, K, \Omega, \Omega'$ and **Brocard's First Triangle** $A_1 = (a^2 : c^2 : b^2)$, $B_1 = (c^2 : b^2 : a^2)$, $C_1 = (b^2 : a^2 : c^2)$ (inversely similar to $\triangle ABC$ with scale $\sin\omega$ and identical Centroid $G$).
* **Circle of Similitude = Nine-Points Circle (ff. ``0227–0229``):** Applied to the three half-scale corner triangles $AB'C', A'BC', A'B'C$, Section IV yields nine concyclic points directly and gives a homothetic-similitude proof of **Feuerbach's Theorem** independent of circular inversion!

----

.. folio:: 0228
   :page: 202

2. Verified Exact Ledger on $\triangle ABC$ $(15, 13, 14)$ (:mod:`geometor.casey.brocard`)
------------------------------------------------------------------------------------------

Constructed in :func:`~geometor.casey.brocard.construct_brocard_and_lemoine_circles` (`0220.g1.svg`):

.. list-table:: Exact Rational Brocard Circle, Triangle A₁B₁C₁ & Antipodal Pair on $(15, 13, 14)$
   :header-rows: 1
   :widths: 34 26 40

   * - Geometric Object
     - Symbol / ETC Index
     - Exact Symbolic Value
   * - **Brocard's First Triangle**
     - $A_1, \; B_1, \; C_1$
     - $\left(\frac{3589}{590}, \frac{1014}{295}\right), \; \left(\frac{3491}{590}, \frac{270}{59}\right), \; \left(7, \frac{1176}{295}\right)$
   * - **Brocard Circle** (7 points)
     - $(M_L, \frac{1}{2}|OK|)$
     - Centre $\left(\frac{1869}{295}, \frac{19143}{4720}\right)$, $R_{\text{Br}}^2 = \frac{397657}{891136}$
   * - **Steiner Point**
     - $S_t = X(99)$
     - $\left(\frac{17253}{2353}, -\frac{9396}{2353}\right) \in (O, A)$
   * - **Tarry Point**
     - $T_r = X(98)$
     - $\left(\frac{15689}{2353}, \frac{115233}{9412}\right) \in (O, A), \quad \frac{S_t + T_r}{2} = O$
