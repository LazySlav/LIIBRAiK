<script>


  export default {
    name: 'errorView',

  }
</script>

<template>
  <div class="error-page">
    <div class="error-page__img">
      <img src="@/assets/img/404.svg">
    </div>
    <div class="error-page__text">
      <p>Страница не найдена. <router-link to="/catalog">Вернуться в каталог</router-link></p>
    </div>
  </div>
</template>

<style lang="scss">
@import "@/assets/css/vars";
.error-page {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: $padding*8 0;
}
.error-page__img {
  width: 500px;
  svg {
    width: 100%;
  }
}
.error-page__text {
  margin-top: $margin*6;
  p {
    padding: 0;
  }
}
</style>