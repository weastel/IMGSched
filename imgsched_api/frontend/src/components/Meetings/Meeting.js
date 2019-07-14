import React from "react";
import { Card, Icon } from "semantic-ui-react";
import { Link } from "react-router-dom";
import Moment from "react-moment";

var ProfileName = (props, sender_id) =>
  props.profiles.map(item => {
    console.log(item.user.id);
    if (item.user.id === sender_id) {
      return `${item.user.first_name} ${item.user.last_name}`;
    }
  });

const SimpleMeeting = props =>
  <Card fluid color="grey" as={Link} to={`/react/meetings/${props.id}`}>
    <Card.Content header={props.header} />
    <Card.Content description={props.description} />
    <Card.Content extra>
      <b>Author</b>:- {ProfileName(props, props.created_by)}
      <br />
      <Icon name="calendar check" />
      <Moment local>{props.time}</Moment>
      <br />
      <Icon name="location arrow" />
      {props.location}
      <br />
      <Icon name="user" />
      {props.member.length + 1} Members
      <br />
      <Icon name="comments outline" />
      {props.comments.length}Comments
    </Card.Content>
  </Card>;

export default SimpleMeeting;
