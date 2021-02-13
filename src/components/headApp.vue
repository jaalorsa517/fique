<template lang="pug">
    header
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
  }
});
</script>

<style lang="stylus">
header
    display flex
    justify-content space-between
    margin 10px

.logo
    margin-left 35%


@media screen and (min-width: 600px)
    header
        max-width 600px
        margin auto
    .logo
        margin-left 40%
</style>
