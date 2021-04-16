<template>
  <v-app>

    <navigationbar></navigationbar>

    <v-main>
      <v-container>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Navigationbar from "@/components/NavigationBar";

export default {
  name: 'App',
  components: {Navigationbar},
  data: () => ({
    //
  }),
};
</script>
