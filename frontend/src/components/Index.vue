<template>
  <div class="pt-5">
    <div v-if="messages && messages.length">
      <div class="card mb-3" v-for="message of messages" v-bind:key="message.id">
        <div class="row no-gutters">
          <div class="col-md-4">
            <svg class="bd-placeholder-img" width="200" xmlns="http://www.w3.org/2000/svg"
                 preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail">
              <title>{{ message.content }}</title>
              <rect width="100%" height="100%" fill="#55595c"/>
              <text x="50%" y="50%" fill="#eceeef" dy=".3em">{{ message.content.charAt(0) }}</text>
            </svg>
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">{{ message.content }}</h5>
              <p class="card-text">{{ message.content }}</p>
              <router-link :to="{name: 'edit', params: { id: message.id }}" class="btn btn-sm btn-primary">Edit
              </router-link>
              <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteSubscription(message)">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p v-if="messages.length == 0">No subscriptions</p>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "Index",
  data() {
    return {
      messages: []
    }
  },
  created() {
        this.all();
    },
    methods: {
        deleteSubscription: function(subscr) {
            if (confirm('Delete ' + subscr.name)) {
                axios.delete(`http://127.0.0.1:8000/api/messages/${subscr.id}`)
                    // eslint-disable-next-line no-unused-vars
                    .then( response => {
                        this.all();
                    });
            }
        },
        all: function () {
            axios.get('http://127.0.0.1:8000/api/messages/')
                .then( response => {
                    this.messages = response.data
                });
        }
    },
}
</script>

<style scoped>

</style>