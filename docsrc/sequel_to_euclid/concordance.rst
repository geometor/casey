:navigation: footer
:nav_title: Concordance
:title: Master Concordance & SymPy Circle Audit

.. _concordance:

Master Cross-Repository Concordance & SymPy Circle Audit
========================================================

.. rubric:: Mapping Casey's *Sequel* (1888 / 1892) Across ``euclid``, ``elements``, ``altshiller-court``, ``etc``, ``pappus``, and ``sympy.geometry``

1. Cross-Repository Canon Concordance
-------------------------------------

Every proposition cluster in :person:`John Casey's <casey>` :cite:`*Sequel to Euclid* <casey:sequel:1892>` bridges classical Euclidean propositions (``geometor/euclid``, ``geometor/elements``) forward to :person:`Nathan Altshiller-Court's <altshiller-court>` :cite:`*College Geometry* <altshiller-court:1952>` (``geometor/altshiller-court``), :person:`Clark Kimberling's <casey>` :cite:`*Encyclopedia of Triangle Centers* <kimberling:etc>` (``geometor/etc``), and projective configurations in ``geometor/pappus``:

.. list-table:: Master Concordance of Casey's *Sequel to Euclid* (Units 1–6)
   :header-rows: 1
   :widths: 10 22 14 14 18 12 10

   * - Unit
     - Casey Locus & Folio (pp.)
     - Theorem / Topic
     - ``euclid`` / ``elements``
     - ``altshiller-court`` (1952)
     - ``etc`` Centers
     - ``geometor.casey`` Symbol
   * - :ref:`Unit 1 <sequel-unit-1-en>`
     - Book I, Prop. 10 Cor. · f. ``0034`` (p. 8)
     - Concurrency of Altitudes (Orthocentre $H$)
     - ``I.12``, ``I.31``, ``I.34``
     - §§ 93–96 (Ch. III)
     - ``X(4)``
     - ``construct_euler_nine_point``
   * - :ref:`Unit 1 <sequel-unit-1-en>`
     - Book I, Props. 17–18 · f. ``0038–0039`` (pp. 12–13)
     - Centres of Mean Position (Weighted Barycentres)
     - ``I.10``, ``VI.2``
     - §§ 65–72 (Ch. III)
     - ``X(2)``
     - ``barycentric_point``
   * - :ref:`Unit 1 <sequel-unit-1-en>`
     - Book I, Misc. Ex. 42–46 · f. ``0046`` (p. 20)
     - Euler Line ($O, G, N, H$ with $HG = 2\,GO$)
     - ``I.29``, ``IV.5``, ``VI.4``
     - §§ 101–103 (Ch. III)
     - ``X(2)``, ``X(3)``, ``X(4)``, ``X(5)``
     - ``construct_euler_nine_point``
   * - :ref:`Unit 1 <sequel-unit-1-en>`
     - Book II, Props. 1–2, 7, 10 · f. ``0048–0052`` (pp. 22–26)
     - Apollonius Median, Euler Identity & Stewart's Theorem
     - ``II.4``, ``II.7``, ``II.12``, ``II.13``
     - §§ 68, 243, 307–309
     - ``X(2)``
     - ``prove_casey_theorem_symbolic``
   * - :ref:`Unit 1 <sequel-unit-1-en>`
     - Book IV, Prop. 5 · f. ``0083–0084`` (pp. 57–58)
     - Nine-Points Circle ($R_9 = R/2$, 9 concyclic points)
     - ``III.21``, ``III.31``, ``IV.5``
     - §§ 104–113 (Ch. III)
     - ``X(5)``
     - ``construct_euler_nine_point``
   * - :ref:`Unit 2 <sequel-unit-2-en>`
     - Book III, Props. 20–22 · f. ``0067–0068`` (pp. 41–42)
     - Inverse Points, Power of a Point & Orthogonal Circles
     - ``I.47``, ``III.35–37``
     - §§ 358–376, 417–428 (Ch. VIII)
     - —
     - ``are_orthogonal_circles``
   * - :ref:`Unit 2 <sequel-unit-2-en>`
     - Book III, Props. 23–24, 28 & VI.V · f. ``0069–0070``, ``0139–0145``
     - Radical Axis, Radical Centre, Coaxal Pencils & Limiting Points
     - ``III.17``, ``III.36``
     - §§ 429–498 (Ch. VIII)
     - —
     - ``construct_radical_axis_and_coaxial_pencil``
   * - :ref:`Unit 3 <sequel-unit-3-en>`
     - Book VI, Sec. I, Props. 2 & 4 · f. ``0093–0095`` (pp. 67–69)
     - Ceva's Concurrency & Menelaus's Transversal Theorems
     - ``VI.1``, ``VI.2``
     - §§ 313–335 (Ch. VI)
     - ``X(1)``, ``X(2)``, ``X(4)``, ``X(7)``, ``X(8)``
     - ``barycentric_point``
   * - :ref:`Unit 3 <sequel-unit-3-en>`
     - Book VI, Sec. II, Props. 1–6 · f. ``0108–0113`` (pp. 82–87)
     - Centres of Similitude & Monge's Four Axes Theorem
     - ``VI.3``, ``VI.4``
     - §§ 23–53, 402–416
     - ``X(55)``, ``X(56)``
     - ``radical_axis_line``
   * - :ref:`Unit 3 <sequel-unit-3-en>`
     - Book VI, Sec. III & Sec. VI · f. ``0113–0120``, ``0153–0166``
     - Harmonic Section, Complete Quadrilateral, Anharmonic Ratio, Desargues & Pascal
     - ``VI.3``, ``VI.A``
     - §§ 339–357 (Chs. VI–VII)
     - *(Pappus VII.129–139)*
     - ``construct_complete_quadrilateral_harmonic``
   * - :ref:`Unit 4 <sequel-unit-4-en>`
     - Book VI, Sec. IV, Props. 1–9 & Cor. 1 · f. ``0121–0129`` (pp. 95–103)
     - Circular Inversion & Pappus's Arbelos Chain
     - ``III.32``, ``III.36``, ``VI.6``
     - §§ 518–535 (Ch. IX)
     - *(Pappus IV)*
     - ``invert_point``
   * - :ref:`Unit 4 <sequel-unit-4-en>`
     - Book VI, Sec. IV, Props. 10–11 & Cor. 2 · f. ``0129–0134`` (pp. 103–108)
     - **Casey's Generalized Ptolemy Theorem**, **Feuerbach's Theorem** & Hart's Circle
     - ``IV.4``, ``VI.D``
     - §§ 200–205, 502–504, 536–546
     - ``X(1)``, ``X(5)``, ``X(11)``
     - ``construct_casey_feuerbach``
   * - :ref:`Unit 4 <sequel-unit-4-en>`
     - Book III, Props. 25, 27 & VI.VII · f. ``0070–0073``, ``0167–0173``
     - Poles & Polars, La Hire's Reciprocity, Self-Conjugate Triangles & Brianchon
     - ``III.17``, ``III.36``
     - §§ 377–401 (Ch. VIII)
     - *(Dual of Pascal)*
     - ``construct_pole_and_polar``
   * - :ref:`Unit 5 <sequel-unit-5-en>`
     - Supp. Ch., Secs. I & III · f. ``0191–0198``, ``0205–0209`` (pp. 165–183)
     - Isogonal Conjugates, Symmedians, Lemoine's Point $K$, Lemoine & Cosine Circles
     - ``III.32``, ``VI.2``
     - §§ 557–590, 616–628, 661–673
     - ``X(6)``, ``X(182)``
     - ``construct_symmedian_and_lemoine_circles``
   * - :ref:`Unit 6 <sequel-unit-6-en>`
     - Supp. Ch., Secs. II–VII & Misc. · f. ``0201–0274`` (pp. 175–248)
     - Brocard Points $\Omega, \Omega'$, Brocard Circle, Tucker/Taylor, Harmonic Polygons, Steiner, Tarry & Longchamps
     - ``III.21``, ``III.32``, ``VI.4``, ``VI.18``
     - §§ 629–689 (Ch. X)
     - ``X(3)``, ``X(6)``, ``X(20)``, ``X(39)``, ``X(98)``, ``X(99)``, ``X(182)``
     - ``construct_brocard_and_lemoine_circles``

