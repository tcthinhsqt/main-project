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

/**
 *
 * @param data
 * @returns {Promise<AxiosResponse<any>>}
 */
export const updateUser = (data) => api.post(`update-user`, data);

/**
 *
 * @param form
 * @param id
 * @returns {Promise<AxiosResponse<any>>}
 */
export const changePassword = (form, id) => api.post(`change-password`, form, {params: {id: id}});