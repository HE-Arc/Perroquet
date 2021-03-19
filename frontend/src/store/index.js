import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

const BASE_URL = process.env.VUE_APP_BASEURL

//to handle state
const state = {
    token: "",
    authenticated: false,

}

//to handle state
const getters = {}

//to handle actions
const actions = {
    login({commit}, fields){
        return new Promise((resolve, reject) => {
            axios.post( BASE_URL + 'token-auth/',
            {
                username: fields.username,
                password: fields.password,
            
            }).then( (response) =>{
                    console.log(response);
                    commit('SET_TOKEN', response.data.token);
                    commit('SET_AUTHENTICATED', true);
                    resolve();            
            } , (error) => {
                reject(error);
            });
        });
    },
}

//to handle mutations
const mutations = {
    SET_TOKEN(state, token) {
        state.token = token;
    },
    SET_AUTHENTICATED(state, authenticated) {
        state.authenticated = authenticated;
    },
}

//export store module
export default new Vuex.Store({
    state,
    getters,
    actions,
    mutations
})