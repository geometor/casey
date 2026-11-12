:layout: book
:title: Unit 5 — Symmedians, Lemoine's Point & Lemoine Circles

.. _sequel-unit-5-en:

Unit 5: Supplementary Chapter, Secs. I & III (Part 1) — Symmedians, Lemoine's Point & Lemoine Circles
=====================================================================================================

.. rubric:: John Casey — *Supplementary Chapter on the Recent Elementary Geometry of the Triangle* (5th ed., 1888 / 6th ed., 1892)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

----

.. _unit-5-conjugates-antiparallels:

.. folio:: 0191
   :page: 165

Section I — Isogonal & Isotomic Conjugates and Antiparallels
------------------------------------------------------------

**Definition (:term:`Isogonal Conjugates <isogonal-conjugates>`).** Two straight lines drawn from a vertex of a triangle making equal angles with the internal bisector of that angle are called *isogonal conjugates*.

.. enunciation::

   **Supplementary Chapter, Section I, Proposition 1 (Isogonal Concurrency & Pedal Circle).** *If three lines drawn from the vertices* $A, B, C$ *of a triangle concur at a point* $P$, *their three isogonal conjugates also concur at a single point* $P'$ *(the Isogonal Conjugate of* $P$*); and the six feet of perpendiculars let fall from* $P$ *and* $P'$ *upon the three sides of* $\triangle ABC$ *lie upon a single circle whose centre is the midpoint of* $PP'$.

   *Classical Specialization:* The circumcentre :g:`O <0205.g1:O>` and orthocentre $H$ are isogonal conjugates, and their shared six-point pedal circle (the three side midpoints and three altitude feet) is the **Nine-Points Circle** centered at $N = \operatorname{midpoint}(O, H)$!

.. folio:: 0193
   :page: 167

**Definition (:term:`Isotomic Conjugates <isotomic-conjugates>`).** Two points $D, D'$ on side $BC$ equidistant from its midpoint $M_a$ ($BD = D'C$) are called *isotomic*; by Ceva's Theorem, if $AD, BE, CF$ concur at $P$, their isotomic cevians $AD', BE', CF'$ concur at the *Isotomic Conjugate* of $P$ (for instance, the Gergonne and Nagel points).

.. folio:: 0195
   :page: 169

**Definition (:term:`Antiparallels <antiparallel>`).** A transversal cutting $AB$ and $AC$ at $D$ and $E$ so that $\angle ADE = \angle ACB$ and $\angle AED = \angle ABC$ is called *antiparallel* to $BC$ with respect to $\angle A$. Every antiparallel to $BC$ makes a cyclic quadrilateral $BCED$ with $BC$, and is parallel to the tangent to the circumcircle :g:`(O A) <0205.g1:( O A )>` at :g:`A <0205.g1:A>` (by Euclid ``III.32``).

----

.. _unit-5-symmedians-lemoine:

.. folio:: 0196
   :page: 170

Theory of Symmedians & Lemoine's Point $K = X(6)$
-------------------------------------------------

**Definition (:term:`Symmedians <symmedian>`).** The isogonal conjugate of a median of a triangle is called a **Symmedian**.

