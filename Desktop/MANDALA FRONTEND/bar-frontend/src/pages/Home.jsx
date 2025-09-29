import React, {useState, useEffect}from "react";
import { useNavigate } from "react-router-dom";
import Header from "../components/Header";
function Home() {
  const navigate = useNavigate();

  const handleNavigate = () => {
    navigate("/inventario");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-purple-800 to-slate-900 p-8">
      <Header />
      <button className="bg-white text-purple-900 rounded-lg px-4 py-2" onClick={() => navigate("/inventario")}>Ir a Inventario</button>
      <button className="bg-white text-purple-900 rounded-lg px-4 py-2 ml-4" onClick={() => navigate("/comanda")}>Ir a Comanda</button>
    </div>
  );
}

export default Home;