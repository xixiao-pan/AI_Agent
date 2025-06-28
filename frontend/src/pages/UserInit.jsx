import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const BASE = "http://localhost:8000";

export default function UserInit() {
  const [userId, setUserId] = useState("");
  const [name, setName] = useState("");
  const [organization, setOrganization] = useState("");
  const [role, setRole] = useState("");
  const navigate = useNavigate(); // ✅ 声明导航器

  const initUser = async () => {
    const res = await fetch(`${BASE}/user/init`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, name, organization, role }),
    });
    const data = await res.json();
    localStorage.setItem("user_id", userId); // 🔐 存 user_id
    alert("✅ 用户初始化成功");
    navigate(`/task?user_id=${userId}`); // ✅ 初始化成功后跳转至 task 页面，附带 user_id
  };

  return (
    <div>
      <h2>用户初始化</h2>
      <input value={userId} onChange={e => setUserId(e.target.value)} placeholder="User ID" />
      <input value={name} onChange={e => setName(e.target.value)} placeholder="Name" />
      <input value={organization} onChange={e => setOrganization(e.target.value)} placeholder="Organization" />
      <input value={role} onChange={e => setRole(e.target.value)} placeholder="Role" />
      <button onClick={initUser}>初始化用户</button>
    </div>
  );
}
