<template lang="pug">
    header
        .logo
            img.logo__img(src="@/assets/logo.png" alt="logo")
        .login
            .login__button
                span Ingresar
</template>

<style lang="stylus">
header
    display flex
    justify-content space-between
    margin 10px

.logo
    margin-left 35%
.login__button
    width 78px
    height 25px
    text-align center
    line-height 25px
    color $color-font
    background: $color-button
    box-shadow: 0px 4px 4px rgba(7, 7, 7, 0.45);
    border-radius: 10px;

@media screen and (min-width: 600px)
    header
        max-width 600px
        margin auto
    .logo
        margin-left 40%
    .login__button
        margin-top 10px
</style>
