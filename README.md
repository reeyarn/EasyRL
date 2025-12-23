# EasyRL
 Easy (non-XML) approach to process XBRL

A lightweight, memory-efficient, and fast Python library for extracting specific information from XBRL filings and taxonomies — **without loading the entire DTS (Discovery Tree)**.

## Motivation

XBRL is powerful but **complex**:
- A single filing includes the instance document, company linkbases, and a huge taxonomy (hundreds of XML files)
- Traditional XBRL processors load the full DTS into memory: slow and memory-intensive
- In many real-world scenarios (data extraction, analysis, reporting), you only need a small subset of the data


**EasyRL** takes a **pragmatic, non-strict** approach:
- Process **one file at a time** (no full DTS loading)
- Extract only what you need into simple Python structures (`dict`, `list`, `pandas.DataFrame`)
- Forget strict XBRL validation and complex object models — focus on **speed and simplicity**
- We do an non-XBRL and non-XML way. Forget about all XML files linked together. Just one at a time. Process as needed, and extract the information to simple python data structure `dict` or **relational-database** with `pandas` DataFrame.

## Features (Planned)

- Extract facts from instance documents (simple alternative to `brel`, `python-xbrl`, etc.)
- Parse **presentation linkbases** (build hierarchical trees, tables, roll-forwards)
- Parse **calculation linkbases** (extract summation rules)
- Parse **definition linkbases** (dimensions, tables, axes)
- Parse **label linkbases** (English/translated labels)
- Parse **taxonomy schema files** (elements, types, from `elts/`, `dis/`, `stm/`)
- Convert XBRL structures to **pandas DataFrames** or **nested dictionaries**
- Support for both **company filings** and **raw US GAAP/SIFMA/IFRS taxonomies**