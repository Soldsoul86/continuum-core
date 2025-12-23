import React from "react";

export default function AuthorityCredibility({ data }) {
  if (!data || Object.keys(data).length === 0) {
    return null;
  }

  return (
    <div style={{ marginTop: "1.5rem" }}>
      <h4>Authority credibility (derived)</h4>

      <table
        style={{
          borderCollapse: "collapse",
          fontSize: "0.9em",
        }}
      >
        <thead>
          <tr>
            <th style={th}>Authority</th>
            <th style={th}>Assertions</th>
            <th style={th}>Observed</th>
            <th style={th}>Contradicted</th>
            <th style={th}>Credibility</th>
          </tr>
        </thead>

        <tbody>
          {Object.entries(data).map(([id, s]) => (
            <tr key={id}>
              <td style={td}>{id}</td>
              <td style={td}>{s.assertions}</td>
              <td style={td}>{s.observed}</td>
              <td style={td}>{s.contradicted}</td>
              <td style={td}>
                {s.credibility_score === null
                  ? "—"
                  : s.credibility_score.toFixed(2)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const th = {
  borderBottom: "1px solid #444",
  padding: "4px 8px",
  textAlign: "left",
};

const td = {
  padding: "4px 8px",
};

