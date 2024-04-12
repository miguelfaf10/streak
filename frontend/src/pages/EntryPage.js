import React, { useContext } from "react"; // Import useContext
import { Link } from "react-router-dom";
import { AuthContext } from "../contexts/AuthContext"; // Import AuthContext

function EntryPage() {
  const { token } = useContext(AuthContext); // Get the token from the AuthContext

  return (
    <div>
      <Link to="/login">
        <button>Login</button>
      </Link>
      <Link to="/signup">
        <button>Signup</button>
      </Link>
    </div>
  );
}

export default EntryPage;
