import Vue from "vue";
import Router from "vue-router";
import store from "./store/index.js";

Vue.use(Router);

export default new Router({
  mode: 'history',
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
      path: "/signin",
      name: "Signin",
      component: () => import("./components/Signin.vue")
    },
    {
      path: "/login",
      name: "Login",
      component: () => import("./components/Login.vue")
    },
    {
      path: "/passwordResetLink",
      name: "PasswordResetLink",
      component: () => import("./components/PasswordResetLink.vue")
    },
    {
      path: "/reset-password/:token",
      name: "ResetPassword",
      component: () => import("./components/PasswordReset.vue")
    },
    {
      path: "/profile/:pId",
      name: "profile",
      component: () => import("./components/Profile.vue")
    },
    {
      path: "/profile",
      redirect: function() { return "/profile/" + store.state.userId},
    },
    {
      path: "/logout",
      redirect: function() { 
        store.dispatch("logout");
        return "/";
      },
    }
  ]
});