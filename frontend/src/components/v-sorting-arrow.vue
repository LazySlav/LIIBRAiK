<script>
export default {
  name: 'v-sorting-arrow',
  props: {
    newValue: [String, Number],
    modelValue: [String, Number],
    isActive: Boolean,
  },
  methods: {
    sorting(value) {
      this.$emit("update:modelValue", value);
      this.$emit('click');
    }
  }
}
</script>

<template>
  <div @click="sorting(newValue)" class="sorting-block__item" :class="{ active: isActive }">
    <img src="@/assets/img/icon_arrow_black.svg" alt="">
  </div>
</template>

<style lang="scss">
@import "@/assets/css/vars";
.sorting-block__item {
  width: 100%;
  border: 2px solid $neutral-color-100;
  transition: .4s;
  border-radius: $border-radius;
  box-shadow: 1px 1px 3px rgba(0, 0, 0, .25);
  display: flex;
  align-items: center;
  justify-content: center;
  &:first-child {
    margin-bottom: $margin;
  }

  &:first-child img {
    transform: rotate(180deg);
  }

  img {
    width: 100%;
    user-select: none;
  }

  &:hover {
    transition: .2s;
    background: $color-white;
    border-color: $color-white;
    cursor: pointer;
  }
  &.active {
    background: $neutral-color-200;
    border-color: $neutral-color-200;
  }
}
</style>