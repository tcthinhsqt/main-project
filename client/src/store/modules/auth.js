import {login, logout, register} from "../../api/authentication.js";
// import api                                from '../../api';

export default {
    namespaced: true,
    state: {
        // access_token  : '',
        // expired_time  : null,
        // token_type    : '',
        responseErrors: null,
        user: null,
    },
    mutations: {
        /**
         *
         * @param state
         */
        resetErrors(state) {
            state.responseErrors = null;
        },
        //
        // /**
        //  *
        //  * @param state
        //  * @param auth
        //  */
        // setAuth(state, auth) {
        //     state.access_token                 = auth?.access_token;
        //     state.expired_time                 = auth?.expired_time;
        //     state.token_type                   = auth?.token_type;
        //     api.defaults.headers.authorization = `${state.token_type} ${state.access_token}`
        // },

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
        }
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
    },
}
