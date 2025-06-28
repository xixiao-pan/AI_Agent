import React, { useState, useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { generateLogo } from "../services/api";

export default function GenerateLogo() {
  const navigate = useNavigate();
  const location = useLocation();

  const [userId, setUserId] = useState("");
  const [taskId, setTaskId] = useState("");
  const [prompt, setPrompt] = useState("");
  const [logoURL, setLogoURL] = useState("");

  useEffect(() => {
    const searchParams = new URLSearchParams(location.search);
    const user_id = searchParams.get("user_id");
    const task_id = searchParams.get("task_id");

    setUserId(user_id);
    setTaskId(task_id);
  }, [location]);

  const handleSubmit = async () => {
    const res = await generateLogo(userId, taskId, prompt);
    setLogoURL("http://localhost:8000" + res.image_path);
  };

  const handleRecreateTask = () => {
    navigate(`/task?user_id=${userId}`); // ✅ 跳转并保留用户信息
  };

  return (
    <div>
      <h2>🎨 Generate Logo</h2>
      <input
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="输入 logo prompt"
        style={{ width: "300px", marginRight: "10px" }}
      />
      <button onClick={handleSubmit}>生成</button>

      {logoURL && (
        <div style={{ marginTop: "20px" }}>
          <img src={logoURL} alt="生成的 logo" width="200" />
        </div>
      )}

      <div style={{ marginTop: "30px" }}>
        <button onClick={handleRecreateTask}>➕ 重新创建任务</button>
      </div>
    </div>
  );
}
