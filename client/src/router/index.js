import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/Login";
import Register from "../views/Register";
import Dashboard from "../views/Dashboard";
import Error from "../views/Error";
import Profile from "../views/Profile";
import Admin from "../views/Admin";
import auth from '../middleware/auth.js'
import Middleware from "../middleware";
import store      from '../store';

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home,
        beforeEnter: (to, from, next) => {
            const currentTime = Math.floor(Date.now() / 1000);
            if (store.state.auth.expired_time < currentTime) {
                store.commit('auth/setUser', null, {root: true});
            }
            next()
        }
    },
    {
        path: "/profile",
        name: "profile",
        component: Profile,
        meta: {
            middleware: [
                auth
            ]
        },
    },
    {
        path: "/login",
        name: "login",
        component: Login,
    },
    {
        path: "/register",
        name: "register",
        component: Register,
    },
    {
        path: "/information",
        name: "information",
        component: Dashboard,
        beforeEnter: (to, from, next) => {
            const currentTime = Math.floor(Date.now() / 1000);
            if (store.state.auth.expired_time < currentTime) {
                store.commit('auth/setUser', null, {root: true});
            }
            next()
        }
    },
    {
        path: "/admin",
        name: "admin",
        component: Admin,
        meta: {
            middleware: [
                auth
            ]
        },
    },
    {
        path: "/error",
        name: "error",
        component: Error,
    },
    {
        path: "*",
        name: "page_not_found",
        component: Error,
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    (new Middleware()).execute(to, from, next);
});

export default router
