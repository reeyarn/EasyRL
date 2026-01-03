# linkbases Contents
## linkbases/__init__.py
```py
"""
XBRL Linkbase Parsers

Parsers for the various XBRL linkbase types:
- Label linkbase: Human-readable labels and documentation
- Reference linkbase: Links to authoritative literature
- Definition linkbase: Hierarchical/dimensional relationships
- Presentation linkbase: Display hierarchy
- Calculation linkbase: Mathematical summation relationships
"""

# Shared hierarchy structures
from .hierarchy import (
    ConceptNode,
    ConceptTree,
    get_hierarchy_dataframe,
)

# Individual linkbase parsers
from .label import parse_label_linkbase, parse_all_labels
from .reference import (
    Reference,
    parse_reference_linkbase,
    parse_reference_linkbase_flat,
)
from .definition import parse_definition_linkbase
from .presentation import parse_presentation_linkbase
from .calculation import (
    CalculationRelationship,
    CalculationNode,
    CalculationTree,
    parse_calculation_linkbase,
    get_calculation_dataframe,
)

__all__ = [
    # Shared hierarchy structures
    'ConceptNode',
    'ConceptTree',
    'get_hierarchy_dataframe',
    # Label
    'parse_label_linkbase',
    'parse_all_labels',
    # Reference
    'Reference',
    'parse_reference_linkbase',
    'parse_reference_linkbase_flat',
    # Definition
    'parse_definition_linkbase',
    # Presentation
    'parse_presentation_linkbase',
    # Calculation
    'CalculationRelationship',
    'CalculationNode',
    'CalculationTree',
    'parse_calculation_linkbase',
    'get_calculation_dataframe',
]
```

