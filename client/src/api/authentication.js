import api from './';

/**
 *
 * @returns {Promise<AxiosResponse<any>>}
 */
export const logout = () => api.post(`logout`);

/**
 *
 * @param data
 * @returns {Promise<AxiosResponse<any>>}
 */
export const login = (data) => api.post(`login`, data);

/**
 *
 * @param data
 * @returns {Promise<AxiosResponse<any>>}
 */
export const register = (data) => api.post(`register`, data);
