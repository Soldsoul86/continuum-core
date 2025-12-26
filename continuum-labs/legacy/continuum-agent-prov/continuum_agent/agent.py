from continuum_agent.isolated_agent import IsolatedAgent


class Agent(IsolatedAgent):
    """
    Continuum provenance agent.

    Isolated.
    No authority.
    No evaluation.
    """

    def __init__(self, agent_id: str):
        super().__init__(agent_id)

