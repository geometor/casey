:title: Unit 2 Notes — Gaultier, Steiner, Poncelet & SymPy Gaps

.. _sequel-unit-2-notes:

Unit 2 Notes: Gaultier, Steiner, Poncelet & Exact Circle Algebra
================================================================

.. rubric:: Historical Provenance & Architectural Notes on Coaxal Systems

1. Historical Synthesis: Gaultier (1813), Poncelet (1822) & Steiner (1826)
--------------------------------------------------------------------------

Three Continental memoirs converged to create the circle theory expounded in Casey's Book III (pp. 41–49) and Book VI, Section V (pp. 113–126):

* :person:`Louis Gaultier <gaultier>` (:cite:`*Journal de l'École Polytechnique* 16, 1813 <gaultier:1813>`) coined *axe radical* ("radical axis") and *centre radical* ("radical centre"), giving the three-circle secant construction for disjoint circles that Casey places in Book III, Props. 21 & 23.
* :person:`Jean-Victor Poncelet <poncelet>` (:cite:`*Traité des propriétés projectives des figures*, 1822 <poncelet:1822>`) introduced coaxal pencils and recognized the **limiting points** (*points limites*) $L_1, L_2$ of a non-intersecting pencil as real zero-radius circles dual to the ideal common chord—a breakthrough demonstrating how imaginary intersections in geometry manifest through real Euclidean invariants ($\delta = +64 \implies L_{1,2} = (\mp 8, 0)$).
* :person:`Jakob Steiner <steiner>` (:cite:`Crelle's *Journal* 1, 1826 <steiner:1826>`) named the *Potenz eines Punktes* ("power of a point") $|PO|^2 - r^2$, unifying Euclid ``III.35`` (interior chord product) and ``III.36`` (exterior secant-tangent product) into a single signed quadratic functional.

2. Cross-Canon Links & ``sympy.geometry.Circle`` Audit
------------------------------------------------------

* **Euclid & Elements:** Generalizes ``III.17`` (tangent construction), ``III.35–37`` (intersecting chords and secants), and ``I.47`` (orthogonality $d^2 = r_1^2 + r_2^2$).
* **Altshiller-Court:** Corresponds directly to :cite:`*College Geometry* <altshiller-court:1952>` Chapter VIII, §§ 358–376 (*Inverse Points & Orthogonal Circles*) and §§ 417–498 (*Power of a Point, Radical Axis & Coaxal Circles*).
* **Exact SymPy Gap Closure:** Standard ``sympy.geometry.Circle`` lacks ``power``, ``is_orthogonal``, ``radical_axis``, and ``limiting_points``; :mod:`geometor.casey.invariants` and :mod:`geometor.casey.coaxial` supply all four with 100% exact rational/radical verification.
