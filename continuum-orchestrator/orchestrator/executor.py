class Executor:
    """
    Executes agents in isolation.

    Executor:
    - does not inspect outputs
    - does not suppress results
    - only invokes
    """

    def __init__(self, agent_registry, history_writer):
        self.agent_registry = agent_registry
        self.history_writer = history_writer

    def execute(self, *, agent_id, context):
        agent = self.agent_registry.get(agent_id)

        self.history_writer.write({
            "event_type": "execution_started",
            "agent_id": agent_id,
            "execution_id": context.execution_id,
            "orchestration_id": context.orchestration_id,
        })

        result = agent.emit(event={})

        self.history_writer.write({
            "event_type": "execution_completed",
            "agent_id": agent_id,
            "execution_id": context.execution_id,
            "orchestration_id": context.orchestration_id,
            "result": result,
        })