----

2. ``sympy.geometry.Circle`` Capability Audit vs. ``geometor.casey``
--------------------------------------------------------------------

Inspection of ``sympy.geometry.curve.Circle`` in SymPy confirms that standard ``sympy.geometry`` provides basic Euclidean primitives (``center``, ``radius``, ``equation``, ``tangent_lines``, ``is_tangent``) yet **omits the entire modern Euclidean circle-algebra toolkit codified by Casey**. :mod:`geometor.casey` supplies exact closed-form symbolic implementations for every gap (audited programmatically via :func:`~geometor.casey.concordance.audit_sympy_circle_gaps`):

.. list-table:: Audit of ``sympy.geometry.Circle`` Capabilities vs. ``geometor.casey``
   :header-rows: 1
   :widths: 22 14 26 38

   * - Euclidean Circle Concept
     - In ``sympy.geometry``?
     - ``geometor.casey`` Implementation
     - Algebraic Invariant / Upstream Candidate Note
   * - Power of a Point $\operatorname{pow}(P, C)$
     - **Missing** (``False``)
     - :func:`~geometor.casey.invariants.circle_power`
     - Exact rational/radical $|PO|^2 - r^2$ (Casey III.20–24).
   * - Circle Orthogonality ($C_1 \perp C_2$)
     - **Missing** (``False``)
     - :func:`~geometor.casey.invariants.are_orthogonal_circles`
     - Exact ``zero_test(|O1 O2|^2 - r1^2 - r2^2)`` (Casey III.22).
   * - Radical Axis & Radical Centre
     - **Missing** (``False``)
     - :func:`~geometor.casey.invariants.radical_axis_line` / :func:`~geometor.casey.coaxial.construct_radical_axis_and_coaxial_pencil`
     - Linear difference $C_1(x, y) - C_2(x, y) = 0$ + compass construction for disjoint circles (Casey III.21, 23–24).
   * - Poncelet Limiting Points $L_1, L_2$
     - **Missing** (``False``)
     - :func:`~geometor.casey.coaxial.construct_radical_axis_and_coaxial_pencil`
     - Real zero-radius members $D \pm |DT_1|\,\hat{u}$ of non-intersecting coaxal pencil (Casey III.23, VI.V).
   * - Circular Inversion $P \mapsto P'$
     - **Missing** (``False``)
     - :func:`~geometor.casey.invariants.invert_point`
     - Exact conformal map $O + \frac{r^2}{|OP|^2}(P - O)$ (Casey VI.IV.1–9).
   * - Pole, Polar & La Hire Reciprocity
     - **Missing** (``False``)
     - :func:`~geometor.casey.invariants.polar_line`, :func:`~geometor.casey.invariants.pole_of_line`
     - Bilinear polarization $(x_0 - h)(x - h) + (y_0 - k)(y - k) = r^2$ + pure-straightedge quadrangle construction (Casey III.25, VI.VII).
   * - Direct & Transverse Bitangent Quadrance
     - **Missing** (``False``)
     - :func:`~geometor.casey.invariants.bitangent_quadrance`, :func:`~geometor.casey.invariants.bitangent_length`
     - Exact $|O_1 O_2|^2 - (r_1 \mp r_2)^2$ powering Casey's Generalized Ptolemy Theorem (Casey VI.IV.9–10).
