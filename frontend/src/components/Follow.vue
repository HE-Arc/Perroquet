<template>
<div>
  <div v-if="profilsAvailable">
    <v-row v-for="profile in profiles" :key="profile.following.id" class="text-center">
      <v-col cols="12">
        <mini-profile :user="profile.following"></mini-profile>
      </v-col>
    </v-row>
  </div>
  <div v-if="!profilsAvailable">
    <v-row>
      <v-col cols="12">
        Nothing to show yet.
      </v-col>
    </v-row>
  </div>
</div>
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