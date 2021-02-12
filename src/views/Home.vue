<template lang="pug">
  .Home
    landing
    footer-app

</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import landing from "@/components/landing.vue";
import FooterApp from "@/components/footerApp.vue";

@Component({
  name: "Home",
  components: {
    landing,
    FooterApp
  }
})
export default class Home extends Vue {}
</script>

<style lang="stylus">
.landing
  margin-bottom 40px
</style>
