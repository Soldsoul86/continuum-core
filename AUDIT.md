# CONTINUUM — AUDIT & INVARIANTS

This document defines **non-negotiable invariants** of the Continuum system.
Any change that violates these invariants is **out of scope** and requires
a **major version reset**, not a patch.

This file is binding.

---

## Core Principle (Frozen)

Continuum is **not an AI system**.

It is a **temporal memory substrate** that records:

- who asserted what
- under which authority
- at what time
- and what outcomes were later observed

Continuum does **not**:
- decide truth
- resolve disagreement
- rank authorities
- learn or optimize

Truth is external.

---

## Core Invariants (All Versions)

### 1. Core Is Non-Intelligent

- Core stores events immutably
- Core performs no inference
- Core performs no aggregation
- Core never deletes or rewrites history

---

### 2. Agents Are Derived and Discardable

- Agents may compute views
- All agent outputs are rebuildable
- Agents may never write back into core

---

### 3. UI Is Non-Authoritative

- UI may visualize disagreement
- UI may never hide disagreement
- UI may never select a “winner”

---

### 4. LLMs Are Commentators Only

- LLMs may explain
- LLMs may summarize
- LLMs may never decide
- LLMs may never persist memory

---

## v0.6-Specific Guarantees (Frozen)

### 5. Disagreement Is First-Class

- Multiple incompatible assertions may coexist
- Disagreement is not an error condition
- Disagreement is preserved across time

---

### 6. Divergence Is Derived, Not Stored

- Divergence is computed from claims
- Divergence is never written to core
- Divergence is fully rebuildable

---

### 7. Divergence Has No Magnitude

- Divergence is structural only
- No scores
- No confidence values
- No severity levels

Allowed output:
```json
"divergent": true | false

