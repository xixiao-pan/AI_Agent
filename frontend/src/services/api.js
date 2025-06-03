const BASE = "http://localhost:8000";

export async function generateLogo(user_id, prompt) {
  const res = await fetch(`${BASE}/logo/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id, prompt }),
  });
  return await res.json();
}

export async function getHistory(user_id) {
  const res = await fetch(`${BASE}/user/history/${user_id}`);
  const data = await res.json();
  return data.history || [];
}