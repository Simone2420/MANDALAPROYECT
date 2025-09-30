import React, { useEffect, useState } from "react";
import axios from "axios";
import Header from "../components/Header";

const API_URL = "http://localhost:8000/api/";
const COMANDA_URL = `${API_URL}comandas/`;

function Comanda() {
  const [comandas, setComandas] = useState([]);
  const fetchComandas = () => {
    axios
      .get(COMANDA_URL)
      .then((res) => setComandas(res.data))
      .catch((err) => console.error(err));
  };
  const printComandas = () => {
    console.log(comandas);
  };
  useEffect(() => {
    fetchComandas();
  }, []);
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-purple-800 to-slate-900 p-8">
      <Header />
      <h1>Comanda Page</h1>
      <button onClick={printComandas}>Print Comandas</button>
    </div>
  );
}

export default Comanda;
