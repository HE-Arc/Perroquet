<template>
  <v-row class="text-center">
    <v-col cols="12">
      <v-card outlined elevation="10">
        <v-card-title>Password reset</v-card-title>
        <v-card-text>
          <v-alert v-if="error" color="red" type="warning">Error</v-alert>
          <v-form v-model="valid">
            <v-text-field
                v-model="fields.password"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show ? 'text' : 'password'"
                required
                :rules="rules.passwordRules"
                label="New password"
                hint="At least 8 characters"
                @click:append="show = !show"
            ></v-text-field>
            <v-text-field
                v-model="fields.password2"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show ? 'text' : 'password'"
                required
                :rules="[
                  v => !!v || 'Password is required',
                  v => fields.password === v || 'Password must match'
                ]"
                label="Password confirmation"
                @click:append="show = !show"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="mr-4" @click="submit" :disabled="!valid"> Save new password</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>

export default {
  name: "PasswordReset",

  data: () => ({
    valid: false,
    show: false,
    error: false,

    fields: {
      password: "",
      password2: "",
    },
    rules: {
      passwordRules: [
        v => !!v || 'Password is required',
        v => (v && v.length >= 8) || 'Password must have 8+ characters',
        v => /(?=.*[A-Z])/.test(v) || 'Must have one uppercase character',
        v => /(?=.*\d)/.test(v) || 'Must have one number',
        v => /([-_!@$%+=])/.test(v) || 'Must have one special character [-_!@#$%+=]'
      ],
    },
  }),

  methods: {
    submit() {
      this.$store.dispatch("passwordReset", {
        password: this.fields.password,
        token: this.$route.params.token
      }).then(() => {
        this.$router.push("/login");
      }).catch(() => {
        this.error = true
      });
    },
  },
};
</script>

<style scoped>
</style>