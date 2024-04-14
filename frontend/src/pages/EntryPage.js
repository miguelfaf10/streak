import React from "react"; // Import useContext
//import Typography from "@mui/material/Typography";
import { Link } from "react-router-dom";

function EntryPage() {
  return (
    <>
      <h1>Entry Page</h1>
      <Link to="/login">
        <button>Login</button>
      </Link>
      {/*
      <Link to="/signup">
        <button>Signup</button>
      </Link> */}
    </>
  );
}

export default EntryPage;
