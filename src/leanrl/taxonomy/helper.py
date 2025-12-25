from pathlib import Path
import re
import pandas as pd


import tempfile
import zipfile
import os
import shutil


from dataclasses import dataclass
from typing import Dict, List, Optional
from ..core.namespaces import Roles
from ..linkbases import (
    parse_label_linkbase,
    parse_reference_linkbase,
    parse_definition_linkbase,
    parse_presentation_linkbase,
    ConceptTree,
)
from ..taxonomy import (
    extract_concepts_from_schema,
    parse_schema_to_dict,
)

@dataclass
class StatementInfo:
    """Information about a concept's presence in a financial statement."""
    statement_type: str  # 'sfp', 'soi', 'scf-indir', 'scf-dir', 'notes'
    path: List[str]
    depth: int


def find_file_by_pattern(directory: Path, pattern: str) -> Optional[Path]:
    """
    Find a file in a directory matching a given pattern.
    """
    if not directory.exists():
        return None
    
    regex = re.compile(pattern)
    for file_path in directory.iterdir():
        if file_path.is_file() and regex.match(file_path.name):
            return file_path
    return None


def build_stm_dis_trees(base_path: str, tree_type='def') -> Dict[str, ConceptTree]:
    """
    Build ConceptTrees for each financial statement and disclosure type.
    
    Scans the stm_path and dis_path directories for definition linkbase files matching
    the patterns "us-gaap-stm-*-def-*.xml" and "us-gaap-dis-*-def-*.xml" respectively.
    
    Returns dict mapping statement and disclosure type to its definition tree.
    """
    trees = {}
    stm_path = Path(base_path) / 'stm'
    dis_path = Path(base_path) / 'dis'
    elts_path = Path(base_path) / 'elts'
    if not stm_path.exists():
        print(f"Warning: Statement path does not exist: {stm_path}")
        return trees
    
    if not dis_path.exists():
        print(f"Warning: Disclosure path does not exist: {dis_path}")
        #return trees
    all_files = []
    
    #us-gaap-dis-ts-def-2020-01-31.xml
    # Use glob patterns (not regex) to find files, then filter with regex
    pattern_stm = re.compile(r'us-gaap-stm-(.+)-'+tree_type+r'-\d{4}(?:-\d{2}-\d{2})?\.xml')
    pattern_dis = re.compile(r'us-gaap-dis-(.+)-'+tree_type+r'-\d{4}(?:-\d{2}-\d{2})?\.xml')
    pattern_elts = re.compile(r'us-gaap-'+tree_type+r'-\d{4}(?:-\d{2}-\d{2})?\.xml')
    
    # Use simple glob patterns and filter with regex
    for file_path in dis_path.glob('us-gaap-dis-*-'+tree_type+'-*.xml'):
        if pattern_dis.match(file_path.name):
            all_files.append(file_path)
        
    for file_path in stm_path.glob('us-gaap-stm-*-'+tree_type+'-*.xml'):
        if pattern_stm.match(file_path.name):
            all_files.append(file_path)
    
    for file_path in elts_path.glob('us-gaap-'+tree_type+'-*.xml'):
        if pattern_elts.match(file_path.name):
            all_files.append(file_path)
    for file_path in all_files:
        #file_path = Path(base_path) / "stm" / "us-gaap-stm-soi-def-2020-01-31.xml"
        match_stm = pattern_stm.match(file_path.name)
        match_dis = pattern_dis.match(file_path.name)
        if not match_stm and not match_dis:
            continue
        # Extract statement type from filename
        stmt_identifier = match_stm.group(1) if match_stm else None
        dis_identifier = match_dis.group(1) if match_dis else None
        # Map statement identifier to statement type
        # e.g., 'sfp-cls' -> 'sfp', 'scf-indir' -> 'scf-indir', 'soi' -> 'soi'
        if stmt_identifier:
            if stmt_identifier.startswith('sfp'):
                statement_type = stmt_identifier #'sfp'
            elif stmt_identifier.startswith('soi'):
                statement_type = stmt_identifier #'soi'
            elif stmt_identifier.startswith('scf'):
                # Keep the full identifier for SCF (e.g., 'scf-indir', 'scf-dir', 'scf-inv')
                statement_type = stmt_identifier #"scf"
            else :
                statement_type = stmt_identifier
        elif dis_identifier:
            statement_type = "dis-" + dis_identifier
        else:
            statement_type = "unknown"
        
        # Load the definition linkbase
        if tree_type == 'def':
            #file_path = Path(base_path) / "stm" / "us-gaap-stm-soi-def-2020-01-31.xml"
            tree = parse_definition_linkbase(str(file_path))
            #tree.nodes['us-gaap_ResearchAndDevelopmentExpense']
        elif tree_type == 'pre':
            #file_path = Path(base_path) / "stm" / "us-gaap-stm-soi-pre-2020-01-31.xml"
            tree = parse_presentation_linkbase(str(file_path))
            #tree.nodes['us-gaap_ResearchAndDevelopmentExpense']
        # elif tree_type == 'ref':
        #     tree = parse_reference_linkbase(str(file_path))
        else:
            print(f"Warning: Unknown tree type: {tree_type}, skipping {file_path.name}")
            continue
        
        if tree is not None:
            trees[statement_type] = tree
            print(f"Loaded {statement_type.upper()}: {len(tree)} concepts (from {file_path.name}) for {tree_type} type")
    
    return trees


