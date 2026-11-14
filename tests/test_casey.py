"""Comprehensive exact symbolic, DAG purity, SVG DOM, and apparatus tests for ``geometor.casey``."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
for _extra in (_REPO_ROOT / "src", _REPO_ROOT.parent / "model" / "src"):
    if _extra.is_dir() and str(_extra) not in sys.path:
        sys.path.insert(0, str(_extra))

import sympy as sp  # noqa: E402
import sympy.geometry as spg  # noqa: E402
from geometor.model import Model, quadrance, zero_test  # noqa: E402

import geometor.casey as casey  # noqa: E402
from geometor.casey.__main__ import main as cli_main  # noqa: E402
from geometor.casey.brocard import (  # noqa: E402
    construct_brocard_and_lemoine_circles,
    construct_symmedian_and_lemoine_circles,
    verify_brocard_identities_symbolic,
)
from geometor.casey.coaxial import construct_radical_axis_and_coaxial_pencil  # noqa: E402
from geometor.casey.concordance import (  # noqa: E402
    audit_sympy_circle_gaps,
    load_apparatus_registry,
    load_concordance,
)
from geometor.casey.feuerbach import (  # noqa: E402
    construct_casey_feuerbach,
    construct_euler_nine_point,
    prove_casey_feuerbach_heronian,
    prove_casey_theorem_symbolic,
)
from geometor.casey.invariants import (  # noqa: E402
    HERONIAN_VERTICES,
    are_orthogonal_circles,
    barycentric_point,
    bitangent_length,
    bitangent_quadrance,
    circle_power,
    invert_point,
    polar_line,
    pole_of_line,
    radical_axis_line,
    signed_triangle_area,
)
from geometor.casey.poles_polars import (  # noqa: E402
    construct_complete_quadrilateral_harmonic,
    construct_pole_and_polar,
    verify_lahire_reciprocity_symbolic,
)
from geometor.casey.render import export_svg, render_svg_string  # noqa: E402


def _assert_model_exact(model: Model) -> None:
    """Assert zero Python float or SymPy Float contamination across an entire Model."""
    assert not model.auto_intersect
    assert len(model.points) > 0
    for el in model:
        assert not any(isinstance(atom, sp.Float) for atom in el.atoms()), f"Float atom in {el}"
        if isinstance(el, spg.Point2D):
            assert not isinstance(el.x, float)
            assert not isinstance(el.y, float)


def test_package_version_and_invariants() -> None:
    """Verify exact circle power, orthogonality, bitangents, inversion, poles/polars, and barycentrics."""
    assert casey.__version__ == "0.1.3"
    a_pt, b_pt, c_pt = HERONIAN_VERTICES
    assert signed_triangle_area(a_pt, b_pt, c_pt) == sp.Integer(84)

    c1 = spg.Circle(spg.Point(0, 0), 5)
    c2 = spg.Circle(spg.Point(13, 0), 12)
    assert circle_power(spg.Point(13, 0), c1) == sp.Integer(144)
    assert are_orthogonal_circles(c1, c2)
    assert bitangent_quadrance(c1, c2, internal=False) == sp.Integer(120)
    assert bitangent_length(spg.Circle(spg.Point(0, 0), 4), spg.Circle(spg.Point(10, 0), 10)) == sp.Integer(8)

    p = spg.Point(10, 5)
    p_inv = invert_point(p, c1.center, c1.radius**2)
    assert p_inv == spg.Point(2, 1)
    assert invert_point(p_inv, c1.center, c1.radius**2) == p

    pol = polar_line(p, c1)
    assert pole_of_line(pol, c1) == p

    rad = radical_axis_line(c1, c2)
    assert rad.contains(spg.Point(sp.Rational(25, 13), 7))

    g_pt = barycentric_point(a_pt, b_pt, c_pt, 1, 1, 1)
    assert g_pt == spg.Point(sp.Rational(19, 3), 4)


def test_casey_generalized_ptolemy_and_feuerbach() -> None:
    """Verify Casey's Generalized Ptolemy Theorem, Euler Nine-Point Circle, and Feuerbach tangency."""
    sym = prove_casey_theorem_symbolic()
    assert sym.verified
    assert sym.inversion_invariance_residual == 0
    assert sym.tangent_line_euler_residual == 0
    assert sym.incircle_casey_residual == 0
    assert sym.incircle_cor2_squares_residual == 0
    assert sym.excircle_a_casey_residual == 0

    heron = prove_casey_feuerbach_heronian()
    assert heron.verified
    assert heron.sides == (sp.Integer(15), sp.Integer(13), sp.Integer(14))
    assert heron.area == sp.Integer(84)
    assert heron.inradius == sp.Integer(4)
    assert heron.circumradius == sp.Rational(65, 8)
    assert heron.nine_point_radius == sp.Rational(65, 16)
    assert heron.casey_signed_sum == 0
    assert heron.ni_distance == sp.Rational(1, 16)
    assert heron.feuerbach_point == spg.Point(6, 8)
    assert heron.excircle_feuerbach_points == (
        spg.Point(sp.Rational(2709, 289), sp.Rational(1792, 289)),
        spg.Point(sp.Rational(553, 233), sp.Rational(1344, 233)),
        spg.Point(sp.Rational(1672, 257), sp.Rational(-24, 257)),
    )
    assert heron.inversion_circle_orthogonal_to_incircle
    assert heron.inversion_circle_orthogonal_to_excircle_a

    u1 = construct_euler_nine_point()
    _assert_model_exact(u1.model)
    assert u1.euler_line.contains(u1.circumcenter)
    assert u1.euler_line.contains(u1.centroid)
    assert u1.euler_line.contains(u1.nine_point_center)
    assert u1.euler_line.contains(u1.orthocenter)
    assert quadrance(u1.orthocenter, u1.centroid) == 4 * quadrance(u1.centroid, u1.circumcenter)
    for pt in (*u1.midpoints, *u1.altitude_feet, *u1.euler_midpoints):
        assert u1.nine_point_circle.contains(pt)

    u4 = construct_casey_feuerbach()
    _assert_model_exact(u4.model)
    assert u4.feuerbach_point == spg.Point(6, 8)
    assert u4.euler_nine_point.nine_point_circle.contains(u4.feuerbach_point)
    assert u4.incircle.contains(u4.feuerbach_point)
    assert are_orthogonal_circles(u4.casey_inversion_circle, u4.incircle)


