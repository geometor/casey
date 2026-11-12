geometor.casey.render
=====================

.. py:module:: geometor.casey.render

.. autoapi-nested-parse::

   Publication-grade interactive ``.euclid-graphic`` SVG renderer for Casey's *Sequel*.

   Generates theme-adaptive SVGs directly from :class:`~geometor.model.Model` instances while
   preserving exact SymPy coordinates in ``<title>`` tooltips, ``data-latex-x``/``data-latex-y``,
   ``data-ref``, and ``data-aliases`` attributes consumed by PHOTON Publish's
   ``geometor_interactive.js`` and ``.. picture::`` directive.



Attributes
----------

.. autoapisummary::

   geometor.casey.render.EMBEDDED_SVG_STYLE


Functions
---------

.. autoapisummary::

   geometor.casey.render.render_svg_string
   geometor.casey.render.export_svg


Module Contents
---------------

.. py:data:: EMBEDDED_SVG_STYLE
   :type:  str
   :value: ''


.. py:function:: render_svg_string(model: geometor.model.Model, *, graphic_id: str = 'g1', title: str = 'Casey Euclidean Circle Construction', width: int = 680, height: int = 480, margin: float = 42.0, bbox: tuple[float, float, float, float] | None = None, focus_points: collections.abc.Sequence[sympy.geometry.Point] | None = None, include_guides: bool = False, show_labels: bool = True, label_overrides: dict[str, tuple[str, str]] | None = None, highlight_point_ids: collections.abc.Sequence[str] | None = None) -> str

   Render a :class:`~geometor.model.Model` into a complete ``.euclid-graphic`` SVG string.

   :param model: Populated :class:`~geometor.model.Model`.
   :param graphic_id: ``data-graphic-id`` identifier for ``geometor_interactive.js``.
   :param title: Accessible SVG title string.
   :param width: Pixel width of the SVG ``viewBox``.
   :param height: Pixel height of the SVG ``viewBox``.
   :param margin: Outer pixel margin around the framed viewport.
   :param bbox: Optional explicit math viewport ``(xmin, xmax, ymin, ymax)``.
   :param focus_points: Optional subset of points used to compute auto-framing bounds.
   :param include_guides: If ``True``, also render elements marked ``guide=True``.
   :param show_labels: Master toggle for point text labels.
   :param label_overrides: Optional mapping ``pt_id -> (base, subscript)``.
   :param highlight_point_ids: Optional point IDs to emphasize with an outer halo ring.

   :returns: UTF-8 XML/SVG string.


.. py:function:: export_svg(model: geometor.model.Model, output_path: str | pathlib.Path, *, graphic_id: str = 'g1', title: str = 'Casey Euclidean Circle Construction', width: int = 680, height: int = 480, margin: float = 42.0, bbox: tuple[float, float, float, float] | None = None, focus_points: collections.abc.Sequence[sympy.geometry.Point] | None = None, include_guides: bool = False, show_labels: bool = True, label_overrides: dict[str, tuple[str, str]] | None = None, highlight_point_ids: collections.abc.Sequence[str] | None = None) -> pathlib.Path

   Write an interactive ``.euclid-graphic`` SVG rendering of ``model`` to ``output_path``.

   :param model: Populated :class:`~geometor.model.Model`.
   :param output_path: Destination ``.svg`` file path.
   :param graphic_id: ``data-graphic-id`` identifier for ``geometor_interactive.js``.
   :param title: Accessible SVG title string.
   :param width: Pixel width of the SVG ``viewBox``.
   :param height: Pixel height of the SVG ``viewBox``.
   :param margin: Outer pixel margin around the framed viewport.
   :param bbox: Optional explicit math viewport ``(xmin, xmax, ymin, ymax)``.
   :param focus_points: Optional subset of points used to compute auto-framing bounds.
   :param include_guides: If ``True``, also render elements marked ``guide=True``.
   :param show_labels: Master toggle for point text labels.
   :param label_overrides: Optional mapping ``pt_id -> (base, subscript)``.
   :param highlight_point_ids: Optional point IDs to emphasize with an outer halo ring.

   :returns: Resolved :class:`pathlib.Path` of the written SVG file.


