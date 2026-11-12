:layout: book
:title: Unit 1 — Books I, II & IV Extensions

.. _sequel-unit-1-en:

Unit 1: Books I, II & IV Extensions — Triangles, Euler Line, Medians & the Nine-Points Circle
=============================================================================================

.. rubric:: John Casey — *A Sequel to the First Six Books of the Elements of Euclid* (5th ed., 1888 / 6th ed., 1892)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

----

.. _unit-1-orthocentre:

.. folio:: 0033
   :page: 7

Book I — Additional Propositions on Concurrency & Centres of Mean Position
--------------------------------------------------------------------------

**Proposition 9.** *The three internal bisectors of the angles of a triangle meet in a point (the Incentre); and two external bisectors and the third internal bisector meet in an Excentre.*

**Demonstration.** Let the internal bisectors of $\angle A$ and $\angle B$ in :g:`△ABC <0083.g1:< A B C >>` meet at $I$. Dropping perpendiculars from $I$ upon $[AB]$, $[BC]$, $[CA]$, by Euclid ``I.26`` the perpendiculars to $[AB]$ and $[AC]$ are equal, and the perpendiculars to $[AB]$ and $[BC]$ are equal; hence the perpendiculars to $[AC]$ and $[BC]$ are equal, so $[CI]$ bisects $\angle C$.

.. folio:: 0034
   :page: 8

**Proposition 10.** *The three perpendicular bisectors of the sides of a triangle meet in a point* (:g:`O <0083.g1:O>`, *the Circumcentre).*

.. enunciation::

   **Proposition 10, Corollary (The Orthocentre).** *The three perpendiculars (altitudes) drawn from the vertices of a triangle to the opposite sides are concurrent at a single point* (:g:`H <0083.g1:H>`, *called the Orthocentre).*

**Demonstration.** Through the vertices :g:`A <0083.g1:A>`, :g:`B <0083.g1:B>`, :g:`C <0083.g1:C>` of :g:`△ABC <0083.g1:< A B C >>` draw straight lines parallel respectively to the opposite sides :g:`[BC] <0083.g1:[ B C ]>`, :g:`[CA] <0083.g1:[ C A ]>`, :g:`[AB] <0083.g1:[ A B ]>` (Euclid ``I.31``), forming the circumscribed anticomplementary triangle $\triangle A'B'C'$. Because $ABCB'$ and $ABA'C$ are parallelograms (Euclid ``I.34``), $A$ is the midpoint of $B'C'$, $B$ of $C'A'$, and $C$ of $A'B'$. Moreover, the altitudes :g:`[A Da] <0083.g1:[ A Da ]>`, :g:`[B Db] <0083.g1:[ B Db ]>`, :g:`[C Dc] <0083.g1:[ C Dc ]>` of $\triangle ABC$ are perpendicular to $B'C'$, $C'A'$, $A'B'$ at their midpoints $A, B, C$. Hence the altitudes of $\triangle ABC$ are the perpendicular bisectors of $\triangle A'B'C'$, and by Proposition 10 they concur at :g:`H <0083.g1:H>`. Q.E.D.

**Proposition 11 (Concurrency of the Medians).** *The three medians of a triangle joining its vertices to the middle points* :g:`Ma <0083.g1:Ma>`, :g:`Mb <0083.g1:Mb>`, :g:`Mc <0083.g1:Mc>` *of the opposite sides concur at the Centroid* :g:`G <0083.g1:G>`, *which trisects each median so that* $|AG| = 2\,|G M_a|$, $|BG| = 2\,|G M_b|$, $|CG| = 2\,|G M_c|$.

----

.. _unit-1-mean-centres:

.. folio:: 0038
   :page: 12

Theory of Centres of Mean Position & Maxima and Minima
------------------------------------------------------

.. enunciation::

   **Propositions 17–18 (Centre of Mean Position).** *If a system of coplanar points* $A_1, A_2, \dots, A_n$ *be affected with multiples (weights)* $m_1, m_2, \dots, m_n$ *whose sum* $M = \sum m_i \neq 0$, *there exists a unique point* $G$—*their* :term:`Centre of Mean Position <centre-of-mean-position>`—*such that the algebraic sum of the perpendiculars let fall from the points upon any straight line* $L$, *each multiplied by its corresponding weight, is equal to* $M$ *times the perpendicular from* $G$ *upon* $L$:

   $$
   \sum_{i=1}^{n} m_i \, p_i = \left(\sum_{i=1}^{n} m_i\right) p_G.
   $$

.. folio:: 0041
   :page: 15

**Propositions 19–22 (Elementary Maxima and Minima).**

