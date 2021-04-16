<template>
  <v-container>
    <v-row class="text-center">
      <v-col v-if="profilsAvailable" cols="12">
        <mini-profile v-for="profile in profiles" :key="profile.user.id" :user="profile.user"></mini-profile>
      </v-col>
      <v-col v-if="!profilsAvailable" cols="12">
        Nothing to show yet.
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import MiniProfile from "@/components/MiniProfile";
export default {
  components: { MiniProfile },
  name: "Follower",

  data: () => ({
    profiles: [] 
  }),
  computed: {
    profilsAvailable: function() {
    // eslint-disable-next-line no-unused-vars
      for (var k in this.profiles){
        return true
      }
      return false;
    }
  },
  methods: {
  },
  mounted() {
    var vm = this;
    this.$store.dispatch("getFollower", this.$route.params.pId).then(
      (p) => {
        vm.profiles = p;
      }
    );
  }
};
</script>

<style scoped>
</style>