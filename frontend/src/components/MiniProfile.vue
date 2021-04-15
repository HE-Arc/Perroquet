<template>
  <v-card outlined elevation="10">
    <v-card-title>
      <router-link :to="'/profile/'+user.id" class="profileLink">
        <v-avatar>
          <v-img :src="user.profile.image" contain></v-img>
        </v-avatar>
        <span class="pa-4">{{ user.username }}</span>
      </router-link>
    </v-card-title>
    <v-card-text>{{ user.profile.bio }}</v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "MiniProfile",
  props: {
    user:Object,
  },
  data: () => ({

  }),
  computed: {
  },
  methods: {
  }
}
</script>

<style scoped>
.profileLink{
  text-decoration: none;
  color: inherit;
}
</style>