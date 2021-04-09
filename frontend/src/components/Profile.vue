<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-card outlined elevation="10">
          <v-card-title>
            <v-avatar>
              <v-img :src="profile.profile.image" contain></v-img>
            </v-avatar>
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
      this.$store.dispatch("saveProfile", vm.profile).then(
        () => {
          vm.edit=false;
        }
      );
    }
  },
  mounted() {
    var vm = this;
    this.$store.dispatch("getProfile", this.$route.params.pId).then(
      (p) => {
        vm.profile = p;
      }
    );
  }
};
</script>

<style scoped>
</style>