import React, { Component } from "react";
import { connect } from "react-redux";
import { getProfiles } from "../../actions/profiles";
import MemberDetail from "./MemberDetail";

export class Member extends Component {
  componentDidMount() {
    this.props.getProfiles();
  }

  render() {
    console.log(this.props);
    return (
      <div>
        <h1>Members</h1>
        {this.props.profiles.map(e => <MemberDetail profile={e} />)}
      </div>
    );
  }
}

const mapStateToProps = state => ({
  profiles: state.profiles.profiles,
});

export default connect(mapStateToProps, { getProfiles })(Member);
