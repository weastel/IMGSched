import React from "react";
import ReactDOM from "react-dom";

const App = () => (
    <h1>React is now activated</h1>
);
const wrapper = document.getElementById("app");
ReactDOM.render(<App />, wrapper);