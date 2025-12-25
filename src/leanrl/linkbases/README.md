# Summary of All Linkbase Parsers

| Linkbase | Parser | Arc Type | Key Feature |
|----------|--------|----------|-------------|
| **Label** | `parse_label_linkbase()` | `labelArc` | Text labels & documentation |
| **Reference** | `parse_reference_linkbase()` | `referenceArc` | Links to FASB/SEC literature |
| **Definition** | `parse_definition_linkbase()` | `definitionArc` | Dimensional hierarchies |
| **Presentation** | `parse_presentation_linkbase()` | `presentationArc` | Display hierarchies |
| **Calculation** | `parse_calculation_linkbase()` | `calculationArc` | Summation with weights |

---

## LABEL LINKBASE

Extract human-readable labels and documentation for concepts.

### Usage

```python
from leanrl import parse_label_linkbase, Roles

# Get documentation (default role)
docs = parse_label_linkbase('us-gaap-doc-2020-01-31.xml')
print(docs.get('us-gaap_ResearchAndDevelopmentExpense'))
# -> 'Sum of the carrying amounts as of the balance sheet date...'

# Get display labels
labels = parse_label_linkbase('us-gaap-lab-2020-01-31.xml', role=Roles.LABEL)
print(labels.get('us-gaap_Assets'))
# -> 'Assets'

# Access labels for concepts
for concept, label in labels.items():
    print(f"{concept}: {label}")
```

### Common Roles

- `Roles.DOCUMENTATION`: Detailed concept descriptions (default)
- `Roles.LABEL`: Standard display labels
- `Roles.TERSE_LABEL`: Short labels
- `Roles.VERBOSE_LABEL`: Extended labels

---

## REFERENCE LINKBASE

Extract references to authoritative literature (FASB, SEC, IFRS, etc.).

### Usage

```python
from leanrl import parse_reference_linkbase, parse_reference_linkbase_flat, Reference

# Parse references (returns dict of concept -> list of Reference objects)
references_dict = parse_reference_linkbase('us-gaap-ref-2020-01-31.xml')

# Get references for a concept
refs = references_dict.get('us-gaap_Assets', [])
for ref in refs:
    print(ref)
    # -> Reference(FASB Accounting Standards Codification Topic 210 Section 10)
    print(ref.parts)
    # -> {'Publisher': 'FASB', 'Name': 'Accounting Standards Codification', 
    #     'Topic': '210', 'Section': '10'}

# Format as string for display
reference_str = ', '.join([str(r) for r in refs])
print(reference_str)
# -> 'Reference(FASB Accounting Standards Codification Topic 210 Section 10)'

# Alternative: flat dictionary format
refs_flat = parse_reference_linkbase_flat('us-gaap-ref-2020-01-31.xml')
```

---

## DEFINITION LINKBASE

Build hierarchical trees of concepts using definition arcs. Used for dimensional relationships.

### Usage

```python
from leanrl import parse_definition_linkbase

# Parse the definition linkbase
tree = parse_definition_linkbase('us-gaap-stm-soi-def-2020-01-31.xml')

# Get parent
tree.get_parent('us-gaap_ResearchAndDevelopmentExpense')
# -> 'us-gaap_ResearchAndDevelopmentExpenseAbstract'

# Get all ancestors (child to root)
tree.get_ancestors('us-gaap_ResearchAndDevelopmentExpense')
# -> ['us-gaap_ResearchAndDevelopmentExpenseAbstract',
#     'us-gaap_OperatingCostsAndExpensesAbstract',
#     'us-gaap_OperatingExpensesAbstract',
#     'us-gaap_OperatingIncomeLossAbstract',
#     'us-gaap_IncomeStatementAbstract']

# Get full path (root to child)
tree.get_ancestor_path('us-gaap_ResearchAndDevelopmentExpense')
# -> ['us-gaap_IncomeStatementAbstract', ..., 'us-gaap_ResearchAndDevelopmentExpense']

# Get children
tree.get_children('us-gaap_ResearchAndDevelopmentExpenseAbstract')
# -> ['us-gaap_ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost',
#     'us-gaap_ResearchAndDevelopmentExpense']

# Get descendants (all children recursively)
tree.get_descendants('us-gaap_OperatingCostsAndExpensesAbstract')

# Get siblings
tree.get_siblings('us-gaap_ResearchAndDevelopmentExpense')

# Check if concept exists
if 'us-gaap_ResearchAndDevelopmentExpense' in tree.nodes:
    print("Concept found in tree")

# Get number of concepts
print(f"Tree contains {len(tree.nodes)} concepts")

# Print tree structure
print(tree.print_tree())

# Convert to pandas DataFrame
from leanrl import get_hierarchy_dataframe
df = get_hierarchy_dataframe(tree)
```

