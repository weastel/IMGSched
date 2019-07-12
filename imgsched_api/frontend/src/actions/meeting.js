import axios from 'axios'

import { GET_MEETINGS } from './types'

export const getMeetings = () => dispatch => {
    axios.get('127.0.0.1:8000/api/meeting/')
        .then(res => {
            console.log(res.data)
        })
        .catch(err => console.log(err))
}