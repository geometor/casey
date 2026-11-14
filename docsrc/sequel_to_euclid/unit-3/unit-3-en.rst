:title: Unit 3 — Transversals, Similitude, Harmonic & Anharmonic Ratios

.. _sequel-unit-3-en:

Unit 3: Book IV & VI Extensions, Part A — Ceva, Menelaus, Similitude, Harmonic & Anharmonic Ratios
==================================================================================================

.. rubric:: John Casey — *A Sequel to the First Six Books of the Elements of Euclid* (5th ed., 1888 / 6th ed., 1892)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

----

.. _unit-3-ceva-menelaus:

.. folio:: 0093
   :page: 67

Book VI, Section I — Theory of Concurrent Lines & Transversals
--------------------------------------------------------------

.. enunciation::

   **Book VI, Section I, Proposition 2 (:person:`Ceva's <ceva>` Theorem, 1678).** *If three straight lines drawn from the vertices* $A, B, C$ *of a triangle to meet the opposite sides in* $D, E, F$ *be concurrent at a point* $O$, *the product of three alternate segments of the sides is equal to the product of the other three:*

   $$
   \frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = +1;
   $$

   *and conversely, if this signed ratio relation holds, the three cevians* $AD, BE, CF$ *are concurrent (or parallel).*

**Demonstration.** By Euclid ``VI.1``, triangles of equal altitude are to one another as their bases; hence $BD : DC = \triangle AOB : \triangle AOC$, $CE : EA = \triangle BOC : \triangle BOA$, and $AF : FB = \triangle COA : \triangle COB$. Compounding the three ratios cancels the three areas identically, yielding $+1$. Conversely, if $AD$ and $BE$ meet at $O$ and $CO$ meets $AB$ in $F'$, then $AF' : F'B = AF : FB$, so $F'$ coincides with $F$. Q.E.D.

.. folio:: 0095
   :page: 69

.. enunciation::

   **Book VI, Section I, Proposition 4 (:person:`Menelaus's <menelaus>` Theorem).** *If a transversal straight line cut the three sides* $BC, CA, AB$ *of a triangle (produced as necessary) in* $D, E, F$, *then with directed segments*

   $$
   \frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = -1,
   $$

   *and conversely, if three points* $D, E, F$ *on the sides satisfy this signed product, they are collinear.*

----

.. _unit-3-similitude:

.. folio:: 0108
   :page: 82

Book VI, Section II — Centres & Axes of Similitude
--------------------------------------------------

**Definition (:term:`Centres of Similitude <centre-of-similitude>`).** For any two circles $(O_1, r_1)$ and $(O_2, r_2)$, the points $S_e$ and $S_i$ dividing the line of centres $O_1 O_2$ externally and internally in the ratio $r_1 : r_2$ are called the **External (Direct)** and **Internal (Transverse) Centres of Similitude**. Every pair of parallel radii joins through $S_e$ (same sense) or $S_i$ (opposite sense), and all common tangents pass through $S_e$ or $S_i$.

**Proposition 4 (Circle of Similitude).** *The locus of a point at which two given unequal circles subtend equal angles is the circle having the segment* $S_e S_i$ *joining their external and internal centres of similitude as diameter—coaxal with the two given circles!*

.. folio:: 0112
   :page: 86

.. enunciation::

   **Book VI, Section II, Proposition 6 (:person:`Monge's <monge>` Theorem).** *Given three coplanar circles, their six centres of similitude lie three by three upon four straight lines—called the four Axes of Similitude:*

   * *all three external centres of similitude are collinear on the External Axis of Similitude;*
   * *any two internal centres of similitude are collinear with the third external centre of similitude.*

**Demonstration.** Apply :person:`Menelaus's <menelaus>` Theorem to the triangle of centres $\triangle O_1 O_2 O_3$ with radii $r_1, r_2, r_3$: the three external centres divide the sides externally in ratios $r_1/r_2, r_2/r_3, r_3/r_1$ whose product is $+1$ in magnitude and $(-1)^3 = -1$ in directed sign; replacing any two external divisions by internal divisions preserves the sign $(-1)(+1)(+1) = -1$. Q.E.D.

----

.. _unit-3-harmonic-quadrilateral:

.. folio:: 0113
   :page: 87

Book VI, Section III — Harmonic Section & the Complete Quadrilateral
--------------------------------------------------------------------

**Definition (:term:`Harmonic Section <harmonic-section>`).** A segment $AB$ is divided *harmonically* at $C$ and $D$ when it is divided internally at $C$ and externally at $D$ in the same ratio ($AC : CB = AD : BD$), so that $AB$ is the harmonic mean of $AC$ and $AD$:

$$
\frac{2}{AB} = \frac{1}{AC} + \frac{1}{AD}, \qquad \text{or, with midpoint } O \text{ of } AB, \qquad OC \cdot OD = OA^2.
$$

*(Note the bridge to Unit 2: two points divide a diameter harmonically if and only if they are inverse points with respect to the circle on that diameter!)*

.. folio:: 0117
   :page: 91

