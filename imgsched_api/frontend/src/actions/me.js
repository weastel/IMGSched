import axios from "axios";

import { GET_ME } from "./types";

export const getMe = () => dispatch => {
  axios
    .get("/api/me")
    .then(res => {
      dispatch({
        type: GET_ME,
        payload: res.data,
      });
    })
    .catch(err => console.log("error", err));
};