## linkbases/calculation.py
```py
"""
Calculation Linkbase Parser

Extract calculation relationships from XBRL calculation linkbases.
Calculation linkbases define summation relationships with weights.
"""

from typing import Dict, List, Set, Any
from dataclasses import dataclass, field
import xml.etree.ElementTree as ET

from ..core.namespaces import qname, ArcRoles
from ..utils import extract_concept_from_href


@dataclass
class CalculationRelationship:
    """
    A single calculation relationship (parent sums children).
    
    Attributes:
        parent: The summing concept (e.g., 'us-gaap_OperatingExpenses')
        child: A contributing concept (e.g., 'us-gaap_ResearchAndDevelopmentExpense')
        weight: 1.0 (adds) or -1.0 (subtracts)
        order: Sort order among siblings
    """
    parent: str
    child: str
    weight: float = 1.0
    order: float = 0.0
    
    def __repr__(self) -> str:
        sign = '+' if self.weight >= 0 else '-'
        return f"{self.parent} {sign}= {self.child}"


@dataclass
class CalculationNode:
    """
    A node in the calculation tree.
    
    Attributes:
        concept: The concept name
        parent: Parent concept (the sum)
        weight: Weight in parent's calculation (1.0 or -1.0)
        children: List of (child_concept, weight) tuples
        order: Sort order among siblings
    """
    concept: str
    parent: str | None = None
    weight: float = 1.0
    children: List[tuple[str, float]] = field(default_factory=list)
    order: float = 0.0


@dataclass
class CalculationTree:
    """
    A tree structure representing calculation relationships.
    
    In a calculation tree:
    - Parent = Sum of (children * weights)
    - Weight is typically 1.0 (add) or -1.0 (subtract)
    
    Example:
        NetIncome = Revenues * 1.0 + Expenses * (-1.0)
        OperatingExpenses = R&D * 1.0 + SG&A * 1.0 + D&A * 1.0
    """
    nodes: Dict[str, CalculationNode] = field(default_factory=dict)
    roots: List[str] = field(default_factory=list)
    
    def __contains__(self, concept: str) -> bool:
        """Check if a concept exists in the tree."""
        return concept in self.nodes
    
    def __len__(self) -> int:
        """Return the number of concepts in the tree."""
        return len(self.nodes)
    
    def get(self, concept: str) -> CalculationNode | None:
        """Get the node for a concept, or None if not found."""
        return self.nodes.get(concept)
    
    def get_parent(self, concept: str) -> str | None:
        """Get the parent (sum) that this concept contributes to."""
        if concept in self.nodes:
            return self.nodes[concept].parent
        return None
    
    def get_weight(self, concept: str) -> float | None:
        """Get the weight of this concept in its parent's calculation."""
        if concept in self.nodes:
            return self.nodes[concept].weight
        return None
    
    def get_children(self, concept: str) -> List[tuple[str, float]]:
        """
        Get children (components) of a concept with their weights.
        
        Returns:
            List of (child_concept, weight) tuples, sorted by order.
            Empty list if concept not found or has no children.
        """
        if concept in self.nodes:
            children = self.nodes[concept].children
            # Sort by order
            return sorted(
                children,
                key=lambda c: self.nodes[c[0]].order if c[0] in self.nodes else 0
            )
        return []
    
    def get_components(self, concept: str) -> Dict[str, float] | None:
        """
        Get the calculation components as a dict.
        
        Returns:
            Dict mapping child concepts to weights.
            None if concept not found.
            
        Example:
            >>> tree.get_components('us-gaap_NetIncomeLoss')
            {'us-gaap_Revenues': 1.0, 'us-gaap_OperatingExpenses': -1.0}
        """
        if concept not in self.nodes:
            return None
        
        return {child: weight for child, weight in self.nodes[concept].children}
    
    def get_formula(self, concept: str) -> str | None:
        """
        Get a human-readable formula for a calculation.
        
        Returns:
            String formula like "A = B + C - D"
            None if concept not found or has no children.
        """
        if concept not in self.nodes:
            return None
        
        children = self.get_children(concept)
        if not children:
            return None
        
        parts = []
        for i, (child, weight) in enumerate(children):
            # Simplify concept names
            short_name = child.split('_')[-1] if '_' in child else child
            
            if i == 0:
                if weight < 0:
                    parts.append(f"-{short_name}")
                else:
                    parts.append(short_name)
            else:
                if weight < 0:
                    parts.append(f"- {short_name}")
                else:
                    parts.append(f"+ {short_name}")
        
        parent_short = concept.split('_')[-1] if '_' in concept else concept
        return f"{parent_short} = {' '.join(parts)}"
    
    def validate_calculation(
        self, 
        concept: str, 
        values: Dict[str, float]
    ) -> tuple[bool, float, float] | None:
        """
        Validate a calculation given fact values.
        
        Args:
            concept: The parent (sum) concept
            values: Dict of concept -> numeric value
        
        Returns:
            Tuple of (is_valid, expected_sum, actual_value) or None if can't validate.
            
        Example:
            >>> values = {
            ...     'us-gaap_NetIncomeLoss': 100,
            ...     'us-gaap_Revenues': 500,
            ...     'us-gaap_OperatingExpenses': 400,
            ... }
            >>> tree.validate_calculation('us-gaap_NetIncomeLoss', values)
            (True, 100.0, 100.0)
        """
        if concept not in self.nodes:
            return None
        
        children = self.get_children(concept)
        if not children:
            return None
        
        # Calculate expected sum
        expected = 0.0
        for child, weight in children:
            if child not in values:
                return None  # Can't validate without all values
            expected += values[child] * weight
        
        # Get actual value
        if concept not in values:
            return None
        
        actual = values[concept]
        is_valid = abs(expected - actual) < 0.01  # Allow small rounding diff
        
        return (is_valid, expected, actual)
    
    def print_tree(self, concept: str | None = None, indent: str = "  ") -> str:
        """
        Print the calculation tree with weights.
        
        Args:
            concept: Starting node (None = print all roots)
            indent: Indentation string
        """
        lines = []
        
        def _print_node(c: str, level: int, weight: float = 1.0):
            prefix = indent * level
            sign = '+' if weight >= 0 else '-'
            weight_str = f" ({sign}{abs(weight):.1f})" if level > 0 else ""
            lines.append(f"{prefix}{c}{weight_str}")
            
            for child, w in self.get_children(c):
                _print_node(child, level + 1, w)
        
        if concept:
            if concept in self.nodes:
                _print_node(concept, 0)
            else:
                return f"<concept '{concept}' not found>"
        else:
            for r in self.roots:
                _print_node(r, 0)
        
        return "\n".join(lines)


def parse_calculation_linkbase(xml_file: str) -> CalculationTree:
    """
    Parse a calculation linkbase and build a calculation tree.
    
    Calculation linkbases define summation relationships:
    - Parent concept = Sum of (child * weight)
    - Weight is 1.0 (add) or -1.0 (subtract)
    
    Args:
        xml_file: Path to the calculation linkbase XML file
    
    Returns:
        CalculationTree with the parsed relationships
    
    Examples:
        >>> tree = parse_calculation_linkbase('us-gaap-stm-soi-cal-2020.xml')
        >>> 
        >>> # Get components of a total
        >>> tree.get_components('us-gaap_OperatingCostsAndExpenses')
        {'us-gaap_ResearchAndDevelopmentExpense': 1.0,
         'us-gaap_SellingGeneralAndAdministrativeExpense': 1.0, ...}
        >>> 
        >>> # Get human-readable formula
        >>> tree.get_formula('us-gaap_NetIncomeLoss')
        'NetIncomeLoss = Revenues - CostOfRevenue - OperatingExpenses'
        >>> 
        >>> # Validate a calculation
        >>> values = {'us-gaap_NetIncome': 100, 'us-gaap_Revenue': 500, ...}
        >>> tree.validate_calculation('us-gaap_NetIncome', values)
    """
    # Pre-compute qualified names
    TAG_LOC = qname('link', 'loc')
    TAG_ARC = qname('link', 'calculationArc')
    
    ATTR_LABEL = qname('xlink', 'label')
    ATTR_HREF = qname('xlink', 'href')
    ATTR_ARCROLE = qname('xlink', 'arcrole')
    ATTR_FROM = qname('xlink', 'from')
    ATTR_TO = qname('xlink', 'to')
    
    # Storage
    loc_map: Dict[str, str] = {}  # label_id -> concept_name
    arcs: List[tuple[str, str, float, float]] = []  # (parent, child, weight, order)
    
    context = ET.iterparse(xml_file, events=('end',))
    
    for event, elem in context:
        tag = elem.tag
        
        if tag == TAG_LOC:
            label_id = elem.get(ATTR_LABEL)
            href = elem.get(ATTR_HREF)
            if label_id and href:
                loc_map[label_id] = extract_concept_from_href(href)
        
        elif tag == TAG_ARC:
            arc_role = elem.get(ATTR_ARCROLE)
            if arc_role == ArcRoles.SUMMATION_ITEM:
                from_id = elem.get(ATTR_FROM)
                to_id = elem.get(ATTR_TO)
                
                weight_str = elem.get('weight', '1.0')
                order_str = elem.get('order', '0')
                
                try:
                    weight = float(weight_str)
                except ValueError:
                    weight = 1.0
                
                try:
                    order = float(order_str)
                except ValueError:
                    order = 0.0
                
                if from_id and to_id:
                    arcs.append((from_id, to_id, weight, order))
        
        elem.clear()
    
    # Build the tree
    tree = CalculationTree()
    has_parent: Set[str] = set()
    
    for from_label, to_label, weight, order in arcs:
        if from_label not in loc_map or to_label not in loc_map:
            continue
        
        parent_concept = loc_map[from_label]
        child_concept = loc_map[to_label]
        
        # Ensure parent node exists
        if parent_concept not in tree.nodes:
            tree.nodes[parent_concept] = CalculationNode(concept=parent_concept)
        
        # Ensure child node exists
        if child_concept not in tree.nodes:
            tree.nodes[child_concept] = CalculationNode(concept=child_concept)
        
        # Set relationship
        tree.nodes[child_concept].parent = parent_concept
        tree.nodes[child_concept].weight = weight
        tree.nodes[child_concept].order = order
        
        # Add to parent's children
        child_tuple = (child_concept, weight)
        if child_tuple not in tree.nodes[parent_concept].children:
            tree.nodes[parent_concept].children.append(child_tuple)
        
        has_parent.add(child_concept)
    
    # Find roots (concepts that are sums but not components of anything else)
    for concept in tree.nodes:
        if concept not in has_parent:
            tree.roots.append(concept)
    
    # Sort roots by order
    tree.roots.sort(key=lambda c: tree.nodes[c].order if c in tree.nodes else 0)
    
    return tree


def get_calculation_dataframe(tree: CalculationTree):
    """
    Convert a CalculationTree to a pandas DataFrame.
    
    Returns DataFrame with columns:
    - parent: Parent (sum) concept
    - child: Child (component) concept
    - weight: Weight (1.0 or -1.0)
    - order: Sort order
    
    Example:
        >>> tree = parse_calculation_linkbase('cal.xml')
        >>> df = get_calculation_dataframe(tree)
        >>> df[df['parent'].str.contains('OperatingExpenses')]
    """
    try:
        import pandas as pd
    except ImportError:
        raise ImportError("pandas is required for get_calculation_dataframe()")
    
    rows = []
    for concept, node in tree.nodes.items():
        for child, weight in node.children:
            child_node = tree.nodes.get(child)
            rows.append({
                'parent': concept,
                'child': child,
                'weight': weight,
                'order': child_node.order if child_node else 0,
            })
    
    return pd.DataFrame(rows)
```

