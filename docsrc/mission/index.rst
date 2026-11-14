:navigation: header
:order: 10
:nav_title: Mission
:title: Mission

.. _casey-mission:

Mission
=======

.. rubric:: Bridging Classical Euclidean Elements and Modern Circle, Projective & Triangle Geometry

``geometor/casey`` establishes the authoritative Digital Scriptorium edition and exact symbolic engine for **John Casey's** *A Sequel to the First Six Books of the Elements of Euclid* (1888 / 1892) within the **GEOMETOR** canon.

1. **Historical Bridge Across the Canon**:
   Before Nathan Altshiller-Court codified *College Geometry* (1925 / 1952, ``geometor/altshiller-court``) and Clark Kimberling indexed 50,000+ triangle centers (``geometor/etc``), John Casey's *Sequel* (first published in 1881 and brought to maturity in the 1886–1892 editions with the *Supplementary Chapter on the Recent Elementary Geometry of the Triangle*) was the premier English-language treatise organizing post-Euclidean synthetic geometry book-by-book onto Euclid's *Elements* (``geometor/euclid``, ``geometor/elements``) while absorbing the projective discoveries of Poncelet, Chasles, Monge, Desargues, Pascal, and Brianchon (``geometor/pappus``).

2. **100% Exact Symbolic Euclidean Circle Algebra**:
   Every geometric invariant in ``geometor.casey``—the power of a point $d^2 - r^2$, circle orthogonality $d^2 = r_1^2 + r_2^2$, radical axes, Poncelet limiting points, circular inversion, pole–polar bilinear reciprocity, Casey's generalized Ptolemy bitangent determinant, Feuerbach's tangency $|NI| = R_9 - r$, and Lemoine–Brocard–Steiner–Tarry coordinates—is computed in **100% exact SymPy rational and algebraic arithmetic** with zero ``float`` or ``sp.Float`` approximations inside :class:`~geometor.model.Model`.

3. **Strict Content / Code Separation**:
   Following GEOMETOR Digital Scriptorium standards, the 6-unit **3-Track Book Codex** (``docsrc/sequel_to_euclid/``) preserves faithful historical enunciations, demonstrations, calibrated interactive ``.euclid-graphic`` SVGs, structured summaries, and cross-repository commentary with **zero embedded Python scripts**, while executable ``@proposition`` constructions and symbolic proofs live cleanly in ``src/geometor/casey/``, ``demos/``, and ``docsrc/demos/``.
