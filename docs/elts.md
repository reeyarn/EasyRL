The files in the `elts` (Elements) folder are the "Global Brain" of the taxonomy. While the `stm` (Statement) files you looked at earlier define how to build a specific report (like an Income Statement), the `elts` files define the **meaning, rules, and logic** of the individual tags themselves.

Here is the breakdown of what these specific files do:

### 1. The "Human and Legal Meaning" Files

These files provide the context for what a tag actually represents.

* **`us-gaap-lab-2020-01-31.xml` (Labels):** * This is the "dictionary." It maps the computer-readable tag (e.g., `CashAndCashEquivalentsAtCarryingValue`) to a human-readable label ("Cash and Cash Equivalents"). It contains different label roles, such as "Standard Label," "Terse Label," and "Total Label."
* **`us-gaap-doc-2020-01-31.xml` (Documentation):** * This contains the **definitions**. If you want to know exactly what the FASB means by a specific tag, this file contains the long-form text explanation for every element in the taxonomy.
* **`us-gaap-ref-2020-01-31.xml` (References):** * This links the XBRL tags to the actual **Accounting Standards Codification (ASC)**. It tells you which part of the law (e.g., ASC 606 for Revenue) requires or defines that specific tag.
* **`us-gaap-cn-ref-2020-01-31.xml` (Change Notes References):** * The "cn" stands for **Change Notes**. This file tracks which references or elements were modified, added, or deprecated in the 2020 version compared to previous years.

---

### 2. The "Dimensional and Technical Logic" Files

The `depcon`, `eedm`, and `tin` files are highly technical. They manage how data is "sliced and diced" across the taxonomy.

#### **`depcon` (Deprecated Concepts)**

* **`us-gaap-depcon-def-2020-01-31.xml`**
* **`us-gaap-depcon-pre-2020-01-31.xml`**
* **What it is:** When the FASB retires a tag (because the accounting law changed), they don't just delete it; they move it to "Deprecated Concepts." These files define the relationship between the **old, retired tag** and the **new, replacement tag**. This allows software to understand older filings.

#### **`eedm` (Equity Elimination and Disclosure Members)**

* **`us-gaap-eedm-def-2020-01-31.xml`**
* **What it is:** This handles the logic for **Consolidation**. When a parent company owns a subsidiary, they have to "eliminate" internal transactions so they aren't counted twice. `eedm` provides the "members" (dimensions) used to flag these eliminations in a digital filing.

#### **`tin` (Tax Information)**

* **`us-gaap-tin-def-2020-01-31.xml`**
* **`us-gaap-tin-ref-2020-01-31.xml`**
* **What it is:** This stands for **Tax Information**. These files contain the specialized elements and references for **Income Tax disclosures** (ASC 740). It includes the logic for things like "Deferred Tax Assets," "Tax Carryforwards," and the reconciliation between the statutory tax rate and the effective tax rate.

---

### Summary Table for your Notes

| Suffix/Code | Full Name | Purpose |
| --- | --- | --- |
| **lab** | Label | Human-readable names for tags. |
| **doc** | Documentation | Detailed accounting definitions of tags. |
| **ref** | Reference | Links tags to official GAAP law (ASC). |
| **cn-ref** | Change Note Ref | History of what changed in this year's taxonomy. |
| **depcon** | Deprecated Concepts | Mapping "dead" tags to their new replacements. |
| **eedm** | Equity Elimination | Logic for consolidating parent/subsidiary financials. |
| **tin** | Tax Information | Elements specifically for Income Tax reporting. |

### Why is this important for you?

If you are writing a script to extract data:

1. **To get the name of a value:** Look in `us-gaap-lab`.
2. **To understand what a value means:** Look in `us-gaap-doc`.
3. **To see why a value is required:** Look in `us-gaap-ref`.
4. **To handle old data:** You must use `us-gaap-depcon` to map old tags to new ones so your database doesn't break when a tag name changes.