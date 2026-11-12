geometor.casey.concordance
==========================

.. py:module:: geometor.casey.concordance

.. autoapi-nested-parse::

   Cross-repository concordance and SymPy capability audit for Casey's *Sequel to Euclid*.

   Provides structured access to ``resources/sequel_to_euclid/concordance.json`` mapping Casey's
   propositions across ``euclid``, ``elements``, ``altshiller-court``, ``etc``, and ``pappus``,
   alongside an empirical audit of ``sympy.geometry.Circle`` capability gaps filled by
   :mod:`geometor.casey`.



Classes
-------

.. autoapisummary::

   geometor.casey.concordance.ConcordanceEntry
   geometor.casey.concordance.SympyCircleGap


Functions
---------

.. autoapisummary::

   geometor.casey.concordance.get_resources_dir
   geometor.casey.concordance.load_apparatus_registry
   geometor.casey.concordance.load_concordance
   geometor.casey.concordance.audit_sympy_circle_gaps


Module Contents
---------------

.. py:class:: ConcordanceEntry

   Single proposition/topic concordance mapping across the GEOMETOR canon.


   .. py:attribute:: id
      :type:  str


   .. py:attribute:: unit
      :type:  str


   .. py:attribute:: casey_locus
      :type:  str


   .. py:attribute:: folio
      :type:  str


   .. py:attribute:: page
      :type:  str


   .. py:attribute:: title
      :type:  str


   .. py:attribute:: euclid_refs
      :type:  tuple[str, ...]


   .. py:attribute:: altshiller_court_refs
      :type:  tuple[str, ...]


   .. py:attribute:: etc_centers
      :type:  tuple[str, ...]


   .. py:attribute:: pappus_refs
      :type:  tuple[str, ...]


   .. py:attribute:: casey_symbol
      :type:  str


.. py:class:: SympyCircleGap

   Audit record comparing ``sympy.geometry.Circle`` against :mod:`geometor.casey`.


   .. py:attribute:: capability
      :type:  str


   .. py:attribute:: sympy_method_present
      :type:  bool


   .. py:attribute:: casey_locus
      :type:  str


   .. py:attribute:: geometor_casey_api
      :type:  str


.. py:function:: get_resources_dir() -> pathlib.Path

   Return the path to ``resources/sequel_to_euclid/`` inside the repository.


.. py:function:: load_apparatus_registry(name: str) -> dict[str, Any]

   Load a JSON apparatus file (``persons``, ``citations``, ``glossary``, ``sources_manifest``).

   :param name: Filename stem without ``.json`` extension.

   :returns: Parsed JSON dictionary.


.. py:function:: load_concordance() -> list[ConcordanceEntry]

   Load all cross-repository concordance entries from ``concordance.json``.

   :returns: List of :class:`ConcordanceEntry` records in codex order.


.. py:function:: audit_sympy_circle_gaps() -> list[SympyCircleGap]

   Inspect :class:`sympy.geometry.Circle` for modern-circle-geometry primitives in Casey.

   :returns: List of :class:`SympyCircleGap` entries documenting native presence vs.
             :mod:`geometor.casey` exact symbolic implementations.