## linkbases/definition.py
```py
"""
Definition Linkbase Parser

Extract hierarchical relationships from XBRL definition linkbases.
"""

from typing import Dict, List, Set
import xml.etree.ElementTree as ET

from ..core.namespaces import qname, ArcRoles
from ..utils import extract_concept_from_href
from .hierarchy import ConceptNode, ConceptTree


def parse_definition_linkbase(
    xml_file: str,
    arcrole: str | None = None,
) -> ConceptTree:
    """
    Parse a definition linkbase and build a concept hierarchy tree.
    
    Definition linkbases use arcs like:
    - domain-member: Hierarchical relationships
    - dimension-domain: Dimension to domain
    - hypercube-dimension: Table to dimension
    
    Args:
        xml_file: Path to the definition linkbase XML file
        arcrole: Optional arc role to filter by. If None, uses domain-member.
                Common values:
                - ArcRoles.DOMAIN_MEMBER (default)
                - ArcRoles.DIMENSION_DOMAIN
                - ArcRoles.HYPERCUBE_DIMENSION
    
    Returns:
        ConceptTree with the parsed hierarchy
    
    Examples:
        >>> tree = parse_definition_linkbase('us-gaap-stm-soi-def-2020.xml')
        >>> 
        >>> # Get parent
        >>> tree.get_parent('us-gaap_ResearchAndDevelopmentExpense')
        'us-gaap_ResearchAndDevelopmentExpenseAbstract'
        >>> 
        >>> # Get full ancestor path
        >>> tree.get_ancestors('us-gaap_ResearchAndDevelopmentExpense')
        ['us-gaap_ResearchAndDevelopmentExpenseAbstract', 
         'us-gaap_OperatingCostsAndExpensesAbstract', ...]
        >>> 
        >>> # Print tree
        >>> print(tree.print_tree())
    """
    if arcrole is None:
        arcrole = ArcRoles.DOMAIN_MEMBER
    
    # Pre-compute qualified names
    TAG_LOC = qname('link', 'loc')
    TAG_ARC = qname('link', 'definitionArc')
    
    ATTR_LABEL = qname('xlink', 'label')
    ATTR_HREF = qname('xlink', 'href')
    ATTR_ARCROLE = qname('xlink', 'arcrole')
    ATTR_FROM = qname('xlink', 'from')
    ATTR_TO = qname('xlink', 'to')
    
    # Storage
    loc_map: Dict[str, str] = {}  # label_id -> concept_name
    arcs: List[tuple[str, str, float]] = []  # (parent_label, child_label, order)
    
    context = ET.iterparse(xml_file, events=('end',))
    
    for event, elem in context:
        tag = elem.tag
        
        if tag == TAG_LOC:
            label_id = elem.get(ATTR_LABEL)
            href = elem.get(ATTR_HREF)
            if label_id and href:
                loc_map[label_id] = extract_concept_from_href(href)
        
        elif tag == TAG_ARC:
            arc_role = elem.get(ATTR_ARCROLE)
            if arc_role == arcrole:
                from_id = elem.get(ATTR_FROM)
                to_id = elem.get(ATTR_TO)
                order_str = elem.get('order', '0')
                try:
                    order = float(order_str)
                except ValueError:
                    order = 0.0
                
                if from_id and to_id:
                    arcs.append((from_id, to_id, order))
        
        elem.clear()
    
    # Build the tree
    return _build_tree(loc_map, arcs)


def _build_tree(
    loc_map: Dict[str, str],
    arcs: List[tuple[str, str, float]]
) -> ConceptTree:
    """Build a ConceptTree from locators and arcs."""
    tree = ConceptTree()
    has_parent: Set[str] = set()
    
    for from_label, to_label, order in arcs:
        if from_label not in loc_map or to_label not in loc_map:
            continue
        
        parent_concept = loc_map[from_label]
        child_concept = loc_map[to_label]
        
        # Ensure parent node exists
        if parent_concept not in tree.nodes:
            tree.nodes[parent_concept] = ConceptNode(concept=parent_concept)
        
        # Ensure child node exists
        if child_concept not in tree.nodes:
            tree.nodes[child_concept] = ConceptNode(concept=child_concept)
        
        # Set relationship
        tree.nodes[child_concept].parent = parent_concept
        tree.nodes[child_concept].order = order
        
        if child_concept not in tree.nodes[parent_concept].children:
            tree.nodes[parent_concept].children.append(child_concept)
        
        has_parent.add(child_concept)
    
    # Find roots (nodes without parents)
    for concept in tree.nodes:
        if concept not in has_parent:
            tree.roots.append(concept)
    
    # Sort roots by order if available
    tree.roots.sort(key=lambda c: tree.nodes[c].order if c in tree.nodes else 0)
    
    # Calculate depths
    def _set_depth(concept: str, depth: int):
        if concept in tree.nodes:
            tree.nodes[concept].depth = depth
            for child in tree.nodes[concept].children:
                _set_depth(child, depth + 1)
    
    for root in tree.roots:
        _set_depth(root, 0)
    
    return tree
```

