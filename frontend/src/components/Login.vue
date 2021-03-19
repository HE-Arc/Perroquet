<template>
  <v-card outlined elevation="10">
    <v-card-title>Login</v-card-title>
    <v-card-text>
      <v-form v-model="valid">
        <v-text-field
            v-model="fields.username"
            :rules="rules.usernameRules"
            label="Username"
        ></v-text-field>
        <v-text-field
            v-model="fields.password"
            :append-icon="passwordShow ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="rules.passwordRules"
            :type="passwordShow ? 'text' : 'password'"
            label="Password"
            @click:append="passwordShow = !passwordShow"
        ></v-text-field>
      </v-form>

      <v-card-actions>
        <router-link to="/signin">Sign in</router-link>
        <v-spacer></v-spacer>
        <v-btn type="submit" @click="submit" color="primary" :disabled="!valid">Login</v-btn>
      </v-card-actions>
    </v-card-text>


  </v-card>
</template>

<script>

const BASE_URL = process.env.VUE_APP_BASEURL
import axios from 'axios';

export default {
  name: "Login",

  data: () => ({
    valid: false,
    passwordShow: false,

    fields: {
      username: '',
      password: '',
    },

    rules: {
      usernameRules: [
        v => !!v || 'Username is required',
      ],
      passwordRules: [
        v => !!v || 'Password is required',
      ],
    },
  }),
  methods: {
    submit() {
      axios.post( BASE_URL + 'token-auth/', {'Access-Control-Allow-Origin': '*',},
      {
          username: this.fields.username,
          password: this.fields.password,
          
      }).then(response=>{
          if(response.status==400){
            alert("Login incorrect");
          }else if(response.status==200){
            console.log(response);
          }
            
      }).catch(e => {
          //affichage erreur
          this.errors.push(e)
      })
    },
  },
}
</script>

<style scoped>

</style>