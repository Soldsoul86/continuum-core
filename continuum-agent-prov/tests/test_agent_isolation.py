import pytest
from continuum_agent.agent_registry import AgentRegistry
from continuum_agent.agent import Agent


def test_agents_are_isolated():
    registry = AgentRegistry()

    a1 = Agent(agent_id="a1")
    a2 = Agent(agent_id="a2")

    registry.register("a1", a1)
    registry.register("a2", a2)

    assert registry.get("a1") is a1
    assert registry.get("a2") is a2
    assert registry.get("a1") is not registry.get("a2")


def test_duplicate_agent_id_is_rejected():
    registry = AgentRegistry()
    registry.register("a1", Agent(agent_id="a1"))

    with pytest.raises(ValueError):
        registry.register("a1", Agent(agent_id="a1"))

