<template lang="pug">
  header
    img.close(
      v-show="isClose"
      src="/@/assets/boton-close.png"
      )
    .logo
      img.logo__img(src="@/assets/logo.png" alt="logo")
    button-head
        
</template>

<script lang="ts">
import Vue from "vue";
import buttonHead from "@/components/buttonHead.vue";

export default Vue.extend({
  name: "Head-App",
  components: {
    buttonHead
  },
  computed: {
    isClose: function() {
      return this.$store.getters.headersComponentesIsClose;
    }
  }
});
</script>

<style lang="stylus">
header
    display flex
    justify-content space-between
    margin 10px
    width 100%

.logo
    margin-left 35%


// @media screen and (min-width: 600px)
//     header
//         max-width 600px
//         margin auto
//     .logo
//         margin-left 40%
</style>
