<template>
  <v-card outlined elevation="10">
    <v-card-title>
      <router-link :to="'/profile/'+message.user.id" class="profileLink">
        <v-avatar>
          <v-img :src="message.user.profile.image" contain></v-img>
        </v-avatar>
        <span class="pa-4">{{ message.user.username }}</span></router-link>


      <v-spacer></v-spacer>
      <v-btn plain v-on:click="like()">
        <span>{{ message.like_count }}</span>
        <v-icon class="ma-2">{{ likeIcon}}</v-icon>
      </v-btn>

    </v-card-title>
    <v-card-text>
      <p class="text-justify">{{ message.content }}</p>
      <v-img :src="message.image"></v-img>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "Message",
  props: {
    message:Object,
  },
  data: () => ({
  }),
  computed: {
    likeIcon : function(){
      return this.message.liked ? "mdi-heart" : "mdi-heart-outline"
    },
  },
  methods: {
    like(){
      this.message.liked=!this.message.liked
      if(this.message.liked){
        this.$store.dispatch("addLike", this.message.id)
        this.message.like_count++
      }else{
        this.$store.dispatch("removeLike", this.message.id)
        this.message.like_count--
      }
    }
  }
}
</script>

<style scoped>
.profileLink{
  text-decoration: none;
  color: inherit;
}

</style>