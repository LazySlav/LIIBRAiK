<script>
import VBreadcrumbs from "@/components/v-breadcrumbs.vue";
import VBlock from "@/components/v-block.vue";
import VButton from "@/components/v-button.vue";
import VPopupReserve from "@/components/v-popup-reserve.vue";
import VPopupEditBook from "@/components/v-popup-edit-book.vue";
import VPopupDelete from "@/components/v-popup-delete.vue";
export default {
  name: 'catalogItemView',
  components: {
    VBreadcrumbs,
    VBlock, VButton,
    VPopupReserve,
    VPopupEditBook,
    VPopupDelete,
  },
  data () {
    return {
      dialogVisible: false,
      showPopup: false,
      showPopupDelete: false,
      popupId: false,
      dateValue: '',

      isAdmin: true,

      id: 1,
      name: "Геодезический мониторинг движений земной коры (по материалам Кавказского региона). В. Р. Ященко, Х. К. Ямбаев",
      author: "Ященко В.Р. / Ямбаев Х.К.",
      year: 2007,
      place: "МИИГАиК М.",
      idBook: "РБ.6 Я 958",
      volume: "208",
      availability: true,

      breadcrumbs: [
        {
          path: '/catalog',
          name: 'Главная',
        },
        {
          path: '/catalog',
          name: 'Каталог',
        },
        {
          path: '/catalog/',
          name: 'Детальная страница книги',
        },
      ],

    }
  },
  methods: {
    showDialog() {
      this.dialogVisible = true;
    },
    showPopupEdit() {
      this.showPopup = true;
    },
    showPopupDel() {
      this.showPopupDelete = true;
    },
  }
}
</script>

<template>
  <div class="catalog-item">
    <v-breadcrumbs :breadcrumbs="breadcrumbs" />
    <div>
      <div>
        <div class="catalog-item__content">
          <h1>
            {{ this.name }}
          </h1>
          <div class="catalog-item__admin" v-if="isAdmin">
            <v-button
                class="catalog-item__admin-button"
                class-color="warn"
                class-size="mid"
                @click="showPopupEdit"
            >
              Редактировать
            </v-button>
            <v-button
              class="catalog-item__admin-button"
              class-color="error"
              class-size="mid"
              @click="showPopupDel"
            >
              Удалить
            </v-button>
          </div>
          <div class="catalog-item__body">
            <div class="catalog-item__col">
              <div class="catalog-item__img">
                <img src="@/assets/img/no-photo.svg" alt="">
              </div>
            </div>
            <div class="catalog-item__col">
              <v-block>
                <h3>
                  Информация о книге
                </h3>
                <div class="catalog-item__info">
                  <div class="catalog-item__info-line">
                    <div class="catalog-item__info-text">
                      Авторы
                    </div>
                    <div class="catalog-item__info-text">
                      {{ this.author }}
                    </div>
                  </div>
                  <div class="catalog-item__info-line">
                    <div class="catalog-item__info-text">
                      Кол-во страниц
                    </div>
                    <div class="catalog-item__info-text">
                      {{ this.volume }}
                    </div>
                  </div>
                  <div class="catalog-item__info-line">
                    <div class="catalog-item__info-text">
                      В наличии
                    </div>
                    <div
                        class="catalog-item__info-text"
                        v-if="this.availability"
                    >
                      <span class="color-success">
                        Есть
                      </span>
                    </div>
                    <div
                        class="catalog-item__info-text"
                        v-else
                    >
                      <span class="color-error">
                        Нет
                      </span>
                    </div>
                  </div>
                  <div class="catalog-item__info-line">
                    <div class="catalog-item__info-text">
                      Год и место издания
                    </div>
                    <div class="catalog-item__info-text">
                      {{ this.year }} {{ this.place }}
                    </div>
                  </div>
                </div>
              </v-block>
            </div>
          </div>
          <div class="catalog-item__bottom">
            <v-button
              @click="showDialog()"
              class-size="large"
              class-color="primary"
              :class="{disabled: this.availability}"
            >Зарезервировать</v-button>
            <v-popup-reserve
                v-model="dateValue"
                v-model:show-popup="dialogVisible"
            />
          </div>
        </div>
      </div>
    </div>


  </div>
  <div v-if="isAdmin">
    <v-popup-edit-book
        v-model:show-popup="showPopup"
        v-model:value-title-model="name"
        v-model:value-author-model="author"
        v-model:value-year-model="year"
        v-model:value-place-model="place"
        v-model:value-volume-model="volume"
        v-model:value-id-model="idBook"
    />
  </div>
  <v-popup-delete
      :id="this.id"
      v-model:show-popup="showPopupDelete"

  />

</template>

<style lang="scss">
@import "@/assets/css/vars";
.catalog-item {
  width: 100%;

  &__admin {
    width: 100%;
    padding: $padding*3 0;
    display: flex;
    align-items: center;
    justify-content: flex-start;

    &-button {
      margin-right: $margin*4;
    }
  }

  &__content {
    width: 100%;
  }
  &__body {
    padding: $padding*3 0;
    width: 100%;
    display: flex;
    align-items: flex-start;
    justify-content: space-between;

  }
  &__bottom {
    padding: $padding*3 0;
  }
  &__col {

    &:nth-child(1) {
      width: 400px;
    }
    &:nth-child(2) {
      width: calc(100% - 400px - $margin*6);

      h3 {
        padding-top: 0;
      }
    }
  }
  &__img {
    width: 100%;
    height: 400px;
    background: $color-white;
    border: 2px solid $primary-color-200;
    border-radius: $border-radius*2;
    display: flex;
    align-items: center;
    justify-content: center;
    
    img {
      max-width: 100%;
      max-height: 100%;
    }
  }
  &__info {
    width: 100%;
    padding-top: $padding*3;
  }
  &__info-line {
    width: 100%;
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    padding: $padding 0;
    &:first-child {
      padding-top: 0;
    }
    &:last-child {
      padding-bottom: 0;
    }
  }
  &__info-text {
    width: 50%;
    @include text($size: $font-size-md, $color: $primary-color-900);
    &:first-child {
      padding-right: $padding*2;
    }
  }
}
</style>