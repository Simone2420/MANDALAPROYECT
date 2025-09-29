// src/App.jsx
import React, { useEffect, useState } from "react";
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import Inventario from "./pages/InventarioPage";
import Comanda from "./pages/ComandaPage";
import Home from "./pages/Home";
function App() {
  

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/inventario" element={<Inventario />} />
        <Route path="/comanda" element={<Comanda />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
