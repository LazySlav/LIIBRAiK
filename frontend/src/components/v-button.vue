<script>
export default {
  components: {

  },
  props: {
    classSize: {
      type: String,
      default: 'mid',
      validator(value) {
        return ['large', 'mid', 'small'].includes(value)
      }
    },
    classColor: {
      type: String,
      default: 'neutral',
      validator(value) {
        return ['neutral', 'primary', 'success', 'warn', 'error'].includes(value)
      }
    },

  }
}
</script>

<template>
  <button :class="'v-button ' + classSize + ' ' + classColor">
    <slot></slot>
  </button>
</template>

<style lang="scss">
@import "../assets/css/_vars.scss";
  .v-button {
    border-radius: $border-radius*2;
    border: none;
    outline: none;
    cursor: pointer;
    transition: .4s;
    &:hover {
      transition: .3s;
    }
    &:active {
      transition: .1s;
    }
    &.disabled {
      cursor: default;
      pointer-events: none;
    }
  }
  .v-button.large {
    padding: $padding*4 $padding*8;
    @include text($size: $font-size-md);
  }
  .v-button.mid {
    padding: $padding*3 $padding*6;
    @include text($size: $font-size-md);
  }
  .v-button.small {
    padding: $padding*2.5 $padding*5;
    @include text($size: $font-size-sm);
  }
  .v-button.neutral {
    background: $neutral-color-500;
    color: $neutral-color-100;
    &:hover {
      background: $neutral-color-400;
    }
    &:active {
      background: $neutral-color-600;
    }
    &.disabled {
      background: $neutral-color-200;
    }
  }
  .v-button.primary {
    background: $primary-color-500;
    color: $primary-color-100;
    &:hover {
      background: $primary-color-400;
    }
    &:active {
      background: $primary-color-600;
    }
    &.disabled {
      background: $primary-color-200;
    }
  }
  .v-button.error {
    background: $error-color-500;
    color: $error-color-100;
    &:hover {
      background: $error-color-400;
    }
    &:active {
      background: $error-color-600;
    }
    &.disabled {
      background: $error-color-200;
    }
  }
  .v-button.warn {
    background: $warn-color-500;
    color: $warn-color-100;
    &:hover {
      background: $warn-color-400;
    }
    &:active {
      background: $warn-color-600;
    }
    &.disabled {
      background: $warn-color-200;
    }
  }
  .v-button.success {
    background: $success-color-500;
    color: $success-color-100;
    &:hover {
      background: $success-color-400;
    }
    &:active {
      background: $success-color-600;
    }
    &.disabled {
      background: $success-color-200;
    }
  }
</style>