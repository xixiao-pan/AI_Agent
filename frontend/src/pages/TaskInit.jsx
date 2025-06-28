import React, { useState } from "react";
import { useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";


const BASE = "http://localhost:8000";

export default function TaskInit() {
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const userId = searchParams.get("user_id"); // ✅ 从URL获取 user_id
  const navigate = useNavigate();


  const [companyName, setCompanyName] = useState("");
  const [industryField, setIndustryField] = useState("");

  if (!userId) {
    return <div>请先初始化用户！</div>; // 如果没有 user_id，提示用户先初始化
  }

  const initTask = async () => {
    const res = await fetch(`${BASE}/task/${userId}/init`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ company_name: companyName, industry_field: industryField }),
    });
    const data = await res.json();
    localStorage.setItem("task_id", data.task_id); // 🔐 存 task_id
    alert(`✅ 任务创建成功：${data.task_id}`);
    // 后续你可以跳转到 /generate 或 /chata
    navigate(`/logo/generate?user_id=${userId}&task_id=${data.task_id}`);
  };

  return (
    <div>
      <h2>为用户 {userId} 创建任务</h2>
      <input value={companyName} onChange={e => setCompanyName(e.target.value)} placeholder="Company Name" />
      <input value={industryField} onChange={e => setIndustryField(e.target.value)} placeholder="Industry Field" />
      <button onClick={initTask}>创建任务</button>
    </div>
  );
}
