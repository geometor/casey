==============
geometor-casey
==============

Digital Scriptorium **3-Track Book Codex** and **100% Exact Symbolic ``geometor.model`` Engine** for **John Casey's** *A Sequel to the First Six Books of the Elements of Euclid, Containing an Easy Introduction to Modern Geometry, with Numerous Examples* (5th ed. 1888 / 6th ed. ed. Patrick A. E. Dowling 1892, Dublin: Hodges, Figgis, & Co. / London: Longmans, Green, & Co.).

Overview
--------

``geometor-casey`` bridges classical Euclidean geometry (``geometor/euclid``, ``geometor/elements``) with modern circle, projective, and triangle geometry (``geometor/altshiller-court``, ``geometor/etc``, ``geometor/pappus``):

1. **6-Unit 3-Track Book Codex (``docsrc/sequel_to_euclid/``)**:
   - Synchronized **English** | **Summary** | **Notes** tracks across Books I–IV, Book VI Sections I–VII, and the *Supplementary Chapter on the Recent Elementary Geometry of the Triangle*.
   - Verified directly against 300-DPI archival page scans (`PDF Folio = Printed Page + 26`), paired with **7 calibrated interactive ``.euclid-graphic`` SVGs** and hoverable ``:person:`` (33 geometers), ``:cite:`` (22 works), and ``:term:`` (30 terms) apparatus cards.
   - Strict content/code separation: zero executable Python scripts inside historical codex ``.rst`` files.

2. **Exact Symbolic Euclidean Circle & Triangle Engine (``src/geometor/casey/``)**:
   - ``geometor.casey.invariants``: Circle power, orthogonality ($d^2 = r_1^2 + r_2^2$), bitangent quadrances, circular inversion, pole–polar bilinear duality, radical axes, barycentric coordinates, and ``@proposition`` compass subconstructions.
   - ``geometor.casey.feuerbach``: Symbolic proof of **Casey's Generalized Ptolemy Theorem** ($\overline{12}\cdot\overline{34} + \overline{14}\cdot\overline{23} = \overline{13}\cdot\overline{24}$), Euler line & Nine-Points Circle, and **Casey's 1861 Orthogonal Inversion Proof of Feuerbach's Theorem** at $F_e = X(11) = (6, 8)$ on the canonical $(15, 13, 14)$ Heronian triangle.
   - ``geometor.casey.coaxial``: Disjoint-circle radical axis construction, Casey's Difference-of-Powers Theorem (Book III, Prop. 24), and **Poncelet's Limiting Points** $L_1, L_2 = (\mp 8, 0)$.
   - ``geometor.casey.poles_polars``: Pure-straightedge Complete Quadrilateral harmonic section, inscribed-quadrangle polar construction, Self-Conjugate Triangle $\triangle DUV$, and **La Hire's Reciprocity**.
   - ``geometor.casey.brocard``: **Lemoine's Symmedian Point** $K = X(6)$, First Lemoine & Cosine Circles, **Brocard Points** $\Omega, \Omega'$, Brocard Angle $\cot\omega = \frac{295}{168}$, **7-Point Brocard Circle**, **Steiner Point** $X(99)$, **Tarry Point** $X(98)$, and **de Longchamps Point** $X(20)$.

Installation & Usage
--------------------

Managed with Python 3.13 and ``uv`` inside the GEOMETOR workspace:

.. code-block:: bash

   # Run the 4 exact symbolic demonstration suites and export SVGs
   python3 demos/casey_feuerbach.py
   python3 demos/coaxial_pencil_and_limiting_points.py
   python3 demos/poles_polars_lahire.py
   python3 demos/brocard_and_lemoine_circles.py

   # CLI ledger & cross-repository concordance
   python3 -m geometor.casey summary
   python3 -m geometor.casey concordance

   # Verification & Book Codex compilation
   pytest
   ruff check src demos tests
   publish build

License
-------

MIT License (code & apparatus); John Casey's 1888 / 1892 *Sequel to Euclid* text is in the public domain.
