// import {login, logout, register} from "../../api/authentication.js";
//
// export default {
//     namespaced: true,
//     state     : {
//         responseData  : null,
//         responseErrors: null,
//         isLogin       : false,
//     },
//     mutations : {
//         /**
//          *
//          * @param state
//          */
//         resetErrors(state) {
//             state.responseErrors = null;
//         },
//
//         /**
//          *
//          * @param state
//          * @param data
//          */
//         setResponseData(state, data) {
//             state.responseData = data;
//         },
//
//         /**
//          *
//          * @param state
//          * @param errors
//          */
//         setErrors(state, errors) {
//             state.responseErrors = errors.response.data;
//         },
//
//         /**
//          *
//          * @param state
//          * @param isLogin
//          */
//         setIsLogin(state, isLogin) {
//             state.isLogin = isLogin;
//         }
//     },
//     actions   : {
//         /**
//          *
//          * @param commit
//          * @param dispatch
//          * @param userData
//          * @returns {Promise<void>}
//          */
//         async register({commit, dispatch}, userData = {}) {
//             dispatch('startLoading', null, {root: true});
//             try {
//                 await register(userData);
//             } catch (errors) {
//                 commit('setErrors', errors);
//             } finally {
//                 dispatch('stopLoading', null, {root: true});
//             }
//         },
//
//         /**
//          *
//          * @param commit
//          * @param dispatch
//          * @param credentials
//          * @returns {Promise<void>}
//          */
//         async login({commit, dispatch}, credentials = {}) {
//             dispatch('startLoading', null, {root: true});
//             try {
//                 const {data} = await login(credentials);
//                 commit('setResponseData', data);
//                 commit('setIsLogin', true);
//             } catch (errors) {
//                 commit('setErrors', errors);
//             } finally {
//                 dispatch('stopLoading', null, {root: true});
//             }
//         },
//
//         /**
//          *
//          * @param commit
//          * @returns {Promise<void>}
//          */
//         async logout({commit}) {
//             try {
//                 await logout();
//                 commit('setResponseData', null);
//                 commit('setIsLogin', false);
//             } catch (errors) {
//                 commit('setErrors', errors);
//             }
//         },
//     },
// }
