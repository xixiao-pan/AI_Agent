import React, { useState } from "react";
import { generateLogo } from "../services/api";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [logoURL, setLogoURL] = useState("");

  const handleSubmit = async () => {
    const res = await generateLogo("test_user", prompt);
    setLogoURL("http://localhost:8000" + res.image_path);
  };

  return (
    <div>
      <h2>Generate Logo</h2>
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
    </div>
  );
}