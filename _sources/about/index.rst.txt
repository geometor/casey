:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:
.. _about-casey:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor/casey`` establishes the authoritative Digital Scriptorium edition and exact symbolic engine for **John Casey's** landmark nineteenth-century treatise, *A Sequel to the First Six Books of the Elements of Euclid* (1888 / 1892). Casey (1820–1891), Fellow of the Royal Society and Professor of Higher Mathematics at the Catholic University of Ireland, stood alongside George Salmon, Richard Townsend, and Robert Stawell Ball at the summit of the nineteenth-century Dublin school of pure geometry.

Before Nathan Altshiller-Court codified *College Geometry* (1925 / 1952, ``geometor/altshiller-court``) and Clark Kimberling catalogued thousands of triangle centers (``geometor/etc``), Casey's *Sequel* was the premier English-language work organizing modern post-Euclidean synthetic geometry book-by-book directly onto Euclid's *Elements* (``geometor/euclid``, ``geometor/elements``) while absorbing the projective methods of Poncelet, Chasles, Monge, Desargues, Pascal, and Brianchon (``geometor/pappus``). It systematically develops the theory of coaxal circles, poles and polars, circular inversion, Casey's celebrated generalized Ptolemy theorem, and the modern geometry of the triangle (the symmedian point, Brocard figures, and Lemoine circles).

Following GEOMETOR Digital Scriptorium standards, this edition extracts the treatise into a synchronized 6-unit **3-Track Book Codex** (``docsrc/sequel_to_euclid/``): pairing faithful historical enunciations and demonstrations with calibrated interactive ``.euclid-graphic`` SVGs, structured mathematical summaries with algebraic invariant ledgers, and comprehensive collation notes. In accordance with strict content/code separation, the running text contains zero embedded execution scripts, while runnable, machine-verified constructions and symbolic proofs live cleanly in ``src/geometor/casey/`` and ``demos/``.

The GEOMETOR Mission
--------------------

The **GEOMETOR** initiative, founded by **phi ARCHITECT**, is dedicated to a three-fold synthesis of classical geometry, exact symbolic computation, and modern knowledge architecture:

* **Extracting Historical Semantic Knowledge**: Moving beyond passive page scans and static OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises. We elevate running prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs where every enunciation, proof step, and historical cross-reference is individually referenceable.
* **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions in 100% exact symbolic algebra (via ``SymPy``) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic number fields rather than lossy floating-point approximations. Every geometric theorem is treated as an exact algebraic truth verifiable through computational modeling.
* **Repurposing Knowledge Across Mediums**: Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (via ``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

John Casey, LL.D., F.R.S. (1820–1891)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**John Casey** (born May 12, 1820, Kilbehenny, County Limerick; died January 3, 1891, Dublin) stands alongside George Salmon, Richard Townsend, and Robert Stawell Ball at the summit of the nineteenth-century Dublin school of pure geometry. Educated first in local Munster schools and largely self-taught in higher mathematics while serving as headmaster of the Kilkenny Central Model Schools, Casey entered **Trinity College Dublin** as a pensioner in 1858 at the age of thirty-eight—having already communicated original discoveries on the geometry of the triangle and circle to Richard Townsend and George Salmon. Electing Scholarship in 1861 and graduating B.A. in 1862, he subsequently served as Professor of Higher Mathematics and Mathematical Physics at the Catholic University of Ireland (from 1873) and Fellow of the Royal University of Ireland (from 1882), elected Fellow of the Royal Society in 1875.

In **1866** (*Proceedings of the Royal Irish Academy*, vol. 9, pp. 396–423), Casey published his celebrated **generalization of Ptolemy's Theorem** (Book VI, Section IV, Proposition 10): four circles $O_1, O_2, O_3, O_4$ are tangent to a fifth circle (or straight line) if and only if the six pairwise common tangents $\overline{ij}$ satisfy a vanishing Cayley–Menger / Ptolemy relation

$$
\overline{12}\cdot\overline{34} \pm \overline{14}\cdot\overline{23} \pm \overline{13}\cdot\overline{24} = 0.
$$

Already as an undergraduate in *Quarterly Journal of Pure and Applied Mathematics* **4** (1861), pp. 245–252, Casey had discovered the three-line circular-inversion proof of **Feuerbach's Theorem**—inverting the incircle and the $A$-excircle into themselves from the midpoint $M_a$ of $BC$ with squared radius $\frac{1}{4}(b - c)^2$ so that the fourth common tangent maps directly onto the nine-points circle!

Editions of the *Sequel* (1881–1892)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Published in the *Dublin University Press Series* (Dublin: Hodges, Figgis, & Co.; London: Longmans, Green, & Co.):

* **1st–3rd Editions (1881–1884)**: Books I–IV and Book VI Sections I–VII, culminating in inversion, Casey's theorem, Feuerbach's theorem, Hart's circle, poles and polars, and coaxal circles.
* **4th Edition (1886)**: Major expansion adding the **Supplementary Chapter on the Recent Elementary Geometry of the Triangle** (pp. 165–222), introducing English-speaking students systematically to Lemoine's symmedian point $K = X(6)$, Brocard's points $\Omega, \Omega'$ and Brocard angle $\omega$, Tucker's and Taylor's circles, Neuberg's and Tarry's theorems, and harmonic polygons.
* **5th Edition (1888)**: Revised and enlarged by Casey himself (pp. i–xviii, 1–251; 276 archival folios), expanding Theory of Harmonic Polygons and Associated Figures. Inspected directly via 300-DPI multimodal scan vision as the primary witness of this codex.
* **6th Edition (1892)**: Posthumously seen through the press and revised by Casey's pupil and son-in-law **Patrick A. E. Dowling, B.A.** (pp. i–xviii, 1–248), preserving the exact proposition and section numbering of the 5th edition; cited canonically as ``[casey:sequel:1892]`` in Nathan Altshiller-Court's *College Geometry* (1952).

Digital Scriptorium Verification Protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every unit in ``docsrc/sequel_to_euclid/`` obeys the GEOMETOR Multimodal Scan Vision protocol:

1. Archival page images rendered at 300 DPI (`PDF Folio = Printed Page + 26` in the 1888 5th-edition witness) were visually inspected directly via multimodal scan vision rather than OCR layers.
2. Each unit pairs synchronized **English** (historical enunciations, demonstrations, corollaries, and calibrated ``.euclid-graphic`` SVGs), **Summary** (mathematical synthesis and invariants ledger), and **Notes** (historical provenance, Dowling 1892 collation, and cross-references to ``euclid``, ``elements``, ``altshiller-court``, ``etc``, and ``pappus``).

Scholarly Apparatus & References:

* :doc:`Reader's Guide and Usage </usage/index>`
* :doc:`Sequel to Euclid Codex </sequel_to_euclid/index>`
* :doc:`Exact Symbolic Demonstrations </demos/index>`
* :doc:`Biographical Register of Persons </sequel_to_euclid/persons>`
* :doc:`Systematic Bibliography </sequel_to_euclid/bibliography>`