## linkbases/hierarchy.py
```py
"""
Hierarchy Data Structures

Shared data structures for hierarchical linkbases (definition, presentation).
These linkbases define parent-child relationships forming tree structures.
"""

from typing import Dict, List, Any
from dataclasses import dataclass, field


@dataclass
class ConceptNode:
    """
    A node in the concept hierarchy tree.
    
    Attributes:
        concept: The concept name (e.g., 'us-gaap_Assets')
        parent: Parent concept name (None if root)
        children: List of child concept names
        order: Numeric order for sorting siblings
        depth: Depth in the tree (0 = root)
    """
    concept: str
    parent: str | None = None
    children: List[str] = field(default_factory=list)
    order: float = 0.0
    depth: int = 0
    
    def __repr__(self) -> str:
        return f"ConceptNode({self.concept}, children={len(self.children)})"


@dataclass 
class ConceptTree:
    """
    A tree structure representing concept hierarchies.
    
    Provides methods for traversing the tree, finding ancestors,
    descendants, and paths between concepts.
    
    Used by both definition and presentation linkbases.
    """
    nodes: Dict[str, ConceptNode] = field(default_factory=dict)
    roots: List[str] = field(default_factory=list)
    
    def __contains__(self, concept: str) -> bool:
        """Check if a concept exists in the tree."""
        return concept in self.nodes
    
    def __len__(self) -> int:
        """Return the number of concepts in the tree."""
        return len(self.nodes)
    
    def get(self, concept: str) -> ConceptNode | None:
        """Get the node for a concept, or None if not found."""
        return self.nodes.get(concept)
    
    def get_parent(self, concept: str) -> str | None:
        """
        Get the parent of a concept.
        
        Returns None if concept not found or has no parent (is root).
        """
        if concept in self.nodes:
            return self.nodes[concept].parent
        return None
    
    def get_children(self, concept: str) -> List[str]:
        """
        Get children of a concept, sorted by order.
        
        Returns empty list if concept not found or has no children.
        """
        if concept in self.nodes:
            children = self.nodes[concept].children
            # Sort by order
            return sorted(children, key=lambda c: self.nodes[c].order if c in self.nodes else 0)
        return []
    
    def get_ancestors(self, concept: str) -> List[str] | None:
        """
        Get all ancestors from concept to root.
        
        Returns:
            List from immediate parent to root, e.g. ['Parent', 'Grandparent', 'Root']
            None if concept is not in the tree
            Empty list [] if concept is a root (has no ancestors)
        """
        if concept not in self.nodes:
            return None
        
        ancestors = []
        current = concept
        seen = set()  # Prevent infinite loops
        
        while current in self.nodes and current not in seen:
            seen.add(current)
            parent = self.nodes[current].parent
            if parent:
                ancestors.append(parent)
                current = parent
            else:
                break
        
        return ancestors
    
    def get_ancestor_path(self, concept: str) -> List[str] | None:
        """
        Get path from root to concept.
        
        Returns:
            List from root to concept (inclusive), e.g. ['Root', 'Grandparent', 'Parent', 'Concept']
            None if concept is not in the tree
        """
        if concept not in self.nodes:
            return None
        
        ancestors = self.get_ancestors(concept)
        if ancestors is None:
            return None
        
        return list(reversed(ancestors)) + [concept]
    
    def get_descendants(self, concept: str, max_depth: int | None = None) -> List[str] | None:
        """
        Get all descendants of a concept.
        
        Args:
            concept: Starting concept
            max_depth: Maximum depth to traverse (None = unlimited)
        
        Returns:
            List of all descendant concepts (breadth-first order)
            None if concept is not in the tree
            Empty list [] if concept has no descendants
        """
        if concept not in self.nodes:
            return None
        
        descendants = []
        queue = [(c, 1) for c in self.get_children(concept)]
        
        while queue:
            child, depth = queue.pop(0)
            if max_depth is not None and depth > max_depth:
                continue
            descendants.append(child)
            for grandchild in self.get_children(child):
                queue.append((grandchild, depth + 1))
        
        return descendants
    
    def get_siblings(self, concept: str) -> List[str] | None:
        """
        Get siblings of a concept (same parent).
        
        Returns:
            List of sibling concepts (excluding self)
            None if concept is not in the tree
            Empty list [] if concept has no siblings
        """
        if concept not in self.nodes:
            return None
        
        parent = self.get_parent(concept)
        if parent:
            return [c for c in self.get_children(parent) if c != concept]
        return []
    
    def get_depth(self, concept: str) -> int | None:
        """
        Get depth of a concept in the tree.
        
        Returns:
            Depth (0 = root)
            None if concept is not in the tree
        """
        if concept in self.nodes:
            return self.nodes[concept].depth
        return None
    
    def find_common_ancestor(self, concept1: str, concept2: str) -> str | None:
        """
        Find the lowest common ancestor of two concepts.
        
        Returns None if either concept is not in the tree or no common ancestor exists.
        """
        if concept1 not in self.nodes or concept2 not in self.nodes:
            return None
        
        ancestors1 = set(self.get_ancestors(concept1) or [])
        ancestors1.add(concept1)
        
        current = concept2
        while current:
            if current in ancestors1:
                return current
            current = self.get_parent(current)
        
        return None
    
    def print_tree(self, root: str | None = None, indent: str = "  ") -> str:
        """
        Print the tree structure as a string.
        
        Args:
            root: Starting node (None = print all roots)
            indent: Indentation string
        
        Returns:
            String representation of the tree
        """
        lines = []
        
        def _print_node(concept: str, level: int):
            prefix = indent * level
            lines.append(f"{prefix}{concept}")
            for child in self.get_children(concept):
                _print_node(child, level + 1)
        
        if root:
            if root in self.nodes:
                _print_node(root, 0)
            else:
                return f"<concept '{root}' not found>"
        else:
            for r in self.roots:
                _print_node(r, 0)
        
        return "\n".join(lines)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert tree to nested dictionary."""
        def _node_to_dict(concept: str) -> Dict[str, Any]:
            return {
                'concept': concept,
                'children': [_node_to_dict(c) for c in self.get_children(concept)]
            }
        
        return {
            'roots': [_node_to_dict(r) for r in self.roots]
        }


def get_hierarchy_dataframe(tree: ConceptTree):
    """
    Convert a ConceptTree to a pandas DataFrame.
    
    Returns DataFrame with columns:
    - concept: Concept name
    - parent: Parent concept name
    - depth: Depth in tree
    - order: Sort order among siblings
    - path: Full path from root as string
    
    Example:
        >>> tree = parse_definition_linkbase('def.xml')
        >>> df = get_hierarchy_dataframe(tree)
        >>> df[df['concept'].str.contains('Research')]
    """
    try:
        import pandas as pd
    except ImportError:
        raise ImportError("pandas is required for get_hierarchy_dataframe()")
    
    rows = []
    for concept, node in tree.nodes.items():
        path = ' > '.join(tree.get_ancestor_path(concept) or [concept])
        rows.append({
            'concept': concept,
            'parent': node.parent,
            'depth': node.depth,
            'order': node.order,
            'path': path,
        })
    
    return pd.DataFrame(rows)
```

