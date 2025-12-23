import { useEffect, useState } from "react";
import { fetchClaims } from "./api/continuum";
import ClaimCard from "./components/ClaimCard";

export default function App() {
  const [claims, setClaims] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchClaims()
      .then(data => {
        setClaims(data);
        setLoading(false);
      })
      .catch(() => {
        setLoading(false);
      });
  }, []);

  return (
    <div style={{ maxWidth: "800px", margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h2>Continuum — Claim Topology</h2>

      {loading && <div>Loading claims…</div>}

      {!loading && claims.length === 0 && (
        <div style={{ opacity: 0.7 }}>
          No claims found.
        </div>
      )}

      {!loading && claims.map(c => (
        <ClaimCard
          key={c.claim_id}
          claim={{
            id: c.claim_id,
            content: c.content,
            authority: c.authority
          }}
        />
      ))}
    </div>
  );
}
