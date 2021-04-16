<template>
  <div >
    <filters v-on:input="requestMessages()"></filters>
    <message v-for="message in this.$store.state.messages"
    :key="message.id"
    v-bind:text="message.content"
    v-bind:author="message.user.username"
    v-bind:avatar="message.user.profile.image">

    </message>
</div>

</template>

<script>
import Message from "@/components/Message";
import Filters from "@/components/Filters";
export default {
  name: "Discover",
  components: {Filters, Message},
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