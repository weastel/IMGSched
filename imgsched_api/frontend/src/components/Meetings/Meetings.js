import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getMeetings } from '../../actions/meeting'

class Meeting extends Component {

    componentDidMount() {
        console.log(this.props)
        this.props.getMeetings();
    }
    render() {
        return (
        <h1>Meetings</h1>
        )
    }
}

const mapStateToProps = state => ({
    meetings: state.meetings.meetings 
})

export default connect( mapStateToProps , { getMeetings } )(Meeting);