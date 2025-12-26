# CONTINUUM — CANONICAL ARCHITECTURE
Version: 1.0 (Frozen)
Status: Constitutional / Immutable

---

## 1. PURPOSE

Continuum is a deterministic epistemic operating system.

It preserves how claims, signals, validations, and authority evolve over time,
without asserting truth, intelligence, or resolution.

The system guarantees replay, auditability, and time-travel by construction.

---

## 2. FOUNDATIONAL AXIOMS (NON-NEGOTIABLE)

These axioms are architectural laws.
Any component violating them is invalid.

1. History is append-only
2. Meaning never mutates history
3. Authority is explicit and recorded
4. Time is first-class
5. Replay is superior to reaction
6. All intelligence is replaceable

---

## 3. LAYERED SYSTEM MODEL (FROZEN)

┌────────────────────────────────────────────┐
│ Epistemic UI (Versioned, Disposable)      │
│  - Timeline                               │
│  - Proposals                              │
│  - Validation                             │
│  - Replay                                 │
├────────────────────────────────────────────┤
│ API Boundary (Stateless, Thin)             │
│  GET  /history?as_of=T                     │
│  POST /proposal                            │
│  POST /validate                            │
│  POST /orchestrate/tick                   │
├────────────────────────────────────────────┤
│ Orchestrator Kernel (v0.7 – Frozen)        │
│  - Deterministic scheduling                │
│  - Time semantics                          │
│  - Payload-blind                           │
├────────────────────────────────────────────┤
│ Agent Layer (v0.6 – Frozen)                │
│  - Isolated agents                         │
│  - Pure functions over history             │
│  - No shared state                         │
├────────────────────────────────────────────┤
│ History Interface (Locked)                 │
│  - HistoryReader                           │
│  - HistoryWriter                           │
│  - Immutable events                        │
├────────────────────────────────────────────┤
│ Persistence Engine (Pluggable)             │
│  SQLite → Postgres → Object Store          │
└────────────────────────────────────────────┘

---

## 4. RESPONSIBILITY BOUNDARIES

Layer        | Allowed                    | Forbidden
-------------|----------------------------|--------------------
UI           | Display, propose, validate | Decide, rank
API          | Transport only             | Logic
Orchestrator | Schedule                   | Interpret
Agents       | Emit signals               | Resolve truth
History      | Store                      | Mutate
Storage      | Persist                    | Reason

---

## 5. EVENT MODEL

{
  "event_id": "uuid",
  "event_type": "agent_emission | proposal | validation | orchestration",
  "source": "agent_id | user_id | ui | orchestrator",
  "timestamp": "ISO-8601",
  "payload": { "opaque": true }
}

---

## 6. REPRODUCIBILITY GUARANTEE

Same history
+ Same orchestrator
+ Same agent versions
= Same outputs

---

## 7. VERSIONING STRATEGY

Hard-frozen:
- History Interface (locked)
- Agent semantics v0.6
- Orchestrator semantics v0.7

Soft-evolving:
- UI versions
- New agents (additive only)
- Models
- Storage backends

Past events are never reinterpreted.

---

## 8. SINGLE-SENTENCE DEFINITION

Continuum is a deterministic epistemic operating system where time is memory,
authority is explicit, and replay is guaranteed.

---

END OF DOCUMENT

