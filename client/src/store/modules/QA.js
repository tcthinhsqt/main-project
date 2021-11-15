import {create} from "../../api/answering";
import {feedback} from "../../api/feedback";

export default {
    namespaced: true,
    state: {
        data: {
            question: null,
            answer: null
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
        setAnswer(state, data) {
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
        async createAnswer({commit, dispatch}, questionData = {}) {
            dispatch('startLoading', null, {root: true});
            try {
                const {data} = await create(questionData.cauHoi, questionData.id);
                commit('setAnswer', data);
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
         * @param feedbackData
         * @returns {Promise<void>}
         */
        async sendFeedback({commit, dispatch}, feedbackData = {}) {
            dispatch('startLoading', null, {root: true});
            try {
                await feedback(feedbackData.feedbackData, feedbackData.id);
            } catch (errors) {
                commit('setErrors', errors);
            } finally {
                dispatch('stopLoading', null, {root: true});
            }
        },
    },
}
