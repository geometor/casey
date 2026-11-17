:title: Book VI, Section II Summary — Centres and Axes of Similitude
:tracks: English: section_02-en | Summary: section_02-summary | Notes: section_02-notes

.. _casey-book-06-sec-02-summary:

Book VI, Section II Summary: Centres and Axes of Similitude
===========================================================

.. rubric:: Modern Geometric & Invariant Analysis of Casey's Book VI, Section II (pp. 82–86)

1. Centres of Similitude as Homothecy Centres
---------------------------------------------

For two coplanar circles $C_1(O_1, r_1)$ and $C_2(O_2, r_2)$:

* **Internal Centre of Similitude ($S_i$):**
  Dividing $O_1 O_2$ internally in ratio $r_1 : r_2$:

  $$
  S_i = \frac{r_2 O_1 + r_1 O_2}{r_1 + r_2}.
  $$

  Negative homothecy centre with scale factor $k = -r_2 / r_1$. Common transverse tangents intersect at $S_i$.

* **External Centre of Similitude ($S_e$):**
  Dividing $O_1 O_2$ externally in ratio $r_1 : r_2$:

  $$
  S_e = \frac{r_2 O_1 - r_1 O_2}{r_2 - r_1} \qquad (r_1 \neq r_2).
  $$

  Positive homothecy centre with scale factor $k = +r_2 / r_1$. Common direct tangents intersect at $S_e$.

----

2. Structured Decompositions
----------------------------

Proposition 3 (Monge's Theorem — Four Axes of Similitude)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Three circles $C_1, C_2, C_3$ with non-collinear centres $A, B, C$ and radii $a, b, c$.
* **Construct:**
  - Three external centres of similitude $A' \in BC, B' \in CA, C' \in AB$.
  - Three internal centres of similitude $A'' \in BC, B'' \in CA, C'' \in AB$.
* **Demonstrate:**
  The directed division ratios along the sides of $\triangle ABC$ are:

  $$
  \frac{BA'}{A'C} = -\frac{b}{c}, \qquad \frac{CB'}{B'A} = -\frac{c}{a}, \qquad \frac{AC'}{C'B} = -\frac{a}{b}.
  $$

  Their product is:

  $$
  \left(-\frac{b}{c}\right) \left(-\frac{c}{a}\right) \left(-\frac{a}{b}\right) = -1.
  $$

  By :person:`Menelaus's <menelaus>` Theorem, the three external centres $A', B', C'$ are collinear on the **External Axis of Similitude**.
  Likewise, taking one external and two internal centres gives:

  $$
  \left(-\frac{b}{c}\right) \left(\frac{c}{a}\right) \left(\frac{a}{b}\right) = -1,
  $$

  so $(A', B'', C'')$, $(A'', B', C'')$, and $(A'', B'', C')$ are each collinear, yielding the **four axes of similitude**.

Proposition 5 (Circle of Similitude)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Two circles $C_1(O_1, r_1)$ and $C_2(O_2, r_2)$ with external centre $S_e$ and internal centre $S_i$.
* **Construct:** The circle having segment $[S_e S_i]$ as diameter.
* **Demonstrate:**
  By Apollonius's locus theorem (Book VI, Prop. 7), the locus of all points $P$ satisfying $|P O_1| / |P O_2| = r_1 / r_2$ is the circle on diameter $[S_e S_i]$. At every such point $P$, the two circles subtend equal angles:

  $$
  \sin \angle (\text{tangent from } P \text{ to } C_1) = \frac{r_1}{|P O_1|} = \frac{r_2}{|P O_2|} = \sin \angle (\text{tangent from } P \text{ to } C_2).
  $$

----

3. Canonical Invariants
-----------------------

* **Coaxal Property of Similitude Circles:** For any three circles taken in pairs, their three circles of similitude belong to a single coaxal pencil whose radical axis is perpendicular to the line of their centres.
* **Radical Axis of Mutually Tangent Pairs:** If two circles touch two others, the radical axis of either pair passes through a centre of similitude of the other pair (Prop. 4).
