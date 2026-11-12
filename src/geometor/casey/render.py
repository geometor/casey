"""Publication-grade interactive ``.euclid-graphic`` SVG renderer for Casey's *Sequel*.

Generates theme-adaptive SVGs directly from :class:`~geometor.model.Model` instances while
preserving exact SymPy coordinates in ``<title>`` tooltips, ``data-latex-x``/``data-latex-y``,
``data-ref``, and ``data-aliases`` attributes consumed by PHOTON Publish's
``geometor_interactive.js`` and ``.. picture::`` directive.
"""

from __future__ import annotations

import html
import math
import re
from collections.abc import Sequence
from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

__all__ = [
    "EMBEDDED_SVG_STYLE",
    "export_svg",
    "render_svg_string",
]

EMBEDDED_SVG_STYLE: str = """
  .euclid-graphic {
    --svg-bg: #fafaf9;
    --ink: #1c1917;
    --label-halo: rgba(250, 250, 249, 0.92);
    --carrier: #475569;
    --circle-base: #0369a1;
    --circle-featured: #b45309;
    --circle-secondary: #0f766e;
    --circle-orth: #7c3aed;
    --circle-aux: #64748b;
    --highlight-line: #d97706;
    --polar-line: #059669;
    --symmedian-line: #db2777;
    --tri-fill: #0284c7;
    --brocard-fill: #7c3aed;
    --pt-given: #0f172a;
    --pt-center: #0369a1;
    --pt-highlight: #d97706;
    --pt-brocard: #7c3aed;
    --pt-harmonic: #059669;
    font-family: "Inter", "Fira Sans", "Segoe UI", system-ui, sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    .euclid-graphic {
      --svg-bg: #141417;
      --ink: #f4f4f5;
      --label-halo: rgba(20, 20, 23, 0.92);
      --carrier: #94a3b8;
      --circle-base: #38bdf8;
      --circle-featured: #fbbf24;
      --circle-secondary: #2dd4bf;
      --circle-orth: #c084fc;
      --circle-aux: #94a3b8;
      --highlight-line: #fbbf24;
      --polar-line: #34d399;
      --symmedian-line: #f472b6;
      --tri-fill: #38bdf8;
      --brocard-fill: #c084fc;
      --pt-given: #e2e8f0;
      --pt-center: #38bdf8;
      --pt-highlight: #fbbf24;
      --pt-brocard: #c084fc;
      --pt-harmonic: #34d399;
    }
  }
  .euclid-graphic .svg-bg { fill: #fafaf9; fill: var(--svg-bg); }
  .euclid-graphic .geom-circle { fill: none; stroke: #0369a1; stroke: var(--circle-base); stroke-width: 1.95; opacity: 0.9; }
  .euclid-graphic .geom-circle.featured-circle { stroke: #b45309; stroke: var(--circle-featured); stroke-width: 2.55; opacity: 0.96; }
  .euclid-graphic .geom-circle.secondary-circle { stroke: #0f766e; stroke: var(--circle-secondary); stroke-width: 1.9; stroke-dasharray: 6 3.5; }
  .euclid-graphic .geom-circle.orth-circle { stroke: #7c3aed; stroke: var(--circle-orth); stroke-width: 2.15; stroke-dasharray: 7 3.5; }
  .euclid-graphic .geom-circle.aux-circle { stroke: #64748b; stroke: var(--circle-aux); stroke-width: 1.35; stroke-dasharray: 4 3; opacity: 0.72; }
  .euclid-graphic .geom-line { fill: none; stroke: #475569; stroke: var(--carrier); stroke-width: 1.5; stroke-linecap: round; }
  .euclid-graphic .carrier-line { stroke: #475569; stroke: var(--carrier); stroke-width: 2.0; opacity: 0.92; }
  .euclid-graphic .cross-line { stroke: #475569; stroke: var(--carrier); stroke-width: 1.25; stroke-opacity: 0.62; stroke-dasharray: 4 3; }
  .euclid-graphic .highlight-line { stroke: #d97706; stroke: var(--highlight-line); stroke-width: 2.5; }
  .euclid-graphic .polar-line { stroke: #059669; stroke: var(--polar-line); stroke-width: 2.4; }
  .euclid-graphic .symmedian-line { stroke: #db2777; stroke: var(--symmedian-line); stroke-width: 1.85; stroke-opacity: 0.86; }
  .euclid-graphic .brocard-ray { stroke: #7c3aed; stroke: var(--circle-orth); stroke-width: 1.45; stroke-opacity: 0.72; }
  .euclid-graphic .geom-polygon.primary-poly { fill: #0284c7; fill: var(--tri-fill); fill-opacity: 0.06; stroke: #475569; stroke: var(--carrier); stroke-width: 2.0; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.brocard-poly { fill: #7c3aed; fill: var(--brocard-fill); fill-opacity: 0.09; stroke: #7c3aed; stroke: var(--circle-orth); stroke-width: 1.85; stroke-linejoin: round; }
  .euclid-graphic .geom-point { fill: #0f172a; fill: var(--pt-given); stroke: #fafaf9; stroke: var(--svg-bg); stroke-width: 1.5; }
  .euclid-graphic .center-point { fill: #0369a1; fill: var(--pt-center); }
  .euclid-graphic .highlight-point { fill: #d97706; fill: var(--pt-highlight); stroke-width: 1.9; }
  .euclid-graphic .brocard-point { fill: #7c3aed; fill: var(--pt-brocard); stroke-width: 1.9; }
  .euclid-graphic .harmonic-point { fill: #059669; fill: var(--pt-harmonic); stroke-width: 1.8; }
  .euclid-graphic .geom-label {
    fill: #1c1917;
    fill: var(--ink);
    font-size: 13px;
    font-weight: 650;
    paint-order: stroke fill;
    stroke: #fafaf9;
    stroke: var(--label-halo);
    stroke-width: 3.5px;
    stroke-linejoin: round;
    user-select: none;
  }
  .euclid-graphic .geom-label-sub { font-size: 9.8px; font-weight: 650; }
""".strip()

