from orchestrator.orchestrator import HybridOrchestrator
from orchestrator.dependency_graph import DependencyGraph


class FakeHistory:
    def read(self):
        return [
            {"agent_id": "A", "event_type": "signal"}
        ]


class FakeWriter:
    def __init__(self):
        self.events = []

    def write(self, e):
        self.events.append(e)


class FakeAgent:
    def emit(self, event):
        return {"ok": True}


class FakeRegistry:
    def get(self, agent_id):
        return FakeAgent()


def test_hybrid_is_deterministic():
    graph = DependencyGraph()
    graph.add_rule(
        trigger_agent="A",
        trigger_event_type="signal",
        target_agent="B"
    )

    writer = FakeWriter()

    orch = HybridOrchestrator(
        history_reader=FakeHistory(),
        executor=__import__("orchestrator.executor").executor.Executor(
            FakeRegistry(), writer
        ),
        dependency_graph=graph,
    )

    orch.run_tick()
    orch.run_tick()

    assert len(writer.events) == 4  # started + completed twice

