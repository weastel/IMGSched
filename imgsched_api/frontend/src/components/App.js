import React from "react";
import ReactDOM from "react-dom";

import { Provider } from 'react-redux'
import store from '../store'
import Meeting from './Meetings/Meetings' 

const App = () => (
    <Provider store={store}>
        <h1>React is now activated</h1>
        <Meeting />
    </Provider>
);
const wrapper = document.getElementById("app");
ReactDOM.render(<App />, wrapper);