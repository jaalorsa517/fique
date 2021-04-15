<template lang="pug">
  section.Home
    landing
    footer-app

</template>

<script lang="ts">
import Vue from "vue";
import landing from "@/components/landing.vue";
import FooterApp from "@/components/footerApp.vue";

export default Vue.extend({
  name: "Home",
  components: {
    landing,
    FooterApp
  }
});
</script>

<style lang="stylus">
.landing
  margin-bottom 40px
</style>