def find_concept_stm_dis(
    concept: str, 
    trees: Dict[str, ConceptTree]
    ) -> Optional[StatementInfo]:
    """
    Find which statement(s) a concept belongs to and its path.
    
    Returns StatementInfo for the first statement found, or None.
    Priority: sfp > soi > scf-indir > scf-dir
    """
    priority0 = ['sfp', 'soi', 'scf']
    stmt_fullname = {"sfp": "Statement of Financial Position", "soi": "Statement of Income", "scf": "Statement of Cash Flows"}
    stm_types = trees.keys()
    priority = priority0.copy()
    for st in stm_types:
        if re.search( '^(' + '|'.join(priority0) + ')', st):
            st0 = st.split('-')[0]
            if st not in priority:
                priority.append(st)
            stmt_fullname[st] = stmt_fullname.get(st0, "unknown")
    #return priority
    #priority = [st for st in stm_types if re.search( '^(' + '|'.join(priority0) + ')', st)]
    for stmt_type in priority:
        if stmt_type not in trees:
            continue
        
        tree = trees[stmt_type]
        
        if concept in tree:
            path = tree.get_ancestor_path(concept)
            if path:
                # Add statement type as conceptual root
                fullname = stmt_fullname.get(stmt_type, "unknown")
                full_path = [f'[{fullname}]'] + path
                print(f"Found {concept} in {fullname} with path: {full_path}")
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
    
    
    # 1. Extract all concepts from schema
    schema_file = find_file_by_pattern(elts_path, r'us-gaap-\d{4}(?:-\d{2}-\d{2})?\.xsd')
    if not schema_file:
        raise FileNotFoundError(f"Schema file not found matching pattern us-gaap-\\d{{4}}(-\\d{{2}}-\\d{{2}})?\\.xsd in {elts_path}")
    
    print(f"Extracting concepts from: {schema_file}")
    all_concepts = extract_concepts_from_schema(str(schema_file), include_abstract=True)
    print(f"Found {len(all_concepts)} concepts")
    
    # Also load schema metadata (type, periodType, balance, abstract)
    schema_dict = parse_schema_to_dict(str(schema_file), include_abstract=True)
    print(f"Loaded schema metadata for {len(schema_dict)} concepts")
    print()
    
    # 2. Load labels
    print("Loading labels...")
    label_file = find_file_by_pattern(elts_path, r'us-gaap-lab-\d{4}(?:-\d{2}-\d{2})?\.xml')
    doc_file = find_file_by_pattern(elts_path, r'us-gaap-doc-\d{4}(?:-\d{2}-\d{2})?\.xml')
    
    labels = {}
    docs = {}
    
    if label_file:
        labels = parse_label_linkbase(str(label_file), role=Roles.LABEL)
        print(f"  Labels: {len(labels)}")
    
    if doc_file:
        docs = parse_label_linkbase(str(doc_file), role=Roles.DOCUMENTATION)
        print(f"  Documentation: {len(docs)}")
    print()
    
    # 3. Build statement trees
    print("Loading statement and disclosure definition linkbases...")
    def_trees = build_stm_dis_trees(base_path, tree_type='def')    
    pre_trees = build_stm_dis_trees(base_path, tree_type='pre')
    # if not "soi" in def_trees.keys() or not "soi" in pre_trees.keys():
    #     raise ValueError("Statement of Income not found in definition or presentation linkbases")
    # if 'us-gaap_ResearchAndDevelopmentExpense' not in def_trees["soi"].nodes and 'us-gaap_ResearchAndDevelopmentExpense' not in pre_trees["soi"].nodes:
    #     raise ValueError("ResearchAndDevelopmentExpense not found in definition or presentation linkbases")
    
    
    # 4. Load references
    print("Loading references...")
    reference_file = find_file_by_pattern(elts_path, r'us-gaap-ref-\d{4}(?:-\d{2}-\d{2})?\.xml')
    if reference_file:
        references_dict = parse_reference_linkbase(str(reference_file))
        print(f"  References: {len(references_dict)}")
        print()
    else:
        print(f"  References file not found matching pattern us-gaap-ref-\\d{{4}}(-\\d{{2}}-\\d{{2}})?\\.xml in {elts_path}")
        references_dict = {}
    
    # 4. Build DataFrame
    print("Building DataFrame...")
    rows = []
    
    for concept in all_concepts:
        # Get label and documentation
        #concept = all_concepts[1280]
        label = labels.get(concept, '')
        documentation = docs.get(concept, '')
        reference = references_dict.get(concept, [])
        # if reference:
        #     #reference = [ref['Publisher'] + ' ' + ref['Name'] + ' ' + ref['Topic'] + ' ' + ref['Section'] for ref in reference]
        #     reference = ', '.join(reference)
        # else:
        #     reference = ''
        
        # Get schema metadata
        schema_info = schema_dict.get(concept)
        if schema_info:
            is_abstract = schema_info.abstract
            period_type = schema_info.period_type  # 'instant' or 'duration'
            is_monetary = schema_info.is_monetary
            balance = schema_info.balance  # 'debit' or 'credit'
            data_type = schema_info.type
        else:
            is_abstract = None
            period_type = None
            is_monetary = None
            balance = None
            data_type = None
        
        # Find statement info
        stm_dis_info = find_concept_stm_dis(concept, def_trees)
        stm_dis_pre  = find_concept_stm_dis(concept, pre_trees)
        
        if stm_dis_pre:
            stm_dis_type = stm_dis_pre.statement_type
            path = ' > '.join(stm_dis_pre.path)
            depth = stm_dis_pre.depth
        elif stm_dis_info:
            stm_dis_type = stm_dis_info.statement_type
            path = '[DEFINITION PATH]:' + ' > '.join(stm_dis_info.path)
            depth = stm_dis_info.depth

        else:
            stm_dis_type = 'unknown'  # Not in any statement = probably notes disclosure
            path = ''
            depth = None
        
        # Check if it's in multiple statements
        statements_present = []
        disclosures_present = []
        for stmt_type, tree in def_trees.items():
            if re.search( '^(sfp|soi|scf)', stmt_type):
                if concept in tree:
                    statements_present.append(stmt_type)
            else:
                if concept in tree:
                    disclosures_present.append(stmt_type)
        rows.append({
            'concept': concept,
            'label': label,
            'documentation': documentation[:4096] if documentation else '',  # Truncate long docs
            'reference': ', '.join([str (r) for r in reference]),
            # Schema metadata
            'data_type': data_type,
            'is_abstract': is_abstract,
            'period_type': period_type,
            'is_monetary': is_monetary,
            'balance': balance,
            # Statement/disclosure info
            'all_statements': ','.join(statements_present) if statements_present else '',
            'all_disclosures': ','.join(disclosures_present) if disclosures_present else '',
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
    print(df['all_statements'].value_counts().to_string())
    print(f"\nBy primary disclosure type:")
    print(df['all_disclosures'].value_counts().to_string())
    print(f"\nConcepts with labels: {(df['label'] != '').sum()}")
    print(f"Concepts with documentation: {(df['documentation'] != '').sum()}")
    
    # Schema metadata summary
    print(f"\n--- Schema Metadata ---")
    print(f"Abstract concepts: {df['is_abstract'].sum()}")
    print(f"Monetary concepts: {df['is_monetary'].sum()}")
    print(f"\nBy period type:")
    print(df['period_type'].value_counts(dropna=False).to_string())
    print(f"\nBy balance type:")
    print(df['balance'].value_counts(dropna=False).to_string())
    
    # Save to CSV
    if output_file:
        df.to_csv(output_file, index=False)
        print(f"\nSaved to: {output_file}")
        df.to_excel(output_file.replace('.csv', '.xlsx'), index=False)
    
    return df



def build_taxonomy_dataframe_from_zip(zip_file: str):
    """
    Extract a taxonomy zip file and build a comprehensive DataFrame of all US-GAAP concepts.
    
    This function extracts the zip file to a temporary directory, calls build_taxonomy_dataframe,
    and then cleans up the temporary files.
    
    Args:
        zip_file: Path to the zip file containing taxonomy data
        
    Returns:
        pandas DataFrame with all concept information (same as build_taxonomy_dataframe)
    """
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Extract the zip file to the temporary directory
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        # Call build_taxonomy_dataframe with the temporary directory path
        df = build_taxonomy_dataframe(temp_dir)
        
        return df
    
    finally:
        # Optionally clean up the temporary directory
        # Note: If you want to keep the files for inspection, comment out the cleanup
        shutil.rmtree(temp_dir, ignore_errors=True)