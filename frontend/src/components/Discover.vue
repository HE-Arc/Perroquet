<template>
  <div > <p>{{this.$store.state.messages}}</p>
    <message v-for="message in this.$store.state.messages"
    :key="message.id"
    v-bind:text="message.content"
    v-bind:author="message.username"
    v-bind:>

    </message>
</div>

</template>

<script>
import Message from "@/components/Message";
export default {
  name: "Discover",
  components: {Message},
  beforeMount() {
      this.$store.dispatch("requestDiscover", "test");
  }

}
</script>

<style scoped>

</style>