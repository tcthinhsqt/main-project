import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/Login";
import Register from "../views/Register";
import Dashboard from "../views/Dashboard";
import Error            from "../views/Error";
import Profile from "../views/Profile";
import Admin from "../views/Admin";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path     : "/profile",
        name     : "profile",
        component: Profile,
    },
    {
        path     : "/login",
        name     : "login",
        component: Login,
    },
    {
        path     : "/register",
        name     : "register",
        component: Register,
    },
    {
        path     : "/information",
        name     : "information",
        component: Dashboard,
    },
    {
        path     : "/admin",
        name     : "admin",
        component: Admin,
    },
    {
        path     : "/error",
        name     : "error",
        component: Error,
    },
    {
        path     : "*",
        name     : "page_not_found",
        component: Error,
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
