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
        <v-btn type="submit" color="primary" :disabled="!valid">Submit</v-btn>
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
}
</script>

<style scoped>

</style>