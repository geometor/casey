:title: Book II, Section I Summary — Additional Propositions
:layout: book
:canonical_id: Book II, Section I Summary
:order: 1
:folio: 0047–0052 (p. 21–26)
:tracks: English: section_01-en | Summary: section_01-summary | Notes: section_01-notes

.. _casey-book-02-sec-01-summary:

Book II, Section I Summary: Additional Propositions
===================================================

.. rubric:: Structured Decomposition & Invariant Ledger for Casey's Book II Section I (pp. 21–26)

.. folio:: 0047
   :page: 21

1. Architectural Overview
-------------------------

Section I extends Euclid's geometric algebra (Book II) to metric quadratic relations in triangles, quadrilaterals, and general point configurations:

* **Apollonius's Median Theorem (Prop. 2):** In any triangle, the sum of the squares of two sides equals twice the square of half the base plus twice the square of the median ($b^2 + c^2 = 2 m_a^2 + \frac{1}{2} a^2$).
* **Euler's Quadrilateral Midpoint Identity (Prop. 4):** The sum of the squares of the four sides of any quadrilateral equals the sum of the squares of the two diagonals plus four times the square of the segment joining the midpoints of the diagonals ($\sum s_i^2 = d_1^2 + d_2^2 + 4\,EF^2$).
* **Difference of Squares Theorem (Prop. 5):** $b^2 - c^2 = 2 a \cdot d$, where $d$ is the distance between the midpoint and the altitude foot on the base.
* **Stewart's Theorem (Prop. 7):** For any cevian $d$ dividing base $a$ into segments $m$ and $n$, $b^2 m + c^2 n = a(d^2 + mn)$.
* **Leibniz's Moment Theorem (Prop. 10):** The quadratic moment of any point $P$ with respect to a weighted system equals the intrinsic moment with respect to the mean centre $O$ plus $(\sum m_i) PO^2$.

----

2. Structured Decompositions
----------------------------

Apollonius Median Theorem (Prop. 2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Triangle $\triangle ABC$ with median $A M_a$ ($B M_a = M_a C = \frac{1}{2} a$).
* **Construct:** Drop altitude $A D_a \perp BC$.
* **Demonstrate:** By Euclid ``II.12`` (obtuse triangle $\triangle A M_a B$ or $\triangle A M_a C$) and ``II.13`` (acute triangle),
  $c^2 = A M_a^2 + M_a B^2 + 2 M_a B \cdot M_a D_a$ and $b^2 = A M_a^2 + M_a C^2 - 2 M_a C \cdot M_a D_a$.
  Since $M_a B = M_a C = \frac{1}{2} a$, the rectangular projection terms cancel: $b^2 + c^2 = 2 A M_a^2 + 2\left(\frac{a}{2}\right)^2 = 2 m_a^2 + \frac{1}{2} a^2$.
* **Invariants:**
  - Length of median $m_a = \frac{1}{2}\sqrt{2 b^2 + 2 c^2 - a^2}$.
  - On canonical Heronian $(15, 13, 14)$ on base $c = 14$: $m_c = \sqrt{\frac{2(15^2) + 2(13^2) - 14^2}{4}} = \sqrt{148} = 2\sqrt{37}$.

Euler's Quadrilateral Identity (Prop. 4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Arbitrary planar quadrilateral $ABCD$ with diagonals $AC, BD$ and diagonal midpoints $E, F$.
* **Construct:** Join $AF, CF, EF$.
* **Demonstrate:** In $\triangle ABD$, median $AF$ gives $AB^2 + AD^2 = 2 AF^2 + 2 FB^2$. In $\triangle BCD$, median $CF$ gives $BC^2 + CD^2 = 2 CF^2 + 2 FB^2$.
  Summing gives $\sum s_i^2 = 2(AF^2 + CF^2) + 4 FB^2$. In $\triangle ACF$, median $EF$ gives $AF^2 + CF^2 = 2 AE^2 + 2 EF^2 = \frac{1}{2} AC^2 + 2 EF^2$.
  Substituting yields $\sum s_i^2 = AC^2 + BD^2 + 4 EF^2$.
* **Invariants:**
  - $EF = 0 \iff ABCD$ is a parallelogram, recovering Euclid / Casey Prop. 3 ($AC^2 + BD^2 = \sum s_i^2$).
