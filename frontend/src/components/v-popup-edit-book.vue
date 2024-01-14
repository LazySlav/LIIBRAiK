<script>
import VInput from "@/components/v-input.vue";
import VButton from "@/components/v-button.vue";

export default {
  name: 'v-popup-edit-book',
  components: {
    VButton,
    VInput,

  },
  data() {
    return {
      valueTitle: this.valueTitleModel,
      valueAuthor: this.valueAuthorModel,
      valueYear: this.valueYearModel,
      valuePlace: this.valuePlaceModel,
      valueVolume: this.valueVolumeModel,
      valueId: this.valueIdModel,
      valueAvailability: this.valueAvailabilityModel,
    }
  },
  props: {
    valueTitleModel: String,
    valueAuthorModel: String,
    valueYearModel: String,
    valuePlaceModel: String,
    valueVolumeModel: [String, Number],
    valueIdModel: String,
    valueAvailabilityModel: Boolean,

    showPopup: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    hidePopup() {
      this.$emit('update:showPopup', false);
    },
    updateInput(model, value) {
      this.$emit(`update:${model}`,  value);
    },
    editBook() {
      this.$emit(`update:valueTitleModel`,  this.valueTitle);
      this.$emit(`update:valueAuthorModel`,  this.valueAuthor);
      this.$emit(`update:valueYearModel`,  this.valueYear);
      this.$emit(`update:valuePlaceModel`,  this.valuePlace);
      this.$emit(`update:valuePlaceModel`,  this.valuePlace);
      this.$emit(`update:valuePlaceModel`,  this.valuePlace);
      this.$emit(`update:valuePlaceModel`,  this.valuePlace);
      this.$emit(`update:valueIdModel`,  this.valueId);

      this.hidePopup();
    },
    cancelEdit() {
      this.valueTitle = this.valueTitleModel;
      this.valueAuthor = this.valueAuthorModel;
      this.valueYear = this.valueYearModel;
      this.valuePlace = this.valuePlaceModel;
      this.valueVolume = this.valueVolumeModel;
      this.valueId = this.valueIdModel;
      this.valueAvailability = this.valueAvailabilityModel;

      this.hidePopup();
    }
  }
}
</script>

<template>
  <div class="v-popup" v-if="showPopup" @click="hidePopup">
    <div class="v-popup__cont" @click.stop>
      <h3>
        Редактировать книгу
      </h3>
      <form class="v-popup__form">
        <v-input
            class="v-popup__form-input"
            placeholder="Введите название"
            type="text"
            name="title"
            message="Поле должно быть заполнено!"
            v-model="valueTitle"
            :model-value="valueTitle"

        />
        <v-input
            class="v-popup__form-input"
            placeholder="Введите автора"
            type="text"
            name="author"
            message="Поле должно быть заполнено!"
            v-model="valueAuthor"
            :model-value="valueAuthor"

        />
        <v-input
            class="v-popup__form-input"
            placeholder="Введите год"
            type="text"
            name="year"
            message="Поле должно быть заполнено!"
            v-model="valueYear"
            :model-value="valueYear"

        />
        <v-input
            class="v-popup__form-input"
            placeholder="Введите место издания"
            type="text"
            name="place"
            message="Поле должно быть заполнено!"
            v-model="valuePlace"
            :model-value="valuePlace"

        />
        <v-input
            class="v-popup__form-input"
            placeholder="Введите объем"
            type="text"
            name="volume"
            message="Поле должно быть заполнено!"
            v-model="valueVolume"
            :model-value="valueVolume"

        />
        <v-input
            class="v-popup__form-input"
            placeholder="Введите идентификатор"
            type="text"
            name="id"
            message="Поле должно быть заполнено!"
            v-model="valueId"
            :model-value="valueId"
        />
        <div class="v-popup__bottom">
          <v-button
              class="v-popup__bottom-button"
              @click.prevent="editBook"
              class-color="success"
          >Редактировать</v-button>
          <v-button
              class="v-popup__bottom-button"
              @click.prevent="cancelEdit"
              class-color="primary"
          >Отменить</v-button>
        </div>
      </form>

    </div>
  </div>
</template>

<style scoped lang="scss">
@import "../assets/css/_vars.scss";
.v-popup__bottom {
  display: flex;
  justify-content: flex-start;
  margin-top: $margin*6;
  &-button {
    margin-right: $margin*4;
    &:last-child {
      margin-right: 0;
    }
  }
}
.v-popup__form-input {
  width: 100%;
  margin-bottom: $margin*5;
}
</style>