<script>
import VButton from "@/components/v-button.vue";

export default {
  name: "v-popup-delete",
  components: {VButton},

  props: {
    showPopup: {
      type: Boolean,
      default: false,
    },
    book: {
      type: Object,
    },
    id: {
      type: Number,
    }
  },
  methods: {
    hidePopup() {
      this.$emit('update:showPopup', false);
    },
    removeBook() {
      this.$emit('remove', this.id);
      this.hidePopup();
    },
  }
}
</script>

<template>
  <div class="v-popup" v-if="showPopup" @click="hidePopup">
    <div class="v-popup__cont" @click.stop>
      <h3>
        Удаление книги
      </h3>
      <div class="v-popup__text">
        <p>Вы уверены, что хотите удалить книгу?</p>
      </div>
      <div class="v-popup__bottom">
        <v-button
            @click="removeBook"
            class-color="error"
            class="v-popup__button"
        >Удалить</v-button>
        <v-button class-color="primary" class="v-popup__button" @click="hidePopup">Отменить</v-button>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
@import "../assets/css/_vars.scss";
.v-popup {
  width: 100%;
  height: 100vh;
  background: rgba(4, 7, 17, 0.50);
  position: fixed;
  z-index: 10;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: center;

  &__cont {
    width: 400px;
    border-radius: $border-radius*2;
    background: $color-white;
    padding: $padding*8 $padding*6;

    h3 {
      padding-top: 0;
      padding-bottom: $padding*6;
    }
  }
  &__text {
    margin-bottom: $margin*6;
  }
  &__bottom {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-start;

  }
  &__button {
    margin-right: $margin*6;
  }
}
</style>