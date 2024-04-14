import React, { useState, useContext } from "react";
import axios from "axios";
import { AuthContext } from "../contexts/AuthContext";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import TextField from "@mui/material/TextField";

const NewActivityButton = ({ fetchActivities }) => {
  const { auth } = useContext(AuthContext);
  const [open, setOpen] = useState(false);
  const [newActivity, setNewActivity] = useState({
    name: "",
    description: "",
    color: "",
  });

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleInputChange = (event) => {
    setNewActivity({ ...newActivity, [event.target.name]: event.target.value });
  };

  const addActivity = async () => {
    console.log("Adding activity...");
    try {
      const response = await axios({
        method: "post",
        url: "http://localhost:8000/activities/",
        headers: {
          "content-type": "application/json",
          Authorization: `Bearer ${auth.token}`,
        },
        data: newActivity,
      });
      fetchActivities();
      handleClose();
    } catch (error) {
      console.error("Failed to fetch activities: ", error);
    }
  };

  return (
    <div>
      <Button variant="contained" color="primary" onClick={handleClickOpen}>
        Add New Activity
      </Button>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="form-dialog-title"
      >
        <DialogTitle id="form-dialog-title">New Activity</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Please enter the details for the new activity.
          </DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            name="name"
            label="Name"
            type="text"
            fullWidth
            onChange={handleInputChange}
          />
          <TextField
            margin="dense"
            name="description"
            label="Description"
            type="text"
            fullWidth
            onChange={handleInputChange}
          />
          <TextField
            margin="dense"
            name="color"
            label="Color"
            type="text"
            fullWidth
            onChange={handleInputChange}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={addActivity}>Add</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default NewActivityButton;
