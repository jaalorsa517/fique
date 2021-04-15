<template lang="pug">
  section.Dashboard
    button-dash(
      v-for="menu,key in menus" 
      :key="key" 
      :title="menu.title" 
      :colorBack="menu.color"
      @buttonClick="onClick"
    )
</template>

<script lang="ts">
import Vue from "vue";
import buttonDash from "@/components/buttonDash.vue";

export default Vue.extend({
  components: {
    buttonDash
  },
  data: function() {
    return {
      menus: [
        { title: "Producto", color: "#F6A9BD" },
        { title: "Cliente", color: "#F4E0E1" },
        { title: "Pedido", color: "#FEE4A7" },
        { title: "Compra", color: "#86DBD4" },
        { title: "Gastos", color: "#95C9E1" }
      ]
    };
  },
  methods: {
    onClick: function() {}
  }
});
</script>

<style lang="stylus">
.Dashboard
  min-width 320px
  max-width 450px
  margin-top 50px
</style>