## linkbases/label.py
```py
"""
Label Linkbase Parser

Extract labels and documentation from XBRL label linkbase files.
"""

from typing import Dict
from ..core.namespaces import qname, Roles
from ..core.streaming import stream_xml
from ..utils import extract_concept_from_href


def parse_label_linkbase(
    xml_file: str,
    role: str = Roles.DOCUMENTATION,
) -> Dict[str, str]:
    """
    Extract labels from a label linkbase file.
    
    Parses an XBRL label linkbase and returns a mapping of concept names
    to their label text for the specified role.
    
    Args:
        xml_file: Path to the label linkbase XML file
        role: The label role URI to extract. Defaults to documentation role.
              Common roles:
              - Roles.DOCUMENTATION: Detailed concept descriptions
              - Roles.LABEL: Standard display labels
              - Roles.TERSE_LABEL: Short labels
              - Roles.VERBOSE_LABEL: Extended labels
    
    Returns:
        Dict mapping concept names to label text.
        Example: {'us-gaap_Assets': 'Sum of the carrying amounts...'}
    
    Examples:
        >>> # Get documentation for all concepts
        >>> docs = parse_label_linkbase('us-gaap-doc-2023.xml')
        >>> print(docs.get('us-gaap_Assets'))
        
        >>> # Get display labels instead
        >>> from easyrl.core.namespaces import Roles
        >>> labels = parse_label_linkbase('us-gaap-lab-2023.xml', role=Roles.LABEL)
    """
    # Pre-compute qualified names for speed
    TAG_LOC = qname('link', 'loc')
    TAG_LABEL = qname('link', 'label')
    TAG_ARC = qname('link', 'labelArc')
    
    ATTR_LABEL = qname('xlink', 'label')
    ATTR_HREF = qname('xlink', 'href')
    ATTR_ROLE = qname('xlink', 'role')
    ATTR_FROM = qname('xlink', 'from')
    ATTR_TO = qname('xlink', 'to')
    
    # Storage
    loc_map: Dict[str, str] = {}    # label_id -> concept_name
    label_map: Dict[str, str] = {}  # label_id -> text
    arc_links: list[tuple[str, str]] = []  # (from_id, to_id)
    
    # Tags we care about
    tags = {TAG_LOC, TAG_LABEL, TAG_ARC}
    
    for tag, elem in stream_xml(xml_file, tags_of_interest=tags):
        
        if tag == TAG_LOC:
            label_id = elem.get(ATTR_LABEL)
            href = elem.get(ATTR_HREF)
            if label_id and href:
                loc_map[label_id] = extract_concept_from_href(href)
        
        elif tag == TAG_LABEL:
            elem_role = elem.get(ATTR_ROLE)
            label_id = elem.get(ATTR_LABEL)
            if elem_role == role and label_id:
                label_map[label_id] = elem.text or ''
        
        elif tag == TAG_ARC:
            from_id = elem.get(ATTR_FROM)
            to_id = elem.get(ATTR_TO)
            if from_id and to_id:
                arc_links.append((from_id, to_id))
    
    # Resolution Phase: join locators with labels via arcs
    return {
        loc_map[loc]: label_map[lbl]
        for loc, lbl in arc_links
        if loc in loc_map and lbl in label_map
    }


def parse_all_labels(xml_file: str) -> Dict[str, Dict[str, str]]:
    """
    Extract all label types from a label linkbase.
    
    Unlike parse_label_linkbase which extracts a single role,
    this function extracts all available label roles.
    
    Args:
        xml_file: Path to the label linkbase XML file
    
    Returns:
        Nested dict: {concept_name: {role: text, ...}, ...}
    
    Examples:
        >>> all_labels = parse_all_labels('us-gaap-lab-2023.xml')
        >>> concept = all_labels['us-gaap_Assets']
        >>> print(concept[Roles.LABEL])        # "Assets"
        >>> print(concept[Roles.DOCUMENTATION]) # "Sum of the carrying..."
    """
    TAG_LOC = qname('link', 'loc')
    TAG_LABEL = qname('link', 'label')
    TAG_ARC = qname('link', 'labelArc')
    
    ATTR_LABEL = qname('xlink', 'label')
    ATTR_HREF = qname('xlink', 'href')
    ATTR_ROLE = qname('xlink', 'role')
    ATTR_FROM = qname('xlink', 'from')
    ATTR_TO = qname('xlink', 'to')
    
    loc_map: Dict[str, str] = {}
    label_map: Dict[str, tuple[str, str]] = {}  # label_id -> (role, text)
    arc_links: list[tuple[str, str]] = []
    
    tags = {TAG_LOC, TAG_LABEL, TAG_ARC}
    
    for tag, elem in stream_xml(xml_file, tags_of_interest=tags):
        
        if tag == TAG_LOC:
            label_id = elem.get(ATTR_LABEL)
            href = elem.get(ATTR_HREF)
            if label_id and href:
                loc_map[label_id] = extract_concept_from_href(href)
        
        elif tag == TAG_LABEL:
            role = elem.get(ATTR_ROLE)
            label_id = elem.get(ATTR_LABEL)
            if role and label_id:
                label_map[label_id] = (role, elem.text or '')
        
        elif tag == TAG_ARC:
            from_id = elem.get(ATTR_FROM)
            to_id = elem.get(ATTR_TO)
            if from_id and to_id:
                arc_links.append((from_id, to_id))
    
    # Build nested result
    result: Dict[str, Dict[str, str]] = {}
    
    for loc_id, label_id in arc_links:
        if loc_id in loc_map and label_id in label_map:
            concept = loc_map[loc_id]
            role, text = label_map[label_id]
            
            if concept not in result:
                result[concept] = {}
            result[concept][role] = text
    
    return result
```

