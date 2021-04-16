<template>
  <v-card outlined elevation="10">
    <v-card-title>
        Say something:
    </v-card-title>
    <v-card-text v-if="add">
        <v-alert v-if="error" color="red" type="warning">Error</v-alert>
        <v-form v-model="valid">
            <v-textarea
            v-model="fields.text"
            required
            auto-grow
            :rules="rules.textRule"
            label="Your message"
            hint="Write your text here"
            ></v-textarea>
            <v-file-input
              accept="image/png, image/jpeg, image/bmp"
              placeholder="Add an image"
              prepend-icon="mdi-image"
              label="Add an image"
              @change="selectFile"
            ></v-file-input>
        </v-form>
        </v-card-text>
        <v-card-actions v-if="add">
            <v-spacer></v-spacer>
        <v-btn class="mr-4" @click="submit" :disabled="!valid"> Save </v-btn>
        </v-card-actions>
        <v-card-actions v-if="!add">
            <v-spacer></v-spacer>
        <v-btn class="mr-4" @click="add=true"> Create a new post </v-btn>
        </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "NewMessage",
  data: () => ({
      valid: false,
      error: false,
      add: false,
      fields:{
          text: "",
          img: ""
      },
      rules: {
        textRule: [
            v => !!v || 'A message is required.',
            v => (v && v.length >= 2) || 'Your text must be at least 2 characters long.',
            v => (v && v.length <=500) || 'Your text must be shorter than 500 chars',
        ],
    },
  }),
  methods: {
      submit() {
        var vm = this;

        var formdata = new FormData();
        formdata.append('content', vm.fields.text)
        if(vm.fields.img!=""){
        formdata.append('image', vm.fields.img)
        }
        this.$store.dispatch("addMessage", formdata).then(
        () => {
          vm.$emit("new")
          vm.fields.text=""
          vm.fields.img=""
          vm.add=false
        }
      );
      },
    selectFile(f) {
      this.fields.img=f
    }
  }
}
</script>

<style scoped>

</style>