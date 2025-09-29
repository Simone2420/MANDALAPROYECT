import React, { useEffect, useState } from "react";
import axios from "axios";
import Header from "../components/Header";

const API_URL = "http://localhost:8000/api/";
const COMANDA_URL = `${API_URL}comandas/`;

function Comanda() {
  return (
    <div>
      <Header />
      <h1>Comanda Page</h1>
    </div>
  );
}

export default Comanda;
