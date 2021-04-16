<template>
    <v-row class="text-center">
      <v-col cols="12">
        <v-card outlined elevation="10">
          <v-card-title>Change your settings</v-card-title>
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
                v-model="fields.email"
                :rules="rules.emailRules"
                label="E-mail"
                required
              ></v-text-field>
              <v-text-field
                v-model="fields.opassword"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show ? 'text' : 'password'"
                :rules="rules.passwordRules"
                label="Enter old password to change it"
                hint="At least 8 characters"
                @click:append="show = !show"
              ></v-text-field>
              <v-text-field
                v-model="fields.npassword"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show ? 'text' : 'password'"
                :rules="rules.passwordRules"
                label="Enter new password to change it"
                hint="At least 8 characters"
                @click:append="show = !show"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
              <v-spacer></v-spacer>
            <v-btn class="mr-4" @click="submit" :disabled="!valid"> Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
</template>

<script>

export default {
  name: "Settings",

  data: () => ({
    valid: false,
    show: false,
    error: false,
    username: "",
    profileId:0,

    fields: {
      email: "",
      npassword: "",
      opassword: "",
      firstname: "",
      lastname: "",
    },
    rules: {
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+/.test(v) || "E-mail must be valid",
      ],
      passwordRules: [
        (v) => (v.length==0 || v.length >= 8) || 'Password must have 8+ characters',
        (v) => (v.length==0 || /(?=.*[A-Z])/.test(v)) || 'Must have one uppercase character',
        (v) => (v.length==0 || /(?=.*\d)/.test(v)) || 'Must have one number',
        (v) => (v.length==0 || /([-_!@$%+=])/.test(v)) || 'Must have one special character [-_!@#$%+=]'
      ],
      nameRules: [
        (v) => !!v || 'Name is required',
        (v) => (v && v.length >= 2) || 'Minimum length is 2',
      ]
    },
  }),

  methods: {
    submit() {
      var vm = this;

      var formdata = new FormData();
      formdata.append('id', this.$store.state.userId)
      formdata.append('username', vm.username)
      formdata.append('first_name', vm.fields.firstname)
      formdata.append('last_name', vm.fields.lastname)
      formdata.append('profile.id', vm.fields.profileId)

      formdata.append('email', vm.fields.email)
      
      this.$store.dispatch("saveProfile", {data:formdata, id: this.$store.state.userId}).then(
        () => {
          this.$store.dispatch("getProfile", this.$store.state.userId).then(
            (p) => {
                vm.fields.firstname = p.first_name;
                vm.fields.lastname = p.last_name;
                vm.fields.email = p.email;
                vm.username = p.username;
                vm.profileId = p.profile.id;
                vm.error=false
            }
          );
        }, 
      ).catch(() => {
        vm.error = true
      });

      this.$store.dispatch("changePassword", {old:vm.fields.opassword, new:vm.fields.npassword, id:vm.profileId}).then(
        () => {
          vm.fields.opassword = ""
          vm.fields.npassword = ""
        }
      ).catch(() => {
        vm.error = true
      });
    },
  },
  mounted(){
    var vm = this;
    this.$store.dispatch("getProfile", this.$store.state.userId).then(
      (p) => {
        vm.fields.firstname = p.first_name;
        vm.fields.lastname = p.last_name;
        vm.fields.email = p.email;
        vm.username = p.username;
        vm.profileId = p.profile.id;
      }
    );
  }
};
</script>

<style scoped>
</style>