import React from "react";
import Home from "./pages/GenerateLogo";
import History from "./pages/History";

// import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import UserInit from "./pages/UserInit";
// import UserLogin from "./pages/UserLogin";
import TaskInit from "./pages/TaskInit";
import GenerateLogo from "./pages/GenerateLogo";
// import HistoryPage from "./pages/HistoryPage";

export default function App() {
  return (
    <Router>
      <nav style={{ padding: 10 }}>
        <Link to="/user">User Init</Link> |{" "}
        {/* <Link to="/login">User Login</Link> |{" "} */}
        <Link to="/task">Task Init</Link> |{" "}
        <Link to="/generate">🎨 生成 Logo</Link> |{" "}
        {/* <Link to="/history">📜 查看历史</Link> */}
      </nav>

      <Routes>
        <Route path="/user" element={<UserInit />} />
        {/* <Route path="/login" element={<UserLogin />} /> */}
        <Route path="/task" element={<TaskInit />} />
        <Route path="/logo/generate" element={<GenerateLogo />} />
        {/* <Route path="/history" element={<HistoryPage />} /> */}
        <Route path="*" element={<div>404 页面不存在</div>} />
      </Routes>
    </Router>
  );
}
