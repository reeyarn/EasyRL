# taxonomy Contents
## taxonomy/__init__.py
```py
"""
XBRL Taxonomy Parsers

Parse taxonomy schema files (.xsd) to extract concept definitions
and metadata.
"""

from .schema import (
    ConceptSchema,
    parse_schema,
    parse_schema_to_dict,
    get_concept_types,
    get_schema_dataframe,
    extract_concepts_from_schema,
    MONETARY_TYPES,
)

from .constants import (
    statement_full_names,
    disclosure_full_names,
)

from .helper import (
    StatementInfo,
    find_file_by_pattern,
    build_stm_dis_trees,
    find_concept_stm_dis,
    build_taxonomy_dataframe,
    build_taxonomy_dataframe_from_zip,
)

__all__ = [
    'ConceptSchema',
    'parse_schema',
    'parse_schema_to_dict',
    'get_concept_types',
    'get_schema_dataframe',
    'extract_concepts_from_schema',
    'MONETARY_TYPES',
    # constants
    'statement_full_names',
    'disclosure_full_names',
    # helper functions
    'StatementInfo',
    'find_file_by_pattern',
    'build_stm_dis_trees',
    'find_concept_stm_dis',
    'build_taxonomy_dataframe',
    'build_taxonomy_dataframe_from_zip',
]
```

