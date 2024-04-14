import React, { useEffect, useState, useContext } from "react";
import axios from "axios";
import { AuthContext } from "../contexts/AuthContext"; // Import AuthContext
import ActivitiesListItem from "../components/ActivitiesListItem";
import NewActivityButton from "../components/NewActivityButton";

function ListActivities() {
  const [activities, setActivities] = useState([]);
  const { auth } = useContext(AuthContext); // Get the token from the AuthContext

  const fetchActivities = async () => {
    try {
      const response = await axios({
        method: "get",
        url: "http://localhost:8000/activities/",
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

  useEffect(() => {
    fetchActivities();
  }, []);

  return (
    <div className="activity-list">
      <p>
        User: {auth.user}; Token: {auth.token}
      </p>
      {activities.map((activity, index) => (
        <ActivitiesListItem
          key={index}
          activity={activity}
          fetchActivities={fetchActivities}
        />
      ))}
      <NewActivityButton fetchActivities={fetchActivities} />
    </div>
  );
}

export default ListActivities;
