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

---

## v0.7 Addendum — Interpreter Hardening (Frozen)

v0.7 introduces **no new epistemic capability**.

The sole change in v0.7 is architectural:

### Canonical Claim Definition

- Claim structure is defined **only** in the claim interpreter
- Downstream agents may consume claims
- No downstream component may invent or infer claim structure

### Removed Patterns (Explicitly Forbidden)

- Adapters that reinterpret raw events at runtime
- Multiple competing claim schemas
- Claim parsing logic outside the interpreter

### Guaranteed Invariants (Carryover)

All v0.6 invariants remain fully in force:

- No truth resolution
- No authority ranking
- No confidence scoring
- No learning
- No memory mutation
- Divergence remains derived-only

v0.7 is therefore a **structural hardening**, not a semantic expansion.

Freeze declaration:
With this addendum, Continuum v0.7 is declared frozen.

Any change that violates this section:
- is not a patch
- is not a minor version
- is a philosophical fork

---

## v0.8 Addendum — Structural Comparison (Paper Freeze Only)

### Status

v0.8 is **paper-frozen**.

No v0.8 code may be written, merged, or deployed until this addendum
is explicitly unfrozen by a future version declaration.

---

### Purpose

v0.8 extends Continuum with **structural comparison** while preserving
all prior epistemic invariants.

v0.8 introduces **no truth**, **no ranking**, and **no belief**.

---

### Core Principle (v0.8)

Continuum constrains **meaning**, not **exploration**.

Users may freely compare, group, export, and interpret data.
Continuum itself must never encode correctness, preference, or trust.

---

### Topics

- Topics may be defined arbitrarily by external actors
- Topic definition is never inferred by Continuum
- Every topic must declare provenance:

```json
"topic_defined_by": "external_identifier"

