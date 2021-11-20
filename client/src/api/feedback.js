import api from './';

export const feedback = (data, id) => api.post(`validate`, data, {params: {id: id}});

export const getFeedbacksData = (start, limit) => api.get(`get-validations`, {params: {start: start, limit: limit}});

export const deleteFeedback = (data) => api.post(`delete-validation`, data);

// export const searchFeedback = (rate) => api.get(`search-validation`, {params: {rate: rate}});