DEFAULT_LABEL_OVERRIDES: dict[str, tuple[str, str]] = {
    "Ma": ("M", "a"),
    "Mb": ("M", "b"),
    "Mc": ("M", "c"),
    "Da": ("D", "a"),
    "Db": ("D", "b"),
    "Dc": ("D", "c"),
    "Ea": ("E", "a"),
    "Eb": ("E", "b"),
    "Ec": ("E", "c"),
    "Ta": ("T", "a"),
    "Tb": ("T", "b"),
    "Tc": ("T", "c"),
    "Ts": ("T", "s"),
    "Fe": ("F", "e"),
    "Rc": ("R", "c"),
    "Om1": ("Ω", ""),
    "Om2": ("Ω′", ""),
    "Ml": ("M", "L"),
    "St": ("S", "t"),
    "Tr": ("T", "r"),
    "Qa": ("Q", "a"),
    "Qb": ("Q", "b"),
}


def _fmt(val: float) -> str:
    """Format a pixel coordinate compactly to 2 decimal places."""
    if abs(val - round(val)) < 1e-5:
        return str(int(round(val)))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def _clip_line_to_rect(
    line: spg.Line,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
) -> tuple[tuple[float, float], tuple[float, float]] | None:
    """Clip an algebraic line ``a*x + b*y + c = 0`` to a math bounding rectangle."""
    a_f = float(line.coefficients[0].evalf())
    b_f = float(line.coefficients[1].evalf())
    c_f = float(line.coefficients[2].evalf())
    eps = 1e-11
    hits: list[tuple[float, float]] = []

    if abs(b_f) > eps:
        for x_edge in (xmin, xmax):
            y_val = -(a_f * x_edge + c_f) / b_f
            if ymin - 1e-7 <= y_val <= ymax + 1e-7:
                hits.append((x_edge, min(max(y_val, ymin), ymax)))

    if abs(a_f) > eps:
        for y_edge in (ymin, ymax):
            x_val = -(b_f * y_edge + c_f) / a_f
            if xmin - 1e-7 <= x_val <= xmax + 1e-7:
                hits.append((min(max(x_val, xmin), xmax), y_edge))

    unique_hits: list[tuple[float, float]] = []
    for hx, hy in hits:
        if not any(math.hypot(hx - ux, hy - uy) < 1e-5 for ux, uy in unique_hits):
            unique_hits.append((hx, hy))

    if len(unique_hits) < 2:
        return None
    best_pair = (unique_hits[0], unique_hits[1])
    best_dist = -1.0
    for i in range(len(unique_hits)):
        for j in range(i + 1, len(unique_hits)):
            d = math.hypot(unique_hits[j][0] - unique_hits[i][0], unique_hits[j][1] - unique_hits[i][1])
            if d > best_dist:
                best_dist = d
                best_pair = (unique_hits[i], unique_hits[j])
    return best_pair


