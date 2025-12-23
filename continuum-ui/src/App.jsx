import { useEffect, useState } from "react";
import { loadSemanticData } from "./api/semantic";
import ClaimsView from "./views/ClaimsView";
import ActorsView from "./views/ActorsView";

export default function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    loadSemanticData().then(setData);
  }, []);

  if (!data) {
    return <div>Loading…</div>;
  }

  return (
    <div>
      <h1>Continuum v0.3 — Semantic Accountability</h1>
      <ClaimsView claims={data.claims} />
      <ActorsView actors={data.actors} />
    </div>
  );
}

