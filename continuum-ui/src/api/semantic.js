export async function loadSemanticData() {
  const res = await fetch("/events.json");
  const events = await res.json();

  const claims = {};
  const actors = {};

  for (const e of events) {
    if (e.claim_id) {
      if (!claims[e.claim_id]) {
        claims[e.claim_id] = [];
      }
      claims[e.claim_id].push(e);
    }

    if (e.actor) {
      if (!actors[e.actor]) {
        actors[e.actor] = [];
      }
      actors[e.actor].push(e);
    }
  }

  return { events, claims, actors };
}

