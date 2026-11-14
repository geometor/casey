:title: Unit 6 Summary — Brocard Circle, Steiner, Tarry & Longchamps

.. _sequel-unit-6-summary:

Unit 6 Summary: Brocard Geometry, Tucker/Taylor Circles & Associated Triangle Points
====================================================================================

.. rubric:: Mathematical Synthesis of Casey's Supplementary Chapter, Sections II–VII & Misc. Exercises

1. Unified Brocard–Steiner–Tarry Architecture
---------------------------------------------

Unit 6 completes the *Supplementary Chapter* by uniting spiral similarity, isogonal bicentric pairs, and circumcircle concurrencies:

* **Brocard Angle $\omega$:** Governed purely by rational quadratic invariants via $\cot\omega = \frac{a^2 + b^2 + c^2}{4\Delta}$ and Heron's identity $(a^2+b^2+c^2)^2 + 16\Delta^2 = 4(a^2 b^2 + b^2 c^2 + c^2 a^2)$:

  $$
  \sin^2\omega = \frac{4\Delta^2}{a^2 b^2 + b^2 c^2 + c^2 a^2}, \qquad \csc^2\omega = \frac{1}{\sin^2 A} + \frac{1}{\sin^2 B} + \frac{1}{\sin^2 C}.
  $$

* **Bicentric Brocard Pair $(\Omega, \Omega')$:** Homogeneous barycentrics $\Omega = \left(\frac{1}{b^2} : \frac{1}{c^2} : \frac{1}{a^2}\right)$ and $\Omega' = \left(\frac{1}{c^2} : \frac{1}{a^2} : \frac{1}{b^2}\right)$, whose midpoint $X(39)$ is the Brocard Midpoint on $[OK]$.
* **Seven-Point Brocard Circle:** Circle on diameter $[OK]$ passing through $O, K, \Omega, \Omega'$ and Brocard's First Triangle $A_1 = (a^2 : c^2 : b^2)$, $B_1 = (c^2 : b^2 : a^2)$, $C_1 = (b^2 : a^2 : c^2)$.
* **Antipodal Circumcircle Pair $(S_t, T_r)$:** Parallels and perpendiculars from $A, B, C$ to $\triangle A_1 B_1 C_1$ concur by Thales's theorem (Euclid ``III.31``) at diametrically opposite points on the circumcircle: **Steiner's Point** $X(99) = \left(\frac{1}{b^2 - c^2} : \frac{1}{c^2 - a^2} : \frac{1}{a^2 - b^2}\right)$ and **Tarry's Point** $X(98)$.

----

2. Verified Exact Ledger on $\triangle ABC$ $(15, 13, 14)$ (:mod:`geometor.casey.brocard`)
------------------------------------------------------------------------------------------

Constructed in :func:`~geometor.casey.brocard.construct_brocard_and_lemoine_circles` (`0220.g1.svg`):

.. list-table:: Exact Rational Brocard, Steiner, Tarry & Longchamps Coordinates on $(15, 13, 14)$
   :header-rows: 1
   :widths: 34 26 40

   * - Geometric Object
     - Symbol / ETC Index
     - Exact Rational Value
   * - Brocard Cotangent & Sine-Squared
     - $\cot\omega, \; \sin^2\omega$
     - $\cot\omega = \frac{295}{168}, \quad \sin^2\omega = \frac{28224}{115249}$
   * - **First Brocard Point**
     - $\Omega$
     - $\left(\frac{697970}{115249}, \frac{397488}{115249}\right)$
   * - **Second Brocard Point**
     - $\Omega'$
     - $\left(\frac{684236}{115249}, \frac{529200}{115249}\right)$
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
   * - **de Longchamps Point**
     - $L = X(20) = 2O - H$
     - $\left(9, \frac{9}{2}\right)$
