:order: 25
:nav_title: Demos
:title: Demos

.. _casey-demos:

Constructive Demonstrations
===========================

.. rubric:: Exact Symbolic ``geometor.model`` Constructions & Algebraic Proofs for Casey's *Sequel*

In accordance with GEOMETOR's strict separation of historical text and executable code, all Python constructions and SymPy symbolic proofs reside in ``src/geometor/casey/`` and ``demos/``. Every coordinate below is an exact SymPy ``Integer``, ``Rational``, or closed-form radical over the canonical Heronian reference triangle $\triangle ABC$ with sides $(a, b, c) = (15, 13, 14)$ and vertices $A = (0, 0), B = (14, 0), C = (5, 12)$ (or integer projective lattices)—**zero ``float`` or ``sp.Float`` approximations** enter any :class:`~geometor.model.Model`.

.. contents:: Demonstration Suites
   :local:
   :depth: 2
   :backlinks: none

----

.. _demo-casey-feuerbach:

1. Casey's Generalized Ptolemy Theorem & Feuerbach's Nine-Point Tangency
------------------------------------------------------------------------

Executes ``demos/casey_feuerbach.py`` (:mod:`geometor.casey.feuerbach`), proving Casey's bitangent relation symbolically and constructing both the **Euler Line & Nine-Points Circle** (Unit 1, Book IV Prop. 5) and **Casey's Orthogonal Inversion Proof of Feuerbach's Theorem** at $F_e = X(11) = (6, 8)$ (Unit 4, Book VI Sec. IV Props. 9–10 & Cor. 2):

* **Exact Centres & Radii on $(15, 13, 14)$**: $\Delta = 84$, $r = 4$, $R = \frac{65}{8}$, $R_9 = \frac{65}{16}$, $O = \left(7, \frac{33}{8}\right)$, $G = \left(\frac{19}{3}, 4\right)$, $N = \left(6, \frac{63}{16}\right)$, $H = \left(5, \frac{15}{4}\right)$, $I = (6, 4)$.
* **Exact Feuerbach Tangency**: $|NI| = \frac{1}{16} = \frac{65}{16} - 4 = R_9 - r$, touching internally at $F_e = X(11) = (6, 8)$, and touching the three excircles externally at $\left(\frac{2709}{289}, \frac{1792}{289}\right)$, $\left(\frac{553}{233}, \frac{1344}{233}\right)$, and $\left(\frac{1672}{257}, -\frac{24}{257}\right)$.
* **Casey's 1861 Inversion Circle**: Circle $(M_a, T_a)$ centered at $M_a = \left(\frac{19}{2}, 6\right)$ of radius $\frac{1}{2} = \frac{|b - c|}{2}$ cuts both the incircle $(I, 4)$ and $A$-excircle $(I_a, 14)$ orthogonally and inverts $T_s = \left(\frac{614}{65}, \frac{392}{65}\right)$ on the fourth common tangent directly onto $F_e = (6, 8)$.

.. picture:: /_static/figures/unit1_euler_nine_point.svg

.. picture:: /_static/figures/unit4_casey_feuerbach.svg

.. literalinclude:: ../../demos/casey_feuerbach.py
   :language: python
   :caption: demos/casey_feuerbach.py

----

.. _demo-coaxial-pencil:

2. Radical Axis, Radical Centre & Coaxal Pencil with Poncelet Limiting Points
-----------------------------------------------------------------------------

Executes ``demos/coaxial_pencil_and_limiting_points.py`` (:mod:`geometor.casey.coaxial`), constructing the radical axis of two non-intersecting circles via an auxiliary secant circle (Casey Book III, Prop. 21, p. 43), verifying Casey's Fundamental Difference-of-Powers Theorem (Prop. 24), and constructing **Poncelet's Limiting Points** $L_1 = (-8, 0), L_2 = (8, 0)$ and the orthogonal circle centered at the Radical Centre $R_c = (0, -6)$ (Book VI, Sec. V, Props. 1–6):

.. picture:: /_static/figures/unit2_coaxial_limiting_points.svg

.. literalinclude:: ../../demos/coaxial_pencil_and_limiting_points.py
   :language: python
   :caption: demos/coaxial_pencil_and_limiting_points.py

----

.. _demo-poles-polars:

3. Complete Quadrilateral Harmonic Ranges, Poles & Polars, and La Hire Reciprocity
----------------------------------------------------------------------------------

Executes ``demos/poles_polars_lahire.py`` (:mod:`geometor.casey.poles_polars`), demonstrating pure-straightedge projective harmonic division on the Complete Quadrilateral (Book VI, Sec. III, Prop. 7, p. 91) and inscribed-quadrangle polar construction, Self-Conjugate Triangle $\triangle DUV$, harmonic secant division $(G_i, H_i; J_i, D) = -1$, and **La Hire's Reciprocity** $Q \in \operatorname{polar}(D) \iff D \in \operatorname{polar}(Q)$ (Book III, Props. 25, 27 & Book VI, Sec. VII):

.. picture:: /_static/figures/unit3_complete_quadrilateral_harmonic.svg

.. picture:: /_static/figures/unit4_poles_polars_lahire.svg

.. literalinclude:: ../../demos/poles_polars_lahire.py
   :language: python
   :caption: demos/poles_polars_lahire.py

----

.. _demo-brocard-lemoine:

4. Symmedian Point, Lemoine Circles, Brocard Circle & Associated Triangle Points
--------------------------------------------------------------------------------

Executes ``demos/brocard_and_lemoine_circles.py`` (:mod:`geometor.casey.brocard`), constructing on $\triangle ABC$ $(15, 13, 14)$:

* **Lemoine's Symmedian Point** $K = X(6) = \left(\frac{1673}{295}, \frac{1176}{295}\right)$ minimizing $\sum d_i^2 = \frac{14112}{295}$, **First Lemoine Circle** (6 concyclic parallel intercepts, chords proportional to $(a^3 : b^3 : c^3)$), and **Cosine (Second Lemoine) Circle** (6 concyclic antiparallel intercepts of diameter $2 R \tan\omega$).
* **Brocard Angle** $\cot\omega = \cot A + \cot B + \cot C = \frac{a^2+b^2+c^2}{4\Delta} = \frac{295}{168}$ ($\sin^2\omega = \frac{28224}{115249}$), **First & Second Brocard Points** $\Omega = \left(\frac{697970}{115249}, \frac{397488}{115249}\right)$ and $\Omega' = \left(\frac{684236}{115249}, \frac{529200}{115249}\right)$, **Brocard's First Triangle** $\triangle A_1 B_1 C_1$, and the **7-Point Brocard Circle** on diameter $OK$ centered at $M_L = X(182) = \left(\frac{1869}{295}, \frac{19143}{4720}\right)$.
* **Associated Points**: **Steiner Point** $S_t = X(99) = \left(\frac{17253}{2353}, -\frac{9396}{2353}\right)$, **Tarry Point** $T_r = X(98) = \left(\frac{15689}{2353}, \frac{115233}{9412}\right)$, and **de Longchamps Point** $X(20) = \left(9, \frac{9}{2}\right)$.

.. picture:: /_static/figures/unit5_symmedian_lemoine_circle.svg

.. picture:: /_static/figures/unit6_brocard_circle.svg

.. literalinclude:: ../../demos/brocard_and_lemoine_circles.py
   :language: python
   :caption: demos/brocard_and_lemoine_circles.py
