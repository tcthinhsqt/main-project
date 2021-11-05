require('./bootstrap');

import Vue from 'vue';
import Fragment from 'vue-fragment';
import App from './App';
import router from './router';
import store from './store';
import "chart.js";
import "hchs-vue-charts";
import './plugins/vee-validate';
import AOS from "aos";

Vue.config.productionTip = false;

Vue.use(Fragment.Plugin);
Vue.use(window.VueCharts);

new Vue({
    created() {
        AOS.init();
    },
    router,
    store,
    render: h => h(App),
}).$mount("#app");
