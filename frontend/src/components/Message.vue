<template>
  <v-card outlined elevation="10">
    <v-card-title>
      <router-link :to="'/profile/'+message.user.id" class="profileLink">
        <v-avatar>
          <v-img :src="message.user.profile.image"></v-img>
        </v-avatar>
        <span class="pa-4">{{ message.user.username }}</span></router-link>


      <v-spacer></v-spacer>
      <v-btn plain v-on:click="like()">
        <span>{{ message.like_count }}</span>
        <v-icon class="ma-2">{{ likeIcon }}</v-icon>
      </v-btn>
      <v-btn plain :to="'/message/'+message.id">
        <span>{{ message.reply_count }}</span>
        <v-icon class="ma-2">mdi-comment-outline</v-icon>
      </v-btn>

    </v-card-title>
    <v-card-text>
      <p class="text-justify">{{ message.content }}</p>
      <!--      <v-img v-if="message.image" :src="message.image" :height="250" width="auto" contain position="left"></v-img>-->
      <v-dialog>
        <template v-slot:activator="{ on, attrs }">
          <v-img v-if="message.image" :src="message.image" :height="250" width="auto" contain position="left"
                 v-bind="attrs" v-on="on"></v-img>
        </template>

        <v-card>
          <v-card-title></v-card-title>
          <v-card-text>
            <v-img v-if="message.image" :src="message.image" contain position="center" max-height="80vh"></v-img>
          </v-card-text>
        </v-card>
      </v-dialog>
    </v-card-text>

  </v-card>
</template>

<script>
export default {
  name: "Message",
  props: {
    message: Object,
  },
  data: () => ({}),
  computed: {
    likeIcon: function () {
      return this.message.liked ? "mdi-heart" : "mdi-heart-outline"
    },
  },
  methods: {
    like() {
      this.message.liked = !this.message.liked
      if (this.message.liked) {
        this.$store.dispatch("addLike", this.message.id)
        this.message.like_count++
      } else {
        this.$store.dispatch("removeLike", this.message.id)
        this.message.like_count--
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