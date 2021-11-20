import {statistic} from "../../api/statistic";
import {getFeedbacksData, deleteFeedback} from "../../api/feedback";

export default {
    namespaced: true,
    state: {
        data: {
            totalUse: null,
            averageRate: null,
            rate: null,
        },
        errors: null,
        validations: null,
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
         * @param validations
         */
        setValidations(state, validations) {
            state.validations = validations;
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

        /**
         *
         * @param commit
         * @param dispatch
         * @param params
         * @returns {Promise<void>}
         */
        async getFeedbacksData({commit, dispatch}, params = {}) {
            dispatch('startLoading', null, {root: true});
            try {
                const {data} = await getFeedbacksData(params.start, params.limit);
                commit('setValidations', data);
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
         * @param dataValidation
         * @returns {Promise<void>}
         */
        async deleteFeedback({commit, dispatch}, dataValidation = {}) {
            dispatch('startLoading', null, {root: true});
            try {
                await deleteFeedback(dataValidation.id);
            } catch (errors) {
                commit('setErrors', errors);
            } finally {
                dispatch('stopLoading', null, {root: true});
            }
        },
        //
        // /**
        //  *
        //  * @param commit
        //  * @param dispatch
        //  * @param rate
        //  * @returns {Promise<void>}
        //  */
        // async searchFeedback({commit, dispatch}, rate = null) {
        //     dispatch('startLoading', null, {root: true});
        //     try {
        //         const {data} = await searchFeedback(rate);
        //         console.log(data);
        //         // commit('setValidations', data);
        //     } catch (errors) {
        //         commit('setErrors', errors);
        //     } finally {
        //         dispatch('stopLoading', null, {root: true});
        //     }
        // },
    },
}
