import React from "react";
import { Paper, Grid, Typography } from "@mui/material";

const Activity = ({ title, color }) => (
  <Paper style={{ padding: "8px", backgroundColor: color, margin: "4px 0" }}>
    <Typography variant="body1">{title}</Typography>
  </Paper>
);

const Day = ({ activities }) => (
  <Grid item xs>
    {activities.map((activity, index) => (
      <Activity key={index} title={activity.title} color={activity.color} />
    ))}
  </Grid>
);

const Week = ({ days }) => (
  <Grid container spacing={1}>
    {days.map((day, index) => (
      <Day key={index} activities={day.activities} />
    ))}
  </Grid>
);

const Agenda = ({ weeks }) => (
  <div>
    {weeks.map((week, index) => (
      <Week key={index} days={week.days} />
    ))}
  </div>
);

// Example usage
const MyAgenda = () => {
  const weeks = [
    {
      days: [
        { activities: [{ title: "Activity 1", color: "#FFA07A" }] },
        // ... other days
      ],
    },
    // ... other weeks
  ];

  return <Agenda weeks={weeks} />;
};

export default MyAgenda;
