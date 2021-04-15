<template lang="pug">
  #app.app
    headApp
    router-view
</template>

<script lang="ts">
import Vue from "vue";
import headApp from "@/components/headApp.vue";

export default Vue.extend({
  name: "Asomufi",
  components: {
    headApp
  }
});
</script>

<style lang="stylus">
@import url('https://fonts.googleapis.com/css2?family=Bangers&family=Roboto:wght@400;700&display=swap');

body
  min-height 667px
  max-width 450px
  margin auto
  padding 0
  font-family 'Roboto' , sans-serif
  background $background
  background-repeat no-repeat

.app
  h1,h2,h3
    $font-bangers(2rem, $color-title)
    -webkit-text-stroke: 1px black
    text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25)
</style>
