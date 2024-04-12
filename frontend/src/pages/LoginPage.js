import React, { useContext } from "react"; // Import useContext
import { Link } from "react-router-dom";
import { AuthContext } from "../contexts/AuthContext"; // Import AuthContext
import Login from "../components/Login";

function EntryPage() {
  const { token } = useContext(AuthContext); // Get the token from the AuthContext

  return (
    <div>
      <Login />
    </div>
  );
}

export default EntryPage;
