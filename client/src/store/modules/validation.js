import {statistic} from "../../api/statistic";

export default {
    namespaced: true,
    state: {
        data: {
            totalUse: null,
            averageRate: null,
            rate: null,
        },
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
        setStatisticData(state, data) {
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
         * @param questionData
         * @returns {Promise<void>}
         */
        async getStatisticData({commit, dispatch}) {
            dispatch('startLoading', null, {root: true});
            try {
                const {data} = await statistic();
                commit('setStatisticData', data);
            } catch (errors) {
                commit('setErrors', errors);
            } finally {
                dispatch('stopLoading', null, {root: true});
            }
        },

    },
}
