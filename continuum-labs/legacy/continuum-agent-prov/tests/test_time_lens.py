from event_writer import emit_event


def test_emitted_events_are_immutable_snapshots():
    event1 = emit_event(
        actor="Authority-A",
        event_type="claim",
        payload={"content": "Rate is 10%"}
    )

    event2 = emit_event(
        actor="Authority-B",
        event_type="claim",
        payload={"content": "Rate is 12%"}
    )

    # Events must be independent snapshots
    assert event1 is not event2

    # Original payload must remain unchanged
    assert event1["payload"]["content"] == "Rate is 10%"
    assert event2["payload"]["content"] == "Rate is 12%"

    # Event metadata must not overlap
    assert event1["event_id"] != event2["event_id"]
    assert event1["timestamp"] != event2["timestamp"]

