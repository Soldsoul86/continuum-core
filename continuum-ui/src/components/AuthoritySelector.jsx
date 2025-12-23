import React from "react";

export default function AuthoritySelector({
  authorities,
  selectedAuthority,
  onChange,
}) {
  return (
    <div style={{ marginBottom: "1rem" }}>
      <label style={{ fontWeight: "bold" }}>
        Authority view:&nbsp;
      </label>

      <select
        value={selectedAuthority || ""}
        onChange={(e) => onChange(e.target.value)}
      >
        <option value="">All authorities</option>

        {authorities.map((a) => (
          <option key={a.authority_id} value={a.authority_id}>
            {a.label}
          </option>
        ))}
      </select>
    </div>
  );
}

