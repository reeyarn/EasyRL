"""
EasyRL - Easy (non-XML) approach to process XBRL

A lightweight, memory-efficient Python library for extracting
specific information from XBRL filings and taxonomies.
"""

__version__ = "0.1.0"

# Core: Namespaces and streaming
from .core.namespaces import (
    Namespaces,
    Roles,
    ArcRoles,
    qname,
    NS_LINK,
    NS_XLINK,
    NS_XBRLI,
)
from .core.streaming import stream_xml

# Linkbase parsers
from .linkbases import parse_label_linkbase, parse_all_labels

# Utilities
from .utils import extract_concept_from_href

__all__ = [
    '__version__',
    # Core
    'Namespaces',
    'Roles',
    'ArcRoles',
    'qname',
    'NS_LINK',
    'NS_XLINK',
    'NS_XBRLI',
    'stream_xml',
    # Linkbases
    'parse_label_linkbase',
    'parse_all_labels',
    # Utils
    'extract_concept_from_href',
]