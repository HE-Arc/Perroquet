<template>
  <div>
    <v-app-bar dense app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-app-bar-title>Perroquet</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn plain v-on:click="themeToogle()">
        <span></span>
        <v-icon class="ma-2">mdi-brightness-6</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app>
      <v-layout column fill-height>
        <router-link :to="'/'" class="profileLink">
          <v-card-title>
            <v-img :src="require('../assets/perroquet_logo/svg/Logo_DarkMagenta.svg')" height="64" width="64"
                   contain></v-img>
            <span class="pa-4">Perroquet</span>
          </v-card-title>
        </router-link>

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
        <v-list class="mb-12">
          <v-list-item link router :to="userLogin.link">
            <v-avatar v-if="userIsAuthenticated">
              <v-img :src="pp"></v-img>
            </v-avatar>
            <v-list-item-icon v-else>
              <v-icon>mdi-login</v-icon>
            </v-list-item-icon>
            <v-list-item-content class="pl-4">
              {{ userLogin.title }}
            </v-list-item-content>
          </v-list-item>

        </v-list>
      </v-layout>


    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  name: "Navigationbar",

  data: () => ({
    drawer: true,
    pp: "",
    username: ""
  }),

  computed: {
    navItems() {
      let navItems = [
        {icon: 'mdi-compass', title: 'Discover', link: '/discover'},
      ]
      if (this.userIsAuthenticated) {
        navItems = [
          {icon: 'mdi-home', title: 'Home', link: '/home'},
          {icon: 'mdi-compass', title: 'Discover', link: '/discover'},
          {icon: 'mdi-account-heart', title: 'Friends', link: '/friends'},
          {icon: 'mdi-cog', title: 'Settings', link: '/settings'},
          {icon: 'mdi-logout', title: 'Disconnect', link: '/logout'},
        ]
      }
      return navItems
    },
    userIsAuthenticated() {
      return this.$store.getters.authenticated
    },
    userLogin() {
      return this.userIsAuthenticated ? {title: this.username, link: "/profile"} : {title: "Login", link: "/login"}
    },
    userId() {
      return this.$store.state.userId
    }

  }, methods: {
    themeToogle() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
      this.$store.dispatch("toogleTheme", this.$vuetify.theme.dark)
    }
  },mounted() {
    this.$vuetify.theme.dark = this.$store.state.darkMode
    if (this.$store.getters.authenticated) {
      var vm = this
      this.$store.dispatch("getProfile", this.$store.state.userId).then((p) => {
        vm.pp = p.profile.image
        vm.username = p.username
      })
    }
  }, watch: {
    userId(id) {
      if (id != 0) {
        var vm = this
        this.$store.dispatch("getProfile", this.$store.state.userId).then((p) => {
          vm.pp = p.profile.image
          vm.username = p.username
        })
      }
    }
  }
}
</script>

<style scoped>
.profileLink {
  text-decoration: none;
  color: inherit;
}
</style>