import api from './';

export const feedback = (data, id) => api.post(`validate`, data, {params: {id: id}});