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
            hint="At least 8 characters"
            @click:append="passwordShow = !passwordShow"
        ></v-text-field>
      </v-form>

      <v-card-actions>
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
        v => (v && v.length >= 8) || 'Password must have 8+ characters',
        v => /(?=.*[A-Z])/.test(v) || 'Must have one uppercase character',
        v => /(?=.*\d)/.test(v) || 'Must have one number',
        v => /([-_!@$%+=])/.test(v) || 'Must have one special character [-_!@#$%+=]'
      ],
    },


  }),
}
</script>

<style scoped>

</style>