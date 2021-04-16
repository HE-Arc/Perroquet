<template>
  <v-card outlined elevation="10">
    <v-card-text>
      <v-btn-toggle v-model="value" @change="change" tile group>
        <v-btn value="new"><v-icon left>mdi-clock-outline</v-icon> New </v-btn>
        <v-spacer></v-spacer>
        <v-btn value="hot"><v-icon left>mdi-arrow-up-bold</v-icon> Hot </v-btn>
        <v-spacer></v-spacer>
        <v-btn value="top"><v-icon left>mdi-heart</v-icon> Like </v-btn>
      </v-btn-toggle>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "Filters",

  data: () => ({
      value:"",
  }),
  methods: {
      change(e) {
        this.$store.dispatch("filter", e);
        this.$emit("input", e);
      },
  },
  mounted() {
      this.value = this.$store.state.filter;
  },
};
</script>

<style scoped>
</style>