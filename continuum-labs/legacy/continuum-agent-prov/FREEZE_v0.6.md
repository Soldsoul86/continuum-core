# CONTINUUM AGENT — v0.6 FREEZE

Freeze Date: 2025-12-24

---

## Status

Version **v0.6** of the Continuum provenance agent is hereby **frozen**.

This freeze marks the end of foundational architecture changes.
All invariants below are final for the v0.x line.

---

## What Is Frozen

### 1. Non-Intelligence Invariant
- Agents perform no evaluation
- No truth resolution
- No ranking
- No optimization
- No corrective logic

### 2. Vocabulary Invariant
The following concepts are forbidden in code, comments, and docs:
- truth
- resolve
- rank
- optimize
- correct
- best

### 3. Runtime Contract Enforcement
- All engines validate inputs at runtime
- Invalid inputs fail immediately
- Silent coercion is forbidden

### 4. Multi-Agent Isolation
- Agents are isolated by construction
- No shared mutable state
- No direct agent-to-agent access
- Interaction only via external history

### 5. Deterministic Tooling
- `python3 -m pip` only
- `python3 -m pytest` only
- `make test` is canonical
- Repo root contains the Makefile

### 6. Structural Invariants
- All production code lives in Python packages
- Tests import only from packages
- No path manipulation
- No implicit behavior

### 7. Engine Creation Invariant
- Engines are created only via `create_engine.sh`
- Every engine has:
  - CONTRACT.md
  - positive test
  - negative contract test

---

## What Is Explicitly Not Frozen

- New engines
- New agents
- New applications
- New UIs
- New integrations

These MUST NOT violate frozen invariants.

---

## Governance Rule

Any change to the above requires:
- a new version (v0.7+)
- a new freeze document
- explicit justification

Silent mutation is a system failure.

---

## Intent

Continuum v0.6 establishes:
- time without authority
- memory without intelligence
- structure without interpretation

This is the base layer.
Everything else builds on top.

