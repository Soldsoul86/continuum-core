class IsolatedAgent:
    """
    Base class for isolated agents.

    Rules:
    - No references to other agents
    - No shared mutable state
    - Interaction only via external history
    """

    def __init__(self, agent_id: str):
        self.agent_id = agent_id

    def emit(self, event):
        return {
            "agent_id": self.agent_id,
            "event": event,
        }

