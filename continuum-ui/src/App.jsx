import { useEffect, useState } from "react";

const CORE_EVENTS_ENDPOINT = "http://localhost:8000/events";
const POLL_INTERVAL_MS = 1000; // 1 second, deterministic

const EVENT_COLORS = {
  proposal: "#3b82f6",
  observation: "#facc15",
  decision: "#8b5cf6",
  outcome: "#22c55e"
};

function App() {
  const [events, setEvents] = useState([]);
  const [replayTime, setReplayTime] = useState(null);

  useEffect(() => {
    let cancelled = false;

    const fetchEvents = async () => {
      try {
        const res = await fetch(CORE_EVENTS_ENDPOINT);
        const data = await res.json();

        if (!cancelled) {
          setEvents(data);
        }
      } catch (err) {
        console.error("Failed to fetch events:", err);
      }
    };

    // Initial fetch
    fetchEvents();

    // Polling loop
    const interval = setInterval(fetchEvents, POLL_INTERVAL_MS);

    return () => {
      cancelled = true;
      clearInterval(interval);
    };
  }, []);

  // Pure temporal truncation — no mutation
  const visibleEvents = replayTime
    ? events.filter(
        (e) => new Date(e.timestamp) <= new Date(replayTime)
      )
    : events;

  return (
    <div style={{ padding: "16px", fontFamily: "monospace" }}>
      <h2>Continuum — Event Timeline</h2>

      <div style={{ marginBottom: "16px" }}>
        <label>
          Replay as of:&nbsp;
          <input
            type="datetime-local"
            onChange={(e) => setReplayTime(e.target.value)}
          />
        </label>
      </div>

      {visibleEvents.map((event, idx) => (
        <div
          key={idx}
          style={{
            borderLeft: `4px solid ${
              EVENT_COLORS[event.event_type] || "#9ca3af"
            }`,
            padding: "8px",
            marginBottom: "10px"
          }}
        >
          <div><strong>type:</strong> {event.event_type}</div>
          <div><strong>actor:</strong> {event.actor}</div>
          <div><strong>time:</strong> {event.timestamp}</div>

          <pre style={{ marginTop: "6px", fontSize: "12px" }}>
            {JSON.stringify(event.payload, null, 2)}
          </pre>
        </div>
      ))}
    </div>
  );
}

export default App;

