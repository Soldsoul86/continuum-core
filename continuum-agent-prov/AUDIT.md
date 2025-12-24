# Continuum Agent — Audit & Invariants

## Core Principle

This repository contains a **non-intelligent provenance agent**.

The agent:
- records inputs and outputs
- preserves temporal order
- does not evaluate, rank, or resolve

---

## Intelligence Prohibition Invariant

No code in this repository may:
- resolve correctness
- determine truth
- rank alternatives
- optimize outcomes
- compare competing claims

This applies to:
- executable logic
- helper functions
- comments
- docstrings
- variable names

---

## Vocabulary Invariant

The following vocabulary MUST NOT appear anywhere
in production code or documentation:

truth  
resolve  
rank  
optimize  
best  
correct  

Presence of this vocabulary is considered
an intelligence leak.

---

## Python Packaging Invariant

- All production code MUST live inside a Python package directory
- Tests MUST import only from packages
- No loose `.py` files at repo root
- No `sys.path` manipulation
- No reliance on `PYTHONPATH`

---

## Tooling Invariant

- Never invoke `pip` directly
- Always use: `python3 -m pip`
- Never invoke `pytest` directly
- Always use: `python3 -m pytest`
- `make test` is the canonical execution path

---

## Enforcement

These invariants are enforced via:
- pytest
- Makefile
- CI

Violations MUST fail loudly.
Silence is a bug.

## Multi-Agent Isolation Invariant

- Agents MUST NOT reference each other directly
- No shared mutable state between agents
- Agents MAY interact only via external history
- Registry MAY store agents but MUST NOT broker logic

