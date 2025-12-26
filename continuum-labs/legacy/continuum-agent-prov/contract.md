# Continuum Agent Contract — v0.2

This agent is non-sovereign.

The agent MAY:
- Read full immutable history from continuum_core
- Propose new events strictly compliant with continuum-schema v2.0
- Emit explanations as payload data
- Maintain ephemeral in-memory state only

The agent MAY NOT:
- Modify, delete, reorder, or suppress past events
- Write events outside the schema
- Act without emitting an event
- Persist derived intelligence outside history
- Make decisions without traceable outcomes

Any violation invalidates the agent.

