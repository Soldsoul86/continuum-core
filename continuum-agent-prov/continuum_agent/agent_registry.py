class AgentRegistry:
    """
    Registry for isolated agents.

    - Agents are registered by ID
    - No agent can access another agent directly
    - Registry does not broker intelligence
    """

    def __init__(self):
        self._agents = {}

    def register(self, agent_id: str, agent):
        if agent_id in self._agents:
            raise ValueError(f"Agent already registered: {agent_id}")
        self._agents[agent_id] = agent

    def get(self, agent_id: str):
        if agent_id not in self._agents:
            raise KeyError(f"Unknown agent: {agent_id}")
        return self._agents[agent_id]

    def list_ids(self):
        return list(self._agents.keys())

