import axios from "axios";

import { GET_MEETINGS } from "./types";

export const getMeetings = () => dispatch => {
  axios
    .get("/api/meeting/")
    .then(res => {
      console.log("This is working");
      dispatch({
        type: GET_MEETINGS,
        payload: res.data,
      });
    })
    .catch(err => console.log("error", err));
};
