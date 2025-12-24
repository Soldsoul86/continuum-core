from datetime import datetime
from orchestrator.history.in_memory import InMemoryHistory
from orchestrator.history.event import HistoryEvent


def test_history_append_and_read():
    history = InMemoryHistory()

    e1 = HistoryEvent(
        event_id="1",
        agent_id="A",
        event_type="alpha",
        occurred_at=datetime.utcnow(),
        payload={"x": 1},
    )

    e2 = HistoryEvent(
        event_id="2",
        agent_id="B",
        event_type="beta",
        occurred_at=datetime.utcnow(),
        payload={"y": 2},
    )

    history.append(e1)
    history.append(e2)

    all_events = history.read_all()
    assert all_events == [e1, e2]

    since = history.read_since(since_event_id="1")
    assert since == [e2]

