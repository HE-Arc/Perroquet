import Vue from "vue";
import Router from "vue-router";
import store from "./store/index.js";

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: "/",
      redirect: '/discover'
    },
    {
      path: "/discover",
      name: "Discover",
      component: () => import("./components/Discover.vue")
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
      path: "/follow/:pId",
      name: "follow",
      component: () => import("./components/Follow.vue")
    },
    {
      path: "/follow",
      redirect: function() { return "/follow/" + store.state.userId},
    },
    {
      path: "/follower/:pId",
      name: "follower",
      component: () => import("./components/Follower.vue")
    },
    {
      path: "/follower",
      redirect: function() { return "/follower/" + store.state.userId},
    },
    {
      path: "/logout",
      redirect: function() { 
        //store.dispatch("logout");
        return "/";
      },
    },
    {
      path: "/settings",
      name: "settings",
      component: () => import("./components/Settings.vue")
    },
  ]
});