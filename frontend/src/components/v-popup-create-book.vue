<script>
import VInput from "@/components/v-input.vue";
import VButton from "@/components/v-button.vue";

 export default {
   name: 'v-popup-create-book',
   components: {
     VButton,
     VInput,

   },
   data() {
     return {
       valueTitle: '',
       valueAuthor: '',
       valueYear: '',
       valuePlace: '',
       valueVolume: '',
       valueId: '',
       valueAvailability: Boolean,
     }
   },
   props: {
     valueTitleModel: String,
     valueAuthorModel: String,
     valueYearModel: String,
     valuePlaceModel: String,
     valueVolumeModel: String,
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
   }
 }
</script>

<template>
  <div class="v-popup" v-if="showPopup" @click="hidePopup">
    <div class="v-popup__cont" @click.stop>
      <h3>
        Добавить книгу
      </h3>
      <form class="v-popup__form">
        <v-input
          class="v-popup__form-input"
          placeholder="Введите название"
          type="text"
          name="title"
          message="Поле должно быть заполнено!"
          v-model="valueTitle"
          :model-value="valueTitleModel"
          @input="updateInput('valueTitleModel', valueTitle)"
        />
        <v-input
          class="v-popup__form-input"
          placeholder="Введите автора"
          type="text"
          name="author"
          message="Поле должно быть заполнено!"
          v-model="valueAuthor"
          :model-value="valueAuthorModel"
          @input="updateInput('valueAuthorModel', valueAuthor)"
        />
        <v-input
          class="v-popup__form-input"
          placeholder="Введите год"
          type="text"
          name="year"
          message="Поле должно быть заполнено!"
          v-model="valueYear"
          :model-value="valueYearModel"
          @input="updateInput('valueYearModel', valueYear)"
        />
        <v-input
          class="v-popup__form-input"
          placeholder="Введите место издания"
          type="text"
          name="place"
          message="Поле должно быть заполнено!"
          v-model="valuePlace"
          :model-value="valuePlaceModel"
          @input="updateInput('valuePlaceModel', valuePlace)"
        />
        <v-input
          class="v-popup__form-input"
          placeholder="Введите объем"
          type="text"
          name="volume"
          message="Поле должно быть заполнено!"
          v-model="valueVolume"
          :model-value="valueVolumeModel"
          @input="updateInput('valueVolumeModel', valueVolume)"
        />
        <v-input
          class="v-popup__form-input"
          placeholder="Введите идентификатор"
          type="text"
          name="id"
          message="Поле должно быть заполнено!"
          v-model="valueId"
          :model-value="valueIdModel"
          @input="updateInput('valueIdModel', valueId)"
        />
        <div class="v-popup__bottom">
          <v-button
              @click.prevent="hidePopup"
              class-color="success"
          >Добавить</v-button>
        </div>
      </form>

    </div>
  </div>

</template>

<style scoped lang="scss">
@import "../assets/css/_vars.scss";
.v-popup__bottom {
  display: flex;
  justify-content: center;
  margin-top: $margin*6;
}
.v-popup__form-input {
  width: 100%;
  margin-bottom: $margin*5;
}
</style>