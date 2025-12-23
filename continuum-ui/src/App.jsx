import { useEffect, useState } from "react";
import "./App.css";

const CORE_EVENTS_ENDPOINT = "http://localhost:8000/events";

function App() {
  const [events, setEvents] = useState([]);

  async function loadEvents() {
    try {
      const res = await fetch(CORE_EVENTS_ENDPOINT);
      const data = await res.json();
      setEvents(data);
    } catch {
      setEvents([]);
    }
  }

  useEffect(() => {
    loadEvents();
    const id = setInterval(loadEvents, 2000);
    return () => clearInterval(id);
  }, []);

  return (
    <div style={{ padding: "16px", fontFamily: "monospace" }}>
      <h1>Continuum v0.1 – UI Observer</h1>

      {events.map((e, i) => (
        <div
          key={i}
          style={{
            borderBottom: "1px solid #333",
            padding: "8px 0",
          }}
        >
          <div style={{ color: "#888" }}>
            {e.timestamp} | {e.agent_id} | {e.event_type}
          </div>
          <pre>{JSON.stringify(e, null, 2)}</pre>
        </div>
      ))}
    </div>
  );
}

export default App;

