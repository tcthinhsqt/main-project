import {create} from "../../api/answering";

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
            state.errors = errors.response.data.errors;
        }
    },
    actions: {
        /**
         *
         * @param commit
         * @param dispatch
         * @param question
         * @returns {Promise<void>}
         */
        async createAnswer({commit, dispatch}, question = {}) {
            dispatch('startLoading', null, {root: true});
            try {
                const {data} = await create(question.question);
                commit('setAnswer', data);
            } catch (errors) {
                commit('setErrors', errors);
            } finally {
                dispatch('stopLoading', null, {root: true});
            }
        },
    },
}
