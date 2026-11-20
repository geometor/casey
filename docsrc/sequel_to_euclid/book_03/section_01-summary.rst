:title: Book III, Section I Summary — Additional Propositions
:layout: book
:canonical_id: Book III, Section I Summary
:order: 1
:folio: 0055–0074 (p. 29–48)
:tracks: English: section_01-en | Summary: section_01-summary | Notes: section_01-notes

.. _casey-book-03-sec-01-summary:
.. _sequel-unit-2-summary:

Book III, Section I Summary: Additional Propositions
====================================================

.. rubric:: Structured Decomposition & Invariant Ledger for Casey's Book III Section I (pp. 29–48)

.. folio:: 0055
   :page: 29

1. Architectural Overview
-------------------------

Section I develops the foundational theory of the circle beyond Euclid (pp. 29–48, Folios 0055–0074):

* **Touching Circles & Common Tangents (Props. 1–8):** Equal tangents, parallel diameters through points of contact, touching semicircle–chord relations, and direct/transverse common tangents.
* **Cyclic Quadrilaterals, :term:`Simson's Line <simson-line>` & Extremal Chords (Props. 9–19):** Rectangle identity $OE \cdot OF = OG \cdot OH$ on opposite sides vs. diagonals (`0060.g1.svg`), **Simson's Pedal Line** of collinear perpendicular feet from circumcircle point $P$ (Prop. 12, f. ``0060–0061``) and **Miquel's four-line pedal point** (Prop. 12 Cor. 2, `0061.g1.svg`), bisection of orthocentre chord $OP$ by Simson's line (Prop. 14), and minimum-intercept tangent triangles (Props. 18–19).
* **Inverse Points with respect to a Circle (Prop. 20):** $OP \cdot OP' = r^2$. For any boundary point $A$, the distance ratio $AP : AP' = r / OP'$ is constant (Apollonian circle property).
* **Power of a Point & Orthogonal Circles (Props. 21–22):** Power $\operatorname{pow}(P, C) = |PO|^2 - r^2 = |PT|^2$. Two circles cut orthogonally iff $|O_1 O_2|^2 = r_1^2 + r_2^2$.
* **The Radical Axis & Radical Centre (Prop. 23):** Locus of points of equal power with respect to two non-concentric circles is a straight line perpendicular to the line of centres. The radical axes of three circles concur at the **Radical Centre** $R_c$.
* **Poncelet's Limiting Points (Prop. 23 Def.):** The point-circles ($r = 0$) of a coaxal pencil, given by $DI = DI' = \sqrt{\operatorname{pow}(D, C_1)}$.
* **Casey's Difference of Powers (Prop. 24):** $\operatorname{pow}(P, C_1) - \operatorname{pow}(P, C_2) = 2\,|O_1 O_2| \cdot PN$.
* **Poles, Polars & Reciprocity (Props. 25–28):** Harmonic conjugation on secants; :person:`La Hire's <la-hire>` reciprocity: $A \in \operatorname{polar}(B) \iff B \in \operatorname{polar}(A)$.

----

.. folio:: 0060
   :page: 34

2. Structured Decompositions
----------------------------

Radical Axis & Poncelet Limiting Points (Prop. 23)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Two non-concentric circles $C_1 = (O_1, r_1)$ and $C_2 = (O_2, r_2)$ with line of centres $O_1 O_2$.
* **Construct:** Find point $D$ on $O_1 O_2$ such that $O_1 D^2 - O_2 D^2 = r_1^2 - r_2^2$. Erect perpendicular $DG \perp O_1 O_2$.
* **Demonstrate:** For any point $G \in DG$, $G O_1^2 - r_1^2 = (GD^2 + O_1 D^2) - r_1^2 = GD^2 + (O_1 D^2 - r_1^2) = GD^2 + (O_2 D^2 - r_2^2) = G O_2^2 - r_2^2$.
  Hence $\operatorname{pow}(G, C_1) = \operatorname{pow}(G, C_2)$ identically, proving that equal-power tangents $|GE| = |GE'|$ hold for all $G \in DG$.
* **Invariants:**

  - Verified symbolically in :func:`~geometor.casey.coaxial.construct_radical_axis_and_coaxial_pencil`:
    - Centers: $O_1 = (-9, 0), r_1 = 5$; $O_2 = (16, 0), r_2 = 12$; $O_3 = (0, 19), r_3 = 13$.
    - Radical foot: $D = (0, 0)$; Radical axis: $x = 0$.
    - Limiting points: $L_1 = (-8, 0), L_2 = (8, 0)$.
    - Radical centre: $R_c = (0, -6)$.

La Hire's Reciprocity (Prop. 25)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Given:** Circle $C = (O, r)$ and points $A, B$ such that $B$ lies on the polar of $A$.
* **Construct:** Polar of $A$ is $PB \perp OA$ where $OP \cdot OA = r^2$. Drop $AQ \perp OB$.
* **Demonstrate:** Concyclic quadrilateral $OPBQ$ has right angles at $P$ and $Q$. By Euclid III.36, $OQ \cdot OB = OP \cdot OA = r^2$.
  Since $AQ \perp OB$ and passes through the inverse point $Q$ of $B$, the line $AQ$ is the polar of $B$, which passes through $A$.
* **Invariants:**
  - Bilinear symmetry: $(x_A - x_O)(x_B - x_O) + (y_A - y_O)(y_B - y_O) = r^2$.
  - Secant cross-ratio: $(P_1, P_2; A, B) = -1$ (harmonic range).