.. enunciation::

   **Book VI, Section III, Proposition 7 (Harmonic Property of the :term:`Complete Quadrilateral <complete-quadrilateral>`).** *In any complete quadrilateral formed by four straight lines* :g:`[AB] <0117.g1:[ A B ]>`, :g:`[BC] <0117.g1:[ B C ]>`, :g:`[CD] <0117.g1:[ C D ]>`, :g:`[DA] <0117.g1:[ D A ]>` *whose opposite sides meet at* :g:`E <0117.g1:E>` *and* :g:`F <0117.g1:F>`, *each of the three diagonals* :g:`[AC] <0117.g1:[ A C ]>`, :g:`[BD] <0117.g1:[ B D ]>`, :g:`[EF] <0117.g1:[ E F ]>` *is divided harmonically by the other two:*

   $$
   (A, C; P, Q_a) = -1, \qquad (B, D; P, Q_b) = -1, \qquad (E, F; Q_a, Q_b) = -1.
   $$

.. picture:: 0117.g1.svg

**Demonstration.** In $\triangle FAB$, the points :g:`D <0117.g1:D>` on $FA$ and :g:`C <0117.g1:C>` on $FB$ determine two cevians :g:`[AC] <0117.g1:[ A C ]>` and :g:`[BD] <0117.g1:[ B D ]>` concurring at :g:`P <0117.g1:P>`, while the line :g:`[CD] <0117.g1:[ C D ]>` is a transversal meeting $FB$ at $C$, $FA$ at $D$, and $AB$ at :g:`E <0117.g1:E>`. Let the third cevian $FP$ meet $AB$ at $K$. Applying **Ceva's Theorem** to $\triangle FAB$ with point $P$ gives $\frac{AK}{KB}\cdot\frac{BC}{CF}\cdot\frac{FD}{DA} = +1$, whereas **Menelaus's Theorem** applied to $\triangle FAB$ with transversal $CDE$ gives $\frac{AE}{EB}\cdot\frac{BC}{CF}\cdot\frac{FD}{DA} = -1$. Dividing the two equations yields $(A, B; K, E) = -1$, so the pencil $F(A, B; P, E)$ is harmonic. Cutting this harmonic pencil by transversal :g:`[AC] <0117.g1:[ A C ]>` gives $(A, C; P, Q_a) = -1$, cutting by :g:`[BD] <0117.g1:[ B D ]>` gives $(B, D; P, Q_b) = -1$, and projecting from $A$ onto :g:`[EF] <0117.g1:[ E F ]>` gives $(E, F; Q_a, Q_b) = -1$. Q.E.D.

----

.. _unit-3-anharmonic-desargues-pascal:

.. folio:: 0153
   :page: 127

Book VI, Section VI — Theory of Anharmonic Section, Desargues & Pascal
----------------------------------------------------------------------

**Definition (:term:`Anharmonic Ratio <anharmonic-ratio>`, :person:`Chasles <chasles>`).** For four collinear points $A, B, C, D$, the **anharmonic (cross) ratio** $(ABCD) = \frac{AC}{CB} : \frac{AD}{DB} = \frac{AC \cdot BD}{AD \cdot BC}$ is invariant under central projection from any vertex $O$:

$$
(ABCD) = \frac{\sin \angle AOC \cdot \sin \angle BOD}{\sin \angle AOD \cdot \sin \angle BOC} = O(ABCD).
$$

.. folio:: 0157
   :page: 131

**Proposition 5 (Anharmonic Property of Four Concyclic Points).** *If* $A, B, C, D$ *be four fixed points on a circle and* $P$ *any variable point on the circumference, the pencil* $P(ABCD)$ *has a constant anharmonic ratio independent of the position of* $P$ *(since equal arcs subtend equal inscribed angles by Euclid III.21).*

.. folio:: 0161
   :page: 135

.. enunciation::

   **Book VI, Section VI, Propositions 9–11 (:person:`Desargues's <desargues>` Homology Theorem & :person:`Pascal's <pascal>` Hexagrammum Mysticum).**

   1. **Desargues's Theorem (Coperspective $\iff$ Coaxial Triangles):** *If two triangles* $\triangle ABC$ *and* $\triangle A'B'C'$ *be in perspective so that* $AA', BB', CC'$ *concur at a Centre of Homology* $O$, *then the three intersections of corresponding sides* $L = BC \cap B'C'$, $M = CA \cap C'A'$, $N = AB \cap A'B'$ *lie on a single straight line (the Axis of Homology).*
   2. **Pascal's Mystic Hexagram (1640):** *If any hexagon* $ABCDEF$ *be inscribed in a circle, the three intersections of its pairs of opposite sides* $L = AB \cap DE$, $M = BC \cap EF$, $N = CD \cap FA$ *are collinear on the Pascal Line.*

**Demonstration of Pascal's Theorem by Anharmonic Pencils.** Project the four concyclic vertices $A, C, D, E$ from the remaining two vertices $B$ and $F$ on the circle; by Proposition 5, the two pencils have equal anharmonic ratios: $B(ACDE) = F(ACDE)$. Cut the pencil $B(ACDE)$ by transversal $DE$ to obtain the range $(L, K, D, E)$ where $L = BA \cap DE$ and $K = BC \cap DE$; cut the pencil $F(ACDE)$ by transversal $CD$ to obtain the range $(N, C, D, J)$ where $N = FA \cap CD$ and $J = FE \cap CD$. Because $(L, K, D, E) = (N, C, D, J)$ and the intersection $D = DE \cap CD$ corresponds to itself in both ranges, by Chasles's perspective lemma (Prop. 4 Cor.) the joins of the remaining corresponding pairs—$LN$, $KC$ (line $BC$), and $EJ$ (line $EF$)—concur at a single point, namely $M = BC \cap EF$. Therefore $L, M, N$ are collinear. Q.E.D.
