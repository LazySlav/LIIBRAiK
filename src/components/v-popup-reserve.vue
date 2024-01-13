<script>
import VButton from "@/components/v-button.vue";
import VInput from "@/components/v-input.vue";
export default {
  name: "v-popup-reserve",
  components: {
    VButton, VInput
  },
  data() {
    return {
      dateValue: '',
    }
  },
  props: {
    modelValue: String,
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
    updateInput () {
      this.$emit('update:modelValue', this.dateValue);
      this.hidePopup();
    }
  }
}
</script>

<template>
  <div class="v-popup" v-if="showPopup" @click="hidePopup">
    <form class="v-popup__cont" @click.stop>
      <h3>
        Резервирование
      </h3>
      <div class="v-popup__text">
        <p>К какому дню Вы придете за книгой?</p>
      </div>
      <v-input
        class="v-popup-reserve__input"
        placeholder="Введите дату в формате 00/00/0000"
        message="Поле должно быть заполнено"
        type="text"
        id="dateInput"
        :value="modelValue"
        v-model="dateValue"
      />
      <div class="v-popup__bottom">
        <v-button
            class-color="error"
            class="v-popup__button"
            @click="hidePopup"
        >Отменить</v-button>
        <v-button
            @click.prevent="updateInput"
            class-color="primary"
            class="v-popup__button"
        >Зарезирвировать</v-button>
      </div>
    </form>
  </div>
</template>

<style lang="scss">
@import "../assets/css/_vars.scss";
.v-popup-reserve__input {
  width: 100%;
  margin-bottom: $margin*6;
}
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
    margin-bottom: $margin*3;
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