import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const BASE = "http://localhost:8000";
export function UserLogin() {
  const [userId, setUserId] = useState("");
  const navigate = useNavigate();

  const handleLogin = () => {
    if (userId) {
      navigate(`/task?user_id=${userId}`); // 跳转到任务初始化页面
    } else {
      alert("请输入用户 ID");
    }
  };

  return (
    <div>
      <h2>用户登录</h2>
      <input
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        placeholder="输入用户 ID"
        style={{ width: "300px", marginRight: "10px" }}
      />
      <button onClick={handleLogin}>登录</button>
    </div>
  );
}