## linkbases/presentation.py
```py
"""
Presentation Linkbase Parser

Extract hierarchical display relationships from XBRL presentation linkbases.
"""

from typing import Dict, List, Set
import xml.etree.ElementTree as ET

from ..core.namespaces import qname, ArcRoles
from ..utils import extract_concept_from_href
from .hierarchy import ConceptNode, ConceptTree


def parse_presentation_linkbase(xml_file: str) -> ConceptTree:
    """
    Parse a presentation linkbase and build a concept hierarchy tree.
    
    Presentation linkbases use parent-child arcs to define how
    concepts should be displayed hierarchically in reports.
    
    Args:
        xml_file: Path to the presentation linkbase XML file
    
    Returns:
        ConceptTree with the parsed hierarchy
    
    Examples:
        >>> tree = parse_presentation_linkbase('us-gaap-stm-soi-pre-2020.xml')
        >>> 
        >>> # Get display hierarchy
        >>> tree.get_children('us-gaap_IncomeStatementAbstract')
        >>> 
        >>> # Print tree
        >>> print(tree.print_tree())
    """
    # Pre-compute qualified names
    TAG_LOC = qname('link', 'loc')
    TAG_ARC = qname('link', 'presentationArc')
    
    ATTR_LABEL = qname('xlink', 'label')
    ATTR_HREF = qname('xlink', 'href')
    ATTR_ARCROLE = qname('xlink', 'arcrole')
    ATTR_FROM = qname('xlink', 'from')
    ATTR_TO = qname('xlink', 'to')
    
    # Storage
    loc_map: Dict[str, str] = {}
    arcs: List[tuple[str, str, float]] = []
    
    context = ET.iterparse(xml_file, events=('end',))
    
    for event, elem in context:
        tag = elem.tag
        
        if tag == TAG_LOC:
            label_id = elem.get(ATTR_LABEL)
            href = elem.get(ATTR_HREF)
            if label_id and href:
                loc_map[label_id] = extract_concept_from_href(href)
        
        elif tag == TAG_ARC:
            # Presentation linkbases use parent-child arcrole
            arc_role = elem.get(ATTR_ARCROLE)
            if arc_role == ArcRoles.PARENT_CHILD:
                from_id = elem.get(ATTR_FROM)
                to_id = elem.get(ATTR_TO)
                order_str = elem.get('order', '0')
                try:
                    order = float(order_str)
                except ValueError:
                    order = 0.0
                
                if from_id and to_id:
                    arcs.append((from_id, to_id, order))
        
        elem.clear()
    
    # Build the tree
    return _build_tree(loc_map, arcs)


def _build_tree(
    loc_map: Dict[str, str],
    arcs: List[tuple[str, str, float]]
) -> ConceptTree:
    """Build a ConceptTree from locators and arcs."""
    tree = ConceptTree()
    has_parent: Set[str] = set()
    
    for from_label, to_label, order in arcs:
        if from_label not in loc_map or to_label not in loc_map:
            continue
        
        parent_concept = loc_map[from_label]
        child_concept = loc_map[to_label]
        
        if parent_concept not in tree.nodes:
            tree.nodes[parent_concept] = ConceptNode(concept=parent_concept)
        
        if child_concept not in tree.nodes:
            tree.nodes[child_concept] = ConceptNode(concept=child_concept)
        
        tree.nodes[child_concept].parent = parent_concept
        tree.nodes[child_concept].order = order
        
        if child_concept not in tree.nodes[parent_concept].children:
            tree.nodes[parent_concept].children.append(child_concept)
        
        has_parent.add(child_concept)
    
    for concept in tree.nodes:
        if concept not in has_parent:
            tree.roots.append(concept)
    
    tree.roots.sort(key=lambda c: tree.nodes[c].order if c in tree.nodes else 0)
    
    def _set_depth(concept: str, depth: int):
        if concept in tree.nodes:
            tree.nodes[concept].depth = depth
            for child in tree.nodes[concept].children:
                _set_depth(child, depth + 1)
    
    for root in tree.roots:
        _set_depth(root, 0)
    
    return tree
```

