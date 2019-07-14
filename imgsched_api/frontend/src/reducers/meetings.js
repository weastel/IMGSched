import { GET_MEETINGS } from "../actions/types.js";

const initalState = {
  meetings: [],
};

export default function(state = initalState, action) {
  switch (action.type) {
    case GET_MEETINGS:
      return {
        ...state,
        meetings: action.payload,
      };
    default:
      return state;
  }
}
