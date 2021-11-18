import {create} from "../../api/generate-data";

export default {
    namespaced: true,
    state: {
        data: null,
        errors: null,
    },
    mutations: {
        /**
         *
         * @param state
         */
        resetErrors(state) {
            state.errors = null;
        },

        /**
         *
         * @param state
         * @param data
         */
        setData(state, data) {
            state.data = data;
        },

        /**
         *
         * @param state
         * @param errors
         */
        setErrors(state, errors) {
            state.errors = errors.response.data;
        }
    },
    actions: {
        /**
         *
         * @param commit
         * @param dispatch
         * @param files
         * @returns {Promise<void>}
         */
        async generateData({commit, dispatch}, files = {}) {
            dispatch('startLoading', null, {root: true});
            try {
                const {data} = await create(files);
                commit('setData', data);
            } catch (errors) {
                commit('setErrors', errors);
            } finally {
                dispatch('stopLoading', null, {root: true});
            }
        },

    },
}
