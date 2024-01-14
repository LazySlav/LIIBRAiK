<script >
  export default {
    name: 'v-cont',
    props: {

    }
  }
</script>

<template>
  <div class="cont">
    <slot></slot>
  </div>
</template>

<style scoped>
  .cont {
    width: 1280px;
    margin: 0 auto;
  }
</style>