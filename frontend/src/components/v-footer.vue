<script>
import VCont from "@/components/v-cont.vue";
import VButton from "@/components/v-button.vue";
export default {
  name: 'v-footer',
  components: {
    VCont,
    VButton
  },
  props: {

  },
  data () {
    return {

    }
  },
  methods: {
    scrollToTop() {
      const element = document.getElementById('top');
      element.scrollIntoView({ behavior: 'smooth' });
    },
  },
}
</script>

<template>
  <div class="v-footer">
    <v-cont>
      <div class="v-footer__cont">
        <div class="v-footer__col">
          <span class="v-footer__logo">
            <img src="../assets/img/logo-header.png" alt="">
          </span>
        </div>
        <div class="v-footer__col">
          <div class="v-footer__text">
            Copyright <b>SAD Clowns</b>
          </div>
        </div>
        <div class="v-footer__col">
          <v-button
              class-color="primary"
              class-size="mid"
              @click="scrollToTop"
          >Наверх</v-button>
        </div>
      </div>
    </v-cont>
  </div>
</template>

<style lang="scss">
@import "../assets/css/_vars.scss";
.v-footer {
  width: 100%;
  background: $primary-color-800;
  padding: $padding*6 0;

  &__cont {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  &__logo {
    height: 60px;
    display: block;

    & > img {
      height: 100%;
    }
  }
  &__text {
    @include text($size: $font-size-xs, $color: $primary-color-100);
  }
}
</style>