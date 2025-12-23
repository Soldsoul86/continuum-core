import React from "react";

export default function LLMExplainer({ explanation }) {
  if (!explanation) return null;

  return (
    <div
      style={{
        marginTop: "1.5rem",
        padding: "1rem",
        border: "1px solid #444",
        background: "#111",
        fontSize: "0.9em",
      }}
    >
      <div style={{ fontWeight: "bold", marginBottom: "0.5rem" }}>
        Explanation (non-authoritative)
      </div>

      <div style={{ whiteSpace: "pre-wrap" }}>
        {explanation}
      </div>
    </div>
  );
}


