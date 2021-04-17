<template>
  <v-container>
    <v-row>
      <v-col>
        <new-message v-on:new="requestMessages()"></new-message>
      </v-col>
    </v-row>
    <v-row v-if="!messagesAvailable">
      <v-col>
        No message to show you yet.
      </v-col>
    </v-row>
    <v-row v-if="messagesAvailable">
      <v-col>
        <filters v-on:input="requestMessages()"></filters>
      </v-col>
    </v-row>
    <v-row v-for="message in this.$store.state.messages" :key="message.id">
      <v-col>
        <new-message v-on:new="requestMessages()"></new-message>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Message from "@/components/Message";
import Filters from "@/components/Filters";
import NewMessage from '@/components/NewMessage.vue';

export default {
  name: "Discover",
  data: () => ({
    scrolledToBottom: false
  }),
  components: {Filters, Message, NewMessage},
  computed: {
    messagesAvailable: function () {
      // eslint-disable-next-line no-unused-vars
      for (var k in this.$store.state.messages) {
        return true
      }
      return false;
    }
  },
  mounted() {
    this.scroll()
  },
  beforeMount() {
    this.requestMessages()

  },
  methods: {
    requestMessages(next = false) {
      this.$store.dispatch("requestDiscover", next);
    },
    requestNextMessages() {
      this.$store.dispatch("requestNextMessages", "test");
    },
    scroll() {
      window.onscroll = () => {
        let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;
        if (bottomOfWindow) {
          this.requestMessages(true);
          console.log("bottom reached. loading next messages");
        }
      };
    },
  },


}
</script>

<style scoped>

</style>