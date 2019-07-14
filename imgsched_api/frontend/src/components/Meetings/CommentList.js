import React from "react";
import { Comment, Icon } from "semantic-ui-react";
import Moment from "react-moment";
var ProfileName = (props, sender_id) =>
  props.profiles.map(item => {
    console.log(item.user.id);
    if (item.user.id === sender_id) {
      return `${item.user.username}`;
    }
  });

const CommentList = props =>
  props.comments.map(e =>
    <Comment.Group key={e.id}>
      <Comment>
        <Comment.Content>
          <Comment.Author>
            {ProfileName(props, e.sender)}
          </Comment.Author>
          <Comment.Metadata>
            <Moment fromNow>
              {e.time_of_comment}
            </Moment>
          </Comment.Metadata>
          <Comment.Text>
            {e.comment}
          </Comment.Text>
        </Comment.Content>
      </Comment>
    </Comment.Group>
  );
export default CommentList;
