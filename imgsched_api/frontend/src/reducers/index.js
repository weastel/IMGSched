import { combineReducers } from "redux";
import meetings from "./meetings";
import profiles from "./profiles";
import me from "./me";

export default combineReducers({
  meetings,
  profiles,
  me,
});
