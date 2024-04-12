import React, { useEffect, useState, useContext } from "react";
import axios from "axios";
import { AuthContext } from "../contexts/AuthContext"; // Import AuthContext

function ListActivities() {
  const [activities, setActivities] = useState([]);
  const { auth } = useContext(AuthContext); // Get the token from the AuthContext

  useEffect(() => {
    const fetchActivities = async () => {
      try {
        const response = await axios({
          method: "get",
          url: "http://localhost:8000/activities",
          headers: {
            "content-type": "application/json",
            Authorization: `Bearer ${auth.token}`, // Include the token in the Authorization header
          },
        });
        setActivities(response.data.Activities);
        console.log("Fetched activities: ", response.data);
      } catch (error) {
        console.error("Failed to fetch activities: ", error);
      }
    };

    fetchActivities();
  }, []);

  return (
    <div>
      <h1>{auth.user} </h1>
      <h2>Activities </h2>
      {activities.map((activity, index) => (
        <div
          key={index}
          className="card"
          style={{ backgroundColor: activity.color, margin: "20px" }}
        >
          <div className="card-body">
            <h2 className="card-title">{activity.name}</h2>
          </div>
        </div>
      ))}
    </div>
  );
}

export default ListActivities;
