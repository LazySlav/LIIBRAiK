<script>
import VBreadcrumbs from "@/components/v-breadcrumbs.vue";
import VBlock from "@/components/v-block.vue";
import VButton from "@/components/v-button.vue";
import VPopupReserve from "@/components/v-popup-reserve.vue";
export default {
  name: 'catalogItemView',
  components: {
    VBreadcrumbs,
    VBlock, VButton,
    VPopupReserve
  },
  data () {
    return {
      dialogVisible: false,
      popupId: false,
      dateValue: '',

      breadcrumbs: [
        {
          path: '/',
          name: 'Главная',
        },
        {
          path: '/catalog',
          name: 'Каталог',
        },
      ],
      catalogValues: [
        {
          id: 1,
          name: "Геодезический мониторинг движений земной коры (по материалам Кавказского региона). В. Р. Ященко, Х. К. Ямбаев",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
          idBook: "РБ.6 Я 958",
          volume: "208",
          availability: true,
        },
        {
          id: 2,
          name: "Геодезия и картография на современном этапе развития 1919 - 1989. В. Р. Ященко, В. Д. Большаков , А.А.Дражнюк и др.",
          author: "Ященко В.Р. / Большаков В.Д. / Дражнюк и др. А.А.",
          year: 1989,
          place: "Недра М.",
          idBook: "РА.1 Г 367",
          volume: "160 ил.",
          availability: true,
        },
        {
          id: 3,
          name: "Геодезические исследования вертикальных движений земной коры. В. Р. Ященко",
          author: "Ященко В.Р.",
          year: 1989,
          place: "Недра М.",
          idBook: "ФИ.2 Я 985",
          volume: "192 ил.",
          availability: false,
        },
        {
          id: 4,
          name: "По геодезическим маршрутам. В. Р. Ященко",
          author: "Ященко В.Р.",
          year: 1990,
          place: "Недра М.",
          idBook: "РА Я 985",
          volume: "95 ил.",
          availability: false,
        },
        {
          id: 5,
          name: "Будни первопроходцев. В. Р. Ященко",
          author: "Ященко В.Р.",
          year: 2006,
          place: "ПКО \"Картография\" М.",
          idBook: "РА Я 958",
          volume: "163 ил.",
          availability: true,
        },
        {
          id: 6,
          name: "Геодезический мониторинг движений земной коры (по материалам Кавказского региона). В. Р. Ященко, Х. К. Ямбаев",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
          idBook: "РБ.6 Я 958",
          volume: 208,
          availability: true,
        },
        {
          id: 7,
          name: "Геодезический мониторинг движений земной коры (по материалам Кавказского региона). В. Р. Ященко, Х. К. Ямбаев",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
          idBook: "РБ.6 Я 958",
          volume: 208,
          availability: true,
        },
        {
          id: 8,
          name: "Геодезический мониторинг движений земной коры (по материалам Кавказского региона). В. Р. Ященко, Х. К. Ямбаев",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
          idBook: "РБ.6 Я 958",
          volume: 208,
          availability: true,
        },
        {
          id: 9,
          name: "Геодезический мониторинг движений земной коры (по материалам Кавказского региона). В. Р. Ященко, Х. К. Ямбаев",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
          idBook: "РБ.6 Я 958",
          volume: 208,
          availability: true,
        },
        {
          id: 10,
          name: "Геодезический мониторинг движений земной коры (по материалам Кавказского региона). В. Р. Ященко, Х. К. Ямбаев",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
          idBook: "РБ.6 Я 958",
          volume: 208,
          availability: true,
        },
      ],
    }
  },
  methods: {
    showDialog() {
      // this.popupId = id;
      this.dialogVisible = true;
    },
  }
}
</script>

<template>
  <div class="catalog-item">
    <v-breadcrumbs :breadcrumbs="breadcrumbs" />
    <div v-for="book in catalogValues" :key="book.id">
      <div v-if="book.id == $route.params.id">
        <div class="catalog-item__content">
          <h1>
            {{ book.name }}
          </h1>
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
                      {{ book.author }}
                    </div>
                  </div>
                  <div class="catalog-item__info-line">
                    <div class="catalog-item__info-text">
                      Кол-во страниц
                    </div>
                    <div class="catalog-item__info-text">
                      {{ book.volume }}
                    </div>
                  </div>
                  <div class="catalog-item__info-line">
                    <div class="catalog-item__info-text">
                      В наличии
                    </div>
                    <div
                        class="catalog-item__info-text"
                        v-if="book.availability"
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
                      {{ book.year }} {{ book.place }}
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
              :class="[book.availability ? 'activeClass' : 'disabled']"
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
</template>

<style lang="scss">
@import "@/assets/css/vars";
.catalog-item {
  width: 100%;
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