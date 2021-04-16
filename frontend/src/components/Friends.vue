<template>
<div>
  <new-message v-on:new="requestMessages()"></new-message>
  <div v-if="!messagesAvailable">
    No message to show you yet.
  </div>
  <div v-if="messagesAvailable">
    <filters v-on:input="requestMessages()"></filters>
    <message v-for="message in this.$store.state.messages"
    :key="message.id"
    :message="message">

    </message>
  </div>
</div>

</template>

<script>
import Message from "@/components/Message";
import Filters from "@/components/Filters";
import NewMessage from '@/components/NewMessage.vue';
export default {
  name: "Friends",
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
this.$store.dispatch("requestFriends", "test");
    }
  },



}
</script>

<style scoped>

</style>