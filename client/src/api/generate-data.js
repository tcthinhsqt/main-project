import api from './';

export const create = (data) => api.post(`generate-data`, data, {
    headers: {
        'Content-Type': 'multipart/form-data',
        'Content-Encoding': 'UTF-8',
    },
    responseType: "blob",
});

export const extractToCsv = () => api.post(`validation-to-csv`, null, {
    headers: {
        'Content-Encoding': 'UTF-8',
    },
    responseType: "blob",
});
