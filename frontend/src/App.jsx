import React from "react";
import Home from "./pages/Home";
import History from "./pages/History";

export default function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Logo Generator</h1>
      <Home />
      <hr />
      <History />
    </div>
  );
}