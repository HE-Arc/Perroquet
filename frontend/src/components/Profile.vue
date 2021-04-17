<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-card outlined elevation="10">
          <v-card-title>
            <v-avatar>
              <v-img :src="profile.profile.image"></v-img>
            </v-avatar>
            <v-file-input
                v-if="edit"
                accept="image/png, image/jpeg, image/bmp, image/gif"
                placeholder="New Profile Picture"
                prepend-icon="mdi-camera"
                label="New Profile Picture"
                @change="selectFile"
            ></v-file-input>
            <span v-if="!edit" class="pa-4">{{ profile.username }}</span>
            <v-text-field v-if="edit" label="Username" v-model="profile.username" :rules="usernameRules"
                          outlined></v-text-field>
            <v-spacer></v-spacer>
            <v-btn v-if="ownProfile && !edit" @click="edit=true">Edit</v-btn>
            <v-btn v-if="ownProfile && edit" @click="saveProfile()">Save</v-btn>
            <v-btn v-if="!ownProfile && !profile.followed" @click="follow">Follow</v-btn>
            <v-btn v-if="!ownProfile && profile.followed" @click="unfollow">Unfollow</v-btn>
          </v-card-title>
          <v-card-text>
            <v-spacer></v-spacer>
            <router-link :to="'/follower/' + profile.id" class="profileLink">
              {{ profile.followers_count }} Followers
            </router-link>
            <router-link :to="'/follow/' + profile.id" class="profileLink">
              {{ profile.follow_count }} Follow
            </router-link>
            <br><br>
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
        <new-message v-if="ownProfile" v-on:new="reload()"></new-message>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <filters v-on:input="reload()"></filters>
      </v-col>
    </v-row>
    <div v-if="messagesAvailable">
      <v-row v-for="message in messages" :key="message.id">
        <v-col>
          <message :message="message"/>
        </v-col>
      </v-row>
    </div>
    <v-row v-if="!messagesAvailable">
      <v-col>
        This account doesn't have any post yet.
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Filters from "@/components/Filters";
import Message from "@/components/Message";
import NewMessage from '@/components/NewMessage.vue';

export default {
  components: {Filters, Message, NewMessage},
  name: "Profile",

  data: () => ({
    edit: false,
    file: '',
    messages: [],

    profile: {
      id: 0,
      username: "",
      first_name: "",
      last_name: "",
      followed: false,
      profile: {
        id: 0,
        bio: "",
        image: ""
      },
      url: ""
    },
    usernameRules: [
      (v) => !!v || "username is required",
      (v) => v.length <= 30 || "maximum lenght is 30",
      (v) => v.length >= 5 || "minimum length is 5",
    ],
  }),
  computed: {
    ownProfile: function () {
      return this.$store.state.userId == this.profile.id
    },
    messagesAvailable: function () {
      // eslint-disable-next-line no-unused-vars
      for (var k in this.messages) {
        return true
      }
      return false;
    }
  },
  methods: {
    saveProfile: function () {
      var vm = this;

      var formdata = new FormData();
      formdata.append('id', vm.profile.id)
      formdata.append('username', vm.profile.username)
      formdata.append('profile.bio', vm.profile.profile.bio)

      if (vm.file != "") {
        formdata.append('profile.image', vm.file)
      }

      this.$store.dispatch("saveProfile", {data: formdata, id: vm.profile.id}).then(
          () => {
            vm.edit = false;
            this.$store.dispatch("getProfile", this.$route.params.pId).then(
                (p) => {
                  vm.profile = p;
                }
            );
          }
      );
    },
    reload() {
      var vm = this;
      this.$store.dispatch("getProfileMessages", this.$route.params.pId).then(
          (m) => {
            vm.messages = m;
          }
      )
    },
    selectFile(f) {
      this.file = f
    },
    follow() {
      var vm = this;
      this.$store.dispatch("follow", this.$route.params.pId).then(
          () => {
            vm.profile.followed = true;
            vm.profile.followers_count++
          }
      )
    },
    unfollow() {
      var vm = this;
      this.$store.dispatch("unfollow", this.$route.params.pId).then(
          () => {
            vm.profile.followed = false;
            vm.profile.followers_count--
          }
      )
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
  },
  watch: {
    '$route.params.pId': function (id) {
      var vm = this;
      this.$store.dispatch("getProfile", id).then(
          (p) => {
            vm.profile = p;
          }
      );
      this.$store.dispatch("getProfileMessages", id).then(
          (m) => {
            vm.messages = m;
          }
      )
    }
  }
};
</script>

<style scoped>
</style>