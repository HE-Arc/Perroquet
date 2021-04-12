<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-card outlined elevation="10">
          <v-card-title>
            <v-avatar>
              <v-img :src="profile.profile.image" contain></v-img>
            </v-avatar>
            <v-file-input 
              v-if="edit"
              accept="image/png, image/jpeg, image/bmp"
              placeholder="New Profile Picture"
              prepend-icon="mdi-camera"
              label="New Profile Picture"
              @change="selectFile"
            ></v-file-input>
            <span v-if="!edit" class="pa-4">{{profile.username}}</span>
            <v-text-field v-if="edit" label="Username" v-model="profile.username" outlined></v-text-field>
            <v-spacer></v-spacer>
            <v-btn v-if="ownProfile && !edit" @click="edit=true">Edit</v-btn>
            <v-btn v-if="ownProfile && edit" @click="saveProfile()">Save</v-btn>
          </v-card-title>
          <v-card-text>
            <v-spacer></v-spacer>TODO follower<br>
            <p v-if="!edit" class="text-justify">{{ profile.profile.bio }}</p>
            <v-textarea label="bio" v-model="profile.profile.bio" v-if="edit" outlined></v-textarea>
          </v-card-text>
          <v-card-actions>
              
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <filters></filters>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        TODO add messages
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Filters from "@/components/Filters";
export default {
  components: { Filters },
  name: "Profile",

  data: () => ({
    edit: false,
    file: '',
    messages: null,

    profile: {
      id: 0,
      username: "",
      first_name: "",
      last_name: "",
      profile: {
        id: 0,
        bio: "",
        image: ""
      },
      url: ""
    }
  }),
  computed: {
    ownProfile: function() {
      //TODO replace
      // return this.$store.state.userId==this.profile.id
      return true;
    }
  },
  methods: {
    saveProfile: function() {
      var vm = this;

      var formdata = new FormData();
      formdata.append('id', vm.profile.id)
      formdata.append('username', vm.profile.username)
      formdata.append('profile.bio', vm.profile.profile.bio)

      if(vm.file!=""){
        formdata.append('profile.image', vm.file)
      }

      this.$store.dispatch("saveProfile", {data:formdata, id: vm.profile.id}).then(
        () => {
          vm.edit=false;
          this.$store.dispatch("getProfile", this.$route.params.pId).then(
            (p) => {
              vm.profile = p;
            }
          );
        }
      );
    },
    selectFile(f) {
      this.file=f
    }
  },
  mounted() {
    var vm = this;
    this.$store.dispatch("getProfile", this.$route.params.pId).then(
      (p) => {
        vm.profile = p;
      }
    );
    this.$store.dispatch("getProfileMessages", this.$route.params.pId).then(
      (m) => {
        vm.messages = m;
      }
    )
  }
};
</script>

<style scoped>
</style>