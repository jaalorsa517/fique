<template lang="pug">
    section.carousel
            .carousel__container
                .carousel-item(v-for="item,index in listImg" :key="index")
                    img(:src="item.img" :alt="item.des")
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "Carousel",
  props: {
    listImg: { type: Array, required: true }
  }
});
</script>

<style lang="stylus">

.carousel
    $flex-hor()
    position relative
    overflow auto

.carousel__container
    margin 5px 0
    padding 50px 10px
    white-space nowrap

.carousel-item
    display inline-block
    width 75px
    height 210px
    margin-right 10px
    position relative
    cursor pointer
    overflow hidden
    border-radius 15px
    transition 450ms all
    transform-origin center left

    img
        width 100%
        height 100%

.carousel-item:hover ~ .carousel-item
    transform translate3d(50px, 0, 0)

.carousel__container:hover
    .carousel-item:hover
        transform scale(1.5)
        opacity 1

    .carousel-item
        opacity 0.3
</style>
