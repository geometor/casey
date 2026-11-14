:title: Unit 4 — Inversion, Casey's & Feuerbach's Theorems, Poles & Polars

.. _sequel-unit-4-en:

Unit 4: Book VI Extensions, Part B & Book III Props. 25, 27 — Inversion, Casey's & Feuerbach's Theorems, Poles & Polars
=======================================================================================================================

.. rubric:: John Casey — *A Sequel to the First Six Books of the Elements of Euclid* (5th ed., 1888 / 6th ed., 1892)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

----

.. _unit-4-inversion-arbelos:

.. folio:: 0121
   :page: 95

Book VI, Section IV — Theory of Circular Inversion & Pappus's Arbelos
---------------------------------------------------------------------

**Definition (:term:`Circular Inversion <inversion>`).** Given a fixed circle of centre $O$ and radius $k$ (the *Circle of Inversion*), if to every point $P \neq O$ there corresponds the point $P'$ on ray $OP$ satisfying $OP \cdot OP' = k^2$, the figure formed by $P'$ is called the *inverse* of the figure formed by $P$.

**Fundamental Properties of Inversion (Propositions 1–9, pp. 95–102):**

1. **Lines & Circles (Props. 1–3):** A straight line not passing through $O$ inverts into a circle passing through $O$ (with diameter perpendicular to the line); a circle passing through $O$ inverts into a straight line not through $O$; a circle not passing through $O$ inverts into a circle not passing through $O$, with $O$ as a centre of similitude of the two circles; and **any circle cutting the circle of inversion orthogonally inverts into itself**!
2. **Distance Distortion Formula (Prop. 4):** By similar triangles $\triangle OAB \sim \triangle OB'A'$ (Euclid ``VI.6``),

   $$
   |A'B'| = \frac{k^2 \cdot |AB|}{|OA| \cdot |OB|}.
   $$