## linkbases/reference.py
```py
"""
Reference Linkbase Parser

Extract references from XBRL reference linkbase files.
References link concepts to authoritative literature (FASB, SEC, IFRS, etc.)
"""

from typing import Dict, List, Any
from dataclasses import dataclass, field
from ..core.namespaces import qname, Roles
from ..core.streaming import stream_xml
from ..utils import extract_concept_from_href


# Reference part namespace
NS_REF = '{http://www.xbrl.org/2006/ref}'


@dataclass
class Reference:
    """
    A single reference to authoritative literature.
    
    Attributes:
        role: The reference role URI (e.g., Roles.REFERENCE)
        parts: Dict of reference parts (Publisher, Name, Topic, Section, etc.)
    """
    role: str
    parts: Dict[str, str] = field(default_factory=dict)
    
    def __repr__(self) -> str:
        publisher = self.parts.get('Publisher', '')
        name = self.parts.get('Name', '')
        topic = self.parts.get('Topic', '')
        section = self.parts.get('Section', '')
        return f"Reference({publisher} {name} Topic {topic} Section {section})"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            'role': self.role,
            **self.parts
        }
    
    def format_citation(self) -> str:
        """
        Format as a human-readable citation string.
        
        Example: "FASB ASC 210-10-S99-1"
        """
        parts = []
        
        # Publisher abbreviation
        publisher = self.parts.get('Publisher', '')
        if publisher:
            parts.append(publisher)
        
        # Name abbreviation
        name = self.parts.get('Name', '')
        if 'Codification' in name:
            parts.append('ASC')
        elif 'Regulation' in name:
            parts.append(name)
        elif name:
            parts.append(name)
        
        # Topic-SubTopic-Section-Paragraph
        topic = self.parts.get('Topic', '')
        subtopic = self.parts.get('SubTopic', '')
        section = self.parts.get('Section', '')
        paragraph = self.parts.get('Paragraph', '')
        
        ref_parts = []
        if topic:
            ref_parts.append(topic)
        if subtopic:
            ref_parts.append(subtopic)
        if section:
            ref_parts.append(section)
        if paragraph:
            ref_parts.append(paragraph)
        
        if ref_parts:
            parts.append('-'.join(ref_parts))
        
        return ' '.join(parts)


def parse_reference_linkbase(
    xml_file: str,
    role: str | None = None,
    ) -> Dict[str, List[Reference]]:
    """
    Extract references from a reference linkbase file.
    
    Reference linkbases link concepts to authoritative literature
    (FASB ASC, SEC Regulation S-X, IFRS standards, etc.)
    
    Unlike labels which contain text, references contain structured
    child elements like Publisher, Name, Topic, Section, Paragraph.
    
    Args:
        xml_file: Path to the reference linkbase XML file
        role: Optional role URI to filter by (e.g., Roles.REFERENCE).
              If None, returns all references.
    
    Returns:
        Dict mapping concept names to lists of Reference objects.
        A concept can have multiple references.
        Example: {
            'us-gaap_Assets': [Reference(...), Reference(...)],
            'us-gaap_Cash': [Reference(...)]
        }
    
    Examples:
        >>> refs = parse_reference_linkbase('us-gaap-ref-2023.xml')
        >>> for ref in refs.get('us-gaap_Assets', []):
        ...     print(ref.format_citation())
        FASB ASC 210-10-S99-1
        FASB ASC 210-10-45-1
        
        >>> # Filter by role
        >>> disclosure_refs = parse_reference_linkbase(
        ...     'us-gaap-ref-2023.xml',
        ...     role=Roles.DISCLOSURE_REF
        ... )
    """
    import xml.etree.ElementTree as ET
    
    # Pre-compute qualified names
    TAG_LOC = qname('link', 'loc')
    TAG_REFERENCE = qname('link', 'reference')
    TAG_ARC = qname('link', 'referenceArc')
    
    ATTR_LABEL = qname('xlink', 'label')
    ATTR_HREF = qname('xlink', 'href')
    ATTR_ROLE = qname('xlink', 'role')
    ATTR_FROM = qname('xlink', 'from')
    ATTR_TO = qname('xlink', 'to')
    
    # Storage
    loc_map: Dict[str, str] = {}           # label_id -> concept_name
    ref_map: Dict[str, Reference] = {}      # label_id -> Reference
    arc_links: List[tuple[str, str]] = []   # (from_id, to_id)
    
    # For reference linkbases, we need to capture child elements.
    # Use iterparse with start/end to track when we're inside a reference element
    current_ref_label: str | None = None
    current_ref_role: str | None = None
    current_ref_parts: Dict[str, str] = {}
    
    context = ET.iterparse(xml_file, events=('start', 'end'))
    
    for event, elem in context:
        tag = elem.tag
        
        if event == 'start':
            if tag == TAG_REFERENCE:
                # Starting a reference element - capture its attributes
                current_ref_label = elem.get(ATTR_LABEL)
                current_ref_role = elem.get(ATTR_ROLE)
                current_ref_parts = {}
        
        elif event == 'end':
            if tag == TAG_LOC:
                label_id = elem.get(ATTR_LABEL)
                href = elem.get(ATTR_HREF)
                if label_id and href:
                    loc_map[label_id] = extract_concept_from_href(href)
                elem.clear()
            
            elif tag == TAG_REFERENCE:
                # Ending a reference element - store it if it passes filters
                if current_ref_label:
                    # Filter by role if specified
                    if role is None or current_ref_role == role:
                        ref_map[current_ref_label] = Reference(
                            role=current_ref_role or '',
                            parts=current_ref_parts.copy()
                        )
                
                current_ref_label = None
                current_ref_role = None
                current_ref_parts = {}
                elem.clear()
            
            elif tag == TAG_ARC:
                from_id = elem.get(ATTR_FROM)
                to_id = elem.get(ATTR_TO)
                if from_id and to_id:
                    arc_links.append((from_id, to_id))
                elem.clear()
            
            elif current_ref_label is not None:
                # We're inside a reference element - this is a child part
                local_name = tag.split('}')[-1] if '}' in tag else tag
                if elem.text:
                    current_ref_parts[local_name] = elem.text.strip()
                elem.clear()
            
            else:
                # Some other element - just clear it
                elem.clear()
    
    # Resolution Phase: join locators with references via arcs
    result: Dict[str, List[Reference]] = {}
    
    for loc_id, ref_id in arc_links:
        if loc_id in loc_map and ref_id in ref_map:
            concept = loc_map[loc_id]
            ref = ref_map[ref_id]
            
            if concept not in result:
                result[concept] = []
            result[concept].append(ref)
    
    return result


def parse_reference_linkbase_flat(
    xml_file: str,
    role: str | None = None,
    ) -> Dict[str, List[Dict[str, str]]]:
    """
    Extract references as flat dictionaries (for pandas/JSON).
    
    Same as parse_reference_linkbase but returns dicts instead of
    Reference objects.
    
    Args:
        xml_file: Path to the reference linkbase XML file
        role: Optional role URI to filter by
    
    Returns:
        Dict mapping concept names to lists of reference dicts.
        Example: {
            'us-gaap_Assets': [
                {'role': '...', 'Publisher': 'FASB', 'Topic': '210', ...},
                ...
            ]
        }
    """
    refs = parse_reference_linkbase(xml_file, role=role)
    return {
        concept: [ref.to_dict() for ref in ref_list]
        for concept, ref_list in refs.items()
    }
```
