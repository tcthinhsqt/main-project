import {login, logout, register, updateUser, changePassword} from "../../api/authentication.js";

export default {
    namespaced: true,
    state: {
        responseErrors: null,
        user: null,
        name: '',
    },
    mutations: {
        /**
         *
         * @param state
         */
        resetErrors(state) {
            state.responseErrors = null;
        },

        /**
         *
         * @param state
         * @param errors
         */
        setErrors(state, errors) {
            state.responseErrors = errors.response.data;
        },

        /**
         *
         * @param state
         * @param user
         */
        setUser(state, user) {
            state.user = user;
        },

        /**
         *
         * @param state
         * @param birthday
         */
        setBirthday(state, birthday) {
            state.user.birthday = birthday
        },

        /**
         *
         * @param state
         */
        setDisplayName(state) {
            state.name = state.user?.name;
        },
    },
    actions: {
        /**
         *
         * @param commit
         * @param dispatch
         * @param userData
         * @returns {Promise<void>}
         */
        async register({commit, dispatch}, userData = {}) {
            dispatch('startLoading', null, {root: true});
            try {
                await register(userData);
            } catch (errors) {
                commit('setErrors', errors);
            } finally {
                dispatch('stopLoading', null, {root: true});
            }
        },

        /**
         *
         * @param commit
         * @param dispatch
         * @param credentials
         * @returns {Promise<void>}
         */
        async login({commit, dispatch}, credentials = {}) {
            dispatch('startLoading', null, {root: true});
            try {
                const {data} = await login(credentials);
                commit('setUser', data);
            } catch (errors) {
                commit('setErrors', errors);
            } finally {
                dispatch('stopLoading', null, {root: true});
            }
        },

        /**
         *
         * @param commit
         * @param state
         * @returns {Promise<void>}
         */
        async logout({commit, state}) {
            try {
                await logout({id: state.user.id});
                // commit('setAuth', null);
                commit('setUser', null);
            } catch (errors) {
                commit('setErrors', errors);
            }
        },

        /**
         *
         * @param commit
         * @param dispatch
         * @param user
         * @returns {Promise<void>}
         */
        async updateUser({commit, dispatch}, user = {}) {
            dispatch('startLoading', null, {root: true});
            try {
                const {data} = await updateUser(user);
                commit('setUser', data);
            } catch (errors) {
                commit('setErrors', errors);
            } finally {
                dispatch('stopLoading', null, {root: true});
            }
        },

        /**
         *
         * @param commit
         * @param dispatch
         * @param dataChangePass
         * @returns {Promise<void>}
         */
        async changePassword({commit, dispatch}, dataChangePass = {}) {
            dispatch('startLoading', null, {root: true});
            try {
                await changePassword(dataChangePass.form, dataChangePass.id);
            } catch (errors) {
                commit('setErrors', errors);
            } finally {
                dispatch('stopLoading', null, {root: true});
            }
        },
    },
}
