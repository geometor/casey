=========
Changelog
=========

0.1.5 (2026-11-15)
------------------

- Rebuilt codex documentation with ``photon-platform/publish`` ``v0.4.6`` so every inline ``.euclid-graphic`` SVG carries explicit ``viewBox`` pixel dimensions, per-diagram scoped ``<style>`` rules, and Nocturnal Codex dark/light theme parity.

0.1.4 (2026-11-15)
------------------

- Ensure canonical GEOMETOR ``logo.png`` and ``favicon.ico`` brand assets are provisioned in ``docsrc/_static/`` and rendered in site headers and browser tabs.

0.1.3 (2026-11-14)
------------------

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.1.2 (2026-11-14)
------------------

- **changed**: Standardized Book Title Page, top-level Header Navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author/Translator profiles in ``People``, and English structural terminology.

0.1.1 (2026-11-13)
------------------

- Resolve 100% of marginal ``.. folio::`` scan links (49 directives) to raw GitHub PNG page scans via ``publish folio-links``.

0.1.0 (2026-11-12)
------------------

- Established ``geometor-casey`` Digital Scriptorium **3-Track Book Codex** (``docsrc/sequel_to_euclid/``) across 6 thematic units covering John Casey's *A Sequel to the First Six Books of the Elements of Euclid* (5th ed. 1888 / 6th ed. ed. Patrick A. E. Dowling 1892).
- Verified 38 archival folios via 300-DPI multimodal scan vision (`PDF Folio = Printed Page + 26`) and authored full prosopographical (33 persons), bibliographic (22 citations), technical glossary (30 terms), and cross-repository concordance apparatus (`euclid`, `elements`, `altshiller-court`, `etc`, `pappus`), including a capability gap audit of ``sympy.geometry.Circle``.
- Implemented exact symbolic Euclidean circle & triangle modeling package ``geometor.casey`` (`invariants`, `feuerbach`, `coaxial`, `poles_polars`, `brocard`, `render`, `concordance`, `__main__`) with zero floating-point coordinates inside ``geometor.model.Model``.
- Added 4 runnable symbolic demonstration suites in ``demos/`` and 7 calibrated interactive ``.euclid-graphic`` SVGs.