1. **Reflection Principle (Heron's Shortest Path, Prop. 19):** *Of all triangles on the same base and having their vertices on a given straight line, that whose two sides make equal angles with the given line has the minimum perimeter.*
2. **Maximum Area on Given Base & Perimeter (Prop. 20):** *Of all triangles standing on the same base and of equal perimeter, the isosceles triangle has the greatest area.*
3. **Isoperimetric Polygon Principle (Props. 21–22):** *Of all polygons having given sides in order except one, the area is greatest when the polygon is inscribed in a semicircle with the undetermined side as diameter; and of all polygons having all sides given, the cyclic polygon has maximum area.*

.. folio:: 0046
   :page: 20

.. porism::

   **Book I, Miscellaneous Exercises 42–46 (The Euler Line).** *In any triangle* :g:`△ABC <0083.g1:< A B C >>`:

   1. *The distance of each vertex from the orthocentre is double the perpendicular from the circumcentre upon the opposite side:* $|AH| = 2\,|O M_a|$, $|BH| = 2\,|O M_b|$, $|CH| = 2\,|O M_c|$.
   2. *The Circumcentre* :g:`O <0083.g1:O>`, *Centroid* :g:`G <0083.g1:G>`, *and Orthocentre* :g:`H <0083.g1:H>` *lie on one straight line—the* :term:`Euler Line <euler-line>` :g:`[O H] <0083.g1:[ O H ]>`—*and* $|HG| = 2\,|GO|$.

----

.. _unit-1-book-ii:

.. folio:: 0048
   :page: 22

Book II — Medians, Euler's Collinearity Identity, Stewart's Theorem & Heron's Area
----------------------------------------------------------------------------------

.. enunciation::

   **Book II, Proposition 1 (Apollonius's Median Theorem).** *The sum of the squares of any two sides of a triangle is equal to twice the square of half the third side together with twice the square of the median bisecting the third side:*

   $$
   AB^2 + AC^2 = 2\,BM_a^2 + 2\,AM_a^2.
   $$

**Demonstration.** Drop the altitude :g:`[A Da] <0083.g1:[ A Da ]>` upon :g:`[BC] <0083.g1:[ B C ]>`. Applying Euclid ``II.12`` and ``II.13`` separately to $\triangle A M_a B$ and $\triangle A M_a C$, where $\angle A M_a B$ and $\angle A M_a C$ are supplementary and $BM_a = M_a C$, the two signed projection rectangles $\pm 2\,BM_a \cdot M_a D_a$ cancel upon addition, leaving $AB^2 + AC^2 = 2\,BM_a^2 + 2\,AM_a^2$. Q.E.D.

.. folio:: 0049
   :page: 23

**Proposition 2 (:person:`Euler's <euler>` Quadrilateral Theorem).** *In any quadrilateral (plane or skew), the sum of the squares of the four sides equals the sum of the squares of the two diagonals plus four times the square of the segment joining the midpoints of the diagonals:*

$$
AB^2 + BC^2 + CD^2 + DA^2 = AC^2 + BD^2 + 4\,MN^2.
$$

*Corollary:* A quadrilateral is a parallelogram if and only if $AB^2 + BC^2 + CD^2 + DA^2 = AC^2 + BD^2$.

.. folio:: 0051
   :page: 25

.. enunciation::

   **Book II, Proposition 7 (:person:`Euler's <euler>` Collinear Four-Point Identity).** *If four points* $A, B, C, D$ *lie in order upon a straight line, then*

   $$
   AB \cdot CD + BC \cdot AD = AC \cdot BD.
   $$

*(In Unit 4, circular inversion from a fourth point lifts this rectilinear identity directly into Ptolemy's Theorem and Casey's Generalized Bitangent Theorem.)*

.. folio:: 0052
   :page: 26

.. enunciation::

   **Book II, Proposition 10 (:person:`Stewart's <stewart>` Theorem, 1746).** *If any point* $D$ *be taken on the base* $BC$ *of a triangle* $ABC$, *then*

   $$
   AB^2 \cdot DC + AC^2 \cdot BD - AD^2 \cdot BC = BC \cdot BD \cdot DC.
   $$

.. folio:: 0056
   :page: 30

**Exercises on Book II (Leibniz's Mean-Square Identity & Heron's Formula).**

* **Leibniz's Theorem:** If $G$ is the centroid of $\triangle ABC$ and $P$ any point in the plane, $PA^2 + PB^2 + PC^2 = GA^2 + GB^2 + GC^2 + 3\,PG^2$.
* **Heron's Area Formula:** Expressing the altitude $AD_a$ from Euclid ``II.13`` as $4 b^2 c^2 - (b^2 + c^2 - a^2)^2 = (a+b+c)(b+c-a)(c+a-b)(a+b-c) = 16 s(s-a)(s-b)(s-c)$ yields $\Delta = \sqrt{s(s-a)(s-b)(s-c)}$.

----

.. _unit-1-nine-points:

.. folio:: 0083
   :page: 57

Book IV — Inradii, Exradii, Circumradius & the Nine-Points Circle
-----------------------------------------------------------------

**Book IV, Propositions 1–4 (Fundamental Triangle Radii Relations).** Denoting the area by $\Delta$, semiperimeter by $s = \frac{1}{2}(a+b+c)$, inradius by $r$, exradii by $r_a, r_b, r_c$, and circumradius by $R$:

$$
\Delta = r s = r_a(s-a) = r_b(s-b) = r_c(s-c) = \frac{abc}{4R} = \sqrt{r\,r_a\,r_b\,r_c}, \qquad r_a + r_b + r_c - r = 4R.
$$

.. enunciation::

   **Book IV, Proposition 5 (The Nine-Points Circle).** *In any triangle* :g:`△ABC <0083.g1:< A B C >>`, *the three middle points of the sides* (:g:`Ma <0083.g1:Ma>`, :g:`Mb <0083.g1:Mb>`, :g:`Mc <0083.g1:Mc>`), *the three feet of the altitudes* (:g:`Da <0083.g1:Da>`, :g:`Db <0083.g1:Db>`, :g:`Dc <0083.g1:Dc>`), *and the three middle points of the segments joining the orthocentre* :g:`H <0083.g1:H>` *to the vertices* (:g:`Ea <0083.g1:Ea>`, :g:`Eb <0083.g1:Eb>`, :g:`Ec <0083.g1:Ec>`) *all lie upon a single circle—the* :term:`Nine-Points Circle <nine-points-circle>` :g:`(N Ma) <0083.g1:( N Ma )>`—*whose centre* :g:`N <0083.g1:N>` *bisects* $|OH|$ *on the Euler Line* :g:`[O H] <0083.g1:[ O H ]>` *and whose radius is half the circumradius* ($R_9 = \frac{1}{2}R$).

.. picture:: 0083.g1.svg

.. folio:: 0084
   :page: 58

**Demonstration.** Let :g:`Ma <0083.g1:Ma>`, :g:`Mb <0083.g1:Mb>`, :g:`Mc <0083.g1:Mc>` be the midpoints of $BC, CA, AB$; :g:`Da <0083.g1:Da>`, :g:`Db <0083.g1:Db>`, :g:`Dc <0083.g1:Dc>` the feet of the altitudes meeting at :g:`H <0083.g1:H>`; and :g:`Ea <0083.g1:Ea>`, :g:`Eb <0083.g1:Eb>`, :g:`Ec <0083.g1:Ec>` the midpoints of $AH, BH, CH$.

1. Consider the segment joining :g:`Ma <0083.g1:Ma>` and :g:`Ea <0083.g1:Ea>`. In $\triangle ABH$, segment $M_c E_a$ joins the midpoints of $AB$ and $AH$, so $M_c E_a \parallel BH$; in $\triangle ABC$, $M_c M_a$ joins the midpoints of $AB$ and $BC$, so $M_c M_a \parallel AC$. Because the altitude $BH$ is perpendicular to $AC$, we have $M_c E_a \perp M_c M_a$, whence $\angle E_a M_c M_a = 90^\circ$.
2. Likewise in $\triangle ACH$, $M_b E_a \parallel CH$, while in $\triangle ABC$, $M_b M_a \parallel AB$; since $CH \perp AB$, we have $\angle E_a M_b M_a = 90^\circ$. Moreover, $\angle E_a D_a M_a = 90^\circ$ because the altitude :g:`[A Da] <0083.g1:[ A Da ]>` is perpendicular to :g:`[BC] <0083.g1:[ B C ]>`.
3. Therefore, by Euclid ``III.31``, the circle described on diameter $M_a E_a$ passes simultaneously through $M_b$, $M_c$, and $D_a$. Since three non-collinear points ($M_a, M_b, M_c$) uniquely determine a circle (Euclid ``IV.5``), this same circle :g:`(N Ma) <0083.g1:( N Ma )>` has $M_a E_a$, $M_b E_b$, and $M_c E_c$ as three diameters, and consequently passes through all nine points $M_a, M_b, M_c, D_a, D_b, D_c, E_a, E_b, E_c$.
4. Finally, because $AH = 2\,OM_a$ and $AH \parallel OM_a$, we have $E_a H = \frac{1}{2} AH = OM_a$ with $E_a H \parallel OM_a$; hence $O E_a M_a H$ is a parallelogram whose diagonals $OH$ and $M_a E_a$ bisect each other at the Nine-Points Centre :g:`N <0083.g1:N>`, and since $\triangle M_a M_b M_c \sim \triangle ABC$ in ratio $1:2$, its radius is $R_9 = \frac{1}{2}R$. Q.E.D.
