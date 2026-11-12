:layout: book
:title: Unit 1 Notes — Historical & Cross-Canon Commentary

.. _sequel-unit-1-notes:

Unit 1 Notes: Historical Provenance & Cross-Repository Commentary
=================================================================

.. rubric:: Collation of the 1888 & 1892 Editions and Links to ``euclid``, ``elements``, ``altshiller-court``, and ``etc``

1. Why Casey Attaches Orthocentre & Mean Centres Directly to Book I
-------------------------------------------------------------------

Unlike Euclid's *Elements*—which postpones the circumcentre and incentre until Book IV (``IV.4``, ``IV.5``) and never names the orthocentre or centroid—:person:`John Casey <casey>` proves the concurrency of all four classical cevians directly in Book I (Props. 9–11, pp. 7–9) using only congruence (``I.4``, ``I.26``) and parallelogram properties (``I.31``, ``I.34``). Notice the elegance of Casey's anticomplementary proof of the orthocentre (Prop. 10 Cor., f. ``0034``): instead of invoking cyclic quadrilaterals from Book III, he embeds $\triangle ABC$ as the medial triangle of $\triangle A'B'C'$ so that altitudes reduce immediately to perpendicular bisectors! In ``geometor/altshiller-court`` (:cite:`*College Geometry* <altshiller-court:1952>`, §§ 93–96), :person:`Nathan Altshiller-Court <altshiller-court>` adopts this exact anticomplementary reduction.

2. Centres of Mean Position & Barycentric Coordinates
-----------------------------------------------------

Casey's treatment of **Centres of Mean Position** (Book I, Props. 17–18, pp. 12–13; Book II, Props. 11–13) follows Simon Antoine Jean L'Huilier (1809) and August Ferdinand Möbius (*Der barycentrische Calcul*, 1827), translating static moments into pure Euclidean geometry so students reading "Mixed Mathematics" (mechanics and hydrostatics at Trinity College Dublin) could derive Leibniz's identity $\sum m_i PA_i^2 = \sum m_i GA_i^2 + (\sum m_i) PG^2$ without analytic coordinates. In ``geometor/casey`` (:func:`~geometor.casey.invariants.barycentric_point`) and ``geometor/etc``, every Kimberling triangle center is represented in exact homogeneous barycentric weights $(u : v : w)$, directly realizing Casey's Mean Centre for $A, B, C$.

3. Lineage of the Nine-Points Circle (Brianchon–Poncelet 1821 & Feuerbach 1822)
-------------------------------------------------------------------------------

Although Euler (1765) already knew that the orthocentre, centroid, and circumcentre are collinear and that the circle through the altitude feet passes through the side midpoints, the explicit nine-point concyclicity was published first by :person:`Charles Julien Brianchon <brianchon>` and :person:`Jean-Victor Poncelet <poncelet>` in Gergonne's *Annales de Mathématiques* **11** (1820–1821) and independently a year later by :person:`Karl Wilhelm Feuerbach <feuerbach>` (:cite:`*Eigenschaften* <feuerbach:1822>`), who discovered its tangency with the four tritangent circles (proved in :ref:`Unit 4 <sequel-unit-4-en>`).

Casey's proof in Book IV, Prop. 5 (ff. ``0083``–``0084``, pp. 57–58) uses the three diameters $M_a E_a, M_b E_b, M_c E_c$ and Thales's semicircle theorem (Euclid ``III.31``). In :person:`Patrick A. E. Dowling's <dowling>` :cite:`1892 Sixth Edition <casey:sequel:1892>`, Book IV Prop. 5 and its corollaries on the orthocentric group $\{A, B, C, H\}$ (where any of the four points is the orthocentre of the remaining three, so all four triangles share the *same* Nine-Points Circle!) remain word-for-word aligned with the 1888 Fifth Edition.
