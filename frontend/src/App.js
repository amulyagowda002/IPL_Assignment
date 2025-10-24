import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Charts from './pages/Charts';

export default function App(){
  return (
    <BrowserRouter>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container">
          <Link className="navbar-brand" to="/">IPL Dashboard</Link>
          <div>
            <Link className="nav-link" to="/">Home</Link>
            <Link className="nav-link" to="/charts">Charts</Link>
          </div>
        </div>
      </nav>
      <div className="container mt-4">
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/charts" element={<Charts/>} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}