// Mock API for v0.5 demo

export async function fetchClaims() {
  return [
    {
      claim_id: "claim-1",
      subject: "RBI",
      predicate: "sets",
      object: "repo_rate",
      assertions: [
        { asserted_by: "authority-rbi", asserted_at_day: 1 },
      ],
    },
    {
      claim_id: "claim-2",
      subject: "Analyst",
      predicate: "predicts",
      object: "rate_cut",
      assertions: [
        { asserted_by: "authority-analyst", asserted_at_day: 3 },
      ],
    },
  ];
}

export async function fetchCredibility(asOfDay) {
  if (asOfDay < 4) {
    return {
      "authority-rbi": {
        assertions: 1,
        observed: 1,
        contradicted: 0,
        credibility_score: 1.0,
      },
      "authority-analyst": {
        assertions: 1,
        observed: 0,
        contradicted: 0,
        credibility_score: null,
      },
    };
  }

  return {
    "authority-rbi": {
      assertions: 1,
      observed: 1,
      contradicted: 0,
      credibility_score: 1.0,
    },
    "authority-analyst": {
      assertions: 1,
      observed: 0,
      contradicted: 1,
      credibility_score: 0.0,
    },
  };
}

export async function fetchExplanation({ claims, credibility, asOfDay }) {
  // This simulates an LLM explanation
  return `
Different authorities may disagree for several reasons:

1. Institutional role:
   - RBI makes policy decisions based on macroeconomic data.
   - Analysts make predictions based on expectations and models.

2. Timing:
   - The RBI assertion occurred earlier (day 1).
   - The analyst prediction occurred later (day 3), before outcomes were observed.

3. Evidence availability:
   - At earlier times, outcomes were not yet known.
   - As time progressed, observed outcomes aligned with RBI actions.

This explanation does not determine correctness.
It only describes why multiple views can coexist at time ${asOfDay}.
`;
}

