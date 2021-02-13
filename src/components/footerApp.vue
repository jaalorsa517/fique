<template lang="pug">
    .footer
        .icon
            img.icon__img(src="@/assets/contacto-icon.png", alt="contact icon")
        .contacts
            .contacts__telephone(class="contacts-container")
                .contacts__telephone--icon(class="contacts-child")
                    img(src="@/assets/telephone-icon.png" alt="telephone icon")
                .contacts__telephone--text(class="contacts-child")
                    span 3505439623
            .contacts__whatsapp(class="contacts-container")
                .contacts__whatsapp--icon(class="contacts-child")
                    img(src="@/assets/whatsapp-icon.png" alt="whatsapp icon")
                .contacts__whatsup--text(class="contacts-child")
                    span 3217637999
            .contacts__email(class="contacts-container")
                .contacts__email--icon(class="contacts-child")
                    img(src="@/assets/gmail-icon.png" alt="gmail icon")
                .contacts__email--text(class="contacts-child")
                    span livasesa72@gmail.com
</template>

<style lang="stylus">
.footer
    margin-top auto
    background-color rgba(0,0,0,0)
    $flex-hor()
    color $color-font

.contacts-container
    display flex
    justify-content flex-start

.contacts-child
    margin 2px 5px
</style>
