import React, { useContext, useState } from "react";

import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import EntryPage from "./pages/EntryPage";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";
import DashboardPage from "./pages/DashboardPage";
import { AuthProvider, AuthContext } from "./contexts/AuthContext";

function App() {
  const [showLogin, setShowLogin] = useState(true);

  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route exact path="/" element={<EntryPage />} />
          <Route exact path="/login" element={<LoginPage />} />
          <Route exact path="/signup" element={<SignupPage />} />
          <Route exact path="/dashboard" element={<DashboardPage />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