## taxonomy/constants.py
```py
"""
Constants for XBRL US GAAP Taxonomies v1.0 (2008-03-31 FINAL release)

Abbreviations used in file names and statement/disclosure types:

STATEMENT ABBREVIATIONS:
    -sfp-  = Statement of Financial Position (Balance Sheet)
    -soi-  = Statement of Income
    -scf-  = Statement of Cash Flows
    -she-  = Statement of Shareholder Equity
    -scp-  = Statement of Partner Capital

INDUSTRY ABBREVIATIONS:
    -bd-   = Broker-Dealer
    -basi- = Banking and Savings
    -ci-   = Commercial and Industrial
    -ins-  = Insurance
    -re-   = Real Estate

LINKBASE TYPES:
    -cal-  = Calculation
    -def-  = Definition
    -doc-  = Documentation (contains xbrl labels having role "documentation")
    -lab-  = Labels (contains labels with 'standard' label role)
    -pre-  = Presentation
    -ref-  = Reference

FILE NAME PATTERNS:
    -std-  = Load a 'minimal' taxonomy with no documentation or references
    -all-  = Load full taxonomy with documentation and references for concepts
    -ent-  = Load a non-gaap entry point with standard labels and linkbases
    -dis-  = A disclosure schema or linkbase
    -stm-  = A statement schema or linkbase

OTHER ABBREVIATIONS:
    int, int1, int2... = Unnumbered is a main extended link, numbered are 
                         alternative calculation sets with NO presentations.
    dbo, dbo1...       = Development stage entities / Discontinued operations
    
ADDITIONAL PREFIXES/CODES:
    ar       = Accounting Report
    exch     = Exchange codes
    mr       = Management Report
    dei      = Document and Entity Information
    mda      = Management Discussion and Analysis
    seccert  = SEC Certification
    stpr     = State-Province codes
    us-gaap  = GAAP taxonomy prefix
    
Source: XBRL US GAAP Taxonomies v1.0 (c) 2008 XBRL US Inc. All rights reserved.
"""

statement_full_names = {
    'stm': 'Statement',
    'scf-indir': 'Statement of Cash Flows - Indirect Method',
    'scf-inv': 'Statement of Cash Flows - Investing Activities',
    'scf-re': 'Statement of Cash Flows - Real Estate Entities',
    'scf-dbo': 'Statement of Cash Flows - Development Stage Entities / Discontinued Operations',
    'sfp-cls': 'Statement of Financial Position - Classified (Balance Sheet - Classified)',
    'scf-sbo': 'Statement of Cash Flows - Supplemental Balance Sheet Offsetting',
    'sfp-clreo': 'Statement of Financial Position - Classified - Real Estate Operations',
    'soi': 'Statement of Income (generic / primary)',
    'sfp-dbo': 'Statement of Financial Position - Development Stage Entities',
    'soi-egm': 'Statement of Income - Equity Method Investments',
    'sfp-ucreo': 'Statement of Financial Position - Unclassified - Real Estate Operations',
    'soi-int': 'Statement of Income - Interest',
    'sfp-ibo': 'Statement of Financial Position - Insurance Based Operations',
    'soi-re': 'Statement of Income - Real Estate',
    'soi-reit': 'Statement of Income - REIT (Real Estate Investment Trust)',
    'soi-sbi': 'Statement of Income - Small Business Issuer',
    'soi-ins': 'Statement of Income - Insurance',
    'scf-sd': 'Statement of Cash Flows - Supplemental Disclosures',
    'scf-dir': 'Statement of Cash Flows - Direct Method',
}

disclosure_full_names = {
    '': 'No Disclosure / General / Unspecified',
    'dis-fifvd': 'Fair Value Disclosures',
    'dis-fs-insa': 'Financial Services - Insurance Assets',
    'dis-fs-ins': 'Financial Services - Insurance',
    'dis-ides': 'Impairment or Disposal of Long-Lived Assets (Including Discontinued Operations)',
    'dis-crcrb': 'Credit Losses - Receivables and Credit Risk Disclosures (Broad)',
    'dis-equity': 'Equity',
    'dis-diha': 'Deferred Income and Other Assets (Possibly Deferred Costs or Intangibles)',
    'dis-cecl': 'Current Expected Credit Losses (CECL)',
    'sheci': "Statement of Shareholders' Equity and Comprehensive Income",
    'dis-cc': 'Commitments and Contingencies',
    'dis-debt': 'Debt',
    'dis-bc': 'Business Combinations',
    'dis-ts': 'Transfers and Servicing (of Financial Assets)',
    'dis-rlnro': 'Related Party Disclosures (Possibly Related Lending or Non-Recourse)',
    'dis-regop': 'Regulatory and Operating Practices (Possibly Segment or Operating Disclosures)',
    'dis-leas': 'Leases',
    'dis-crcsbp': 'Credit Risk - Securities Borrowing and Lending (Possibly)',
    'soc': 'Segment Reporting (Statement of Operating Segments / Operating Segments)',
    'dis-fs-bt': 'Financial Services - Broker and Trader',
    'dis-disops': 'Discontinued Operations',
    'dis-ap': 'Accounting Policies',
    'dis-invco': 'Inventory',
    'dis-bsoff': 'Balance Sheet Offsetting',
    'dis-fs-bd': 'Financial Services - Banking and Depository',
    'dis-iago': 'Intangible Assets and Goodwill',
    'dis-schedoi-sumhold': 'Schedule of Investments - Summary Holdings',
    'dis-schedoi-hold': 'Schedule of Investments - Holdings',
    'dis-ppe': 'Property, Plant, and Equipment',
    'dis-eps': 'Earnings Per Share',
    'dis-ocpfs': 'Other Comprehensive Income (Possibly Postretirement or Pension)',
    'dis-inctax': 'Income Taxes',
    'dis-schedoi-otsh': 'Schedule of Investments - Other Securities',
    'dis-ni': 'Net Income (Loss)',
    'dis-acec': 'Asset Retirement and Environmental Obligations (Possibly Accrued Environmental Costs)',
    'dis-schedoi-fednote': 'Schedule of Investments - Federal Notes',
    'dis-guar': 'Guarantees',
    'dis-edco': 'Equity Method and Joint Ventures (Possibly Equity Derivatives)',
    'dis-re': 'Real Estate',
    'spc': 'Special Purpose Company / Entity Disclosures (Often SPAC-related)',
    'dis-rpd': 'Research and Development',
    'dis-sr': 'Subsequent Events (Possibly Stock Repurchase)',
    'dis-inv': 'Investments',
    'com': 'Commitments (Possibly Commitments and Contingencies or Compensation)',
    'dis-ei': 'Extraordinary Items (Possibly Environmental)',
    'dis-emjv': 'Equity Method Investments and Joint Ventures',
    'dis-othliab': 'Other Liabilities',
    'dis-schedoi-shorthold': 'Schedule of Investments - Short-Term Holdings',
    'dis-rbtmp011': 'Regulated Broker/Temporary Template 011 (Industry-specific modeling)',
    'dis-reorg': 'Reorganization',
    'dis-cce': 'Cash and Cash Equivalents',
    'dis-ero': 'Earnings Release (Possibly Other Revenue)',
    'dis-te': 'Temporary Equity (Redeemable Preferred Stock)',
    'dis-rcc': 'Receivables and Credit Losses (Possibly Related Credit Concentrations)',
    'dis-fifvdtmp02': 'Fair Value Disclosures Temporary Template 02',
    'dis-foct': 'Financial Instruments - Other Comprehensive Income (Possibly Fair Value Option)',
    'dis-sec-sum': 'Securities (Summary)',
    'dis-eui': 'Equity Underwriting (Possibly Energy)',
    'dis-ru': 'Revenue Recognition (Possibly Regulated Utilities)',
    'dis-rbtmp09': 'Regulated Broker Temporary Template 09',
    'dis-sec-vq': 'Securities - Variable Interest Entities (Possibly Variable Quality)',
    'dis-rbtmp07': 'Regulated Broker Temporary Template 07',
    'dis-rbtmp06': 'Regulated Broker Temporary Template 06',
    'dis-rbtmp08': 'Regulated Broker Temporary Template 08',
    'dis-rbtmp05': 'Regulated Broker Temporary Template 05',
    'dis-rbtmp03': 'Regulated Broker Temporary Template 03',
    'dis-schedoi-iiaa': 'Schedule of Investments - Investments in Affiliates',
    'dis-sec-reins': 'Securities - Reinsurance',
    'dis-rbtmp02': 'Regulated Broker Temporary Template 02',
    'dis-crcgen': 'Credit Risk - General',
    'dis-insldtmp021': 'Insurance Liabilities Disclosures Temporary Template 021',
    'dis-fifvdtmp01': 'Fair Value Disclosures Temporary Template 01',
    'dis-cecltmp01': 'CECL Temporary Template 01',
    'dis-hco': 'Health Care Organizations',
    'dis-idestmp021': 'Impairment/Disposal Temporary Template 021',
    'dis-rbtmp04': 'Regulated Broker Temporary Template 04',
    'dis-cecltmp02': 'CECL Temporary Template 02',
    'dis-sec-re': 'Securities - Real Estate',
    'dis-nt': 'Noncontrolling Interests (Possibly Notes)',
    'dis-insldtmp041': 'Insurance Liabilities Disclosures Temporary Template 041',
    'dis-idestmp022': 'Impairment/Disposal Temporary Template 022',
    'dis-rbtmp012': 'Regulated Broker Temporary Template 012',
    'dis-insldtmp031': 'Insurance Liabilities Disclosures Temporary Template 031',
    'dis-idestmp011': 'Impairment/Disposal Temporary Template 011',
    'dis-insldtmp061': 'Insurance Liabilities Disclosures Temporary Template 061',
    'dis-insldtmp032': 'Insurance Liabilities Disclosures Temporary Template 032',
    'dis-cecltmp05': 'CECL Temporary Template 05',
    'dis-insldtmp051': 'Insurance Liabilities Disclosures Temporary Template 051',
    'dis-cecltmp04': 'CECL Temporary Template 04',
    'dis-rd': 'Research and Development',
    'dis-cecltmp03': 'CECL Temporary Template 03',
    'dis-sec-suppc': 'Securities - Supplemental Parent Company',
    'dis-rbtmp041': 'Regulated Broker Temporary Template 041',
    'dis-rcctmp05': 'Receivables/Credit Concentrations Temporary Template 05',
    'dis-ir': 'Interim Reporting',
    'dis-sec-supins': 'Securities - Supplemental Insurance',
    'dis-idestmp012': 'Impairment/Disposal Temporary Template 012',
    'dis-schedoi-oocw': 'Schedule of Investments - Other Ownership Changes',
    'dis-fs-fhlb': 'Financial Services - Federal Home Loan Bank',
    'dis-insldtmp062': 'Insurance Liabilities Disclosures Temporary Template 062',
    'dis-sec-mort': 'Securities - Mortgage',
    'dis-sec-cndfir': 'Securities - Condensed Financial Information',
    'dis-insldtmp01': 'Insurance Liabilities Disclosures Temporary Template 01',
    'dis-oi': 'Operating Income (Possibly Other Income)',
    'dis-se': 'Stockholders\' Equity (Possibly Subsequent Events)',
    'dis-insldtmp042': 'Insurance Liabilities Disclosures Temporary Template 042',
    'dis-insldtmp024': 'Insurance Liabilities Disclosures Temporary Template 024',
    'dis-rcctmp01': 'Receivables/Credit Concentrations Temporary Template 01',
    'dis-insldtmp023': 'Insurance Liabilities Disclosures Temporary Template 023',
    'dis-rbtmp125': 'Regulated Broker Temporary Template 125',
    'dis-rbtmp131': 'Regulated Broker Temporary Template 131',
    'dis-insldtmp052': 'Insurance Liabilities Disclosures Temporary Template 052',
    'dis-insldtmp025': 'Insurance Liabilities Disclosures Temporary Template 025',
    'dis-fs-mort': 'Financial Services - Mortgage',
    'dis-insldtmp022': 'Insurance Liabilities Disclosures Temporary Template 022',
    'dis-rbtmp112': 'Regulated Broker Temporary Template 112',
    'dis-rcctmp04': 'Receivables/Credit Concentrations Temporary Template 04',
    'dis-insldtmp033': 'Insurance Liabilities Disclosures Temporary Template 033',
    'dis-rbtmp104': 'Regulated Broker Temporary Template 104',
    'dis-rbtmp111': 'Regulated Broker Temporary Template 111',
    'dis-rbtmp121': 'Regulated Broker Temporary Template 121',
    'dis-rbtmp122': 'Regulated Broker Temporary Template 122',
    'dis-rbtmp102': 'Regulated Broker Temporary Template 102',
    'dis-rbtmp123': 'Regulated Broker Temporary Template 123',
    'dis-rbtmp103': 'Regulated Broker Temporary Template 103',
    'dis-rbtmp141': 'Regulated Broker Temporary Template 141',
    'dis-rcctmp03': 'Receivables/Credit Concentrations Temporary Template 03',
    'dis-con': 'Consolidation',
    'dis-rbtmp105': 'Regulated Broker Temporary Template 105',
}
```

