import React, { useState, useContext } from "react";
import axios from "axios";
import { AuthContext } from "../contexts/AuthContext";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import Switch from "@mui/material/Switch";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import Button from "@mui/material/Button";

const ActivitiesListItem = ({
  activity,
  handleSwitchChange,
  fetchActivities,
}) => {
  const { auth } = useContext(AuthContext);
  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const deleteActivity = async () => {
    console.log("Deleting activity...");
    try {
      console.log("Deleting activity: ", activity);
      await axios({
        method: "delete",
        url: `http://localhost:8000/activities/${activity.activity_id}`,
        headers: {
          "content-type": "application/json",
          Authorization: `Bearer ${auth.token}`,
        },
      });
      fetchActivities();
      handleClose();
    } catch (error) {
      console.error("Failed to delete activity: ", error);
    }
  };

  return (
    <div>
      <Card
        sx={{ backgroundColor: activity.color, margin: 2 }}
        onClick={handleClickOpen}
      >
        <CardContent>
          <Typography variant="h5" component="div">
            {activity.name}
          </Typography>
          <Switch
            checked={activity.isActive || false}
            onChange={() => handleSwitchChange(activity.id)}
            inputProps={{ "aria-label": "controlled" }}
          />
        </CardContent>
      </Card>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"Delete Activity"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            Are you sure you want to delete this activity?
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={deleteActivity} autoFocus>
            Delete
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default ActivitiesListItem;
