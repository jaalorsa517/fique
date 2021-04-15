<template lang="pug">
    .login-button
        .to-house(v-if="$route.name !== 'Home'")
            router-link(to="/")
                img(src="@/assets/inicio-icon.png" alt="home icon")
        .login__button(v-else)
            router-link.ancle(to="Login") Ingresar
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "ButtonHead"
});
</script>

<style lang="stylus">

.to-house
    $size-square(24px)
    img
        $size-square(100%)

.login__button
    width 78px
    height 25px
    text-align center
    line-height 25px
    color $color-font
    $redound-shadow($color-button)

    .ancle
        text-decoration none
        color $color-font

.login__button, .to-house
    transition 500ms all

.login__button:hover , .to-house:hover
    transform scale(1.2)

// @media screen and (min-width: 600px)
//     .login__button,.to-house
//         margin-top 10px
</style>
