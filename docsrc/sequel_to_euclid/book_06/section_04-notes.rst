:title: Book VI, Section IV Notes — Casey (1861, 1866) & Hart (1861)
:layout: book
:canonical_id: Book VI, Section IV Notes
:order: 4
:folio: 0121–0138 (p. 95–112)
:tracks: English: section_04-en | Summary: section_04-summary | Notes: section_04-notes

.. _casey-book-06-sec-04-notes:
.. _sequel-unit-4-notes:

Book VI, Section IV Notes: Casey's Dublin Memoirs & Hart's Circle
=================================================================

.. rubric:: Historical Context of Casey's Discoveries & Cross-Canon Links

.. folio:: 0121
   :page: 95

1. John Casey's Two Famous Memoirs (1861 & 1866)
------------------------------------------------

Section IV preserves **John Casey's own most celebrated contributions to pure mathematics**, integrated directly into his text:

* **1861 Feuerbach Inversion Proof (:cite:`QJM 4, 1861 <casey:1861:feuerbach>`):** When :person:`Karl Wilhelm Feuerbach <feuerbach>` proved his nine-point tangency theorem in :cite:`1822 <feuerbach:1822>`, his proof relied on heavy trigonometric computation. While still an undergraduate pensioner at Trinity College Dublin in 1860–1861, Casey noticed that the circle centered at $M_a$ of radius $\frac{1}{2}|b-c|$ cuts $(I)$ and $(I_a)$ orthogonally and inverts their fourth common tangent into the Nine-Points Circle! Immediately upon seeing Casey's proof, Trinity Vice-Provost :person:`Andrew Searle Hart <hart>` extended it to three arbitrary circles (:cite:`QJM 4, 1861 <hart:1861>`), discovering **Hart's Circle** (Book VI, Sec. IV, Prop. 11).
* **1866 Generalized Ptolemy Theorem (:cite:`Proc. R.I.A. 9, 1866 <casey:1866:circles>`):** Five years later, Casey discovered the bitangent criterion $\overline{12}\cdot\overline{34} \pm \overline{14}\cdot\overline{23} \pm \overline{13}\cdot\overline{24} = 0$ while investigating systems of circles touching three fixed circles on the plane and sphere—turning Feuerbach's theorem into a three-line algebraic corollary! Note that for sufficiency, modern expositions (Zacharias, Altshiller-Court § 502) specify compatible contact orientations (signed radii), which :func:`~geometor.casey.feuerbach.prove_casey_theorem_symbolic` verifies explicitly for both internal incircle and external excircle cases.

2. Cross-Canon Links (`etc`, `pappus`)
--------------------------------------

* **Kimberling's ETC (`geometor/etc`):** The Feuerbach Point $F_e = X(11)$ has homogeneous barycentric coordinates $((b-c)^2(s-a) : (c-a)^2(s-b) : (a-b)^2(s-c))$. On our canonical $(15, 13, 14)$ triangle ($s = 21, s-a = 6, s-b = 8, s-c = 7$), these evaluate to $(1\cdot 6 : 1\cdot 8 : 4\cdot 7) = (3 : 4 : 14)$, yielding $\frac{3(0,0) + 4(14,0) + 14(5,12)}{21} = (6, 8)$—in 100% agreement with both the ray intersection of $[NI]$ ($x = 6$) with $(I, 4)$ and Casey's orthogonal inversion of $T_s = \left(\frac{614}{65}, \frac{392}{65}\right)$ in $(M_a, \frac{1}{2})$!
* **Pappus's Arbelos (`geometor/pappus`):** Proposition 9, Corollary 1 provides the modern inversion proof of Pappus of Alexandria's ancient shoemaker's knife theorem (*Synagoge*, Book IV), establishing that the $n$-th circle in the arbelos chain has centre height $2n r_n$.
