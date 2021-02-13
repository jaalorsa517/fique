<template lang="pug">
  #app
    head-app
    router-view
</template>

<script lang="ts">
import Vue from "vue";
import HeadApp from "@/components/headApp.vue";

export default Vue.extend({
  name: "Asomufi",
  components: {
    HeadApp
  }
});
</script>

<style lang="stylus">
@import url('https://fonts.googleapis.com/css2?family=Bangers&family=Roboto:wght@400;700&display=swap');

body
  display flex
  height 100%
  flex-direction column
  margin 0
  padding 0
  font-family 'Roboto' , sans-serif
  background $background
  background-repeat no-repeat

#app
  h1,h2,h3
    font-family 'Bangers', cursive
    font-size 2rem
    color $color-title
    -webkit-text-stroke: 1px black
    text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25)
</style>
