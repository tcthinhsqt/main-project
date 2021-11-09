import api from './';

export const create = (data) => api.post(`question`, data);

export const test = () => api.get(`test`);