import React, { useContext } from "react"; // Import useContext
import { Link } from "react-router-dom";
import { AuthContext } from "../contexts/AuthContext"; // Import AuthContext
import SignUp from "../components/SignUp";

function EntryPage() {
  const { token } = useContext(AuthContext); // Get the token from the AuthContext

  return (
    <div>
      <SignUp />
    </div>
  );
}

export default EntryPage;
