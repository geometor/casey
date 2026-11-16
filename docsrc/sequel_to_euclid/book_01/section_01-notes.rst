:title: Book I, Section I Notes — Historical & Cross-Canon Commentary
:layout: book
:canonical_id: Book I, Section I Notes
:order: 1
:tracks: English: section_01-en | Summary: section_01-summary | Notes: section_01-notes

.. _casey-book-01-sec-01-notes:
.. _sequel-unit-1-notes:

Book I, Section I Notes: Historical Provenance & Cross-Repository Commentary
============================================================================

.. rubric:: Collation of the 1888 & 1892 Editions and Links to ``euclid``, ``elements``, ``altshiller-court``, and ``etc``

1. Why Casey Attaches Orthocentre & Mean Centres Directly to Book I
-------------------------------------------------------------------

Unlike Euclid's *Elements*—which postpones the circumcentre and incentre until Book IV (``IV.4``, ``IV.5``) and never names the orthocentre or centroid—:person:`John Casey <casey>` proves the concurrency of all four classical cevians directly in Book I (Props. 10–11, pp. 7–9) using only congruence (``I.4``, ``I.26``) and parallelogram properties (``I.31``, ``I.34``). Notice the elegance of Casey's anticomplementary proof of the orthocentre (Prop. 10 Cor. 1, f. ``0034``): instead of invoking cyclic quadrilaterals from Book III, he embeds $\triangle ABC$ as the medial triangle of $\triangle A'B'C'$ so that altitudes reduce immediately to perpendicular bisectors! In ``geometor/altshiller-court`` (:cite:`*College Geometry* <altshiller-court:1952>`, §§ 93–96), :person:`Nathan Altshiller-Court <altshiller-court>` adopts this exact anticomplementary reduction.

2. Centres of Mean Position & Barycentric Coordinates
-----------------------------------------------------

Casey's treatment of **Centres of Mean Position** (Book I, Props. 16–17, pp. 12–13) follows Simon Antoine Jean L'Huilier (1809) and August Ferdinand Möbius (*Der barycentrische Calcul*, 1827), translating static moments into pure Euclidean geometry so students reading "Mixed Mathematics" (mechanics and hydrostatics at Trinity College Dublin) could derive Leibniz's identity $\sum m_i PA_i^2 = \sum m_i GA_i^2 + (\sum m_i) PG^2$ without analytic coordinates. In ``geometor/casey`` (:func:`~geometor.casey.invariants.barycentric_point`) and ``geometor/etc``, every Kimberling triangle center is represented in exact homogeneous barycentric weights $(u : v : w)$, directly realizing Casey's Mean Centre for $A, B, C$.

3. Collation with the 1892 Sixth Edition
----------------------------------------

In :person:`Patrick A. E. Dowling's <dowling>` :cite:`1892 Sixth Edition <casey:sequel:1892>`, Book I Section I remains word-for-word aligned with the 1888 Fifth Edition, preserving Casey's enunciation numbering, notations, and demonstrations unchanged.
