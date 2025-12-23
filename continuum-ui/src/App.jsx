import { useEffect, useState } from "react";
import AuthoritySelector from "./components/AuthoritySelector";
import AuthorityCredibility from "./components/AuthorityCredibility";
import TimeSlider from "./components/TimeSlider";
import LLMExplainer from "./components/LLMExplainer";
import {
  fetchClaims,
  fetchCredibility,
  fetchExplanation,
} from "./api/continuum";

function App() {
  const [claims, setClaims] = useState([]);
  const [credibility, setCredibility] = useState({});
  const [explanation, setExplanation] = useState("");
  const [selectedAuthority, setSelectedAuthority] = useState(null);
  const [day, setDay] = useState(1);

  useEffect(() => {
    fetchClaims().then(setClaims);
  }, []);

  useEffect(() => {
    fetchCredibility(day).then(setCredibility);
  }, [day]);

  useEffect(() => {
    fetchExplanation({ claims, credibility, asOfDay: day })
      .then(setExplanation);
  }, [claims, credibility, day]);

  const authorities = Array.from(
    new Map(
      claims
        .flatMap((c) => c.assertions || [])
        .map((a) => [
          a.asserted_by,
          { authority_id: a.asserted_by, label: a.asserted_by },
        ])
    ).values()
  );

  const visibleClaims = selectedAuthority
    ? claims.filter((c) =>
        (c.assertions || []).some(
          (a) => a.asserted_by === selectedAuthority
        )
      )
    : claims;

  return (
    <div style={{ padding: "1.5rem", fontFamily: "sans-serif" }}>
      <h2>Continuum — Authority View</h2>

      <TimeSlider min={1} max={5} value={day} onChange={setDay} />

      <AuthoritySelector
        authorities={authorities}
        selectedAuthority={selectedAuthority}
        onChange={setSelectedAuthority}
      />

      <ul>
        {visibleClaims.map((c) => (
          <li key={c.claim_id} style={{ marginBottom: "1rem" }}>
            <strong>{c.subject}</strong> {c.predicate}{" "}
            <strong>{c.object}</strong>
            <ul>
              {(c.assertions || []).map((a, i) => (
                <li key={i} style={{ fontSize: "0.85em" }}>
                  asserted by: {a.asserted_by} (day {a.asserted_at_day})
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>

      <AuthorityCredibility data={credibility} />
      <LLMExplainer explanation={explanation} />
    </div>
  );
}

export default App;

