class DependencyGraph:
    """
    Declarative dependency graph.

    Defines which agent should run
    when certain events exist in history.
    """

    def __init__(self):
        self._rules = []

    def add_rule(self, *, trigger_agent, trigger_event_type, target_agent):
        self._rules.append({
            "trigger_agent": trigger_agent,
            "trigger_event_type": trigger_event_type,
            "target_agent": target_agent,
        })

    def rules(self):
        return list(self._rules)