def test_coaxial_pencil_and_limiting_points() -> None:
    """Verify disjoint-circle radical axis, Casey's Prop. 24 identity, and Poncelet limiting points."""
    res = construct_radical_axis_and_coaxial_pencil()
    _assert_model_exact(res.model)
    assert res.radical_center == spg.Point(0, -6)
    assert res.radical_foot == spg.Point(0, 0)
    assert res.limiting_points == (spg.Point(-8, 0), spg.Point(8, 0))
    assert res.report.verified
    assert res.report.symbolic_prop24_residual == 0
    assert res.report.radical_axis_power_diff == 0
    assert res.report.orthogonal_to_c1
    assert res.report.orthogonal_to_c2
    assert res.report.orthogonal_to_c3


def test_complete_quadrilateral_and_poles_polars() -> None:
    """Verify complete-quadrilateral harmonic ranges, self-conjugate triangle, and La Hire reciprocity."""
    lh = verify_lahire_reciprocity_symbolic()
    assert lh.verified
    assert lh.reciprocity_bilinear_diff == 0
    assert lh.secant_cross_ratio == -1

    quad = construct_complete_quadrilateral_harmonic()
    _assert_model_exact(quad.model)
    assert quad.opposite_meets == (spg.Point(8, 0), spg.Point(sp.Rational(12, 5), sp.Rational(18, 5)))
    assert quad.diagonal_center == spg.Point(sp.Rational(18, 5), sp.Rational(9, 5))
    assert quad.third_diagonal_meets == (
        spg.Point(sp.Rational(9, 2), sp.Rational(9, 4)),
        spg.Point(-6, 9),
    )
    assert quad.cross_ratio_ac == -1
    assert quad.cross_ratio_bd == -1

    pol = construct_pole_and_polar()
    _assert_model_exact(pol.model)
    assert pol.pole_d == spg.Point(sp.Rational(15, 2), sp.Rational(5, 4))
    assert pol.self_conjugate_triangle == (
        spg.Point(sp.Rational(15, 2), sp.Rational(5, 4)),
        spg.Point(3, 2),
        spg.Point(sp.Rational(5, 3), 10),
    )
    assert pol.cross_ratio_secant_1 == -1
    assert pol.cross_ratio_secant_2 == -1
    assert pol.lahire_verified


