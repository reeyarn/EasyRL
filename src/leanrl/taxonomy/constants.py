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
