:title: Book IV, Section I Summary — Additional Propositions
:layout: book
:canonical_id: Book IV, Section I Summary
:order: 1
:folio: 0079–0089 (p. 53–63)
:tracks: English: section_01-en | Summary: section_01-summary | Notes: section_01-notes

.. _casey-book-04-sec-01-summary:

Book IV, Section I Summary: Additional Propositions
====================================================

.. rubric:: Structured Decomposition & Invariant Ledger for Casey's Book IV Section I (pp. 53–63)

.. folio:: 0079
   :page: 53

1. Architectural Overview
-------------------------

Section I extends Euclid's Book IV into the modern geometry of triangles and regular polygons:

* **Inscribed & Escribed Contact Segments and Radii Relations (Prop. 1):** Contact segments $s-a, s-b, s-c$; area relations $\Delta = rs = r'(s-a) = \sqrt{s(s-a)(s-b)(s-c)} = \sqrt{r\,r'\,r''\,r'''}$.
* **Metric Properties of Regular Polygons (Props. 2–4):**
  - Sum of perpendiculars from any interior point to sides of regular $n$-gon is $n R_{\text{in}}$.
  - Sum of perpendiculars from contact points to any tangent is $nR$.
  - Sum of squared distances from any point $P$ at distance $R'$ from centre is $n(R^2 + R'^2)$; on the circumference ($R'=R$), the sum is $2n R^2$.
* **The Nine-Points Circle (Prop. 5):** Concyclicity of the 3 side midpoints ($G, H, I$), the 3 altitude feet ($D, E, F$), and the 3 Euler midpoints ($K, L, M$) of $OA, OB, OC$.
* **Fourth Common Tangent to Escribed Circles (Prop. 6):** Constructing the transverse common tangent to two excircles touching the base produced without describing the circles.
* **Inversion & Feuerbach's Theorem (Prop. 7):**
  - The Nine-Points Circle is the inverse of the fourth common tangent with respect to the circle on the midpoint of the base cutting the excircles orthogonally (radius $\frac{b+c}{2}$).
  - *Feuerbach's Theorem:* The Nine-Points Circle touches the inscribed circle and the three escribed circles of the triangle.
* **Circumcircle Perpendicular Diameter Projections (Prop. 8):** Projections of vertical angle bisectors and side relations ($DL \cdot EF = \left(\frac{b+c}{2}\right)^2$, $EL \cdot FD = \left(\frac{b-c}{2}\right)^2$).
* **Incentre & Excentres as Centres of Mean Position (Prop. 9):**
  - Incentre $O$ is the mean centre of vertices $A, B, C$ for system of multiples $a, b, c$.
  - Excentres $O', O'', O'''$ are mean centres for $(-a, b, c)$, $(a, -b, c)$, and $(a, b, -c)$.

----

2. Structured Decompositions
----------------------------

The Nine-Points Circle (Prop. 5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Triangle $ABC$ with orthocentre $O$, feet of altitudes $D, E, F$, side midpoints $G, H, I$, and midpoint segments $K, L, M$ of $OA, OB, OC$.
* **Construct:** Join $HK, HG, IK, IG$.
* **Demonstrate:**
  - $HK \parallel CO$ and $HG \parallel AB$; since $CO \perp AB$, $\angle GHK = 90^\circ$.
  - Circle on diameter $GK$ passes through $H$, and similarly through $I$.
  - Since $\angle KDG = 90^\circ$, it also passes through altitude foot $D$.
  - By symmetry on diameters $HL$ and $IM$, the circle passes through all nine points $D, E, F; G, H, I; K, L, M$.
* **Invariants:**
  - Nine-points centre $N$ bisects the segment between circumcentre and orthocentre ($ON = NH$).
  - Nine-points radius $R_9 = \frac{1}{2} R$.

Feuerbach's Theorem via Inversion (Prop. 7)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Triangle $ABC$, its incircle and three excircles, and the midpoint $D$ of base $BC$.
* **Construct:** Circle centred at $D$ with radius $DG = \frac{1}{2}(b+c)$ cutting the two excircles touching $BC$ produced orthogonally.
* **Demonstrate:**
  - The fourth common tangent $HI$ is shown to have inverse points lying on the Nine-Points Circle.
  - Since inversion preserves tangency and the orthogonal circle leaves the excircles invariant, the inverse of the fourth common tangent (the Nine-Points Circle) must touch both excircles.
  - Extending to the incircle and the third excircle via the difference circle (radius $\frac{1}{2}|b-c|$) completes the proof of contact with all four tritangent circles.

----

3. Canonical Heronian Ledger on $\triangle ABC$ $(15, 13, 14)$
--------------------------------------------------------------

Verified on $a=14, b=15, c=13$:

.. list-table:: Exact Rational Coordinates & Radii on $(15, 13, 14)$
   :header-rows: 1
   :widths: 30 35 35

   * - Geometric Object
     - Casey Symbol
     - Exact Rational Value
   * - Semiperimeter & Area
     - $s, \Delta$
     - $s = 21, \; \Delta = 84$
   * - Inradius & Exradii
     - $r, r_a, r_b, r_c$
     - $r = 4, \; r_a = 12, \; r_b = 14, \; r_c = \frac{21}{2}$
   * - Circumradius
     - $R$
     - $R = \frac{65}{8}$
   * - Nine-Points Radius
     - $R_9 = \frac{1}{2}R$
     - $R_9 = \frac{65}{16}$
   * - Radii Product Relation
     - $\sqrt{r\,r_a\,r_b\,r_c}$
     - $\sqrt{4 \cdot 12 \cdot 14 \cdot \frac{21}{2}} = \sqrt{7056} = 84 = \Delta$
   * - Exradii Sum Relation
     - $r_a + r_b + r_c - r$
     - $12 + 14 + \frac{21}{2} - 4 = \frac{65}{2} = 4R$
