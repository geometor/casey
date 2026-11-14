:navigation: header
:order: 20
:nav_title: Usage

==================
Using This Edition
==================

.. rubric:: Interactive Features & Reader's Guide to John Casey's *Sequel to Euclid*

Welcome to the **GEOMETOR Digital Scriptorium** edition of :person:`John Casey's <casey>` landmark treatise, *A Sequel to the First Six Books of the Elements of Euclid* (1888 Fifth Edition & 1892 Sixth Edition edited by :person:`Patrick A. E. Dowling <dowling>`). This edition bridges classical Euclidean planar deduction with nineteenth-century synthetic circle, projective, and modern triangle geometry through interactive multi-track codices and exact symbolic proofs.

Interactive Reader Features
---------------------------

1. Synchronized Reading Tracks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every unit in the :doc:`Book Codex </sequel_to_euclid/index>` is published as a synchronized 3-track edition accessible via the companion track switcher bar:

* **English**: Complete primary text of Casey's propositions, corollaries, and exercises, paired with calibrated interactive ``.euclid-graphic`` SVGs.
* **Summary**: Executive summaries condensing the deductive trajectory, key theorems (Euler line, Nine-Points Circle, Casey's theorem, Feuerbach's point $X(11)$, Lemoine point $K = X(6)$, Brocard points $\Omega, \Omega'$), and algebraic invariant ledgers.
* **Notes**: Scholarly commentary detailing historical provenance, Dowling 1892 collation notes, and systematic cross-references to Euclid's *Elements*, Altshiller-Court's *College Geometry*, Kimberling's *Encyclopedia of Triangle Centers* (ETC), and Pappus's *Synagoge*.

2. Primary-Source Folio Milestones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Marginal folio links such as ``[f. 0007]`` or ``[p. 45]`` record the exact leaf and printed page boundaries of the 1888 Dublin University Press witness (`PDF Folio = Printed Page + 26`). Clicking any marginal folio link or the header **Folio** badge opens high-resolution 300-DPI archival scans directly, verifying every proposition against the historical print.

3. Interactive Diagrams & Deductive Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every diagram across the six units is rendered natively as an interactive SVG generated from exact SymPy coordinates:

* **Geometric Cross-References**: In-line mathematical expressions and geometric markers highlight corresponding geometric elements in the diagram upon hover or click.
* **Rational & Symbolic Precision**: Every figure is constructed in :mod:`geometor.casey` using exact rational or radical numbers (such as the canonical Heronian triangle $(15, 13, 14)$ with integer coordinates and rational circumradius/inradius), completely eliminating floating-point rounding errors.

4. Full-Text Search with In-Page Highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The search box in the sidebar provides instantaneous full-text indexing across the treatise, apparatus, and demonstrations. Queries append ``?highlight=`` parameters to URLs, automatically highlighting searched terminology directly inside proofs, lemmas, and historical notes.

5. Categories, Tags, Document Types & Collection Views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sidebar exposes faceted taxonomy browsing:

* **Categories & Tags**: Navigate topics by mathematical domain (*circles*, *inversion*, *triangles*, *symmedians*, *brocard*, *projective*, *poles-and-polars*).
* **Document Types**: Filter pages by content type (*treatise*, *unit*, *demos*, *biography*, *log*).
* **Collection Views**: Collection index pages offer view toggles between **Cards**, **Banners**, and **List** modes.

6. People, Bibliography & Glossary Tooltips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Prosopographical Hover Cards**: Links marked with ``:person:`` (e.g., :person:`John Casey <casey>`, :person:`Patrick A. E. Dowling <dowling>`, :person:`Karl Wilhelm Feuerbach <feuerbach>`, :person:`Émile Lemoine <lemoine>`, :person:`Henri Brocard <brocard>`) open instant biographical profiles and direct links to the :doc:`People </sequel_to_euclid/persons>` register.
* **Bibliographic Citations**: Citations formatted with ``:cite:`` link directly to the :doc:`Bibliography </sequel_to_euclid/bibliography>`.
* **Glossary Tooltips**: Technical terms linked with ``:term:`` provide instant geometric definitions.
* **Light / Dark Theme**: Toggle visual themes using the control in the upper navigation bar.

----

Command-Line & Python API
-------------------------

Command-Line Interface (CLI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``geometor-casey`` CLI provides immediate shell-level verification and concordance tables:

.. code-block:: bash

   # Display an executive Rich summary table of all verified theorems
   python3 -m geometor.casey summary

   # Display the master cross-repository concordance table
   python3 -m geometor.casey concordance

Python API
~~~~~~~~~~

Run exact symbolic verifications and inspect geometric invariants:

.. code-block:: python

   from geometor.casey.brocard import construct_brocard_and_lemoine_circles
   from geometor.casey.coaxial import construct_radical_axis_and_coaxial_pencil
   from geometor.casey.feuerbach import prove_casey_feuerbach_heronian, prove_casey_theorem_symbolic
   from geometor.casey.poles_polars import construct_pole_and_polar, verify_lahire_reciprocity_symbolic

   # Verify Casey's Generalized Ptolemy Theorem symbolically
   casey_res = prove_casey_theorem_symbolic()
   print("Casey's Theorem verified:", casey_res.verified)

   # Verify Feuerbach's Theorem on the canonical Heronian triangle
   fb = prove_casey_feuerbach_heronian()
   print(f"Feuerbach point Fe: {fb.feuerbach_point}")
   print(f"Distance |N - I| == R/2 - r: {fb.ni_distance == fb.r9 - fb.r}")

   # Construct Coaxal Circles and Limiting Points
   coax = construct_radical_axis_and_coaxial_pencil()
   print(f"Radical Center: {coax.radical_center}")
   print(f"Poncelet Limiting Points: {coax.limiting_points}")
