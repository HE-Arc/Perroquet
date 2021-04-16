<template>
    <v-row class="text-center">
      <v-col v-if="profilsAvailable" cols="12">
        <mini-profile v-for="profile in profiles" :key="profile.following.id" :user="profile.following"></mini-profile>
      </v-col>
      <v-col v-if="!profilsAvailable" cols="12">
        Nothing to show yet.
      </v-col>
    </v-row>
</template>

<script>
import MiniProfile from "@/components/MiniProfile";
export default {
  components: { MiniProfile },
  name: "Follow",

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
    this.$store.dispatch("getFollow", this.$route.params.pId).then(
      (p) => {
        vm.profiles = p;
      }
    );
  }
};
</script>

<style scoped>
</style>