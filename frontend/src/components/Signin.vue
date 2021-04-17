<template>
  <v-row class="text-center">
    <v-col cols="12">
      <v-card outlined elevation="10">
        <v-card-title>Sign in</v-card-title>
        <v-card-text>
          <v-alert v-if="error" color="red" type="warning">Error.</v-alert>
          <v-form v-model="valid">
            <v-text-field
                v-model="fields.firstname"
                :counter="30"
                :rules="rules.nameRules"
                label="Firstname"
                required
            ></v-text-field>
            <v-text-field
                v-model="fields.lastname"
                :counter="30"
                :rules="rules.nameRules"
                label="Lastname"
                required
            ></v-text-field>
            <v-text-field
                v-model="fields.username"
                :counter="30"
                :rules="rules.usernameRules"
                label="Username"
                required
            ></v-text-field>
            <v-text-field
                v-model="fields.email"
                :rules="rules.emailRules"
                label="E-mail"
                required
            ></v-text-field>
            <v-text-field
                v-model="fields.password"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show ? 'text' : 'password'"
                required
                :rules="rules.passwordRules"
                label="Password"
                hint="At least 8 characters"
                @click:append="show = !show"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="mr-4" @click="submit" :disabled="!valid"> Sign in</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>

export default {
  name: "Signin",

  data: () => ({
    valid: false,
    show: false,
    error: false,

    fields: {
      username: "",
      email: "",
      password: "",
      firstname: "",
      lastname: "",
    },
    rules: {
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+/.test(v) || "E-mail must be valid",
      ],
      usernameRules: [
        (v) => !!v || "username is required",
        (v) => v.length <= 30 || "maximum lenght is 30",
        (v) => v.length >= 5 || "minimum length is 5",
      ],
      passwordRules: [
        v => !!v || 'Password is required',
        v => (v && v.length >= 8) || 'Password must have 8+ characters',
        v => /(?=.*[A-Z])/.test(v) || 'Must have one uppercase character',
        v => /(?=.*\d)/.test(v) || 'Must have one number',
        v => /([-_!@$%+=])/.test(v) || 'Must have one special character [-_!@#$%+=]'
      ],
      nameRules: [
        v => !!v || 'Name is required',
        v => v.length >= 2 || 'Minimum length is 2',
      ]
    },
  }),

  methods: {
    submit() {
      this.$store.dispatch("register", this.fields).then(() => {
        this.$router.push("/profile");
      }).catch(() => {
        this.error = true
      });
    },
  },
};
</script>

<style scoped>
</style>