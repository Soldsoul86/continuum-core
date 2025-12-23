export default function ActorsView({ actors }) {
  return (
    <div>
      <h2>Actors</h2>
      {Object.entries(actors).map(([actor, events]) => (
        <div key={actor} style={{ border: "1px solid #ccc", margin: 10, padding: 10 }}>
          <h4>{actor}</h4>
          <pre>{JSON.stringify(events, null, 2)}</pre>
        </div>
      ))}
    </div>
  );
}


