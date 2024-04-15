// React imports
import React from "react"; // Import useContext
// MUI imports
import Grid from "@mui/material/Unstable_Grid2";
import Box from "@mui/material/Box";
// Custom imports
import ActivitiesList from "../components/ActivitiesList";
import MyAgenda from "../components/MyAgenda";

function DashboardPage() {
  return (
    <Box p={5}>
      <Grid container spacing={5}>
        <Grid xs={8}>
          <MyAgenda />
        </Grid>
        <Grid item xs={4}>
          <ActivitiesList />
        </Grid>
      </Grid>
    </Box>
  );
}

export default DashboardPage;
