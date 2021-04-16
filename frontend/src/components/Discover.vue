<template>
<div>
  <v-row><v-col>
    <new-message v-on:new="requestMessages()"></new-message>
  </v-col></v-row>
  <div v-if="!messagesAvailable">
    No message to show you yet.
  </div>
  <div v-if="messagesAvailable">
    <v-row><v-col>
      <filters v-on:input="requestMessages()"></filters>
    </v-col></v-row>
    <v-row v-for="message in this.$store.state.messages" :key="message.id">
      <v-col>
        <message :message="message"></message>
      </v-col>
    </v-row>
  </div>
</div>

</template>

<script>
import Message from "@/components/Message";
import Filters from "@/components/Filters";
import NewMessage from '@/components/NewMessage.vue';
export default {
  name: "Discover",
  components: {Filters, Message, NewMessage },
  computed: {
    messagesAvailable: function() {
    // eslint-disable-next-line no-unused-vars
      for (var k in this.$store.state.messages){
        return true
      }
      return false;
    }
  },
  beforeMount() {
    this.requestMessages()

  },
  methods: {
    requestMessages(){
this.$store.dispatch("requestDiscover", "test");
    }
  },



}
</script>

<style scoped>

</style>