export async function fetchClaims() {
  const res = await fetch("http://localhost:8000/claims");
  return res.json();
}

export async function fetchClaimTopology(claimId) {
  const res = await fetch(`http://localhost:8000/claim/${claimId}/topology`);
  return res.json();
}
