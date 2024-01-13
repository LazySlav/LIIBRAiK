<script >
  export default {

    props: {
      breadcrumbs: {
        type: Array,
        required: true
      }
    }
  }
</script>

<template>
  <div class="v-breadcrumbs">
    <router-link
        v-for="breadcrumb in breadcrumbs"
        v-bind:key="breadcrumb.name"
        :to="`${breadcrumb.path}`"
        class="v-breadcrumbs__item"
    >
      {{ breadcrumb.name }}
    </router-link>
  </div>

</template>

<style lang="scss">
@import "@/assets/css/vars";

.v-breadcrumbs {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  flex-wrap: wrap;
  padding: $padding*2 0;
  margin: 0 $margin*(-1);

  &__item {
    margin: $margin*1 $margin*1;
    padding-right: $padding*8;
    display: inline-block;
    align-items: center;
    position: relative;
    @include text($size: $font-size-sm, $color: $primary-color-900);
    font-weight: 500;
    cursor: pointer;
    transition: .4s;
    max-width: 75%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;

    &:hover {
      color: $primary-color-500;
      transition: .3s;
    }
    &:active {
      color: $primary-color-800;
      transition: .2s;
    }

    &:after {
      content: '';
      display: block;
      width: 16px;
      height: 2px;
      background: $primary-color-900;
      padding-right: $padding*2;
      position: absolute;
      bottom: 50%;
      right: 0;
    }

    &.router-link-active {
      color: $neutral-color-400;
      padding-right: 0;
      cursor: default;
      pointer-events: none;
      &:after {
        display: none;
      }
    }
  }
}
</style>