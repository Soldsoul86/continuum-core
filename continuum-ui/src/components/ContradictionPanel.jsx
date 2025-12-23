export default function ContradictionPanel({ incoming, outgoing }) {
  return (
    <div style={{ marginTop: "1rem", padding: "0.75rem", border: "1px solid #ddd" }}>
      <h4>Contradictions</h4>

      <div>
        <strong>Incoming</strong>
        {incoming.length === 0 ? (
          <div style={{ fontSize: "0.9em", opacity: 0.6 }}>None</div>
        ) : (
          <ul>
            {incoming.map(edge => (
              <li key={edge.edge_id}>
                {edge.relation_type} by {edge.from_claim}
                {" "}({edge.dimension})
              </li>
            ))}
          </ul>
        )}
      </div>

      <div style={{ marginTop: "0.5rem" }}>
        <strong>Outgoing</strong>
        {outgoing.length === 0 ? (
          <div style={{ fontSize: "0.9em", opacity: 0.6 }}>None</div>
        ) : (
          <ul>
            {outgoing.map(edge => (
              <li key={edge.edge_id}>
                {edge.relation_type} → {edge.to_claim}
                {" "}({edge.dimension})
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
