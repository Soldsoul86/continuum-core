export default function ClaimsView({ claims }) {
  return (
    <div>
      <h2>Claims</h2>
      {Object.entries(claims).map(([id, events]) => (
        <div key={id} style={{ border: "1px solid #ccc", margin: 10, padding: 10 }}>
          <h4>{id}</h4>
          <pre>{JSON.stringify(events, null, 2)}</pre>
        </div>
      ))}
    </div>
  );
}


