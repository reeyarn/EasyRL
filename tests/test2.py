"""
US-GAAP Taxonomy Analysis Script

This script processes the US-GAAP 2020 taxonomy files and creates a comprehensive
DataFrame with information about each concept including:
- Labels and documentation
- Statement classification (sfp, soi, scf, notes)
- Hierarchy path within each statement
"""

import sys
import re
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass
import pandas as pd
# Add src to path if running from repo root
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from leanrl import (
    parse_label_linkbase,
    parse_definition_linkbase,
    parse_presentation_linkbase,
    extract_concepts_from_schema,
    ConceptTree,
    Roles,
)


@dataclass
class StatementInfo:
    """Information about a concept's presence in a financial statement."""
    statement_type: str  # 'sfp', 'soi', 'scf-indir', 'scf-dir', 'notes'
    path: List[str]
    depth: int




def build_statement_trees(base_path: str) -> Dict[str, ConceptTree]:
    """
    Build ConceptTrees for each financial statement type.
    
    Scans the stm_path directory for definition linkbase files matching
    the pattern "us-gaap-stm-*-def-*.xml" and infers statement types from filenames.
    
    Returns dict mapping statement type to its definition tree.
    """
    trees = {}
    stm_path = Path(base_path) / 'stm'
    
    if not stm_path.exists():
        print(f"Warning: Statement path does not exist: {stm_path}")
        return trees
    
    # Pattern to match definition linkbase files
    pattern = re.compile(r'us-gaap-stm-(.+)-def-\d{4}-\d{2}-\d{2}\.xml')
    
    # Find all definition linkbase files
    for file_path in stm_path.glob('us-gaap-stm-*-def-*.xml'):
        match = pattern.match(file_path.name)
        if not match:
            continue
        
        # Extract statement type from filename
        stmt_identifier = match.group(1)
        
        # Map statement identifier to statement type
        # e.g., 'sfp-cls' -> 'sfp', 'scf-indir' -> 'scf-indir', 'soi' -> 'soi'
        if stmt_identifier.startswith('sfp'):
            statement_type = 'sfp'
        elif stmt_identifier.startswith('soi'):
            statement_type = 'soi'
        elif stmt_identifier.startswith('scf'):
            # Keep the full identifier for SCF (e.g., 'scf-indir', 'scf-dir', 'scf-inv')
            statement_type = stmt_identifier
        else:
            # For any other types, use the identifier as-is
            statement_type = stmt_identifier
        
        # Load the definition linkbase
        tree = parse_definition_linkbase(str(file_path))
        trees[statement_type] = tree
        print(f"Loaded {statement_type.upper()}: {len(tree)} concepts (from {file_path.name})")
    
    return trees


def find_concept_statement(
    concept: str, 
    trees: Dict[str, ConceptTree]
    ) -> Optional[StatementInfo]:
    """
    Find which statement(s) a concept belongs to and its path.
    
    Returns StatementInfo for the first statement found, or None.
    Priority: sfp > soi > scf-indir > scf-dir
    """
    priority = ['sfp', 'soi', 'scf-indir', 'scf-dir']
    
    for stmt_type in priority:
        if stmt_type not in trees:
            continue
        
        tree = trees[stmt_type]
        
        if concept in tree:
            path = tree.get_ancestor_path(concept)
            if path:
                # Add statement type as conceptual root
                full_path = [f'[{stmt_type.upper()}]'] + path
                return StatementInfo(
                    statement_type=stmt_type,
                    path=full_path,
                    depth=len(path)
                )
    
    return None


