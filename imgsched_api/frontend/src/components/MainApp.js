import React, { Component } from "react";
import { Route, Link, BrowserRouter as Router } from "react-router-dom";
import {
  Button,
  Icon,
  Form,
  Grid,
  Header,
  Image,
  Message,
  Segment,
} from "semantic-ui-react";
import { connect } from "react-redux";
import Meeting from "./Meetings/Meetings";
import MeetingDetail from "./Meetings/MeetingIndex";
import MenuBar from "./Menu";
import Member from "./Members/Member";
import Home from "./Home/Home";
import { getMe } from "../actions/me";
import { getMeetings } from "../actions/meeting";
import { getProfiles } from "../actions/profiles";

class MainApp extends Component {
  componentDidMount() {
    this.props.getMe();
  }
  render() {
    console.log(this.props.me.id);
    var ifLoggined = (
      <Router>
        <MenuBar />
        <Segment stacked>
          <Route exact path="/react/" component={Home} />
          <Route exact path="/react/meetings" component={Meeting} />
          <Route exact path="/react/members" component={Member} />
          <Route path="/react/meetings/:id" component={MeetingDetail} />
        </Segment>
      </Router>
    );
    if (Number.isInteger(this.props.me.id)) {
      return ifLoggined;
    } else {
      return (
        <Grid
          textAlign="center"
          style={{ height: "100vh" }}
          verticalAlign="middle"
        >
          <Grid.Column style={{ maxWidth: 450 }}>
            <Header as="h2" color="orange" textAlign="center">
              Log-in to your account
            </Header>
            <a href="/login/google-oauth2/?next=/react/">
              <Button color="google plus">
                <Icon name="google" />Log in with Google Plus
              </Button>
            </a>
          </Grid.Column>
        </Grid>
      );
    }
  }
}

const mapStateToProps = state => ({
  me: state.me.me,
});

export default connect(mapStateToProps, { getMeetings, getProfiles, getMe })(
  MainApp
);
