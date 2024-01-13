<script>
export default {
  name: "v-input",
  data () {
    return {
      newValue: '',
      isError: false,
    }
  },
  props: {
    id: String,
    placeholder: String,
    type: String,
    name: String,
    modelValue: [String, Number],
    message: String,
  },
  methods: {
    updateInput(event) {
      this.newValue = event.target.value;
      this.$emit('update:modelValue', event.target.value);
      // console.log(this.isError);
      if (this.newValue === '') {
        this.isError = true;
      } else {
        this.isError = false;
      }
    }
  }
}
</script>

<template>
  <div class="v-input">
    <label class="v-input__label" :class="{error: isError}">
      <input
          :id="id"
          :type="type"
          class="v-input__item"
          placeholder=""
          :value="modelValue"
          @input="updateInput"
      >
      <div class="v-input__text">
        {{ placeholder }}
      </div>
      <span class="v-input__message">{{ message }}</span>
    </label>
  </div>
</template>

<style lang="scss">
@import "@/assets/css/vars";
.v-input {
  width: 400px;

  &__label {
    width: 100%;
    position: relative;
    display: block;
  }
  &__label.error &__item {
    border-color: $error-color-200;
    background: $error-color-100;
  }
  &__label.error &__message {
    display: inline-block;
  }
  &__label.error &__text:after {
    background: $error-color-100;
  }
  &__text {
    @include text($size: $font-size-md, $color: $primary-color-900);
    line-height: 100%;
    position: absolute;
    top: 50%;
    left: 24px;
    right: auto;
    transition: .3s;
    display: block;
    transform: translateY(-50%);
    z-index: 0;
    cursor: text;
    &:after {
      content: '';
      position: absolute;
      top: 50%;
      left: 0;
      width: 100%;
      height: 50%;
      background: $primary-color-100;
      z-index: -1;
      display: none;
    }
  }
  &__item {
    width: 100%;
    border: 2px solid $primary-color-200;
    background: $primary-color-100;
    padding: $padding*3 $padding*6;
    border-radius: $border-radius*2;
    @include text($size: $font-size-md, $color: $primary-color-900);
  }
  &__label.error &__item:focus ~ &__text,
  &__label.error &__item:focus-visible ~ &__text,
  &__label.error &__item:focus-within ~ &__text,
  &__label.error &__item:not(:placeholder-shown) ~ &__text {
    @include text($size: $font-size-sm, $color: $error-color-300);
  }
  &__item:focus ~ &__text,
  &__item:focus-visible ~ &__text,
  &__item:focus-within ~ &__text,
  &__item:not(:placeholder-shown) ~ &__text {
    @include text($size: $font-size-sm, $color: $primary-color-300);
    line-height: 100%;
    top: 0;
    transition: .2s;
    cursor: default;
    &:after {
      display: block;
    }
  }
  &__message {
    position: absolute;
    top: calc(100% + $padding);
    left: 0;
    width: 100%;
    display: none;
    @include text($size: $font-size-xs, $color: $error-color-500);
  }
}
</style>