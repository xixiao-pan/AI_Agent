const BASE = "http://localhost:8000";

/**
 * 初始化用户
 * @param {Object} user - 包含 user_id, name, organization, role
 */
export async function initUser(user) {
  const res = await fetch(`${BASE}/user/init`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(user),
  });
  return await res.json();
}

/**
 * 为某个用户创建任务
 * @param {string} user_id
 * @param {string} company_name
 * @param {string} industry_field
 */
export async function initTask(user_id, company_name, industry_field) {
  const res = await fetch(`${BASE}/user/${user_id}/task/init`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ company_name, industry_field }),
  });
  return await res.json(); // { task_id, task }
}

export async function generateLogo(user_id, task_id, prompt) {
  const res = await fetch(`${BASE}/logo/generate/${user_id}/${task_id}`, {
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