<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <mini-profile v-for="profile in profiles" :key="profile.id" :user="profile"></mini-profile>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import MiniProfile from "@/components/MiniProfile";
export default {
  components: { MiniProfile },
  name: "Profile",

  data: () => ({
    profiles: [] 
  }),
  computed: {
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