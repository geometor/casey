:layout: book
:title: Unit 2 — Power of a Point, Orthogonal & Coaxal Circles

.. _sequel-unit-2-en:

Unit 2: Book III & Book VI Sec. V Extensions — Power of a Point, Orthogonal & Coaxal Circles
============================================================================================

.. rubric:: John Casey — *A Sequel to the First Six Books of the Elements of Euclid* (5th ed., 1888 / 6th ed., 1892)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

----

.. _unit-2-inverse-and-orthogonal:

.. folio:: 0067
   :page: 41

Book III — Inverse Points, Power of a Point & Orthogonal Circles
----------------------------------------------------------------

**Definition (Inverse Points with respect to a Circle).** *If on any radius (produced) of a circle of centre* $O$ *and radius* $r$ *two points* $P, P'$ *be taken such that the rectangle* $OP \cdot OP' = r^2$, *the points* $P$ *and* $P'$ *are called* :term:`inverse points <inversion>` *with respect to the circle.*

**Proposition 20 (Ratio Property of Inverse Points).** *If* $P, P'$ *be inverse points with respect to a circle* $(O, r)$, *the ratio* $AP : AP'$ *of the distances of any point* $A$ *on the circumference from* $P$ *and* $P'$ *is constant and equal to* $\sqrt{OP / OP'} = OP / r = r / OP'$.

**Demonstration.** Because $OP \cdot OP' = OA^2$ and $\angle POA$ is common to $\triangle OAP$ and $\triangle OP'A$, by Euclid ``VI.6`` the triangles $\triangle OAP$ and $\triangle OP'A$ are equiangular and similar; therefore $AP : AP' = OA : OP' = r : OP'$, independent of the position of $A$ on the circumference. Q.E.D.

.. folio:: 0068
   :page: 42

**Definition (:term:`Power of a Point <power-of-a-point>`).** By Euclid ``III.35`` and ``III.36``, for any secant $PAB$ drawn from $P$ cutting a circle $(O, r)$ in $A$ and $B$, the signed rectangle $PA \cdot PB = |PO|^2 - r^2$ depends only upon $P$ and the circle, and equals the square of the tangent $|PT|^2$ when $P$ lies outside $(O, r)$.

.. enunciation::

   **Book III, Proposition 22 (:term:`Orthogonal Circles <orthogonal-circles>`).** *Two circles* $(O_1, r_1)$ *and* $(O_2, r_2)$ *cut each other orthogonally (so that the tangents at their points of intersection are at right angles) if and only if the square of the distance between their centres equals the sum of the squares of their radii:*

   $$
   |O_1 O_2|^2 = r_1^2 + r_2^2.
   $$

   *Equivalently, any secant drawn from the centre of one orthogonal circle through the other cuts it in two points which are inverse with respect to the first circle.*

----

.. _unit-2-radical-axis:

.. folio:: 0069
   :page: 43

Radical Axis, Radical Centre & Poncelet's Limiting Points
---------------------------------------------------------

.. enunciation::

   **Book III, Proposition 23 (The :term:`Radical Axis <radical-axis>` & :term:`Radical Centre <radical-axis>`).** *The locus of a point from which tangents drawn to two given non-concentric circles* :g:`(O1) <0069.g1:( O1 )>` *and* :g:`(O2) <0069.g1:( O2 )>` *are equal—more generally, whose powers* $|PO_1|^2 - r_1^2$ *and* $|PO_2|^2 - r_2^2$ *are equal—is a straight line* :g:`[D Rc] <0069.g1:[ D Rc ]>` *perpendicular to the line of centres* :g:`[O1 O2] <0069.g1:[ O1 O2 ]>`, *dividing* $O_1 O_2$ *at* :g:`D <0069.g1:D>` *so that*

   $$
   O_1 D^2 - O_2 D^2 = r_1^2 - r_2^2.
   $$

   *Corollary (Radical Centre):* *The three radical axes of three circles taken in pairs concur at a single point* (:g:`Rc <0069.g1:Rc>`, *the Radical Centre).*

