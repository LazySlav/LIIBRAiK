<script >
import VButton from "@/components/v-button.vue";
export default {
  name: 'v-pagination',
  components: {
    VButton,
  },
  methods: {
    goToPage(pageNumber) {
      this.$emit('update:modelValue', pageNumber);
    },
  },
  props: {
    currentPage: Number,
    pageCount: Number,
    modelValue: Number,
    displayCount: {
      type: Number,
      default: 5,
    },
  },
  computed: {
    displayedPages() {
      const pages = [];

      let start = Math.max(1, this.currentPage - Math.floor(this.displayCount / 2));
      let end = Math.min(this.pageCount, start + this.displayCount - 1);

      if (end - start + 1 < this.displayCount) {
        start = Math.max(1, end - this.displayCount + 1);
      }
      for (let i = start; i <= end; i++) {
        pages.push(i);
      }

      return pages;
    },
  },
}
</script>

<template>
  <div class="v-pagination">
    <v-button
      class-color="primary"
      class-size="small"
      class="v-pagination__button first-button"
      :class-disabled="(currentPage === 1)? 'disabled': ''"
      @click="goToPage(currentPage - 1)"
    >
      <img src="@/assets/img/icon_arrow_white.svg" alt="">
    </v-button>
    <v-button
      v-for="page in displayedPages"
      v-bind:key="page"
      class-color="primary"
      class-size="small"
      class="v-pagination__button"
      :class="(page === currentPage)? 'current-page': ''"
      @click="goToPage(page)"
    >{{ page }}</v-button>

    <v-button
        class-color="primary"
        class-size="small"
        class="v-pagination__button last-button"
        :class-disabled="(currentPage === pageCount)? 'disabled': ''"
        @click="goToPage(currentPage + 1)"
    >
      <img src="@/assets/img/icon_arrow_white.svg" alt="">
    </v-button>
  </div>
</template>

<style lang="scss">
@import "@/assets/css/vars";

.v-pagination {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding: $padding*3 0;

  &__button {
    margin-right: $margin*2;
    padding: 0;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    user-select: none;

    &:not(:hover) {
      background: $primary-color-200 !important;
    }
    &.current-page {
      background: $primary-color-500 !important;
      cursor: default;
      pointer-events: none;
    }

    &.last-button {
      img {
        transform: rotate(180deg);
      }
    }

    &:last-child {
      margin-right: 0;
    }

    img {
      height: 24px;
      user-select: none;
    }
  }
}
</style>