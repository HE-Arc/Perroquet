<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-card outlined elevation="10">
          <v-card-title>Password reset</v-card-title>
          <v-card-text>
            <v-alert v-if="error" color="red" type="warning"
              >Unknown email.</v-alert
            >
            <v-alert v-if="success" color="green" type="success"
              >We have sent you a reset link.</v-alert
            >
            <v-form v-model="valid">
              <v-text-field
                v-model="fields.email"
                :rules="rules.emailRules"
                label="E-mail"
                required
              ></v-text-field>
            </v-form>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                type="submit"
                @click="submit"
                color="primary"
                :disabled="!valid"
                >Send me a reset link</v-btn
              >
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "PasswordResetLink",

  data: () => ({
    valid: false,
    error: false,
    success: false,

    fields: {
      email: "",
    },

    rules: {
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+/.test(v) || "E-mail must be valid",
      ],
    },
  }),
  methods: {
    submit() {
      this.$store
        .dispatch("passwordResetLink", this.fields)
        .then(() => {
          //TODO correct redirect
          this.success = true;
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