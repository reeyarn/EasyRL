Q: how to understand relationships between the element of XBRL instance, XBRL taxonomy, in terms of relational database. Fact ID -> (Context ID, Fact Value) Am I right? and what else?

A: 

Yes, your intuition is good, but let's make it more complete and accurate.

In XBRL (especially **XBRL 2.1** and **Inline XBRL**), the main logical entities and their relationships can indeed be modeled in a relational way. Below is a simplified yet realistic relational database schema that captures the most important relationships.

### Core XBRL instance entities and their relationships

| Entity / Table                | Primary Key(s)                          | Main Foreign Keys / Relationships                                                                 | Typical columns (examples)                                                                 |
|-------------------------------|-----------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **Fact**                      | factID                                  | → contextID<br>→ conceptID<br>→ unitID (optional)                                                 | factID, contextID, conceptID, unitID, value, decimals, footnotes (optional)               |
| **Context**                   | contextID                               | → entityID<br>→ periodID<br>→ scenarioID (optional)<br>→ identifierScheme                     | contextID, entityID, periodID, scenarioID, identifier, identifierScheme                   |
| **Entity**                    | entityID                                |                                                                                                   | entityID, identifier, identifierScheme (e.g. http://www.sec.gov/edgar)                   |
| **Period**                    | periodID                                |                                                                                                   | periodID, instantDate / startDate / endDate, foreverFlag                                  |
| **Scenario** (optional)       | scenarioID                              |                                                                                                   | scenarioID, segmentContent (XML fragment or normalized tuples)                            |
| **Concept**                   | conceptID (or qname)                    | → taxonomyID (or namespace + localName)                                                           | conceptID, namespace, localName, type, substitutionGroup, periodType, balanceType, ...    |
| **Unit**                      | unitID                                  |                                                                                                   | unitID, measureQNames (e.g. iso4217:USD), divideNumerator, divideDenominator              |
| **Footnote**                  | footnoteID                              | → factID (or link to multiple facts)                                                              | footnoteID, factID(s), footnoteType (factFootnote / footnoteLink), language, text         |
| **Taxonomy / DTS** (optional) | taxonomyID / schemaURI                  |                                                                                                   | schemaURI, namespace, roleTypes, arcroleTypes, label links, reference links, ...          |

### Most important direct relationships (foreign keys)

| From table       | To table       | Relationship name / meaning                                      | Cardinality (typical) |
|------------------|----------------|------------------------------------------------------------------|-----------------------|
| Fact             | Context        | every fact belongs to exactly one context                        | 1 → 1                     |
| Fact             | Concept        | every fact reports exactly one concept                           | many → 1                  |
| Fact             | Unit           | numeric/monetary facts have exactly one unit (optional)          | many → 0..1               |
| Context          | Entity         | every context has exactly one entity                             | many → 1                  |
| Context          | Period         | every context has exactly one period                             | many → 1                  |
| Context          | Scenario       | context may have zero or one scenario                            | many → 0..1               |
| Fact             | Footnote       | a fact can have multiple footnotes                               | 1 → 0..*                  |

### Your original statement

> `Fact ID -> (Context ID, Fact Value)`

**Yes, that's basically correct**, but incomplete.

More precisely:

```sql
Fact(factID, contextID, conceptID, unitID, value, ...)
```

So the minimal required parts of a fact are:

- **factID** (internal identifier)
- **contextID** (tells *who*, *when*, *under what scenario*)
- **conceptID** (what is being reported)
- **value** (the actual number/text)
- **unitID** (if it's a numeric/monetary value)

### Typical simplified relational model (most common in practice)

```sql
-- Core tables
Fact (
  factID         PK,
  conceptQName   NOT NULL,    -- e.g. us-gaap:Assets
  contextID      NOT NULL FK,
  unitID         NULL     FK,
  value          NOT NULL,
  decimals       NULL
)

Context (
  contextID      PK,
  entityID       NOT NULL FK,
  periodID       NOT NULL FK,
  scenarioID     NULL     FK
)

Entity (
  entityID       PK,
  identifier     NOT NULL,    -- e.g. 0000320193
  scheme         NOT NULL     -- e.g. http://www.sec.gov/CIK
)

Period (
  periodID       PK,
  periodType     NOT NULL,    -- instant / duration / forever
  instant        NULL,
  startDate      NULL,
  endDate        NULL
)

Unit (
  unitID         PK,
  unitString     NULL         -- for pure units (iso4217:USD, shares, etc.)
  -- or divideNumerator / divideDenominator for ratio units
)
```

### Summary: What you need at minimum to understand a fact

To fully understand a single fact you need to follow these joins:

```
Fact
  ↓ contextID
Context
  ├─ entityID ──> Entity (who?)
  └─ periodID ──> Period (when?)
      └─ (scenarioID) ──> Scenario (under what assumptions?)
  ↓ conceptQName
Concept (what?)
  ↓ (unitID)
Unit (how is it measured?)
  ↓ value
The actual reported number/text
```

So your initial intuition `Fact ID → (Context ID, Fact Value)` is **correct as a starting point**, but to really understand the meaning of a fact you also need to pull in **Concept** and **Unit**, and then expand the Context into Entity + Period (+ Scenario if present).

Let me know if you'd like the more detailed version (including linkbases, dimensions, tuples, etc.).


Q: In the instance presentation linkbase, label linkbase, calculation linkbase, definition linkbase, and what other linkbases, how does the above relations extend?

In XBRL, the **linkbases** are part of the **Taxonomy** (the DTS — Discoverable Taxonomy Set), not the instance document. They define relationships between concepts (and sometimes between concepts and other resources) that help software interpret, present, validate, and display the facts in the instance.

The relational model we discussed earlier (facts, contexts, concepts, units, etc.) lives in the **instance document**. The linkbases live in the **taxonomy** and provide **additional semantics** that apply to the concepts used in the instance.

Here’s how the main linkbases extend the understanding of the relationships:

| Linkbase Type              | Main Purpose                                                                 | Key Relationships Defined                                                                 | How it extends the relational model                                                                 |
|----------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| **Presentation Linkbase**  | Defines how concepts should be organized and presented in reports (tree/hierarchy) | Parent-child concept relationships (via `presentationArc`)                                 | Adds **display hierarchy** and **order** among concepts (e.g., Assets → CurrentAssets → Cash)       |
| **Label Linkbase**         | Provides human-readable labels for concepts (in different languages, roles)  | Concept → Label (via `labelArc`)                                                           | Adds **human-readable names** (standard, terse, verbose, negated, etc.) and **language support**     |
| **Reference Linkbase**     | Links concepts to authoritative references (GAAP, IFRS standards, etc.)      | Concept → Reference (via `referenceArc`)                                                   | Adds **external documentation** (e.g., FASB ASC 310-10-45-2 for a specific concept)                 |
| **Calculation Linkbase**   | Defines additive relationships between concepts for validation              | Concept A → Concept B (weight +1 or -1) via `calculationArc`                               | Adds **roll-up validation rules** (e.g., TotalAssets = CurrentAssets + NoncurrentAssets)            |
| **Definition Linkbase**    | Defines complex relationships, especially **dimensional** relationships     | Concept → Dimension (via `definitionArc` with arcroles like hypercube, dimension, domain) | Adds **dimensional model** (axes, domains, members) for multidimensional facts                      |

### Additional (less common) linkbases / link types

| Linkbase Type                  | Purpose                                                                 | Key Relationships                                                                 | How it extends the model                                                                 |
|--------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Formula Linkbase**           | Advanced validation and computation rules (XBRL Formula 1.0)            | Concept → Formula (via `formulaArc`)                                              | Adds **computed facts**, **business rules**, **existence checks**, etc.                  |
| **Generic Linkbase**           | Catch-all for custom relationships                                      | Arbitrary arcs between concepts or to resources                                   | Allows **custom semantics** not covered by standard linkbases                            |
| **Inline XBRL-specific**       | Inline XBRL uses embedded linkbases in HTML                             | Same as above, but embedded in `<link:linkbase>` tags inside HTML                 | No new relationships — just a different delivery format                                  |

### How these linkbases relate to the instance facts (relational view)

The **instance facts** reference **concepts** by their **qname** (e.g., `us-gaap:Assets`).

The linkbases add **metadata** to those concepts:

| Entity in instance | Linkbase that adds information | What it tells you about the fact |
|--------------------|--------------------------------|-----------------------------------|
| Fact → Concept     | Presentation Linkbase          | Where this concept should appear in a table/tree (position, order, indentation) |
| Fact → Concept     | Label Linkbase                 | What label to show instead of the technical qname (e.g., "Total Assets") |
| Fact → Concept     | Reference Linkbase             | Which accounting standard/paragraph defines this line item |
| Fact → Concept     | Calculation Linkbase           | Whether this fact should be checked against other facts (e.g., must sum to parent) |
| Fact → Concept     | Definition Linkbase            | Whether this concept is a dimension member, hypercube, domain, etc. (affects how contexts are built) |

### Example: How a single fact is enriched by linkbases

Suppose a fact is:

```xml
<us-gaap:Assets contextRef="c1" unitRef="u1">1000000</us-gaap:Assets>
```

The **instance** gives you:

- Value = 1,000,000
- Context = c1 (who, when)
- Unit = u1 (USD)

The **taxonomy linkbases** add:

| Linkbase              | Adds to understanding                                                                 |
|-----------------------|---------------------------------------------------------------------------------------|
| Label                 | Display as "Assets" or "Total Assets" (depending on role)                             |
| Presentation          | Show under "Balance Sheet" → "Assets" → "Current Assets" → "Cash and Cash Equivalents" |
| Calculation           | Must equal sum of its children (e.g., CurrentAssets + NoncurrentAssets)               |
| Reference             | Based on ASC 210-10-45-1 or IFRS IAS 1.54                                            |
| Definition (if dimensional) | May belong to a hypercube "Balance Sheet" with dimensions like "ClassOfDebt"          |

### Summary: Extended relational model with linkbases

| Core instance entity | Extended by linkbase(s)                              | Resulting meaning added to the fact |
|----------------------|------------------------------------------------------|-------------------------------------|
| Fact → Concept       | Presentation + Label + Reference                     | How to display, label, and document it |
| Fact → Concept       | Calculation                                          | Validation (sums, roll-ups)         |
| Fact → Concept       | Definition                                           | Dimensional structure (axes, members) |
| Fact → Concept       | Formula (advanced)                                   | Complex business rules              |

So the **core instance relations** (facts, contexts, concepts) are **static** — they describe the data.

The **linkbases** are **metadata** that **enrich** and **constrain** the interpretation and validation of those facts.

If you want to model this in a relational database, you would typically have:

- **Instance tables** (facts, contexts, units, etc.) — the data
- **Taxonomy tables** (concepts, linkbase arcs, labels, references, etc.) — the metadata/rules

Let me know if you want a sample schema that combines both!