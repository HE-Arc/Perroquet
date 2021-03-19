import Vue from 'vue'
import App from './App.vue'
import router from "./router"

import BootstrapVue from "bootstrap-vue";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import vuetify from './plugins/vuetify';

import store from './store';

Vue.use(BootstrapVue)


new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')