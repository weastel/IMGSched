import { GET_ME } from "../actions/types.js";

const initalState = {
  me: {},
};

export default function(state = initalState, action) {
  switch (action.type) {
    case GET_ME:
      return {
        ...state,
        me: action.payload,
      };
    default:
      return state;
  }
}
