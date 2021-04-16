<template>
  <v-app>

    <navigationbar></navigationbar>

    <v-main>
      <router-view/>
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
