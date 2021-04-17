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
  </v-container>
</template>

<script>
import Message from "@/components/Message";
import Filters from "@/components/Filters";
import NewMessage from '@/components/NewMessage.vue';

export default {
  name: "Friends",
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
  methods: {
    requestMessages() {
      this.$store.dispatch("requestFriends", "test");
    }
  },


}
</script>

<style scoped>

</style>