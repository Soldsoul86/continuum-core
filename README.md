# Continuum

Continuum is a temporal substrate for recording assertions, authority, and outcomes over time — without asserting truth.

It preserves disagreement, tracks authority drift, and exposes how beliefs evolve, without collapsing perspectives into a single answer.

---

## Core Principle (Non-Negotiable)

> Continuum does not decide what is true.  
> It records who said what, when, and under which authority.

Truth, correctness, and judgment are **external** to the system.

---

## Architecture Overview

Continuum is composed of four strictly separated layers:

### 1. Core (Memory)
- Append-only
- Immutable
- No intelligence
- No authority ranking
- No truth evaluation

The core only remembers.

---

### 2. Authority Layer
- Multiple authorities may assert the same claim
- Authorities may contradict each other
- No authority is privileged
- No authority is ranked

Authority is metadata, not logic.

---

### 3. Agent Layer (Derived Views)
- Computes credibility from historical outcomes
- Rebuildable at any time
- Not written back to core
- Produces proposals, not decisions

Agents may be wrong. Core remains right.

---

### 4. UI Layer (Human Lens)
- Filters and visualizes perspectives
- Shows authority drift over time
- Displays credibility numerically
- Never selects a winner

The UI does not tell users what to believe.

---

### 5. LLM Explainer (Commentator)
- Explains why authorities may disagree
- Non-authoritative
- Ephemeral
- Never persisted as truth

LLMs explain — they do not decide.

---

## What Continuum Explicitly Does NOT Do

- No single “best answer”
- No global truth f