### ConceptTree Methods

| Method | Description |
|--------|-------------|
| `get_parent(concept)` | Get immediate parent |
| `get_children(concept)` | Get direct children (sorted by order) |
| `get_ancestors(concept)` | Get all ancestors (child → root) |
| `get_ancestor_path(concept)` | Get full path (root → child) |
| `get_descendants(concept)` | Get all descendants recursively |
| `get_siblings(concept)` | Get concepts with same parent |
| `get_depth(concept)` | Get depth in tree (0 = root) |
| `find_common_ancestor(c1, c2)` | Find lowest common ancestor |
| `print_tree()` | ASCII tree visualization |
| `to_dict()` | Convert to nested dict |
| `__contains__(concept)` | Check if concept exists (`concept in tree`) |
| `__len__()` | Get number of concepts (`len(tree)`) |

---

## PRESENTATION LINKBASE

Build display hierarchies for financial statements. Similar API to definition linkbase.

### Usage

```python
from leanrl import parse_presentation_linkbase

# Parse presentation linkbase
tree = parse_presentation_linkbase('us-gaap-stm-soi-pre-2020-01-31.xml')

# Same methods as definition linkbase
path = tree.get_ancestor_path('us-gaap_ResearchAndDevelopmentExpense')
print(' > '.join(path))
# -> 'us-gaap_IncomeStatementAbstract > ... > us-gaap_ResearchAndDevelopmentExpense'

# Convert to DataFrame
from leanrl import get_hierarchy_dataframe
df = get_hierarchy_dataframe(tree)
```

### Working with Multiple Statement Trees

```python
from pathlib import Path
from leanrl import parse_presentation_linkbase, ConceptTree
from typing import Dict

def build_statement_trees(base_path: str) -> Dict[str, ConceptTree]:
    """Build trees for each financial statement."""
    trees = {}
    stm_path = Path(base_path) / 'stm'
    
    # Find all presentation linkbase files
    for file_path in stm_path.glob('us-gaap-stm-*-pre-*.xml'):
        # Extract statement type from filename
        # e.g., 'us-gaap-stm-soi-pre-2020-01-31.xml' -> 'soi'
        match = re.match(r'us-gaap-stm-(.+)-pre-', file_path.name)
        if match:
            stmt_type = match.group(1)
            trees[stmt_type] = parse_presentation_linkbase(str(file_path))
    
    return trees

# Build trees for all statements
trees = build_statement_trees('/path/to/us-gaap-2020-01-31')

# Check which statements contain a concept
concept = 'us-gaap_ResearchAndDevelopmentExpense'
for stmt_type, tree in trees.items():
    if concept in tree:
        path = tree.get_ancestor_path(concept)
        print(f"Found in {stmt_type}: {' > '.join(path)}")
```

---

## CALCULATION LINKBASE

Extract summation relationships with weights.

### Usage

```python
from leanrl import parse_calculation_linkbase

tree = parse_calculation_linkbase('us-gaap-stm-soi-cal-2020-01-31.xml')

# What components make up R&D?
tree.get_components('us-gaap_ResearchAndDevelopmentExpense')
# -> {'us-gaap_ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost': 1.0,
#     'us-gaap_ResearchAndDevelopmentExpenseSoftwareExcludingAcquiredInProcessCost': 1.0,
#     'us-gaap_ResearchAndDevelopmentInProcess': 1.0}

# What does R&D contribute to?
tree.get_parent('us-gaap_ResearchAndDevelopmentExpense')
# -> 'us-gaap_OperatingCostsAndExpenses'

tree.get_weight('us-gaap_ResearchAndDevelopmentExpense')
# -> 1.0  (adds to parent)

# Human-readable formula
tree.get_formula('us-gaap_NetIncomeLoss')
# -> 'NetIncomeLoss = ProfitLoss - NetIncomeLossAttributableToNoncontrollingInterest'

# Validate actual numbers
values = {
    'us-gaap_NetIncomeLoss': 100,
    'us-gaap_ProfitLoss': 500,
    'us-gaap_NetIncomeLossAttributableToNoncontrollingInterest': 400
}
tree.validate_calculation('us-gaap_NetIncomeLoss', values)
# -> (True, 100.0, 100.0)  # (is_valid, expected, actual)

# Print tree with weights
print(tree.print_tree())
# us-gaap_NetIncomeLoss
#   us-gaap_Revenues (+1.0)
#   us-gaap_OperatingCostsAndExpenses (-1.0)
#     us-gaap_ResearchAndDevelopmentExpense (+1.0)
#     ...

# Convert to DataFrame
from leanrl import get_calculation_dataframe
df = get_calculation_dataframe(tree)
```

