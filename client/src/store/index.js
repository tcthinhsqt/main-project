import Vue from "vue";
import Vuex from "vuex";
import SecureLS from "secure-ls";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

const ls = new SecureLS({isCompression: false});

import QA from './modules/QA';
import auth from './modules/auth.js';
import validation from "./modules/validation";
import generation from "./modules/generation";

export default new Vuex.Store({
    state: {
        isLoading: false,
    },
    mutations: {
        setLoading(state, isLoading) {
            state.isLoading = isLoading;
        },
    },
    actions: {
        startLoading({commit}) {
            commit('setLoading', true);
        },
        stopLoading({commit}) {
            commit('setLoading', false);
        },
    },
    modules: {
        QA,
        auth,
        validation,
        generation
    },
    plugins: [
        createPersistedState({
            storage: {
                getItem: (key) => {
                    return ls.get(key)
                },
                setItem: (key, value) => ls.set(key, value),
                removeItem: (key) => ls.remove(key),
            },
        })
    ],
});
