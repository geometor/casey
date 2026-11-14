"""Exact symbolic geometry constructions and Digital Scriptorium apparatus for John Casey's *Sequel*.

Models the landmark theorems and straightedge-and-compass constructions of **John Casey's**
*A Sequel to the First Six Books of the Elements of Euclid, Containing an Easy Introduction
to Modern Geometry* (5th ed. 1888 / 6th ed. 1892):

- **Euler Line & Nine-Points Circle** (:func:`construct_euler_nine_point`)
- **Radical Axis, Coaxal Circles & Poncelet Limiting Points**
  (:func:`construct_radical_axis_and_coaxial_pencil`, :func:`verify_coaxial_fundamental_theorem`)
- **Complete Quadrilateral Harmonic Division** (:func:`construct_complete_quadrilateral_harmonic`)
- **Casey's Generalized Ptolemy Theorem & Feuerbach's Theorem**
  (:func:`prove_casey_theorem_symbolic`, :func:`prove_casey_feuerbach_heronian`,
  :func:`construct_casey_feuerbach`)
- **Poles, Polars, Harmonic Secants & La Hire's Reciprocity**
  (:func:`construct_pole_and_polar`, :func:`verify_lahire_reciprocity_symbolic`)
- **Symmedians, Lemoine Circles, Brocard Points, Brocard Circle, Steiner & Tarry Points**
  (:func:`construct_symmedian_and_lemoine_circles`, :func:`construct_brocard_and_lemoine_circles`)
"""

from __future__ import annotations

from geometor.casey.brocard import (
    BrocardLemoineReport,
    BrocardLemoineResult,
    LemoineCirclesResult,
    construct_brocard_and_lemoine_circles,
    construct_symmedian_and_lemoine_circles,
    verify_brocard_identities_symbolic,
)
from geometor.casey.coaxial import (
    CoaxialPencilResult,
    CoaxialTheoremReport,
    construct_radical_axis_and_coaxial_pencil,
    verify_coaxial_fundamental_theorem,
)
from geometor.casey.concordance import (
    ConcordanceEntry,
    SympyCircleGap,
    audit_sympy_circle_gaps,
    get_resources_dir,
    load_apparatus_registry,
    load_concordance,
)
from geometor.casey.feuerbach import (
    CaseyFeuerbachHeronianReport,
    CaseyFeuerbachResult,
    CaseySymbolicProof,
    EulerNinePointResult,
    compass_internal_angle_bisector,
    construct_casey_feuerbach,
    construct_euler_nine_point,
    prove_casey_feuerbach_heronian,
    prove_casey_theorem_symbolic,
)
from geometor.casey.invariants import (
    HERONIAN_VERTICES,
    are_orthogonal_circles,
    barycentric_point,
    bitangent_length,
    bitangent_quadrance,
    circle_power,
    compass_midpoint,
    compass_parallel_line,
    compass_perp_bisector,
    compass_perpendicular_line,
    cross_ratio,
    invert_point,
    is_harmonic,
    line_spread,
    polar_line,
    pole_of_line,
    quadrance,
    radical_axis_line,
    signed_triangle_area,
)
from geometor.casey.poles_polars import (
    CompleteQuadrilateralResult,
    LaHireSymbolicProof,
    PolePolarResult,
    construct_complete_quadrilateral_harmonic,
    construct_pole_and_polar,
    verify_lahire_reciprocity_symbolic,
)
from geometor.casey.render import EMBEDDED_SVG_STYLE, export_svg, render_svg_string

__version__ = "0.1.1"

__all__ = [
    "__version__",
    "EMBEDDED_SVG_STYLE",
    "HERONIAN_VERTICES",
    "BrocardLemoineReport",
    "BrocardLemoineResult",
    "CaseyFeuerbachHeronianReport",
    "CaseyFeuerbachResult",
    "CaseySymbolicProof",
    "CoaxialPencilResult",
    "CoaxialTheoremReport",
    "CompleteQuadrilateralResult",
    "ConcordanceEntry",
    "EulerNinePointResult",
    "LaHireSymbolicProof",
    "LemoineCirclesResult",
    "PolePolarResult",
    "SympyCircleGap",
    "are_orthogonal_circles",
    "audit_sympy_circle_gaps",
    "barycentric_point",
    "bitangent_length",
    "bitangent_quadrance",
    "circle_power",
    "compass_internal_angle_bisector",
    "compass_midpoint",
    "compass_parallel_line",
    "compass_perp_bisector",
    "compass_perpendicular_line",
    "construct_brocard_and_lemoine_circles",
    "construct_casey_feuerbach",
    "construct_complete_quadrilateral_harmonic",
    "construct_euler_nine_point",
    "construct_pole_and_polar",
    "construct_radical_axis_and_coaxial_pencil",
    "construct_symmedian_and_lemoine_circles",
    "cross_ratio",
    "export_svg",
    "get_resources_dir",
    "invert_point",
    "is_harmonic",
    "line_spread",
    "load_apparatus_registry",
    "load_concordance",
    "polar_line",
    "pole_of_line",
    "prove_casey_feuerbach_heronian",
    "prove_casey_theorem_symbolic",
    "quadrance",
    "radical_axis_line",
    "render_svg_string",
    "signed_triangle_area",
    "verify_brocard_identities_symbolic",
    "verify_coaxial_fundamental_theorem",
    "verify_lahire_reciprocity_symbolic",
]