**Construction of the Radical Axis of Two Non-Intersecting Circles (Prop. 21 / Prop. 23 Cor.).** Draw any auxiliary circle cutting :g:`(O1) <0069.g1:( O1 )>` in two real points and :g:`(O2) <0069.g1:( O2 )>` in two real points; produce the two common chords until they intersect at :g:`Rc <0069.g1:Rc>`. By Euclid ``III.35–36``, :g:`Rc <0069.g1:Rc>` has equal power with respect to all three circles; dropping the perpendicular from :g:`Rc <0069.g1:Rc>` upon :g:`[O1 O2] <0069.g1:[ O1 O2 ]>` at :g:`D <0069.g1:D>` constructs the exact radical axis :g:`[D Rc] <0069.g1:[ D Rc ]>`.

.. picture:: 0069.g1.svg

**Definition (:person:`Poncelet's <poncelet>` :term:`Limiting Points <limiting-points>`).** When two circles :g:`(O1) <0069.g1:( O1 )>` and :g:`(O2) <0069.g1:( O2 )>` do not intersect, the foot :g:`D <0069.g1:D>` of the radical axis on the line of centres lies outside both circles. Drawing the tangent from :g:`D <0069.g1:D>` to :g:`(O1) <0069.g1:( O1 )>` at :g:`T1 <0069.g1:T1>` and laying off $|DL_1| = |DL_2| = |DT_1|$ along :g:`[O1 O2] <0069.g1:[ O1 O2 ]>` determines the two **Limiting Points** :g:`L1 <0069.g1:L1>` and :g:`L2 <0069.g1:L2>` (zero-radius circles of the coaxal pencil).

.. folio:: 0070
   :page: 44

.. enunciation::

   **Book III, Proposition 24 (Casey's Fundamental Difference-of-Powers Theorem).** *The difference of the powers of any point* $P$ *with respect to two circles* $(O_1, r_1)$ *and* $(O_2, r_2)$ *is equal to twice the rectangle contained by the distance between their centres and the perpendicular distance* $PN$ *from* $P$ *upon their radical axis:*

   $$
   \operatorname{pow}(P, C_1) - \operatorname{pow}(P, C_2) = 2\,|O_1 O_2| \cdot PN.
   $$

----

.. _unit-2-coaxial-systems:

.. folio:: 0139
   :page: 113

Book VI, Section V — Coaxal Systems of Circles
----------------------------------------------

**Definition (:term:`Coaxal System <coaxal-circles>`).** A family of circles is called *coaxal* when every pair of circles in the system possesses the same radical axis. All centres of a coaxal system lie on a common straight line perpendicular to the radical axis.

.. folio:: 0140
   :page: 114

.. enunciation::

   **Book VI, Section V, Propositions 1–5 (Conjugate Orthogonal Pencils & Limiting Points).**

   1. **Prop. 1 (Constant Power Ratio):** *If from any point on a third circle of a coaxal system tangents be drawn to two given circles of the system, the squares of these tangents are in a constant ratio (directly from Book III, Prop. 24).*
   2. **Prop. 2 (Circle of Apollonius):** *The locus of a point whose distances from two fixed points—the Limiting Points* :g:`L1 <0069.g1:L1>` *and* :g:`L2 <0069.g1:L2>`—*have a constant ratio is a circle of the non-intersecting coaxal system.*
   3. **Props. 3–4 (Invariance of Limiting Points):** *The Limiting Points* :g:`L1 <0069.g1:L1>` *and* :g:`L2 <0069.g1:L2>` *are mutually inverse points with respect to* **every** *circle of the coaxal system; and every circle* :g:`(Rc L1) <0069.g1:( Rc L1 )>` *whose centre lies on the radical axis and whose radius equals the tangent from its centre to any circle of the system passes through both* :g:`L1 <0069.g1:L1>` *and* :g:`L2 <0069.g1:L2>` *and cuts every circle of the coaxal system orthogonally.*
   4. **Prop. 5 (Conjugate Pencils):** *The circles cutting a non-intersecting coaxal system orthogonally form an intersecting coaxal system whose common chord is* $L_1 L_2$ *and whose radical axis is the line of centres of the original system.*
