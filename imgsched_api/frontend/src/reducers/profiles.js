import { GET_PROFILES } from "../actions/types.js";

const initalState = {
  profiles: [],
};

export default function(state = initalState, action) {
  switch (action.type) {
    case GET_PROFILES:
      return {
        ...state,
        profiles: action.payload,
      };
    default:
      return state;
  }
}
