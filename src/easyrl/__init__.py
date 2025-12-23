"""
EasyRL - Easy (non-XML) approach to process XBRL

A lightweight, memory-efficient Python library for extracting
specific information from XBRL filings and taxonomies.
"""

from .core.namespaces import (
    Namespaces,
    Roles,
    ArcRoles,
    NS_LINK,
    NS_XLINK,
    NS_XBRLI,
)

from .linkbases.label import LabelLinkbaseParser
#from .instance.facts import FactExtractor

# Re-export commonly used items for convenience
from .core.namespaces import (
    Namespaces,
    Roles,
    ArcRoles,
    NS_LINK,
    NS_XLINK,
    NS_XBRLI,
)

__version__ = "0.1.0"
__all__ = [
    "LabelLinkbaseParser", "FactExtractor"
    "Namespaces", "Roles", "ArcRoles", "NS_LINK", "NS_XLINK", "NS_XBRLI"
    ]