import React, { Component } from "react";
import { connect } from "react-redux";
import { getMeetings } from "../../actions/meeting";
import { getProfiles } from "../../actions/profiles";
import { Header, Divider, Icon } from "semantic-ui-react";
import CommentList from "./CommentList";
import SimpleMeeting from "./Meeting";

class MeetingDetail extends Component {
  componentDidMount() {
    this.props.getMeetings();
    this.props.getProfiles();
    console.log(this.props);
  }

  render() {
    return (
      <div>
        {this.props.meetings
          .filter(item => item.id == this.props.match.params.id)
          .map(e =>
            <div key={e.id}>
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
              <Divider horizontal>
                <Header as="h4">
                  <Icon name="comments" />
                  Comments
                </Header>
              </Divider>
              <CommentList
                comments={e.comments}
                profiles={this.props.profiles}
              />
            </div>
          )}
      </div>
    );
  }
}

const mapStateToProps = state => ({
  meetings: state.meetings.meetings,
  profiles: state.profiles.profiles,
});

export default connect(mapStateToProps, { getMeetings, getProfiles })(
  MeetingDetail
);