## taxonomy/helper.py
```py
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


def build_stm_dis_trees(base_path: str, tree_type='def', debug = False) -> Dict[str, ConceptTree]:
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
            if debug:
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
                #print(f"Found {concept} in {fullname} with path: {full_path}")
                return StatementInfo(
                    statement_type=stmt_type,
                    path=full_path,
                    depth=len(path)
                )
    return None


    
def build_taxonomy_dataframe(
    base_path: str,
    output_file: str | None = None,
    debug = False
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
    if debug:
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
        zip_file_name = Path(zip_file).stem
        # Call build_taxonomy_dataframe with the temporary directory path
        df = build_taxonomy_dataframe(os.path.join(temp_dir, zip_file_name))
        
        return df
    
    finally:
        # Optionally clean up the temporary directory
        # Note: If you want to keep the files for inspection, comment out the cleanup
        shutil.rmtree(temp_dir, ignore_errors=True)
```

## taxonomy/schema.py
```py
"""
XBRL Taxonomy Schema Parser

Extract concept definitions from XBRL taxonomy schema (.xsd) files.
Includes metadata like type, periodType, balance, and abstract status.
"""

from typing import List, Dict, Optional, Set
from dataclasses import dataclass, field, asdict
from pathlib import Path
import xml.etree.ElementTree as ET


# XML Schema namespace
XS_NS = '{http://www.w3.org/2001/XMLSchema}'

# XBRL Instance namespace (for periodType, balance attributes)
XBRLI_NS = '{http://www.xbrl.org/2003/instance}'

# Common monetary type patterns
MONETARY_TYPES = {
    'xbrli:monetaryItemType',
    'monetaryItemType',
    'us-types:monetaryItemType',
}

# Patterns that indicate monetary types (suffix matching)
MONETARY_TYPE_SUFFIXES = (
    'MonetaryItemType',
    'monetaryItemType',
)


@dataclass
class ConceptSchema:
    """
    Schema metadata for an XBRL concept extracted from a taxonomy .xsd file.
    
    This represents the schema-level definition of a concept, including
    its data type, period type, balance, and other XML Schema attributes.
    
    Note: This is different from ConceptNode (which represents a node in 
    a hierarchy tree from linkbases).
    
    Attributes:
        name: Concept name (e.g., 'us-gaap_Assets')
        id: Element ID attribute
        type: XML Schema type (e.g., 'xbrli:monetaryItemType')
        period_type: 'instant' or 'duration'
        balance: 'debit', 'credit', or None
        abstract: Whether this is an abstract grouping element
        substitution_group: The substitution group (e.g., 'xbrli:item')
        nillable: Whether the element can be nil
    """
    name: str
    id: str = ''
    type: str = ''
    period_type: Optional[str] = None  # 'instant' or 'duration'
    balance: Optional[str] = None       # 'debit' or 'credit'
    abstract: bool = False
    substitution_group: str = ''
    nillable: bool = True
    
    @property
    def is_monetary(self) -> bool:
        """Check if this concept represents a monetary value."""
        if not self.type:
            return False
        
        # Exact match
        if self.type in MONETARY_TYPES:
            return True
        
        # Suffix match (handles derived types)
        if self.type.endswith(MONETARY_TYPE_SUFFIXES):
            return True
        
        return False
    
    @property
    def is_instant(self) -> bool:
        """Check if this is a point-in-time (balance sheet) concept."""
        return self.period_type == 'instant'
    
    @property
    def is_duration(self) -> bool:
        """Check if this is a period (income statement) concept."""
        return self.period_type == 'duration'
    
    @property
    def is_debit(self) -> bool:
        """Check if this concept has debit balance."""
        return self.balance == 'debit'
    
    @property
    def is_credit(self) -> bool:
        """Check if this concept has credit balance."""
        return self.balance == 'credit'
    
    @property
    def short_name(self) -> str:
        """Get the local name without prefix."""
        if '_' in self.name:
            return self.name.split('_', 1)[1]
        return self.name
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return asdict(self)


def parse_schema(
    schema_path: str,
    prefix: str = 'us-gaap',
    filter_monetary: bool = False,
    filter_instant: bool = False,
    filter_duration: bool = False,
    include_abstract: bool = False,
    ) -> List[ConceptSchema]:
    """
    Parse an XBRL taxonomy schema and extract concept definitions.
    
    Args:
        schema_path: Path to the .xsd schema file
        prefix: Namespace prefix to filter by (e.g., 'us-gaap', 'dei')
                Set to None to include all concepts.
        filter_monetary: If True, only return monetary type concepts
        filter_instant: If True, only return instant (balance sheet) concepts
        filter_duration: If True, only return duration (income statement) concepts
        include_abstract: If True, include abstract grouping elements
    
    Returns:
        List of ConceptSchema objects matching the filters
    
    Examples:
        >>> # All concrete US-GAAP concepts
        >>> schemas = parse_schema('us-gaap-2020-01-31.xsd')
        >>> len(schemas)
        15000
        
        >>> # Only monetary concepts
        >>> monetary = parse_schema('us-gaap-2020-01-31.xsd', filter_monetary=True)
        >>> 
        >>> # Balance sheet items only
        >>> bs_items = parse_schema('us-gaap-2020-01-31.xsd', 
        ...                         filter_monetary=True, 
        ...                         filter_instant=True)
        >>> 
        >>> # Income statement items only
        >>> is_items = parse_schema('us-gaap-2020-01-31.xsd',
        ...                         filter_monetary=True,
        ...                         filter_duration=True)
    """
    tree = ET.parse(schema_path)
    root = tree.getroot()
    
    results = []
    
    # Find all xs:element declarations
    for elem in root.iter(f'{XS_NS}element'):
        name = elem.get('name')
        if not name:
            continue
        
        # Add prefix if not present
        if prefix and not name.startswith(f'{prefix}_'):
            # Check if the element has an id with the prefix
            elem_id = elem.get('id', '')
            if elem_id.startswith(f'{prefix}_'):
                name = elem_id
            else:
                name = f'{prefix}_{name}'
        
        # Get attributes
        elem_id = elem.get('id', '')
        elem_type = elem.get('type', '')
        abstract = elem.get('abstract', 'false').lower() == 'true'
        nillable = elem.get('nillable', 'true').lower() == 'true'
        substitution_group = elem.get('substitutionGroup', '')
        
        # XBRL-specific attributes
        period_type = elem.get(f'{XBRLI_NS}periodType')
        balance = elem.get(f'{XBRLI_NS}balance')
        
        # Create concept schema
        schema = ConceptSchema(
            name=name,
            id=elem_id,
            type=elem_type,
            period_type=period_type,
            balance=balance,
            abstract=abstract,
            substitution_group=substitution_group,
            nillable=nillable,
        )
        
        # Apply filters
        if not include_abstract and abstract:
            continue
        
        if filter_monetary and not schema.is_monetary:
            continue
        
        if filter_instant and not schema.is_instant:
            continue
        
        if filter_duration and not schema.is_duration:
            continue
        
        results.append(schema)
    
    return results


def parse_schema_to_dict(
    schema_path: str,
    **kwargs
    ) -> Dict[str, ConceptSchema]:
    """
    Parse schema and return as dict keyed by concept name.
    
    Same parameters as parse_schema().
    
    Returns:
        Dict mapping concept name (str) to ConceptSchema object
    """
    schemas = parse_schema(schema_path, **kwargs)
    return {s.name: s for s in schemas}


def get_concept_types(schema_path: str) -> Dict[str, Set[str]]:
    """
    Get a summary of all concept types in the schema.
    
    Returns:
        Dict with keys 'types', 'period_types', 'balances', 'substitution_groups'
    """
    schemas = parse_schema(schema_path, include_abstract=True)
    
    return {
        'types': set(s.type for s in schemas if s.type),
        'period_types': set(s.period_type for s in schemas if s.period_type),
        'balances': set(s.balance for s in schemas if s.balance),
        'substitution_groups': set(s.substitution_group for s in schemas if s.substitution_group),
    }


def get_schema_dataframe(schema_path: str, **kwargs):
    """
    Parse schema and return as pandas DataFrame.
    
    Same parameters as parse_schema().
    
    Returns:
        pandas DataFrame with concept schema information
    """
    try:
        import pandas as pd
    except ImportError:
        raise ImportError("pandas is required for get_schema_dataframe()")
    
    schemas = parse_schema(schema_path, **kwargs)
    
    rows = [s.to_dict() for s in schemas]
    df = pd.DataFrame(rows)
    
    # Add derived columns
    if not df.empty:
        df['is_monetary'] = df.apply(
            lambda r: ConceptSchema(**r).is_monetary, axis=1
        )
    
    return df


def extract_concepts_from_schema(
    schema_path: str,
    prefix: str = 'us-gaap',
    filter_monetary: bool = False,
    include_abstract: bool = False,
    ) -> List[str]:
    """
    Extract concept names from an XBRL taxonomy schema.
    
    This is a simplified function that returns just concept names (strings).
    For full metadata, use parse_schema() which returns ConceptSchema objects.
    
    Args:
        schema_path: Path to the .xsd schema file
        prefix: Namespace prefix (e.g., 'us-gaap')
        filter_monetary: If True, only return monetary type concepts
        include_abstract: If True, include abstract grouping elements
    
    Returns:
        List of concept name strings (e.g., ['us-gaap_Assets', 'us-gaap_Liabilities', ...])
    
    Examples:
        >>> concepts = extract_concepts_from_schema('us-gaap-2020-01-31.xsd')
        >>> len(concepts)
        15000
        >>> concepts[:3]
        ['us-gaap_AccountingStandardsUpdateExtensibleList', ...]
    """
    schemas = parse_schema(
        schema_path,
        prefix=prefix,
        filter_monetary=filter_monetary,
        include_abstract=include_abstract,
    )
    return [s.name for s in schemas]
```