def _split_point_label(
    pt_id: str,
    overrides: dict[str, tuple[str, str]] | None = None,
) -> tuple[str, str]:
    """Split a point identifier into ``(base, subscript)`` for ``<tspan>`` rendering."""
    if overrides and pt_id in overrides:
        return overrides[pt_id]
    if pt_id in DEFAULT_LABEL_OVERRIDES:
        return DEFAULT_LABEL_OVERRIDES[pt_id]
    m = re.match(r"^([A-Za-z]+)(\d+)$", pt_id)
    if m:
        return (m.group(1), m.group(2))
    return (pt_id, "")


def _circle_css_classes(classes: set[str]) -> str:
    """Map model circle classes to semantic SVG CSS classes."""
    out = ["geom-circle"]
    if "featured" in classes:
        out.append("featured-circle")
    elif "orthogonal_circle" in classes:
        out.append("orth-circle")
    elif "secondary" in classes or "secondary_circle" in classes:
        out.append("secondary-circle")
    elif "auxiliary_circle" in classes:
        out.append("aux-circle")
    return " ".join(out)


def _line_css_classes(classes: set[str]) -> str:
    """Map model line classes to semantic SVG CSS classes."""
    out = ["geom-line"]
    if "carrier" in classes:
        out.append("carrier-line")
    if "highlight" in classes:
        out.append("highlight-line")
    elif "polar_line" in classes or "harmonic" in classes:
        out.append("polar-line")
    elif "symmedian" in classes:
        out.append("symmedian-line")
    elif "brocard_ray" in classes:
        out.append("brocard-ray")
    elif (
        "cross" in classes
        or "altitude" in classes
        or "radical_chord" in classes
        or "diagonal" in classes
        or "inversion_line" in classes
    ):
        out.append("cross-line")
    return " ".join(out)


def _polygon_css_classes(classes: set[str]) -> str:
    """Map model polygon classes to semantic SVG CSS classes."""
    if "brocard_triangle" in classes or "diamond" in classes:
        return "geom-polygon brocard-poly"
    return "geom-polygon primary-poly"


def _point_css_and_radius(classes: set[str]) -> tuple[str, float]:
    """Map model point classes to ``(css_class_string, pixel_radius)``."""
    out = ["geom-point"]
    radius = 3.9
    if "highlight_point" in classes or "feuerbach" in classes:
        out.append("highlight-point")
        radius = 5.5
    elif "brocard_point" in classes or "steiner_point" in classes or "tarry_point" in classes:
        out.append("brocard-point")
        radius = 5.0
    elif "harmonic" in classes or "pole" in classes or "conjugate" in classes:
        out.append("harmonic-point")
        radius = 4.6
    elif "center" in classes:
        out.append("center-point")
        radius = 4.3
    elif "given" in classes or "vertex" in classes:
        radius = 4.4
    return (" ".join(out), radius)


def _point_to_segment_dist(
    px: float,
    py: float,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
) -> float:
    """Compute pixel distance from ``(px, py)`` to segment ``(x1, y1)-(x2, y2)``."""
    dx = x2 - x1
    dy = y2 - y1
    len_sq = dx * dx + dy * dy
    if len_sq < 1e-9:
        return math.hypot(px - x1, py - y1)
    t = max(0.0, min(1.0, ((px - x1) * dx + (py - y1) * dy) / len_sq))
    return math.hypot(px - (x1 + t * dx), py - (y1 + t * dy))


