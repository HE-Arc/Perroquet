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
            v-for="item in navItems"
            :key="item.title"
            link
            router
            :to="item.link"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-spacer></v-spacer>
      <v-list>
        <v-list-item link router :to="userLogin.link">
          <v-avatar v-if="userIsAuthenticated"></v-avatar>
          <v-list-item-icon v-else>
            <v-icon >mdi-login</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            {{ userLogin.title }}
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

  computed: {
    navItems () {
      let navItems = [
        {icon: 'mdi-compass', title: 'Discover', link: '/'},
      ]
      if (this.userIsAuthenticated) {
        navItems = [
          {icon: 'mdi-home', title: 'Home', link: '/create'},
          {icon: 'mdi-compass', title: 'Discover', link: '/edit'},
          {icon: 'mdi-account-heart', title: 'Friends', link: '/'},
          {icon: 'mdi-cog', title: 'Settings', link: '/'},
        ]
      }
      return navItems
    },
    userIsAuthenticated () {
      return false
    },

    userLogin(){
      return this.userIsAuthenticated ? {title: "Username", link:"/profile"} : {title: "Login", link:"/login"}
    }

  }
}
</script>

<style scoped>

</style>