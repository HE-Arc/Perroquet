<template>
  <div>
    <v-row>
      <v-col>
        <new-message v-on:new="requestMessages()"></new-message>
      </v-col>
    </v-row>
    <div v-if="!messagesAvailable">
      <v-row>
        <v-col>
          No message to show you yet.
        </v-col>
      </v-row>
    </div>
    <div v-if="messagesAvailable">
      <v-row>
        <v-col>
          <filters v-on:input="requestMessages()"></filters>
        </v-col>
      </v-row>
      <v-row v-for="message in this.$store.state.messages" :key="message.id">
        <v-col>
          <message :message="message"></message>
        </v-col>
      </v-row>
    </div>
    <div id="bottomPage"></div>
  </div>

</template>

<script>
import Message from "@/components/Message";
import Filters from "@/components/Filters";
import NewMessage from '@/components/NewMessage.vue';

export default {
  name: "Home",
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
    },
  },
  mounted() {
    this.scroll()
  },
  beforeMount() {
    this.requestMessages()

  },
  methods: {
    requestMessages(next = false) {
      this.$store.dispatch("requestHome", next);
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