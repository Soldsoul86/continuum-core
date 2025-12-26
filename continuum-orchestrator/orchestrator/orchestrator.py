from orchestrator.scheduler import Scheduler
from orchestrator.context import ExecutionContext


class HybridOrchestrator:
    """
    Hybrid orchestrator:
    - time-driven
    - event-filtered
    - deterministic
    """

    def __init__(self, *, history_reader, executor, dependency_graph):
        self.history_reader = history_reader
        self.executor = executor
        self.dependency_graph = dependency_graph
        self.scheduler = Scheduler(history_reader)

    def run_tick(self):
        context = self.scheduler.tick()
        history = self.history_reader.read()

        for rule in self.dependency_graph.rules():
            exists = any(
                e["agent_id"] == rule["trigger_agent"] and
                e["event_type"] == rule["trigger_event_type"]
                for e in history
            )

            if exists:
                self.executor.execute(
                    agent_id=rule["target_agent"],
                    context=context
                )

