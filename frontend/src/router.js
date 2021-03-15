import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: '/index'
    },
    {
      path: "/index",
      name: "HelloWorld",
      component: () => import("./components/HelloWorld.vue")
    },
    {
      path: "/login",
      name: "Login",
      component: () => import("./components/Login.vue")
    },
  ]
});