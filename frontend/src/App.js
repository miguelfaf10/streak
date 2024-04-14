import React, { useContext } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import EntryPage from "./pages/EntryPage";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";
import DashboardPage from "./pages/DashboardPage";
import { AuthProvider, AuthContext } from "./contexts/AuthContext";

function App() {
  return (
    <AuthProvider>
      <RoutesComponent />
    </AuthProvider>
  );
}

function RoutesComponent() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<EntryPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
      </Routes>
    </Router>
  );
}

export default App;
