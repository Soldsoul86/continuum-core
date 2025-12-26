from orchestrator.context import ExecutionContext


class Scheduler:
    """
    Time-sliced scheduler.

    Evaluates event presence at fixed ticks.
    """

    def __init__(self, history_reader):
        self.history_reader = history_reader

    def tick(self):
        return ExecutionContext.create(reason="time_tick")

