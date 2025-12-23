# Continuum System Audit

This document defines the invariants that must hold true
for all future versions of Continuum.

Any violation INVALIDATES the version.

---

## CORE (continuum-core)

- [ ] Core does NOT rank authorities
- [ ] Core does NOT decide truth
- [ ] Core does NOT learn
- [ ] Core is append-only
- [ ] History is never rewritten

Allowed:
- Storing assertions
- Storing authority metadata
- Storing outcomes
- Deterministic replay

---

## AUTHORITY

- [ ] Multiple authorities may assert the same claim
- [ ] Contradictions are preserved
- [ ] No authority is privileged by default
- [ ] Authority hierarchy is structural only
- [ ] Temporal validity does not imply correctness

---

## AGENT (continuum-agent-prov)

- [ ] Agents compute derived views only
- [ ] Agents never write back to core
- [ ] All agent outputs are rebuildable
- [ ] Credibility ≠ truth
- [ ] Credibility is numeric only

---

## UI (continuum-ui)

- [ ] UI never selects a winner
- [ ] UI never hides disagreement
- [ ] UI filters views, not facts
- [ ] Time slider does not delete history
- [ ] Credibility is shown without judgment

---

## LLM EXPLAINER

- [ ] LLM output is labeled non-authoritative
- [ ] LLM output is ephemeral
- [ ] LLM output is not persisted as truth
- [ ] LLM cannot write to core or agent memory

---

## TIME

- [ ] Past views are reproducible
- [ ] Authority drift is visible
- [ ] No overwrites of historical state

---

If any box is violated, the version must be rejected.

