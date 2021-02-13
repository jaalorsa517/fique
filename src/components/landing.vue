<template lang="pug">
    .landing
        h1 ASOMUFI
        carousel(:listImg="listImg")
        p La linea de aseo FIQUE, son productos fabricados por la Asociación de Mujeres Fiqueras (ASOMUFI) del Municipio de Támesis (Antioquia), donde su ingrediente principal es el jugo de la hoja de Fique, mezclado con aceite reciclado de cocina, brindando multiples beneficios, a nivel doméstico e industrial.
        p 
            b Producto biodegradable, 100% artesanal.
</template>

<script>
import Vue from "vue";
import Carousel from "@/components/carousel.vue";
import c1 from "@/assets/cuadrado.png";
import c2 from "@/assets/cuadrado-1.png";
import c3 from "@/assets/cuadrado-2.png";
import c4 from "@/assets/cuadrado-3.png";
import c5 from "@/assets/cuadrado-4.png";
import c6 from "@/assets/cuadrado-5.png";

export default Vue.extend({
  name: "landing",
  data: function() {
    return {
      listImg: [
        {
          img: c1,
          des: "Jabon lavaplatos"
        },
        { img: c2, des: "Limpiahornos" },
        { img: c3, des: "Jabón Líquido" },
        { img: c4, des: "Jabón Mascotas" },
        {
          img: c5,
          des: "Jabón multiusos grande"
        },
        {
          img: c6,
          des: "Jabón multiusos pequeño"
        }
      ]
    };
  },
  components: {
    Carousel
  }
});
</script>

<style lang="stylus">
p
  color $color-font
  text-align center
</style>
