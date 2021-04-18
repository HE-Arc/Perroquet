<template>
  <v-card outlined elevation="10">
    <router-link :to="'/message/'+message.replyTo" class="profileLink">
    <v-card-subtitle v-if="message.replyTo" class="py-0">
      <v-container>
        <v-row>
          <v-col md="auto" class="text-no-wrap pl-0">
            Replying to
            <router-link :to="'/profile/'+message.reply_info.user.id" class="profileLink">
              <v-avatar size="20">
                <v-img :src="message.reply_info.user.profile.image"></v-img>
              </v-avatar>
              <span class="pa-1">{{ message.reply_info.user.username }}</span></router-link>
            's message :
          </v-col>
          <v-col class="text-truncate px-0 font-weight-bold" style="max-width: min-content">
              {{ message.reply_info.content }}
          </v-col>
          <v-col md="auto" v-if="message.reply_info.image" class="px-0" style="max-width: min-content">
            <v-icon size="20">mdi-image</v-icon>
          </v-col>
        </v-row>
      </v-container>
    </v-card-subtitle></router-link>

    <v-card-title>
      <router-link :to="'/profile/'+message.user.id" class="profileLink">
        <v-avatar>
          <v-img :src="message.user.profile.image"></v-img>
        </v-avatar>
        <span class="pa-4">{{ message.user.username }}</span></router-link>
        <span class="pa-0 subtitle-2 font-weight-light">{{ new Date(message.date).toLocaleString()  }}</span>

      <v-spacer></v-spacer>
      <v-btn :disabled="!$store.getters.authenticated" plain v-on:click="like()">
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