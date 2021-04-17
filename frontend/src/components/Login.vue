<template>
    <v-row class="text-center">
      <v-col cols="12">
        <v-card outlined elevation="10">
          <v-card-title>Login</v-card-title>
          <v-card-text>
            <v-alert v-if="error" color="red" type="warning"
              >Incorrect username or password.</v-alert
            >
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
              <v-row>
                <v-col>
                  <v-btn
                    type="submit"
                    @click="submit"
                    color="primary"
                    :disabled="!valid"
                    >Login</v-btn
                  >
                  <v-spacer></v-spacer>
                  <router-link to="/signin"><v-btn>Sign in</v-btn></router-link> 
                  <router-link to="/passwordResetLink"><v-btn>Forgot your password?</v-btn></router-link>
                </v-col>
              </v-row>
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
</template>

<script>
export default {
  name: "Login",

  data: () => ({
    valid: false,
    passwordShow: false,
    error: false,

    fields: {
      username: "",
      password: "",
    },

    rules: {
      usernameRules: [(v) => !!v || "Username is required"],
      passwordRules: [(v) => !!v || "Password is required"],
    },
  }),
  methods: {
    submit() {
      this.$store
        .dispatch("login", this.fields)
        .then(() => {
          //TODO correct redirect
          this.$router.push("/index");
        })
        .catch(() => {
          this.error = true;
        });
    },
  },
};
</script>

<style scoped>
</style>