Q: Help me understand these XBRL US-GAAP taxonomy XML files. I want to know the `soi` (statement of income) files; I know `pre` stands for presentation linkbase and `cal` stand for caculation linkbase, `def` is definition linkbase; how about egm indira int re reit sbi? are they industry specific? To what extent are XBRL taxonomy industry specific? 

``` shell
ls -R |grep soi    
us-gaap-stm-soi-2020-01-31.xsd
us-gaap-stm-soi-cal-2020-01-31.xml
us-gaap-stm-soi-def-2020-01-31.xml
us-gaap-stm-soi-egm-2020-01-31.xsd
us-gaap-stm-soi-egm-def-2020-01-31.xml
us-gaap-stm-soi-egm-pre-2020-01-31.xml
us-gaap-stm-soi-indira-2020-01-31.xsd
us-gaap-stm-soi-indira-pre-2020-01-31.xml
us-gaap-stm-soi-ins-2020-01-31.xsd
us-gaap-stm-soi-ins-def-2020-01-31.xml
us-gaap-stm-soi-ins-pre-2020-01-31.xml
us-gaap-stm-soi-int-2020-01-31.xsd
us-gaap-stm-soi-int-def-2020-01-31.xml
us-gaap-stm-soi-int-pre-2020-01-31.xml
us-gaap-stm-soi-pre-2020-01-31.xml
us-gaap-stm-soi-re-2020-01-31.xsd
us-gaap-stm-soi-re-def-2020-01-31.xml
us-gaap-stm-soi-re-pre-2020-01-31.xml
us-gaap-stm-soi-reit-2020-01-31.xsd
us-gaap-stm-soi-reit-def-2020-01-31.xml
us-gaap-stm-soi-reit-pre-2020-01-31.xml
us-gaap-stm-soi-sbi-2020-01-31.xsd
us-gaap-stm-soi-sbi-def-2020-01-31.xml
us-gaap-stm-soi-sbi-pre-2020-01-31.xml
us-gaap-stm-soi1-cal-2020-01-31.xml
us-gaap-stm-soi4-cal-2020-01-31.xml
```

A: Those abbreviations identify **industry-specific "entry points"** within the US GAAP taxonomy.

In the XBRL world, a "Statement of Income" () for a regular tech company looks very different from one for a bank or an insurance company. Instead of having one massive, messy file for everyone, the FASB (Financial Accounting Standards Board) breaks them into industry-specific schemas.

### Meaning of the Abbreviations

Here is the breakdown of the specific codes in your file list:

| Abbreviation | Industry / Meaning | Description |
| --- | --- | --- |
| **egm** | **Equity Method** | Extractive industries (e.g., Energy, Gas, Mining) or similar specialized groupings  |
| **indira** | **Alternative Aggregations** | The "catch-all" for companies that don't fit the standard industry buckets but still don't follow the "standard" income statement layout. |
| **ins** | **Insurance** | Specific to Insurance companies (e.g., premiums, claims). |
| **int** | **Interest-based** | Financial institutions where "Interest Income" is the primary top-line. |
| **re** | **Real Estate** | Standard Real Estate operations. |
| **reit** | **REITs** | Real Estate Investment Trusts (adds specific metrics like FFO). |
| **sbi** | **Securities Broker-Intermediary** | Specifically for Broker-Dealers and financial intermediaries. |

---

### To What Extent is the Taxonomy Industry-Specific?

The US-GAAP taxonomy is **modular**. It uses a "base" set of concepts that everyone uses (like *Assets* or *Net Income*) but adds specialized layers:

1. **Core Concepts:** About 80% of the taxonomy is shared. Every company uses the same tag for `CashAndCashEquivalentsAtCarryingValue`.
2. **Industry Entry Points:** When a filer (a company) creates their XBRL report, they "import" one of these entry points. An insurance company will import the `ins` files to get access to tags like `PolicyholderDividends`, which a retail company would never see.
3. **Calculation & Presentation Differences:** Even if two industries use the same tag, they might "calculate" it differently. For example, a bank's "Operating Income" calculation ( file) includes interest expense, while a manufacturing company's does not.

### Why so many files?

You see three main types for each industry in your `ls` output:

* **.xsd (Schema):** The "dictionary" that defines which tags are allowed for that industry.
* **-pre.xml (Presentation):** Defines the **order** and hierarchy of how the statement should look on a screen.
* **-def.xml (Definition):** Defines the **relationships** (e.g., "This tag is a subset of that tag").
* **-cal.xml (Calculation):** Defines the **math** (e.g., ).

> **Note:** If you see `soi1` or `soi4` (like at the bottom of your list), these usually refer to specific "Statement of Income" variations, such as a **Single-Step** vs. **Multi-Step** income statement.

