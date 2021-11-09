import axios from 'axios';
import apiConfig from '../config/api';

export default axios.create({
    baseURL: `${apiConfig.internal.baseUrl}/api`,
    headers: {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
});
