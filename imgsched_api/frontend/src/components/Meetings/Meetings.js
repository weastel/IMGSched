import React, { Component } from "react";
import { connect } from "react-redux";
import { getMeetings } from "../../actions/meeting";
import { getProfiles } from "../../actions/profiles";
import SimpleMeeting from "./Meeting";

class Meeting extends Component {
  componentDidMount() {
    this.props.getMeetings();
    this.props.getProfiles();
  }
  render() {
    return (
      <div>
        <h1>Meetings</h1>
        {this.props.meetings.map(e =>
          <SimpleMeeting
            key={e.id}
            id={e.id}
            time={e.meeting_on}
            location={e.venue}
            header={e.name_of_meeting}
            description={e.description_of_meeting}
            member={e.member}
            comments={e.comments}
            profiles={this.props.profiles}
            created_by={e.created_by}
          />
        )}
      </div>
    );
  }
}

const mapStateToProps = state => ({
  meetings: state.meetings.meetings,
  profiles: state.profiles.profiles,
});

export default connect(mapStateToProps, { getProfiles, getMeetings })(Meeting);
