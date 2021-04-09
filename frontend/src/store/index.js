import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

const BASE_URL = process.env.VUE_APP_BASEURL

//to handle state
const state = {
    token: "",
    profiles: [],
    filter: "new",
}

//to handle state
const getters = {
    authenticated: state => {
        return state.token != ""
    }
}

//to handle actions
const actions = {
    login({ commit }, fields) {
        return new Promise((resolve, reject) => {
            axios.post(BASE_URL + 'token/',
                {
                    username: fields.username,
                    password: fields.password,
                }).then((response) => {
                    commit('LOGIN', response.data.token);
                    resolve();
                }, (error) => {
                    reject(error);
                });
        });
    },
    logout({ commit }) {
        commit('LOGOUT');
        this.$router.push("index")
    },
    register({ commit }, fields) {
        return new Promise((resolve, reject) => {
            axios.post(BASE_URL + 'register/',
                {
                    username: fields.username,
                    password: fields.password,
                    password2: fields.password,
                    email: fields.email,
                    first_name: fields.firstname,
                    last_name: fields.lastname
                }).then(() => {
                    resolve();
                }, (error) => {
                    reject(error);
                });
            axios.post(BASE_URL + 'token/',
                {
                    username: fields.username,
                    password: fields.password,
                }).then((response) => {
                    commit('LOGIN', response.data.token);
                    resolve();
                }, (error) => {
                    reject(error);
                });
        });
    },
    getProfile({ commit }, id) {
        return new Promise((resolve, reject) => {
            if (state.profiles[id] !== undefined) {
                resolve(state.profiles[id]);
            } else {
                axios.get(BASE_URL + "user/"+id+"/").then((response) => {
                    commit('ADDPROFILE', response.data);
                    resolve(state.profiles[id]);
                }, (error) => {
                    reject(error);
                })
            }
        });
    },
    passwordResetLink({commit}, fields) {
        return new Promise((resolve, reject) => {
                axios.post(BASE_URL + "password_reset", {email: fields.email}).then(() => {
                    commit('LOGOUT');
                    resolve();
                }, (error) => {
                    reject(error);
                })
        });
    },
    passwordReset({commit}, fields) {
        return new Promise((resolve, reject) => {
                axios.post(BASE_URL + "password_reset/confirm/", fields).then(() => {
                    commit('LOGOUT');
                    resolve();
                }, (error) => {
                    reject(error);
                })
        });
    },
    filter({ commit }, filter) {
        commit('FILTER', filter);
    },
}

//to handle mutations
const mutations = {
    LOGIN(state, token) {
        state.token = token;
        localStorage.setItem("token", token);
    },
    LOGOUT(state) {
        state.token = "";
        localStorage.setItem("token", "");
    },
    initialiseStore(state) {
        if (localStorage.getItem('token') != null) {
            state.token = localStorage.getItem('token');
        }
    },
    ADDPROFILE(state, profile) {
        state.profiles[profile.id] = profile;
    },
    FILTER(state, filter) {
        state.filter = filter;
    }
}

//export store module
export default new Vuex.Store({
    state,
    getters,
    actions,
    mutations
})