3. **Conformal Angle & Cross-Ratio Preservation (Props. 5–8):** Two curves intersect at the **same angle** as their inverse curves (in opposite orientation), tangency is preserved, and the anharmonic ratio of four concyclic or collinear points is preserved under inversion.
4. **Inversion Invariance of Normalized Bitangents (Prop. 9):** If two circles of radii $r_1, r_2$ and common direct tangent $t_{12}$ invert into two circles of radii $r_1', r_2'$ and common direct tangent $t_{12}'$, then

   $$
   \frac{t_{12}^2}{r_1 r_2} = \frac{t_{12}'^{\,2}}{r_1' r_2'}.
   $$

.. folio:: 0129
   :page: 103

**Proposition 9, Corollary 1 (:person:`Pappus's <pappus>` Ancient Arbelos Chain Theorem).** *In the shoemaker's knife (Arbelos) bounded by three mutually tangent semicircles on collinear diameters* $AB, AC, CB$, *let a chain of circles* $O_1, O_2, \dots, O_n$ *be inscribed, each touching the two fixed boundary semicircles on* $AB$ *and* $AC$ *and touching the preceding circle of the chain. Then the perpendicular height* $h_n$ *of the centre of the* $n$-*th circle above the base line* $AB$ *is equal to* $2n$ *times its radius* ($h_n = 2 n r_n$).

*(Inverting from $A$, the two boundary semicircles through $A$ become parallel straight lines, and the chain $O_1, \dots, O_n$ becomes a column of equal congruent spheres/circles stacked between two parallel lines!)*

----

.. _unit-4-casey-feuerbach:

Casey's Generalized Ptolemy Theorem, Feuerbach's Theorem & Hart's Circle
------------------------------------------------------------------------

.. enunciation::

   **Book VI, Section IV, Proposition 10 (:person:`Casey's <casey>` :term:`Generalized Ptolemy Theorem <caseys-theorem>`, 1866).** *If four circles* $O_1, O_2, O_3, O_4$ *be all tangent to a fifth circle* $\Sigma$ *(or straight line), the six common tangents joining the four circles in pairs (direct tangents when two circles touch* $\Sigma$ *on the same side, transverse tangents when on opposite sides) satisfy the relation*

   $$
   \overline{12} \cdot \overline{34} + \overline{14} \cdot \overline{23} = \overline{13} \cdot \overline{24}.
   $$

**Demonstration.** Invert the configuration from any point $O$ taken on the circumference of the fifth circle $\Sigma$. Because $\Sigma$ passes through the centre of inversion $O$, $\Sigma$ inverts into a **straight line** $L$, while $O_1, O_2, O_3, O_4$ invert into four circles $O_1', O_2', O_3', O_4'$ tangent to $L$ at four collinear points $A', B', C', D'$! Along the straight line $L$, :person:`Euler's <euler>` collinear identity (Book II, Prop. 7) holds for the contact segments:

$$
A'B' \cdot C'D' + A'D' \cdot B'C' = A'C' \cdot B'D'.
$$

Dividing through by $2\sqrt{r_1' r_2' r_3' r_4'}$ and applying Proposition 9 ($A'B' / \sqrt{r_1' r_2'} = \overline{12} / \sqrt{r_1 r_2}$) multiplies back by $2\sqrt{r_1 r_2 r_3 r_4}$ to yield $\overline{12}\cdot\overline{34} + \overline{14}\cdot\overline{23} = \overline{13}\cdot\overline{24}$ identically! Conversely, when the relation holds, the fourth circle touches the circle touching the first three. When $r_1 = r_2 = r_3 = r_4 = 0$, the theorem reduces to :person:`Ptolemy's <ptolemy>` Theorem for cyclic quadrilaterals (Euclid ``VI.D``). Q.E.D.

.. folio:: 0130
   :page: 104

.. enunciation::

   **Proposition 10, Corollary 2 (:person:`Feuerbach's <feuerbach>` Theorem — Both Proofs by :person:`Casey <casey>`).** *In any triangle* :g:`△ABC <0130.g1:< A B C >>`, *the* :term:`Nine-Points Circle <nine-points-circle>` :g:`(N Ma) <0130.g1:( N Ma )>` *touches the Incircle* :g:`(I Ta) <0130.g1:( I Ta )>` *internally at the* :term:`Feuerbach Point <feuerbach-point>` :g:`Fe <0130.g1:Fe>` *and touches each of the three Excircles externally.*

.. picture:: 0130.g1.svg

**First Proof (Immediate Corollary of Casey's Theorem, pp. 104–105).** Regard the three side midpoints :g:`Ma <0130.g1:Ma>`, :g:`Mb <0130.g1:Mb>`, :g:`Mc <0130.g1:Mc>` as three point-circles ($r_1 = r_2 = r_3 = 0$) and the Incircle :g:`(I Ta) <0130.g1:( I Ta )>` as the fourth circle $O_4$. Their mutual "common tangents" are:

* Midpoint chord lengths: $\overline{23} = |M_b M_c| = \frac{1}{2}a$, $\overline{31} = |M_c M_a| = \frac{1}{2}b$, $\overline{12} = |M_a M_b| = \frac{1}{2}c$.
* Tangents from $M_a, M_b, M_c$ to the Incircle touching $BC, CA, AB$ at :g:`Ta <0130.g1:Ta>`, :g:`Tb <0130.g1:Tb>`, :g:`Tc <0130.g1:Tc>`: since $|B T_a| = s - b$ and $|B M_a| = \frac{1}{2}a$, we have

  $$
  \overline{14} = |M_a T_a| = \tfrac{1}{2}|b - c|, \qquad \overline{24} = |M_b T_b| = \tfrac{1}{2}|c - a|, \qquad \overline{34} = |M_c T_c| = \tfrac{1}{2}|a - b|.
  $$

Assuming without loss of generality $a \ge c \ge b$ (as in our canonical $(15, 13, 14)$ triangle!),

$$
\overline{23}\cdot\overline{14} + \overline{31}\cdot\overline{24} - \overline{12}\cdot\overline{34}
= \frac{a(c - b) + b(a - c) - c(a - b)}{4} \equiv 0!
$$

By the converse of Casey's Theorem, the circle circumscribing the three point-circles $M_a, M_b, M_c$—which is the **Nine-Points Circle** :g:`(N Ma) <0130.g1:( N Ma )>`—is tangent to the Incircle :g:`(I Ta) <0130.g1:( I Ta )>` at :g:`Fe <0130.g1:Fe>`! Replacing $(s-b)$ by $s$ for the $A$-excircle gives $|M_a T_a'| = \frac{1}{2}(b+c)$, $|M_b T_b'| = \frac{1}{2}(a+c)$, and $|M_c T_c'| = \frac{1}{2}(a+b)$, satisfying $\frac{1}{4}[a(c-b) + c(a+b) - b(a+c)] \equiv 0$, proving external tangency with all three excircles.

.. folio:: 0131
   :page: 105

**Second Proof (:person:`Casey's <casey>` 1861 Orthogonal Inversion Proof, pp. 105–106).** Let :g:`Ma <0130.g1:Ma>` be the midpoint of $BC$. The Incircle $(I)$ and $A$-Excircle $(I_a)$ touch $BC$ at :g:`Ta <0130.g1:Ta>` and $T_a'$ symmetrically about :g:`Ma <0130.g1:Ma>` at equal distance $|M_a T_a| = |M_a T_a'| = \frac{1}{2}|b - c|$. Therefore the circle :g:`(Ma Ta) <0130.g1:( Ma Ta )>` of centre :g:`Ma <0130.g1:Ma>` and radius $\frac{1}{2}|b - c|$ **cuts both the Incircle and the $A$-Excircle orthogonally**, and hence inverts each of them into itself!

Now consider the **fourth common tangent** :g:`[C Ts] <0130.g1:[ C Ts ]>` to $(I)$ and $(I_a)$ (the reflection of $BC$ across the internal/external bisector line $I I_a$, which on the $(15, 13, 14)$ triangle passes directly through $C$ and touches $(I)$ at :g:`Ts <0130.g1:Ts>`!). Under inversion in :g:`(Ma Ta) <0130.g1:( Ma Ta )>`, this straight line—being tangent to both $(I)$ and $(I_a)$—inverts into a circle passing through the centre of inversion :g:`Ma <0130.g1:Ma>` and through :g:`Mb <0130.g1:Mb>` and :g:`Mc <0130.g1:Mc>`, namely the **Nine-Points Circle** :g:`(N Ma) <0130.g1:( N Ma )>`. Because inversion preserves tangency while leaving $(I)$ and $(I_a)$ fixed, the Nine-Points Circle touches $(I)$ internally at the inverse :g:`Fe <0130.g1:Fe>` of :g:`Ts <0130.g1:Ts>`, and touches $(I_a)$ externally! Q.E.D.

.. folio:: 0132
   :page: 106

**Proposition 11 (:person:`Hart's <hart>` :term:`Circle <harts-circle>`, 1861).** *Given any circular triangle formed by three arbitrary circles, the eight Apollonius circles touching all three partition into groups of four (analogous to the incircle and three excircles of a rectilinear triangle) such that each quartet of four circles is touched by a common circle—Hart's Circle.*

----

.. _unit-4-poles-polars:

.. folio:: 0070
   :page: 44

Book III (Props. 25, 27) & Book VI, Section VII — Poles, Polars & Reciprocation
-------------------------------------------------------------------------------

**Definition (:term:`Pole and Polar <pole-and-polar>`).** If $D'$ be the inverse of a point :g:`D <0071.g1:D>` with respect to a circle :g:`(O G1) <0071.g1:( O G1 )>`, the straight line :g:`[U V] <0071.g1:[ U V ]>` drawn through $D'$ perpendicular to $OD$ is called the **Polar** of :g:`D <0071.g1:D>`, and :g:`D <0071.g1:D>` is called the **Pole** of :g:`[U V] <0071.g1:[ U V ]>`.

.. folio:: 0071
   :page: 45

.. enunciation::

   **Book III, Propositions 25 & 27 (:person:`La Hire's <lahire>` Reciprocity & Harmonic Secant Property).**

   1. **Prop. 25 (La Hire's Reciprocity, 1685):** *If a point* :g:`Q <0071.g1:Q>` *lie upon the polar* :g:`[U V] <0071.g1:[ U V ]>` *of a point* :g:`D <0071.g1:D>` *with respect to a circle, then* :g:`D <0071.g1:D>` *lies upon the polar of* :g:`Q <0071.g1:Q>`.
   2. **Prop. 27 (Harmonic Secant Theorem):** *Any secant drawn from a pole* :g:`D <0071.g1:D>` *cutting the circle in* :g:`G1 <0071.g1:G1>`, :g:`H1 <0071.g1:H1>` *and cutting its polar* :g:`[U V] <0071.g1:[ U V ]>` *in* :g:`J1 <0071.g1:J1>` *is divided harmonically:* $(G_1, H_1; J_1, D) = -1$.

**Demonstration of La Hire's Reciprocity.** Let $D'$ be the inverse of :g:`D <0071.g1:D>` on $OD$ ($OD \cdot OD' = r^2$, $D'Q \perp OD$), and drop $DK \perp OQ$. Because $\angle OD'Q = \angle OKD = 90^\circ$, the quadrilateral $D'DKQ$ is cyclic (Euclid ``III.22``); therefore by Euclid ``III.36`` from $O$, $OQ \cdot OK = OD \cdot OD' = r^2$. Hence $K$ is the inverse of :g:`Q <0071.g1:Q>`, and $DK$—being perpendicular to $OQ$ at $K$—is the polar of :g:`Q <0071.g1:Q>`, passing through :g:`D <0071.g1:D>`! Q.E.D.

.. picture:: 0071.g1.svg

.. folio:: 0167
   :page: 141

**Book VI, Section VII, Propositions 1–6 (Inscribed Quadrangle Polar Construction, Self-Conjugate Triangles & :term:`Reciprocation <reciprocation>`).**

1. **Prop. 2 (Pure-Straightedge Polar & Self-Conjugate Triangle):** Draw any two secants from :g:`D <0071.g1:D>` cutting the circle in :g:`G1 <0071.g1:G1>`, :g:`H1 <0071.g1:H1>` and :g:`G2 <0071.g1:G2>`, :g:`H2 <0071.g1:H2>`. For the inscribed quadrangle $G_1 H_1 H_2 G_2$, let opposite chord pairs meet at :g:`U <0071.g1:U>` and :g:`V <0071.g1:V>`. By the Complete Quadrilateral theorem (Unit 3) and Prop. 27, the line :g:`[U V] <0071.g1:[ U V ]>` is the exact **polar** of :g:`D <0071.g1:D>`—constructed using **straightedge alone**—and $\triangle DUV$ is a **Self-Conjugate Triangle** in which each vertex is the pole of the opposite side!
2. **Prop. 3 (:person:`Salmon's <salmon>` Theorem):** *The distances of any two points from the centre of a circle are proportional to the perpendicular distances of each point from the polar of the other.*
3. **Props. 4–6 (:person:`Brianchon's <brianchon>` Theorem by Polar Reciprocation):** Replacing every point on a circle by its tangent (polar) and every inscribed chord by the intersection of tangents (pole) reciprocates :person:`Pascal's <pascal>` inscribed hexagon theorem directly into **Brianchon's Theorem**: *In any hexagon circumscribed about a circle, the three diagonals joining opposite vertices concur at a single point (the Brianchon Point).*
