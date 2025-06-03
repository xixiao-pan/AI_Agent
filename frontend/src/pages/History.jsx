import React, { useEffect, useState } from "react";
import { getHistory } from "../services/api";
import LogoCard from "../components/LogoCard";

export default function History() {
  const [logos, setLogos] = useState([]);

  useEffect(() => {
    getHistory("test_user").then(setLogos);
  }, []);

  return (
    <div>
      <h2>历史 Logo</h2>
      {logos.map((item, index) => (
        <LogoCard key={index} data={item} />
      ))}
    </div>
  );
}