<script>
import VCont from "@/components/v-cont.vue";
export default {
  name: 'v-Header',
  components: {
    VCont
  },
  props: {

  }
}
</script>

<template>
  <header class="header">
    <v-cont>
      <div class="header__cont">
        <div class="header__col">
          <a href="/" class="header__logo">
            <img src="../assets/img/logo-header.png" alt="">
          </a>
        </div>
        <div class="header__col">
          <div class="header__row">
            <router-link to="/catalog" class="header__link">Каталог</router-link>
            <router-link to="/my-books" class="header__link">Мои книги</router-link>
            <router-link to="/profile" class="header__link">Профиль</router-link>
          </div>
        </div>
      </div>
    </v-cont>
  </header>
</template>

<style lang="scss">
@import "../assets/css/_vars.scss";

.header {
  width: 100%;
  background: #2843A4;
  padding: $padding*5 0;
  z-index: 5;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;

  &__cont {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  &__col {

  }

  &__row {

  }

  &__logo {
    display: block;
    height: 60px;
  }

  &__logo img {
    height: 100%;
  }

  &__link {
    display: inline-block;
    margin-right: $margin*8;
    position: relative;
    padding: $padding 0;
    overflow: hidden;
    @include text($size: $font-size-md, $color: $primary-color-100);

    &:hover {
      color: $primary-color-100;
    }
    &:after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      height: 1px;
      width: 100%;
      background: #EEF1FB;
      transition: .3s;
      transform: translateX(-110%);
    }

    &:hover:after {
      transform: translateX(0);
    }

    &:last-child {
      margin-right: 0;
    }

    &.router-link-active:after {
      transform: translateX(0);
    }
  }
}

</style>