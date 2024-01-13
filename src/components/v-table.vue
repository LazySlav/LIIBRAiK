<script >
export default {
  name: 'v-table',

}
</script>

<template>
  <div class="v-table">
    <table class="v-table__item">
      <slot></slot>
    </table>
  </div>

</template>

<style lang="scss">
@import "@/assets/css/vars";
.v-table {
  width: 100%;
  background: $primary-color-100;
  border: 2px solid $primary-color-200;
  border-radius: $border-radius*2;
  padding: $padding*6 0;



  &__item {
    border-collapse: collapse;
  }
  &__block {
    padding: $padding*2 $padding;
    text-align: left;
    height: 100%;
    display: block;
  }
  td:first-child &__block, th:first-child &__block {
    padding-left: $padding*8;
  }
  td:last-child &__block, th:last-child &__block {
    padding-right: $padding*8;
  }
  th &__block {
    @include text($size: $font-size-md, $color: $primary-color-900);
    font-weight: normal;
    padding-bottom: $padding*6;
    padding-top: 0;
  }
  td &__block {
    @include text($size: $font-size-md, $color: $primary-color-900);
    font-weight: normal;
  }
  tr {
    height: auto;
  }
  //tbody tr:nth-child(2n + 1) &__block {
  //  background: $primary-color-200;
  //}
  tbody tr:nth-child(2n + 1) {
    background: $color-white;

  }
  tbody tr {
    transition: .3s;
    &:hover {
      transition: .1s;
      background: $primary-color-200;
    }
  }
  th {

  }
  th:nth-child(1) {
    width: 40%;
  }
  th:nth-child(2) {
    width: 15%;
  }
  th:nth-child(3) {
    width: 15%;
  }
  th:nth-child(4) {
    width: 10%;
  }
  th:nth-child(5) {
    width: 10%;
  }
  th:nth-child(6) {
    width: 10%;
  }
  td {
    vertical-align: center;
    height: 100%;

  }
}
</style>