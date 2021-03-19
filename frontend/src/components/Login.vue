<template>
  <v-card outlined elevation="10">
    <v-card-title>Login</v-card-title>
    <v-card-text>
      <v-alert v-if="error" color="red" type="warning">Incorrect username or password.</v-alert>
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
        <v-btn type="submit" @click="submit" color="primary" :disabled="!valid"
          >Login</v-btn
        >
      </v-card-actions>
    </v-card-text>
  </v-card>
</template>

<script>


export default {
  name: "Login",

  data: () => ({
    valid: false,
    passwordShow: false,
    error: false,

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
      this.$store.dispatch("login", this.fields).then(() => {
        //TODO correct redirect
        window.location.href = 'index';
      }).catch(()=>{
        this.error = true
      });
    },
  },
}
</script>

<style scoped>
</style>