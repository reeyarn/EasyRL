The definition linkbase (and presentation linkbase) creates a **tree/hierarchy** of concepts using parent-child arcs. Let me build a parser for this.Now update the linkbases `__init__.py`:Now let's test it:Let's copy to outputs:Here's the new `parse_definition_linkbase` function. It builds a recursive tree structure:

## Usage

```python
from easyrl import parse_definition_linkbase

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

# Print tree structure
print(tree.print_tree())

# Convert to pandas DataFrame
from easyrl import get_hierarchy_dataframe
df = get_hierarchy_dataframe(tree)
```

## ConceptTree Methods

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