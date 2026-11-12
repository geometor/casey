:layout: book
:title: Unit 3 Notes — Pappus, Chasles, Desargues & Pascal

.. _sequel-unit-3-notes:

Unit 3 Notes: From Pappus's *Synagoge* to Chasles & Pascal
==========================================================

.. rubric:: Historical Lineage & Cross-Repository Links to ``geometor/pappus``, ``hilbert``, and ``altshiller-court``

1. Ancient Roots in Pappus Book VII (`geometor/pappus`)
-------------------------------------------------------

As :person:`Michel Chasles <chasles>` demonstrated in his *Aperçu historique* (1837) and :cite:`*Traité de géométrie supérieure* (1852) <chasles:1852>`, nearly every projective proposition in Casey's Book VI, Sections III & VI descends from :person:`Pappus of Alexandria's <pappus>` :cite:`*Synagoge* Book VII <pappus:synagoge>` (c. 340 CE, modeled symbolically in ``geometor/pappus``):

* Cross-ratio invariance under central projection appears in *Synagoge* VII, Prop. 129;
* The harmonic division of the diagonals of a complete quadrilateral appears in *Synagoge* VII, Prop. 131;
* Pappus's Hexagon Theorem (VII, Props. 138–139) is the degenerate two-line conic specialization of :person:`Blaise Pascal's <pascal>` *Hexagrammum Mysticum* (1640), which Casey proves for the circle using Chasles's perspective-pencil lemma ($B(ACDE) = F(ACDE)$ with shared point $D$).

2. Axiom-Independence Context (`geometor/hilbert`)
--------------------------------------------------

In ``geometor/hilbert`` (*Grundlagen der Geometrie*, Chs. V–VI), David Hilbert reveals the deep metamathematical role of Desargues's and Pascal's theorems: planar Desargues characterizes embeddability in 3-space (or associativity of the segment division ring), while Pascal characterizes commutativity of multiplication (Pappus's theorem). Casey's elementary proofs in Book VI, Sec. VI rely explicitly on Euclid's theory of proportion (Book V / VI, which embeds the Archimedean axiom) and inscribed angles (``III.21``, which uses congruence).

3. Concordance with Altshiller-Court (`geometor/altshiller-court`)
------------------------------------------------------------------

Casey's Book VI, Secs. I–III correspond directly to :cite:`*College Geometry* <altshiller-court:1952>` Chapter II (*Similitude and Homothecy*, §§ 23–53), Chapter VI (*Transversals: Menelaus, Ceva & Desargues*, §§ 306–344), and Chapter VII (*Harmonic Division & Complete Quadrilaterals*, §§ 345–357), while Casey's Sec. VI goes substantially deeper than Altshiller-Court into general anharmonic (cross) ratios and homographic pencils.
