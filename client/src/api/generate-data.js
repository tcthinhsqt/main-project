import api from './';

export const create = (data) => api.post(`generate-data`, data, {
    headers: {
        'Content-Type': 'multipart/form-data',
        'Content-Encoding': 'UTF-8',
    },
    responseType: "blob",
});

export const extractToCsv = () => api.get(`validation-to-csv`, {
    headers: {
        'Content-Type': 'multipart/form-data',
        'Content-Encoding': 'UTF-8',
    },
    responseType: "blob",
});
