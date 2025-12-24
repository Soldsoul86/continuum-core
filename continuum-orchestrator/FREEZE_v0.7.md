# CONTINUUM ORCHESTRATOR — v0.7 FREEZE

Freeze Date: 2025-12-24

---

## Status

Version **v0.7** of the Continuum Orchestrator is hereby **frozen**.

This version defines the orchestration semantics that sit
above the Continuum Agent v0.6 substrate.

All invariants below are final for the v0.7 line.

---

## Role of the Orchestrator

The orchestrator exists to determine:

- **when** agents are invoked
- **with what historical context**
- **under what execution metadata**

The orchestrator does **not** determine correctness,
priority, quality, or meaning of agent outputs.

---

## Hybrid Orchestration Model (Frozen)

The v0.7 orchestrator implements a **hybrid model**:

- **Time-sliced evaluation**
- **Event-existence filtering**

This model is constrained as follows.

---

## Frozen Invariants

### 1. Time Boundary Invariant
- Orchestration occurs only at fixed time boundaries
- No immediate reaction to events is permitted
- Time moves monotonically forward

### 2. Event Existence Invariant
- Events may trigger execution only by **existence**
- Matching is allowed only on:
  - `agent_id`
  - `event_type`
- Event payloads are opaque and forbidden from inspection

### 3. Payload Blindness Invariant
- Orchestrator MUST NOT read, parse, inspect, or interpret payloads
- Payloads are treated as uninterpreted data blobs

### 4. No Resolution Invariant
- Orchestrator MUST NOT:
  - resolve conflicts
  - rank agents
  - suppress outputs
  - merge results
  - infer correctness

All outputs are written as-is into history.

### 5. Determinism Invariant
- Given identical history and identical rules,
  orchestration MUST produce identical execution graphs
- No randomness
- No wall-clock dependence beyond declared time ticks

### 6. Replay Invariant
- Full history replay MUST reproduce the same orchestration behavior
- Orchestrator state MUST be derivable entirely from history

### 7. Execution Lineage Invariant
- Each orchestration run has:
  - orchestration_id
  - execution_id
  - trigger reason
- Agents MUST NOT be triggered by events emitted under the same execution_id

### 8. Isolation Invariant
- Orchestrator does not hold agent logic
- Orchestrator does not share agent state
- Agents remain isolated as defined in Continuum Agent v0.6

---

## What Is Explicitly Not Frozen

- New orchestration rules
- New agents
- New domains
- New terminals or UIs
- New history backends

Thes