def render_svg_string(
    model: Model,
    *,
    graphic_id: str = "g1",
    title: str = "Casey Euclidean Circle Construction",
    width: int = 680,
    height: int = 480,
    margin: float = 42.0,
    bbox: tuple[float, float, float, float] | None = None,
    focus_points: Sequence[spg.Point] | None = None,
    include_guides: bool = False,
    show_labels: bool = True,
    label_overrides: dict[str, tuple[str, str]] | None = None,
    highlight_point_ids: Sequence[str] | None = None,
) -> str:
    """Render a :class:`~geometor.model.Model` into a complete ``.euclid-graphic`` SVG string.

    Args:
        model: Populated :class:`~geometor.model.Model`.
        graphic_id: ``data-graphic-id`` identifier for ``geometor_interactive.js``.
        title: Accessible SVG title string.
        width: Pixel width of the SVG ``viewBox``.
        height: Pixel height of the SVG ``viewBox``.
        margin: Outer pixel margin around the framed viewport.
        bbox: Optional explicit math viewport ``(xmin, xmax, ymin, ymax)``.
        focus_points: Optional subset of points used to compute auto-framing bounds.
        include_guides: If ``True``, also render elements marked ``guide=True``.
        show_labels: Master toggle for point text labels.
        label_overrides: Optional mapping ``pt_id -> (base, subscript)``.
        highlight_point_ids: Optional point IDs to emphasize with an outer halo ring.

    Returns:
        UTF-8 XML/SVG string.
    """
    visible_points = [pt for pt in model.points if include_guides or not model[pt].guide]
    visible_lines = [ln for ln in model.lines if include_guides or not model[ln].guide]
    visible_polygons = [
        poly
        for poly in model
        if isinstance(poly, spg.Polygon) and (include_guides or not model[poly].guide)
    ]
    visible_circles = [
        circ
        for circ in model.circles
        if include_guides or not model[circ].guide
    ]

    frame_pts = list(focus_points) if focus_points else visible_points
    if bbox is not None:
        xmin_m, xmax_m, ymin_m, ymax_m = bbox
    elif frame_pts or visible_circles:
        xs = [float(p.x.evalf()) for p in frame_pts]
        ys = [float(p.y.evalf()) for p in frame_pts]
        if focus_points is None:
            for circ in visible_circles:
                ccx = float(circ.center.x.evalf())
                ccy = float(circ.center.y.evalf())
                cr = float(circ.radius.evalf())
                xs.extend((ccx - cr, ccx + cr))
                ys.extend((ccy - cr, ccy + cr))
        xmin_m, xmax_m = min(xs), max(xs)
        ymin_m, ymax_m = min(ys), max(ys)
        span_x = max(xmax_m - xmin_m, 1.0)
        span_y = max(ymax_m - ymin_m, 1.0)
        xmin_m -= 0.10 * span_x
        xmax_m += 0.10 * span_x
        ymin_m -= 0.10 * span_y
        ymax_m += 0.10 * span_y
    else:
        xmin_m, xmax_m, ymin_m, ymax_m = -2.0, 16.0, -2.0, 14.0

    span_x = max(xmax_m - xmin_m, 1e-6)
    span_y = max(ymax_m - ymin_m, 1e-6)
    avail_w = max(width - 2.0 * margin, 100.0)
    avail_h = max(height - 2.0 * margin, 100.0)
    scale = min(avail_w / span_x, avail_h / span_y)

    cx_m = 0.5 * (xmin_m + xmax_m)
    cy_m = 0.5 * (ymin_m + ymax_m)
    cx_s = 0.5 * width
    cy_s = 0.5 * height

    def to_svg(mx: float, my: float) -> tuple[float, float]:
        return (cx_s + (mx - cx_m) * scale, cy_s - (my - cy_m) * scale)

    inset_px = 14.0
    clip_xmin = cx_m - (cx_s - inset_px) / scale
    clip_xmax = cx_m + (width - inset_px - cx_s) / scale
    clip_ymin = cy_m - (height - inset_px - cy_s) / scale
    clip_ymax = cy_m + (cy_s - inset_px) / scale

    pt_svg_coords: dict[spg.Point, tuple[float, float]] = {
        pt: to_svg(float(pt.x.evalf()), float(pt.y.evalf())) for pt in visible_points
    }

    # Circles
    circle_elems: list[str] = []
    drawn_circles_px: list[tuple[float, float, float]] = []
    for circ in visible_circles:
        el = model[circ]
        primary_c_ref = el.ID
        ccx_s, ccy_s = to_svg(float(circ.center.x.evalf()), float(circ.center.y.evalf()))
        r_px = float(circ.radius.evalf()) * scale
        drawn_circles_px.append((ccx_s, ccy_s, r_px))

        on_curve_ids = [
            model[pt].ID
            for pt in visible_points
            if model[pt].ID and circ.contains(pt)
        ]
        c_aliases: list[str] = []
        if circ.center in model and model[circ.center].ID:
            cid = model[circ.center].ID
            c_aliases.append(f"( {cid} )")
            for pid in on_curve_ids:
                cand2 = f"( {cid} {pid} )"
                if cand2 != primary_c_ref:
                    c_aliases.append(cand2)
        if len(on_curve_ids) >= 3:
            cand3 = f"( {on_curve_ids[0]} {on_curve_ids[1]} {on_curve_ids[2]} )"
            if cand3 != primary_c_ref:
                c_aliases.append(cand3)
        c_alias_attr = f' data-aliases="{html.escape(" | ".join(c_aliases))}"' if c_aliases else ""
        c_ref_attr = f' data-ref="{html.escape(primary_c_ref)}"' if primary_c_ref else ""
        css_cls = _circle_css_classes(set(el.classes.keys()))
        eq_c_str = str(circ.equation())
        circle_elems.append(
            f'      <circle class="{css_cls}" cx="{_fmt(ccx_s)}" cy="{_fmt(ccy_s)}" r="{_fmt(r_px)}"'
            f'{c_ref_attr}{c_alias_attr} fill="none">'
            f"<title>{html.escape(primary_c_ref)}: {html.escape(eq_c_str)} = 0</title></circle>"
        )

    # Polygons
    polygon_elems: list[str] = []
    for poly in visible_polygons:
        el = model[poly]
        pts_attr = " ".join(
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[0])},"
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[1])}"
            for v in poly.vertices
        )
        vert_ids = [model[v].ID for v in poly.vertices if v in model and model[v].ID]
        poly_ref = f"< {' '.join(vert_ids)} >" if vert_ids else el.ID
        css_cls = _polygon_css_classes(set(el.classes.keys()))
        polygon_elems.append(
            f'      <polygon class="{css_cls}" points="{pts_attr}" '
            f'data-ref="{html.escape(poly_ref)}" />'
        )

    # Lines
    line_elems: list[str] = []
    drawn_segments_px: list[tuple[float, float, float, float]] = []
    for ln in visible_lines:
        clipped = _clip_line_to_rect(ln, clip_xmin, clip_xmax, clip_ymin, clip_ymax)
        if clipped is None:
            continue
        (mx1, my1), (mx2, my2) = clipped
        sx1, sy1 = to_svg(mx1, my1)
        sx2, sy2 = to_svg(mx2, my2)
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        drawn_segments_px.append((sx1, sy1, sx2, sy2))

        el = model[ln]
        css_cls = _line_css_classes(set(el.classes.keys()))
        incident_ids = [
            model[pt].ID
            for pt in visible_points
            if model[pt].ID
            and _point_to_segment_dist(pt_svg_coords[pt][0], pt_svg_coords[pt][1], sx1, sy1, sx2, sy2) < 0.85
            and ln.contains(pt)
        ]
        primary_ref = el.ID or (
            f"[ {incident_ids[0]} {incident_ids[-1]} ]" if len(incident_ids) >= 2 else ""
        )
        aliases: list[str] = []
        for i in range(len(incident_ids)):
            for j in range(i + 1, len(incident_ids)):
                cand_line = f"[ {incident_ids[i]} {incident_ids[j]} ]"
                cand_seg = f"/ {incident_ids[i]} {incident_ids[j]} /"
                for cand in (cand_line, cand_seg):
                    if cand != primary_ref:
                        aliases.append(cand)
        alias_attr = f' data-aliases="{html.escape(" | ".join(aliases))}"' if aliases else ""
        ref_attr = f' data-ref="{html.escape(primary_ref)}"' if primary_ref else ""
        eq_str = str(ln.equation())
        line_elems.append(
            f'      <path class="{css_cls}" '
            f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}"'
            f'{ref_attr}{alias_attr} fill="none">'
            f"<title>{html.escape(primary_ref)}: {html.escape(eq_str)} = 0</title></path>"
        )

    # Points & collision-avoiding labels
    highlight_ids = set(highlight_point_ids or ())
    point_elems: list[str] = []
    label_elems: list[str] = []
    placed_label_boxes: list[tuple[float, float, float, float]] = []
    all_pt_px = list(pt_svg_coords.values())

    candidate_angles = [
        -0.5 * math.pi,
        0.5 * math.pi,
        -0.28 * math.pi,
        -0.72 * math.pi,
        0.28 * math.pi,
        0.72 * math.pi,
        0.0,
        math.pi,
        -0.14 * math.pi,
        -0.86 * math.pi,
        0.14 * math.pi,
        0.86 * math.pi,
    ]

    for pt in visible_points:
        sx, sy = pt_svg_coords[pt]
        if sx < -8 or sx > width + 8 or sy < -8 or sy > height + 8:
            continue
        el = model[pt]
        pid = el.ID
        css_cls, radius = _point_css_and_radius(set(el.classes.keys()))
        x_latex = sp.latex(pt.x)
        y_latex = sp.latex(pt.y)
        tooltip = f"{pid} = ({pt.x}, {pt.y})"

        if pid in highlight_ids or "highlight_point" in el.classes:
            point_elems.append(
                f'      <circle class="geom-point-halo" cx="{_fmt(sx)}" cy="{_fmt(sy)}" '
                f'r="{_fmt(radius + 4.0)}" fill="none" stroke="currentColor" stroke-opacity="0.38" stroke-width="1.6" />'
            )

        ref_attr = f' data-ref="{html.escape(pid)}"' if pid else ""
        point_elems.append(
            f'      <circle class="{css_cls}" cx="{_fmt(sx)}" cy="{_fmt(sy)}" r="{_fmt(radius)}"'
            f'{ref_attr} data-latex-x="{html.escape(x_latex)}" data-latex-y="{html.escape(y_latex)}">'
            f"<title>{html.escape(tooltip)}</title></circle>"
        )

        if not show_labels or not pid:
            continue

        base_txt, sub_txt = _split_point_label(pid, label_overrides)
        est_w = 8.8 * len(base_txt) + 6.0 * len(sub_txt) + 4.0
        est_h = 13.5
        dist_r = radius + 11.5

        best_pos = (sx + 6.0, sy - 9.0)
        best_box = (sx, sy - est_h, sx + est_w, sy)
        best_score = -1e12
        for ang in candidate_angles:
            cand_cx = sx + math.cos(ang) * (dist_r + 0.35 * est_w)
            cand_cy = sy + math.sin(ang) * (dist_r + 0.25 * est_h)
            box = (
                cand_cx - 0.5 * est_w,
                cand_cy - 0.5 * est_h,
                cand_cx + 0.5 * est_w,
                cand_cy + 0.5 * est_h,
            )
            score = 0.0
            if box[0] < 6 or box[2] > width - 6 or box[1] < 6 or box[3] > height - 6:
                score -= 500.0
            for lx1, ly1, lx2, ly2 in drawn_segments_px:
                d_line = _point_to_segment_dist(cand_cx, cand_cy, lx1, ly1, lx2, ly2)
                if d_line < 11.5:
                    score -= (11.5 - d_line) * 15.0
            for ccx_p, ccy_p, cr_p in drawn_circles_px:
                d_circ = abs(math.hypot(cand_cx - ccx_p, cand_cy - ccy_p) - cr_p)
                if d_circ < 10.0:
                    score -= (10.0 - d_circ) * 12.0
            for opx, opy in all_pt_px:
                d_pt = math.hypot(cand_cx - opx, cand_cy - opy)
                if d_pt < 15.0:
                    score -= (15.0 - d_pt) * 20.0
            for bx1, by1, bx2, by2 in placed_label_boxes:
                ox = max(0.0, min(box[2], bx2) - max(box[0], bx1))
                oy = max(0.0, min(box[3], by2) - max(box[1], by1))
                if ox > 0 and oy > 0:
                    score -= ox * oy * 6.5
            if score > best_score:
                best_score = score
                best_pos = (cand_cx - 0.45 * est_w, cand_cy + 0.34 * est_h)
                best_box = box

        placed_label_boxes.append(best_box)
        lx, ly = best_pos
        if sub_txt:
            inner_txt = (
                f"{html.escape(base_txt)}"
                f'<tspan class="geom-label-sub" dy="3">{html.escape(sub_txt)}</tspan>'
            )
        else:
            inner_txt = html.escape(base_txt)
        label_elems.append(
            f'      <text class="geom-label" x="{_fmt(lx)}" y="{_fmt(ly)}"{ref_attr}>{inner_txt}</text>'
        )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
        f'viewBox="0 0 {width} {height}" data-graphic-id="{html.escape(graphic_id)}" '
        f'role="img" aria-label="{html.escape(title)}">',
        f"  <title>{html.escape(title)}</title>",
        "  <style>",
        EMBEDDED_SVG_STYLE,
        "  </style>",
        f'  <rect class="svg-bg" x="0" y="0" width="{width}" height="{height}" rx="6" />',
        '  <g id="elements">',
        '    <g id="graphics">',
        *polygon_elems,
        *circle_elems,
        *line_elems,
        "    </g>",
        '    <g id="highlights"></g>',
        '    <g id="points">',
        *point_elems,
        "    </g>",
        '    <g id="labels">',
        *label_elems,
        "    </g>",
        "  </g>",
        "</svg>",
        "",
    ]
    return "\n".join(parts)


