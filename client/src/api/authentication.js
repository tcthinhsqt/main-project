import api from './';

/**
 *
 * @param id
 * @returns {Promise<AxiosResponse<any>>}
 */
export const logout = (id) => api.post(`logout`, id);

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