def build_taxonomy_dataframe(
    base_path: str,
    output_file: str | None = None
    ):
    """
    Build a comprehensive DataFrame of all US-GAAP concepts.
    
    Args:
        base_path: Path to the US-GAAP taxonomy folder (containing elts/, stm/, etc.)
        output_file: Output CSV filename
    
    Returns:
        pandas DataFrame with all concept information
    """
    
    
    base = Path(base_path)
    elts_path = base / 'elts'
    
    print("=" * 60)
    print("US-GAAP Taxonomy Analysis")
    print("=" * 60)
    print()
    
    # 1. Extract all concepts from schema
    schema_file = elts_path / 'us-gaap-2020-01-31.xsd'
    if not schema_file.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_file}")
    
    print(f"Extracting concepts from: {schema_file}")
    all_concepts = extract_concepts_from_schema(str(schema_file))
    print(f"Found {len(all_concepts)} concepts")
    print()
    
    # 2. Load labels
    print("Loading labels...")
    label_file = elts_path / 'us-gaap-lab-2020-01-31.xml'
    doc_file = elts_path / 'us-gaap-doc-2020-01-31.xml'
    
    labels = {}
    docs = {}
    
    if label_file.exists():
        labels = parse_label_linkbase(str(label_file), role=Roles.LABEL)
        print(f"  Labels: {len(labels)}")
    
    if doc_file.exists():
        docs = parse_label_linkbase(str(doc_file), role=Roles.DOCUMENTATION)
        print(f"  Documentation: {len(docs)}")
    print()
    
    # 3. Build statement trees
    print("Loading statement definition linkbases...")
    trees = build_statement_trees(base_path)
    print()
    
    # 4. Build DataFrame
    print("Building DataFrame...")
    rows = []
    
    for concept in all_concepts:
        # Get label and documentation
        label = labels.get(concept, '')
        documentation = docs.get(concept, '')
        
        # Find statement info
        stmt_info = find_concept_statement(concept, trees)
        
        if stmt_info:
            statement_type = stmt_info.statement_type
            path = ' > '.join(stmt_info.path)
            depth = stmt_info.depth
        else:
            statement_type = 'notes'  # Not in any statement = probably notes disclosure
            path = ''
            depth = None
        
        # Check if it's in multiple statements
        statements_present = []
        for stmt_type, tree in trees.items():
            if concept in tree:
                statements_present.append(stmt_type)
        
        rows.append({
            'concept': concept,
            'label': label,
            'documentation': documentation[:4096] if documentation else '',  # Truncate long docs
            'statement_type': statement_type,
            'all_statements': ','.join(statements_present) if statements_present else 'notes',
            'depth': depth,
            'path': path,
        })
    
    df = pd.DataFrame(rows)
    
    # Summary statistics
    print()
    print("=" * 60)
    print("Summary Statistics")
    print("=" * 60)
    print(f"\nTotal concepts: {len(df)}")
    print(f"\nBy primary statement type:")
    print(df['statement_type'].value_counts().to_string())
    print(f"\nConcepts with labels: {(df['label'] != '').sum()}")
    print(f"Concepts with documentation: {(df['documentation'] != '').sum()}")
    
    # Save to CSV
    if output_file:
        df.to_csv(output_file, index=False)
        print(f"\nSaved to: {output_file}")
    
    return df


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Analyze US-GAAP taxonomy and build concept DataFrame'
    )
    parser.add_argument(
        'taxonomy_path',
        help='Path to US-GAAP taxonomy folder (e.g., ./us-gaap-2020-01-31)'
    )
    parser.add_argument(
        '-o', '--output',
        default='us_gaap_taxonomy.csv',
        help='Output CSV filename (default: us_gaap_taxonomy.csv)'
    )
    
    args = parser.parse_args()
    
    df = build_taxonomy_dataframe(args.taxonomy_path, args.output)
    
    # Show some examples
    print("\n" + "=" * 60)
    print("Sample Records")
    print("=" * 60)
    
    # Show R&D expense
    rd = df[df['concept'] == 'us-gaap_ResearchAndDevelopmentExpense']
    if not rd.empty:
        print("\nResearchAndDevelopmentExpense:")
        row = rd.iloc[0]
        print(f"  Label: {row['label']}")
        print(f"  Statement: {row['statement_type']}")
        print(f"  Path: {row['path'][:100]}..." if len(row['path']) > 100 else f"  Path: {row['path']}")
    
    # Show Assets
    assets = df[df['concept'] == 'us-gaap_Assets']
    if not assets.empty:
        print("\nAssets:")
        row = assets.iloc[0]
        print(f"  Label: {row['label']}")
        print(f"  Statement: {row['statement_type']}")
        print(f"  Path: {row['path'][:100]}..." if len(row['path']) > 100 else f"  Path: {row['path']}")
    
    return df


if __name__ == '__main__':
    main()