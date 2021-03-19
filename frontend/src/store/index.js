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
    login({commit}){
        axios.post( BASE_URL + 'token-auth/',
        {
            username: "test",
            password: "yo",
          
        }).then(response=>{
            if(response.status==400){
                console.log(response);
            }else if(response.status==200){
                console.log(response);
                commit('SET_TOKEN', response.data.token);
                commit('SET_AUTHENTICATED', true);
            }
            
        }).catch(e => {
            //affichage erreur
            this.errors.push(e)
        })
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