.. enunciation::

   **Section I, Propositions 5–7 (:person:`Lemoine's <lemoine>` Symmedian Point & Minimum-Square Property).**

   1. **Concurrency at $K$:** *The three symmedians* :g:`[A K] <0205.g1:[ A K ]>`, :g:`[B K] <0205.g1:[ B K ]>`, :g:`[C K] <0205.g1:[ C K ]>` *of* :g:`△ABC <0205.g1:< A B C >>` *concur at a single point* :g:`K <0205.g1:K>` (*the Symmedian Point or Lemoine's Point,* $X(6)$, *isogonal conjugate of the Centroid* $G$).
   2. **Antiparallel Bisection & Tangency Construction:** *Each symmedian* :g:`[A K] <0205.g1:[ A K ]>` *bisects every antiparallel to* $BC$, *passes through the pole of* $BC$ *with respect to the circumcircle* :g:`(O A) <0205.g1:( O A )>` *(the intersection of the circumcircle tangents at* $B$ *and* $C$*), and divides the opposite side* $BC$ *in the ratio of the squares of the adjacent sides* ($c^2 : b^2$).
   3. **Proportional Distances & Lagrange's Minimum:** *The perpendicular distances* $(x, y, z)$ *from* :g:`K <0205.g1:K>` *upon the sides* $(a, b, c)$ *are directly proportional to the lengths of those sides:*

      $$
      \frac{x}{a} = \frac{y}{b} = \frac{z}{c} = \frac{2\Delta}{a^2 + b^2 + c^2},
      $$

      *and among all points in the plane,* :g:`K <0205.g1:K>` *strictly minimizes the sum of squares of perpendicular distances to the sides,* $x^2 + y^2 + z^2 \ge \frac{4\Delta^2}{a^2 + b^2 + c^2}$.

**Demonstration of Minimum Property.** By Cauchy's / Lagrange's identity,

$$
(a^2 + b^2 + c^2)(x^2 + y^2 + z^2) - (ax + by + cz)^2 = (bx - ay)^2 + (cy - bz)^2 + (az - cx)^2 \ge 0.
$$

Since $ax + by + cz = 2\Delta$ is constant for every interior point, $x^2 + y^2 + z^2$ attains its unique minimum $\frac{4\Delta^2}{a^2 + b^2 + c^2}$ if and only if $x : y : z = a : b : c$, which uniquely characterizes :g:`K <0205.g1:K>`. Q.E.D.

----

.. _unit-5-lemoine-circles:

.. folio:: 0205
   :page: 179

Section III (Part 1) — Lemoine's First Circle & the Cosine Circle
-----------------------------------------------------------------

.. enunciation::

   **Section III, Proposition 1 (:term:`Lemoine's First Circle / Triplicate-Ratio Circle <lemoine-circle>`).** *If through the Symmedian Point* :g:`K <0205.g1:K>` *three straight lines* :g:`[parBC] <0205.g1:[ parBC ]>`, :g:`[parCA] <0205.g1:[ parCA ]>`, :g:`[parAB] <0205.g1:[ parAB ]>` *be drawn parallel respectively to the sides* :g:`[BC] <0205.g1:[ B C ]>`, :g:`[CA] <0205.g1:[ C A ]>`, :g:`[AB] <0205.g1:[ A B ]>`, *meeting the sides in six points* :g:`D1 <0205.g1:D1>`, :g:`D2 <0205.g1:D2>` *on* $BC$, :g:`E1 <0205.g1:E1>`, :g:`E2 <0205.g1:E2>` *on* $CA$, *and* :g:`F1 <0205.g1:F1>`, :g:`F2 <0205.g1:F2>` *on* $AB$:

   1. *All six points lie upon a single circle—Lemoine's First Circle* :g:`(Ml D1) <0205.g1:( Ml D1 )>`;
   2. *Its centre* :g:`Ml <0205.g1:Ml>` ($X(182)$) *is the midpoint of the segment joining the Circumcentre* :g:`O <0205.g1:O>` *and Symmedian Point* :g:`K <0205.g1:K>`;
   3. *The three chords* $|D_1 D_2|, |E_1 E_2|, |F_1 F_2|$ *cut off upon the sides* $BC, CA, AB$ *are directly proportional to the* **cubes** *of those sides* ($a^3 : b^3 : c^3$, *hence :person:`Tucker's <tucker>` name "Triplicate-Ratio Circle").*

.. picture:: 0205.g1.svg

**Demonstration.** In parallelogram $A F_2 K E_1$ ($K E_1 \parallel AB$ and $K F_2 \parallel AC$), the diagonal $AK$ lies along the symmedian :g:`[A K] <0205.g1:[ A K ]>`. Because the adjacent sides of $A F_2 K E_1$ are proportional to the distances from $K$ to $AC, AB$ divided by $\sin A$—hence proportional to $b : c$—triangle $\triangle A F_2 E_1$ is inversely similar to $\triangle ABC$, so the chord $E_1 F_2$ is **antiparallel** to $BC$! Meanwhile $E_2 F_1$ passes through $K$ **parallel** to $BC$; hence $F_2 F_1 E_2 E_1$ is an isosceles-angle cyclic trapezium, making $E_1, E_2, F_1, F_2$ concyclic. By cyclic symmetry, $F_1, F_2, D_1, D_2$ and $D_1, D_2, E_1, E_2$ are each concyclic; since any two of these three circles share two points on one side and would otherwise have three non-concurrent radical chords $BC, CA, AB$, all six points $D_1, D_2, E_1, E_2, F_1, F_2$ lie on a single circle :g:`(Ml D1) <0205.g1:( Ml D1 )>`. Moreover, the perpendicular bisectors of the three antiparallel chords $D_2 E_1, E_2 F_1, F_2 D_1$ bisect segment $OK$, fixing the centre at :g:`Ml <0205.g1:Ml>` $= \operatorname{midpoint}(O, K)$. Finally, since $K = (a^2 : b^2 : c^2)$, the parallel intercepts cut off middle segment $|D_1 D_2| = \frac{a^3}{a^2 + b^2 + c^2}$, proportional to $a^3 : b^3 : c^3$. Q.E.D.

.. folio:: 0209
   :page: 183

.. porism::

   **Proposition 1, Corollary 4 (:term:`The Cosine Circle / Second Lemoine Circle <cosine-circle>`).** *If through* :g:`K <0205.g1:K>` *three straight lines be drawn* **antiparallel** *respectively to* $BC, CA, AB$, *each is bisected at* :g:`K <0205.g1:K>` *and all three antiparallel segments have equal length! Consequently their six extremities on the sides of* $\triangle ABC$ *lie on a single circle* :g:`(K Cb2) <0205.g1:( K Cb2 )>` *centered at* :g:`K <0205.g1:K>` *itself, cutting off chords on* $BC, CA, AB$ *proportional to* $\cos A : \cos B : \cos C$ *(hence called the Cosine Circle).*
