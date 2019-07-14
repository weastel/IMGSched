import React, { Component } from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import MainApp from "./MainApp";
import store from "../store";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <MainApp />
      </Provider>
    );
  }
}

const wrapper = document.getElementById("app");
ReactDOM.render(<App />, wrapper);
