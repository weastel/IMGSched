import axios from "axios";

import { GET_PROFILES } from "./types";

export const getProfiles = () => dispatch => {
  axios
    .get("/api/Users/")
    .then(res => {
      console.log("This is working");
      dispatch({
        type: GET_PROFILES,
        payload: res.data,
      });
    })
    .catch(err => console.log("error", err));
};
