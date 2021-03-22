<template>
  <v-card outlined elevation="10">
    <v-card-title>
      <div>
        <v-avatar>
          <v-img :src="avatar" contain></v-img>
        </v-avatar>
        <span class="pa-4">{{ author }}</span></div>


      <v-spacer></v-spacer>
      <v-btn text>        <span>{{ likes }}</span>
        <v-icon class="ma-2">mdi-heart</v-icon></v-btn>




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
    avatar: String
  },
  data: () => ({}),
}
</script>

<style scoped>

</style>