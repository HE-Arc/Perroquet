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
        <message :message="message"></message>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-layout justify-center>
        <v-progress-circular
          v-if="loading"
          indeterminate
          color="primary"
        ></v-progress-circular>
        </v-layout>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Message from "@/components/Message";
import Filters from "@/components/Filters";
import NewMessage from '@/components/NewMessage.vue';

export default {
  name: "Friends",
  data: () => ({
    scrolledToBottom: false,
    loading: false
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
  beforeMount() {
    this.requestMessages()

  },
  mounted() {
    this.scroll()
  },
  methods: {
    requestMessages(next=false) {
      this.loading = true
      var vm = this
      this.$store.dispatch("requestFriends", next).then(() =>{vm.loading = false});
    },
    scroll() {
      window.onscroll = () => {
        let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;
        if (bottomOfWindow) {
          this.requestMessages(true);
        }
      };
    },
  },


}
</script>

<style scoped>

</style>