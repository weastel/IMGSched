import React from "react";
import { Card, Icon } from "semantic-ui-react";

const MemberDetail = props => {
  var name = `${props.profile.user.first_name} ${props.profile.user.last_name}`;
  var occupation = props.profile.occupation == "dev" ? "Developer" : "Designer";
  var year = `${props.profile.user.first_name} is studying in ${props.profile
    .year} year`;
  console.log(props);
  return <Card header={name} meta={occupation} description={year} />;
};

export default MemberDetail;
