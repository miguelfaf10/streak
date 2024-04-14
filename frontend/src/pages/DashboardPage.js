import React from "react"; // Import useContext
import ActivitiesList from "../components/ActivitiesList";
import Grid from "@mui/material/Unstable_Grid2";
import Box from "@mui/material/Box";

function DashboardPage() {
  return (
    <Box p={5}>
      <Grid container spacing={5}>
        <Grid xs={8}>
          <h1>Dashboard</h1>
        </Grid>
        <Grid item xs={4}>
          <ActivitiesList />
        </Grid>
      </Grid>
    </Box>
  );
}

export default DashboardPage;
