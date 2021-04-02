<template>
  <v-card outlined elevation="10">
    <v-card-title>
      <router-link to="/profile" class="profileLink">
        <v-avatar>
          <v-img :src="avatar" contain></v-img>
        </v-avatar>
        <span class="pa-4">{{ author }}</span></router-link>


      <v-spacer></v-spacer>
      <v-btn plain v-on:click="$emit('updateLike')">
        <span>{{ likes }}</span>
        <v-icon class="ma-2">{{ getLikeIcon()}}</v-icon>
      </v-btn>

    </v-card-title>
    <v-card-text>
      <p class="text-justify">{{ text }}</p>
      <v-img :src="img"></v-img>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "Message",
  props: {
    text: String,
    img: String,
    likes: Number,
    author: String,
    avatar: String,
    id: Number,
    liked: Boolean,
  },
  data: () => ({
  }),

  methods: {

    getLikeIcon(){
      return this.liked ? "mdi-heart" : "mdi-heart-outline"
    },

  }
}
</script>

<style scoped>
.profileLink{
  text-decoration: none;
  color: inherit;
}

</style>