import React from "react"; // Import useContext
//import Typography from "@mui/material/Typography";
import { Link } from "react-router-dom";
import Button from "@mui/material/Button";

function EntryPage() {
  return (
    <>
      <h1>Entry Page</h1>
      <Link to="/login">
        <Button variant="contained">Login</Button>
      </Link>

      <Link to="/signup">
        <Button variant="contained">Signup</Button>
      </Link>
    </>
  );
}

export default EntryPage;
