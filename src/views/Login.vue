<template lang="pug">
    section.Login
        h1 Bienvenido
        h4 Ingrese los datos para iniciar sesión
        form
            label(for="username") Usuario
            input.username.input(type="text" name="username" autocomplete="off")
            label(for="password") Contraseña
            input.password.input(type="password" name="password")
            input.submit.input(type="button" value="INGRESAR" @click="$router.replace({name: 'Dashboard'})")
</template>

<style lang="stylus">
.Login
    margin-bottom 30vh
    $flex-ver()
    > h1
        margin-left $margin-left
        align-self flex-start
    > h4
        color $color-font
    > form
        display flex
        flex-direction column
        .submit
            width 50%
            padding 5px
            margin-top 30px
            align-self center
            font-weight bold
        .submit:hover
            cursor pointer
            transform scale(1.1)
        label
            font-size 0.8rem
        input
            margin-bottom 10px
            padding 5px
            border none
            outline none
            transition 500ms transform
            transform-origin center bottom 10px
            $redound-shadow($color-button)
        label, input
            color $color-font
        input:focus
            transform scale(1.1)
</style>
