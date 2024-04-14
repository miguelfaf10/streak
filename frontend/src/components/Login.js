import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";

import Button from "@mui/material/Button";

import axios from "axios";
import qs from "qs"; // You need to install qs with npm install qs
import { AuthContext } from "../contexts/AuthContext"; // Import AuthContext

function Login() {
  // Get setAuth from AuthContext
  const { auth, setAuth } = useContext(AuthContext);

  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });

  const navigate = useNavigate();

  const handleLogin = async (event) => {
    event.preventDefault();
    try {
      const response = await axios({
        method: "post",
        url: "http://localhost:8000/auth/token",
        data: qs.stringify({
          username: formData.username,
          password: formData.password,
        }),
        headers: {
          "content-type": "application/x-www-form-urlencoded;charset=utf-8",
        },
      });
      const token = response.data.access_token;
      console.log("Login successful! Token: ", token);

      // Save the token in the auth context
      setAuth({ user: formData.username, token: token });

      // Navigate to the dashboard page
      console.log("Navigating to the dashboard page...");
      navigate("/dashboard");
    } catch (error) {
      console.error("Login failed: ", error);
    }
  };

  return (
    <div className="container mt-5">
      <h1>Login</h1>

      <form onSubmit={handleLogin}>
        <div className="mb-3">
          <label htmlFor="username" className="form-label">
            Username
          </label>
          <input
            type="username"
            className="form-control"
            id="username"
            value={formData.username}
            onChange={(event) =>
              setFormData({ ...formData, username: event.target.value })
            }
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password" className="form-label">
            Password
          </label>
          <input
            type="password"
            className="form-control"
            id="password"
            value={formData.password}
            onChange={(event) =>
              setFormData({ ...formData, password: event.target.value })
            }
            required
          />
        </div>
        <Button variant="contained" onClick={(event) => handleLogin(event)}>
          Login
        </Button>
        ;
      </form>
    </div>
  );
}

export default Login;
