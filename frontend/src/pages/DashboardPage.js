import React, { useContext } from "react"; // Import useContext
import { Link } from "react-router-dom";
import { AuthContext } from "../contexts/AuthContext"; // Import AuthContext
import ListActivities from "../components/ListActivities";

function DashboardPage() {
  const { token } = useContext(AuthContext); // Get the token from the AuthContext

  return (
    <div>
      <ListActivities />
    </div>
  );
}

export default DashboardPage;
