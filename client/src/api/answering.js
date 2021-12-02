import api from './';

export const create = (data, id = 0) => api.post(`question`, data, {params: {id: id}});

export const test = () => api.get(`test`);