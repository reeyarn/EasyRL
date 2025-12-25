### Understanding the Statement of Cash Flows (SCF) Linkbase Files in the 2020 US GAAP XBRL Taxonomy

These files are part of the **US GAAP Financial Reporting Taxonomy (2020 release)** published by the FASB. They define different **presentation roles** (views or templates) for the **Statement of Cash Flows** (SCF). 

In XBRL taxonomies, financial statements like the SCF are modeled using multiple "roles" to support varying reporting practices. Each role has its own entry point schema (`.xsd`) and associated linkbases (`-pre.xml` for presentation, `-cal.xml` for calculation, `-def.xml` for definition/dimensional disaggregations). This allows companies to choose the role that matches their presentation while using standardized elements.

The SCF is unique because US GAAP allows **two primary methods** for presenting operating activities:
- **Indirect method** (most common): Starts with net income and adjusts for non-cash items/changes in working capital.
- **Direct method** (encouraged by FASB but rarely used): Reports gross cash receipts and payments from operating activities.

The taxonomy provides separate structures for these, plus supplemental disclosures and specialized views.

#### Breakdown of the File Groups

| File Prefix          | Meaning / Role Description                                                                 | Linkbases Included                                                                 | Purpose / Key Features |
|----------------------|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|-----------------------|
| **dir**             | **Direct Method** (full statement using direct method for operating activities)           | .xsd (entry), -cal, -def, -pre                                                    | Models the entire SCF with direct operating cash flows (e.g., cash received from customers, cash paid to suppliers). Includes investing/financing as usual. |
| **indir**           | **Indirect Method** (standard full statement using indirect method for operating activities) | .xsd (entry), -cal, -def, -pre                                                    | Most commonly used role. Starts operating section with net income, then adjustments (e.g., + depreciation, - increase in receivables). |
| **indira**          | **Indirect Method, Alternative** (variant of indirect, possibly with different ordering or additional reconciliations) | .xsd (entry), -pre (no cal/def in your list)                                       | A secondary/alternative layout for indirect method presentations. |
| **inv**             | **Investing Activities** (focused on investing section, often supplemental)               | .xsd (entry), -cal, -def, -pre                                                    | Detailed hierarchy for investing cash flows (e.g., purchases/sales of PPE, acquisitions). Used in disaggregated views. |
| **dbo**             | **Disclosure By Operating** (detailed breakdowns/disclosures specific to operating activities) | .xsd (entry), -cal, -def, -pre                                                    | Supports extended disclosures for operating cash flows (e.g., breakdowns used in direct method or supplemental to indirect). |
| **re**              | **Reconciliation** (likely the reconciliation of net income to operating cash flows, or supplemental schedules) | .xsd (entry), -def, -pre (no cal)                                                 | Focuses on the indirect method reconciliation section. |
| **sbo**             | **Supplemental By Operating** (supplemental disclosures by operating activity type)       | .xsd (entry), -def, -pre (no cal)                                                 | Additional non-mandatory breakdowns for operating cash flows. |
| **sd**              | **Supplemental Disclosures** (general supplemental cash flow disclosures)                 | .xsd (entry), -def, -pre (no cal)                                                 | Covers other SCF notes/disclosures (e.g., non-cash transactions, restricted cash). |

#### Key Notes on Usage and Processing
- **Entry point schemas** (`.xsd` files like `us-gaap-stm-scf-dir-2020-01-31.xsd`): These are the starting points for a specific "view" of the SCF. They import core elements and reference the role-specific linkbases.
- **Presentation linkbases** (`-pre.xml`): Define the human-readable hierarchy (parent-child order, like sections: Operating > Investing > Financing).
- **Calculation linkbases** (`-cal.xml`): Define summation relationships (e.g., Net Cash from Operating + Investing + Financing = Change in Cash).
- **Definition linkbases** (`-def.xml`): Model dimensional tables/disaggregations (e.g., cash flows by segment or type).
- Not all roles have all linkbases (e.g., some supplemental ones lack calculation because they aren't summative).
- Abstracts are prevalent here too (e.g., `NetCashProvidedByUsedInOperatingActivitiesAbstract`) for grouping sections.
- In practice: Most filings use the **indirect** role (`indir`). Direct method filers would use `dir`. Others are for detailed disclosures.

When processing these for core SCF accounts (e.g., Depreciation, ChangesInWorkingCapital), look across roles—especially `indir` for standard industrial firms—but filter to concrete elements and use presentation linkbases for hierarchies.

This modular design ensures the taxonomy supports diverse SCF presentations while maintaining data comparability. If you're extracting hierarchies, start with the `-pre.xml` files in the primary roles (`indir` or `dir`).