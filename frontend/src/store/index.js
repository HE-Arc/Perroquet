import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

const BASE_URL = process.env.VUE_APP_BASEURL

//to handle state
const state = {
    token: ""

}

//to handle state
const getters = {
    authenticated: state => {
        return state.token!=""
    }
}

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
                    commit('LOGIN', response.data.token);
                    resolve();            
            } , (error) => {
                reject(error);
            });
        });
    },
    logout({commit}){
        commit('LOGOUT');
        this.$router.push("index")
    },
}

//to handle mutations
const mutations = {
    LOGIN(state, token) {
        state.token = token;
        localStorage.setItem("token", token);
    },
    LOGOUT(state){
        state.token = "";
        localStorage.setItem("token", "");
    },
    initialiseStore(state) {
        if (localStorage.getItem('token')!=null) {
          state.token = localStorage.getItem('token');
        }
      },
}

//export store module
export default new Vuex.Store({
    state,
    getters,
    actions,
    mutations
})