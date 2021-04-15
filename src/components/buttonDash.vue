<template lang="pug">
  .button-dash(:style="getBackColor" @click="$emit('buttonClick')")
    .title
      span {{title}}
    .amount(v-show="true")
      .back-redound {{amount}}
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  props: {
    title: { required: true, type: String },
    amount: { default: 0, type: Number },
    colorBack: { default: "#fff", type: String }
  },
  computed: {
    getBackColor: function() {
      return `background-color:${this.colorBack}`;
    }
  }
});
</script>

<style lang="stylus">
.button-dash
  display flex
  align-items center
  width 90%
  height 20px
  padding 15px
  margin 30px auto
  position relative
  text-align center
  line-height 0.7
  box-shadow 0px 4px 4px rgba(7, 7, 7, 0.45)
  border-radius 10px
  transition transform 800ms
  &:hover
    transform scale(1.1)
    cursor pointer
  .title
    flex-grow 4
    $font-bangers(1.3rem, $color-font)
  .amount
    width  20px
    height 20px
    padding 5px
    right 0
    top 0
    text-align center
    $font-bangers(1.3rem, $color-font)
    line-height 1
    border-radius 50%
    background-color $color-button
</style>