---

## COMPREHENSIVE EXAMPLE: Combining All Linkbases

This example shows how to combine multiple linkbases to build a comprehensive concept database:

```python
import re
from pathlib import Path
from leanrl import (
    parse_label_linkbase,
    parse_reference_linkbase,
    parse_definition_linkbase,
    parse_presentation_linkbase,
    Roles,
    ConceptTree,
)
from typing import Dict, Optional

def build_taxonomy_database(base_path: str):
    """Build comprehensive taxonomy database from all linkbases."""
    base = Path(base_path)
    elts_path = base / 'elts'
    
    # 1. Load labels and documentation
    label_file = elts_path / 'us-gaap-lab-2020-01-31.xml'
    doc_file = elts_path / 'us-gaap-doc-2020-01-31.xml'
    
    labels = parse_label_linkbase(str(label_file), role=Roles.LABEL)
    docs = parse_label_linkbase(str(doc_file), role=Roles.DOCUMENTATION)
    
    # 2. Load references
    ref_file = elts_path / 'us-gaap-ref-2020-01-31.xml'
    references = parse_reference_linkbase(str(ref_file))
    
    # 3. Build definition and presentation trees for statements
    def_trees = {}
    pre_trees = {}
    
    stm_path = base / 'stm'
    for file_path in stm_path.glob('us-gaap-stm-*-def-*.xml'):
        match = re.match(r'us-gaap-stm-(.+)-def-', file_path.name)
        if match:
            stmt_type = match.group(1)
            def_trees[stmt_type] = parse_definition_linkbase(str(file_path))
    
    for file_path in stm_path.glob('us-gaap-stm-*-pre-*.xml'):
        match = re.match(r'us-gaap-stm-(.+)-pre-', file_path.name)
        if match:
            stmt_type = match.group(1)
            pre_trees[stmt_type] = parse_presentation_linkbase(str(file_path))
    
    # 4. Find concept information
    def find_concept_info(concept: str) -> Dict:
        """Get all available information for a concept."""
        info = {
            'concept': concept,
            'label': labels.get(concept, ''),
            'documentation': docs.get(concept, ''),
            'reference': ', '.join([str(r) for r in references.get(concept, [])]),
        }
        
        # Find in presentation trees (preferred) or definition trees
        for stmt_type, tree in pre_trees.items():
            if concept in tree:
                path = tree.get_ancestor_path(concept)
                info['statement'] = stmt_type
                info['path'] = ' > '.join(path)
                info['depth'] = len(path)
                break
        else:
            for stmt_type, tree in def_trees.items():
                if concept in tree:
                    path = tree.get_ancestor_path(concept)
                    info['statement'] = stmt_type
                    info['path'] = ' > '.join(path)
                    info['depth'] = len(path)
                    break
        
        return info
    
    # Example: Get info for a concept
    rd_info = find_concept_info('us-gaap_ResearchAndDevelopmentExpense')
    print(f"Label: {rd_info['label']}")
    print(f"Documentation: {rd_info['documentation'][:100]}...")
    print(f"Reference: {rd_info['reference']}")
    print(f"Statement: {rd_info['statement']}")
    print(f"Path: {rd_info['path']}")
    
    return {
        'labels': labels,
        'docs': docs,
        'references': references,
        'def_trees': def_trees,
        'pre_trees': pre_trees,
        'find_concept_info': find_concept_info,
    }

# Usage
db = build_taxonomy_database('/path/to/us-gaap-2020-01-31')
```

---

## Finding Concepts Across Multiple Trees

```python
from leanrl import ConceptTree
from typing import Dict, List

def find_concept_in_trees(concept: str, trees: Dict[str, ConceptTree]) -> List[Dict]:
    """Find a concept across multiple statement/disclosure trees."""
    results = []
    
    for tree_name, tree in trees.items():
        if concept in tree:
            path = tree.get_ancestor_path(concept)
            results.append({
                'tree': tree_name,
                'path': path,
                'depth': len(path),
                'parent': tree.get_parent(concept),
            })
    
    return results

# Example usage
trees = {
    'soi': parse_definition_linkbase('us-gaap-stm-soi-def-2020-01-31.xml'),
    'sfp': parse_definition_linkbase('us-gaap-stm-sfp-cls-def-2020-01-31.xml'),
    'scf-indir': parse_definition_linkbase('us-gaap-stm-scf-indir-def-2020-01-31.xml'),
}

results = find_concept_in_trees('us-gaap_CashAndCashEquivalentsAtCarryingValue', trees)
for r in results:
    print(f"Found in {r['tree']} at depth {r['depth']}")
    print(f"  Path: {' > '.join(r['path'])}")
```
