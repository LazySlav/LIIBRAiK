<script>
export default {
  name: 'v-block',

}
</script>

<template>
  <div class="v-block primary">
    <slot></slot>
  </div>
</template>

<style lang="scss">
@import "@/assets/css/vars";
.v-block {
  width: 100%;
  border-radius: $border-radius*2;
  padding: $padding*6 $padding*8;

}
.v-block.primary {
  background: $primary-color-100;
  border: 2px solid $primary-color-200;
  color: $primary-color-900;
}
.v-block.warn {
  background: $warn-color-100;
  border: 2px solid $warn-color-200;
  color: $warn-color-900;
}
.v-block.error {
  background: $error-color-100;
  border: 2px solid $error-color-200;
  color: $error-color-900;
}
.v-block.success {
  background: $success-color-100;
  border: 2px solid $success-color-200;
  color: $success-color-900;
}
.v-block.neutral {
  background: $neutral-color-100;
  border: 2px solid $neutral-color-200;
  color: $neutral-color-900;
}
</style>