import React from "react";

export default function ExplainerBox({ explanation }) {
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
      <h4>Why do authorities disagree?</h4>

      <p style={{ whiteSpace: "pre


