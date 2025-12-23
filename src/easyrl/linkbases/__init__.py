"""
XBRL Linkbase Parsers

Parsers for the various XBRL linkbase types:
- Label linkbase: Human-readable labels and documentation
- Presentation linkbase: Hierarchical display structure
- Calculation linkbase: Mathematical relationships
- Definition linkbase: Dimensional relationships
"""

from .label import parse_label_linkbase, parse_all_labels

__all__ = [
    'parse_label_linkbase',
    'parse_all_labels',
]