def test_symmedian_lemoine_and_brocard_geometry() -> None:
    """Verify symmedians, First Lemoine & Cosine circles, 7-point Brocard circle, Steiner, and Tarry."""
    sym = verify_brocard_identities_symbolic()
    assert zero_test(sym["cot_omega_residual"])
    assert zero_test(sym["lagrange_symmedian_residual"])

    u5 = construct_symmedian_and_lemoine_circles()
    _assert_model_exact(u5.model)
    assert u5.symmedian_point == spg.Point(sp.Rational(1673, 295), sp.Rational(1176, 295))
    assert u5.lemoine_center == spg.Point(sp.Rational(1869, 295), sp.Rational(19143, 4720))
    for pt in u5.lemoine_hexagon:
        assert u5.first_lemoine_circle.contains(pt)
    for pt in u5.cosine_hexagon:
        assert u5.cosine_circle.contains(pt)

    u6 = construct_brocard_and_lemoine_circles()
    _assert_model_exact(u6.model)
    assert u6.report.verified
    assert u6.report.cot_omega == sp.Rational(295, 168)
    assert u6.report.sin_sq_omega == sp.Rational(28224, 115249)
    assert u6.report.lemoine_intercept_ratios == (
        sp.Rational(3375, 2197),
        sp.Rational(3375, 2744),
    )
    assert u6.report.min_perp_squares_sum == sp.Rational(14112, 295)
    assert u6.brocard_1 == spg.Point(sp.Rational(697970, 115249), sp.Rational(397488, 115249))
    assert u6.brocard_2 == spg.Point(sp.Rational(684236, 115249), sp.Rational(529200, 115249))
    for pt in (
        u6.circumcenter,
        u6.symmedian_point,
        u6.brocard_1,
        u6.brocard_2,
        *u6.brocard_first_triangle,
    ):
        assert u6.brocard_circle.contains(pt)
    assert u6.steiner_point == spg.Point(sp.Rational(17253, 2353), sp.Rational(-9396, 2353))
    assert u6.tarry_point == spg.Point(sp.Rational(15689, 2353), sp.Rational(115233, 9412))
    assert spg.Point.midpoint(u6.steiner_point, u6.tarry_point) == u6.circumcenter
    assert u6.longchamps_point == spg.Point(9, sp.Rational(9, 2))


def test_svg_renderer_and_apparatus_concordance(tmp_path: Path) -> None:
    """Verify .euclid-graphic SVG DOM integrity, cross-repo concordance, and apparatus anchors."""
    u1 = construct_euler_nine_point()
    svg_str = render_svg_string(u1.model, graphic_id="0083.g1", title="Test Nine-Point SVG")
    root = ET.fromstring(svg_str)
    assert "euclid-graphic" in root.attrib.get("class", "")
    assert root.attrib.get("data-graphic-id") == "0083.g1"

    out_file = export_svg(u1.model, tmp_path / "test.svg", graphic_id="0083.g1")
    assert out_file.is_file()

    entries = load_concordance()
    assert len(entries) >= 15
    assert {e.unit for e in entries} == {f"unit-{i}" for i in range(1, 7)}

    gaps = audit_sympy_circle_gaps()
    assert len(gaps) == 8
    assert all(g.sympy_method_present is False for g in gaps)

    # Verify JSON <-> RST apparatus anchor parity
    doc_dir = _REPO_ROOT / "docsrc" / "sequel_to_euclid"
    for kind, rst_name, prefix in (
        ("citations", "bibliography.rst", "cite"),
        ("persons", "persons.rst", "person"),
        ("glossary", "glossary.rst", "term"),
    ):
        reg = load_apparatus_registry(kind)
        assert len(reg) >= 20
        rst_text = (doc_dir / rst_name).read_text(encoding="utf-8")
        for key in reg:
            slug = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")
            assert f".. _{prefix}-{slug}:" in rst_text

    # Verify zero embedded Python code blocks inside historical codex .rst files
    for rst_path in doc_dir.rglob("*.rst"):
        txt = rst_path.read_text(encoding="utf-8")
        assert ".. code-block:: python" not in txt
        assert "literalinclude::" not in txt

    assert cli_main(["summary"]) == 0
    assert cli_main(["concordance"]) == 0
