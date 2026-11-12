# GEOMETOR • casey (`geometor-casey`)

Digital Scriptorium **3-Track Book Codex** and **100% Exact Symbolic `geometor.model` Engine** for **John Casey's** *A Sequel to the First Six Books of the Elements of Euclid, Containing an Easy Introduction to Modern Geometry, with Numerous Examples* (5th ed. 1888 / 6th ed. ed. Patrick A. E. Dowling 1892 — cited as `casey:sequel:1892` in `geometor/altshiller-court`).

## Architectural Mandates

1. **100% Exact Symbolic Precision**:
   - Every coordinate, circle power, radical axis, inversion image, pole/polar, bitangent length, Feuerbach contact point, and Lemoine–Brocard–Steiner–Tarry center is an exact SymPy `Integer`, `Rational`, or closed-form radical.
   - **Never** inject `float` or `sp.Float` into `geometor.model.Model`; always instantiate `Model(..., auto_intersect=False)` with explicit `model.intersect(...)`.
2. **Strict Content / Code Separation**:
   - `docsrc/sequel_to_euclid/` (`:layout: book`) contains **zero** embedded Python scripts; all executable SymPy constructions live in `src/geometor/casey/`, `demos/`, `docsrc/demos/index.rst`, and `tests/`.
3. **Multimodal Scan Vision Protocol**:
   - Archival folios (`PDF Folio = Printed Page + 26` in the 1888 5th-edition witness, `resources/sequel_to_euclid/sources_manifest.json`) are verified directly via 300-DPI page PNG inspection (`view_file`), never via OCR text extraction.

## Repository Layout

- `src/geometor/casey/`:
  - `invariants.py`: Circle power, orthogonality, bitangent quadrances, inversion, poles/polars, radical axis, barycentric helpers, and `@proposition` compass subconstructions.
  - `feuerbach.py`: Symbolic proof of Casey's Generalized Ptolemy Theorem + Heronian `(15, 13, 14)` Euler/Nine-Points and Feuerbach $X(11) = (6, 8)$ constructions.
  - `coaxial.py`: Disjoint-circle radical axis, Casey's Prop. 24 difference-of-powers identity, and Poncelet limiting points $L_1, L_2 = (\mp 8, 0)$.
  - `poles_polars.py`: Complete Quadrilateral harmonic ranges, inscribed-quadrangle polar construction, Self-Conjugate Triangle, and La Hire's Reciprocity.
  - `brocard.py`: Symmedian point $K = X(6)$, First Lemoine & Cosine Circles, Brocard points $\Omega, \Omega'$, 7-point Brocard Circle, Steiner $X(99)$, Tarry $X(98)$, and Longchamps $X(20)$.
  - `render.py`: Theme-adaptive `.euclid-graphic` SVG exporter with collision-avoiding labels and exact LaTeX coordinate metadata.
  - `concordance.py`: Cross-repo concordance loader (`euclid`, `elements`, `altshiller-court`, `etc`, `pappus`) + `sympy.geometry.Circle` capability audit.
- `demos/`: 4 standalone Rich + SVG demonstration scripts.
- `resources/sequel_to_euclid/`: `sources_manifest.json`, `persons.json`, `citations.json`, `glossary.json`, `concordance.json` (`pdfs/` git-ignored).
- `docsrc/`: Sphinx source for the 6-unit 3-Track Book Codex (`sequel_to_euclid/`), `demos/`, `modules/`, `mission/`, `about/`, and `log/`.
- `tests/test_casey.py`: Full symbolic proof, DAG purity, SVG DOM, and concordance test suite.

## Development & Verification Commands

```bash
/home/phi/PROJECTS/geometor/.venv/bin/python -m pytest -v
/home/phi/.local/bin/ruff check src demos tests
/home/phi/.local/bin/publish build
```
