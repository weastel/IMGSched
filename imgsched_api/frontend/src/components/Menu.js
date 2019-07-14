import React, { Component } from "react";
import { Menu, Segment } from "semantic-ui-react";
import { Link } from "react-router-dom";

export default class MenuExampleInvertedSecondary extends Component {
  state = { activeItem: "home" };

  handleItemClick = (e, { name }) => this.setState({ activeItem: name });

  render() {
    const { activeItem } = this.state;

    return (
      <Segment inverted>
        <Menu inverted pointing secondary>
          <Link to="/react/">
            <Menu.Item
              name="home"
              active={activeItem === "home"}
              onClick={this.handleItemClick}
            />
          </Link>
          <Link to="/react/meetings">
            <Menu.Item
              name="Meetings"
              active={activeItem === "Meetings"}
              onClick={this.handleItemClick}
            />
          </Link>
          <Link to="/react/members">
            <Menu.Item
              name="Members"
              active={activeItem === "Members"}
              onClick={this.handleItemClick}
            />
          </Link>
          <Menu.Menu position="right">
            <a href="/api/logout">
              <Menu.Item
                name="logout"
                active={activeItem === "logout"}
                onClick={this.handleItemClick}
              />
            </a>
          </Menu.Menu>
        </Menu>
      </Segment>
    );
  }
}
