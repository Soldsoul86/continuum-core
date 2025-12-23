import React from "react";

export default function TimeSlider({ value, min, max, onChange }) {
  return (
    <div style={{ margin: "1rem 0" }}>
      <label style={{ fontWeight: "bold" }}>
        View as of:&nbsp;
      </label>

      <input
        type="range"
        min={min}
        max={max}
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
        style={{ width: "300px", verticalAlign: "middle" }}
      />

      <span style={{ marginLeft: "10px" }}>
        Day {value}
      </span>
    </div>
  );
}

