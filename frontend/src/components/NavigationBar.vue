<template>
  <v-navigation-drawer app>
    <v-layout column fill-height>
      <v-card-title>
        <v-img :src="require('../assets/perroquet_logo/svg/Logo_DarkMagenta.svg')" height="64" width="64"
               contain></v-img>
        <span class="pa-4">Perroquet</span>
      </v-card-title>

      <v-divider></v-divider>

      <v-list>
        <v-list-item
            v-for="[icon, text] in links"
            :key="icon"
            link
        >
          <v-list-item-icon>
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-spacer></v-spacer>
      <v-list>
        <v-list-item link>
          <v-list-item-icon>
            <v-icon>mdi-login</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Login
          </v-list-item-content>
        </v-list-item>

      </v-list>
    </v-layout>


  </v-navigation-drawer>
</template>

<script>
export default {
  name: "Navigationbar",

  data: () => ({
    links: [
      ['mdi-home', 'Home'],
      ['mdi-compass', 'Discover'],
      ['mdi-account-heart', 'Friends'],
      ['mdi-cog', 'Settings'],

    ],

  }),
}
</script>

<style scoped>

</style>