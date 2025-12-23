import { useEffect, useState } from "react";
import { fetchClaimTopology } from "../api/continuum";
import ContradictionPanel from "./ContradictionPanel";

export default function ClaimCard({ claim }) {
  const [topology, setTopology] = useState(null);

  useEffect(() => {
    fetchClaimTopology(claim.id).then(setTopology);
  }, [claim.id]);

  return (
    <div style={{ border: "1px solid #ccc", padding: "1rem", marginBottom: "1rem" }}>
      <div style={{ fontWeight: "bold" }}>{claim.content}</div>
      <div style={{ fontSize: "0.85em", opacity: 0.7 }}>
        Authority: {claim.authority}
      </div>

      {topology && (
        <ContradictionPanel
          incoming={topology.incoming_contradictions}
          outgoing={topology.outgoing_contradictions}
        />
      )}
    </div>
  );
}
