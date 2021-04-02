<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-card outlined elevation="10">
          <v-card-title>Sign in</v-card-title>
          <v-card-text>
            
          </v-card-text>
          <v-card-actions>
              
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

export default {
  name: "Profile",

  data: () => ({
    
  }),
  computed: {
      profile() {
          var p = null;
          this.$store.dispatch("getProfile", this.$route.params.token).then(
              (p) => {
                  
              }
          );
      }
  },
  methods: {

  },
};
</script>

<style scoped>
</style>