def export_svg(
    model: Model,
    output_path: str | Path,
    *,
    graphic_id: str = "g1",
    title: str = "Casey Euclidean Circle Construction",
    width: int = 680,
    height: int = 480,
    margin: float = 42.0,
    bbox: tuple[float, float, float, float] | None = None,
    focus_points: Sequence[spg.Point] | None = None,
    include_guides: bool = False,
    show_labels: bool = True,
    label_overrides: dict[str, tuple[str, str]] | None = None,
    highlight_point_ids: Sequence[str] | None = None,
) -> Path:
    """Write an interactive ``.euclid-graphic`` SVG rendering of ``model`` to ``output_path``.

    Args:
        model: Populated :class:`~geometor.model.Model`.
        output_path: Destination ``.svg`` file path.
        graphic_id: ``data-graphic-id`` identifier for ``geometor_interactive.js``.
        title: Accessible SVG title string.
        width: Pixel width of the SVG ``viewBox``.
        height: Pixel height of the SVG ``viewBox``.
        margin: Outer pixel margin around the framed viewport.
        bbox: Optional explicit math viewport ``(xmin, xmax, ymin, ymax)``.
        focus_points: Optional subset of points used to compute auto-framing bounds.
        include_guides: If ``True``, also render elements marked ``guide=True``.
        show_labels: Master toggle for point text labels.
        label_overrides: Optional mapping ``pt_id -> (base, subscript)``.
        highlight_point_ids: Optional point IDs to emphasize with an outer halo ring.

    Returns:
        Resolved :class:`pathlib.Path` of the written SVG file.
    """
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    svg_text = render_svg_string(
        model,
        graphic_id=graphic_id,
        title=title,
        width=width,
        height=height,
        margin=margin,
        bbox=bbox,
        focus_points=focus_points,
        include_guides=include_guides,
        show_labels=show_labels,
        label_overrides=label_overrides,
        highlight_point_ids=highlight_point_ids,
    )
    target.write_text(svg_text, encoding="utf-8")
    return target.resolve()
