<template>
  <v-container>
    You are being disconnected.
  </v-container>
</template>

<script>
export default {
  name: "Logout",
  mounted() {
    this.$store.dispatch("logout");
    this.$router.push("/index");
  }
};
</script>

<style scoped>
</style>