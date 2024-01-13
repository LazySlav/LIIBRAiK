<script>
import VBreadcrumbs from "@/components/v-breadcrumbs.vue";
import VTable from "@/components/v-table.vue";
import VInput from "@/components/v-input.vue";
import VButton from "@/components/v-button.vue";
export default {
  name: 'catalogView',
  components: {
    VButton, VInput,
    VBreadcrumbs,
    VTable,
  },
  data () {
    return {
      pageTitle: 'Каталог',
      showAdvancedFilterCont: false,
      showAdvancedFilterLink: 'Расширенный поиск',

      valueTitle: '',
      isErrorTitle: false,
      valueAuthor: '',
      valueYear: '',
      valuePlace: '',
      valueVolume: '',

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
    filterHandler() {
      const advancedFilter = document.querySelector('#advancedFilterCont');
      console.log(advancedFilter);
      if (this.showAdvancedFilterCont) {
        this.showAdvancedFilterCont = false;
        this.showAdvancedFilterLink = 'Расширенный поиск';

      } else {
        this.showAdvancedFilterCont = true;
        this.showAdvancedFilterLink = 'Скрыть расширенный поиск';
      }
    },
    formSubmit(event) {
      console.log(this.valueTitle)
      if (this.valueTitle === '') {
        event.preventDefault()
      }
    }
  }
}
</script>

<template>
  <div class="catalog-view">
    <v-breadcrumbs :breadcrumbs="breadcrumbs" />
    <h1>
      {{ pageTitle }}
    </h1>
    <div class="catalog__content">
      <div class="catalog__filters">
        <form
            id="formFilters"
            action="#"
            method="post"
            class="v-catalog-filters"
        >
          <div class="v-catalog-filters__head">
            <div class="v-catalog-filters__head-col">
              <v-input
                  id="filterTitle"
                  placeholder="Поиск по названию"
                  type="text"
                  name="title"
                  v-model="valueTitle"
                  message="Поле должно быть заполнено"
              />

              <div
                  @click="filterHandler"
                  class="v-catalog-filters__more"
                  v-if="this.showAdvancedFilterCont"
              >
                {{ this.showAdvancedFilterLink }}
              </div>
              <div
                  @click="filterHandler"
                  class="v-catalog-filters__more"
                  v-else
              >
                {{ this.showAdvancedFilterLink }}
              </div>
            </div>
            <div class="v-catalog-filters__head-col">
              <v-button
                  @click="formSubmit"
                  class-size="mid"
                  class-color="primary"
              >Найти</v-button>
            </div>
          </div>
          <div
              v-show="this.showAdvancedFilterCont"
              id="advancedFilterCont"
              class="v-catalog-filters__body"
          >
            <v-input
                id="filterAuthor"
                placeholder="Автор"
                type="text"
                name="author"
                v-model="valueAuthor"
            />
            <v-input
                id="filterYear"
                placeholder="Год издания"
                type="text"
                name="year"
                v-model="valueYear"
            />
            <v-input
                id="filterPlace"
                placeholder="Место издания"
                type="text"
                name="place"
                v-model="valuePlace"
            />
            <v-input
                id="filterVolume"
                placeholder="Объем"
                type="text"
                name="volume"
                v-model="valueVolume"
            />
          </div>
        </form>
      </div>
      <div class="catalog__info" v-if="catalogValues.length">
        <v-table>
          <thead>
          <tr>
            <th>
              <div class="v-table__block">
                Название
              </div>
            </th>
            <th>
              <div class="v-table__block">
                Автор
              </div>
            </th>
            <th>
              <div class="v-table__block">
                Год и место издания
              </div>
            </th>
            <th>
              <div class="v-table__block">
                Объем
              </div>
            </th>
            <th>
              <div class="v-table__block">
                Наличие
              </div>
            </th>
            <th>
              <div class="v-table__block">
                Идентификатор
              </div>
            </th>
          </tr>
          </thead>
          <tbody>
          <tr
            v-for="catalogValue in catalogValues"
            :key="catalogValue.id"
          >
            <td>
              <div class="v-table__block">
                <router-link :to="{path: '/catalog/' + catalogValue.id}">{{ catalogValue.name }}</router-link>
              </div>
            </td>
            <td >
              <div class="v-table__block">
                {{ catalogValue.author }}
              </div>
            </td>
            <td>
              <div class="v-table__block">
                {{ catalogValue.year }} <br>
                {{ catalogValue.place }}
              </div>
            </td>
            <td>
              <div class="v-table__block">
                {{ catalogValue.volume }}
              </div>
            </td>
            <td>
              <div
                  class="v-table__block"
                  v-if="catalogValue.availability"
              >
                <span class="color-success">
                  Есть
                </span>
              </div>
              <div
                  class="v-table__block"
                  v-else
              >
                <span class="color-error">
                  Нет
                </span>
              </div>
            </td>
            <td>
              <div class="v-table__block">
                {{ catalogValue.idBook }}
              </div>
            </td>
          </tr>
          </tbody>
        </v-table>
      </div>
      <p v-else>Список книг пуст</p>
      <div class="catalog__pagination"></div>
    </div>

  </div>
</template>

<style lang="scss">
@import "@/assets/css/vars";
.v-catalog-filters {
  padding: $padding*3 0;

  &__head {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;


  }
  &__head-col {
    display: flex;
    align-items: center;
    justify-content: flex-start;
  }
  &__more {
    margin-left: $margin*3;
    @include text($size: $font-size-xs, $color: $primary-color-500);
    transition: .3s;
    user-select: none;

    &:hover {
      color: $primary-color-600;
      transition: .2s;
      cursor: pointer;
    }
    &:active {
      color: $primary-color-400;
      transition: .4s;
    }
  }
  &__body {
    width: 100%;
    margin-top: $margin*6;

    .v-input {
      margin-bottom: $margin*3;

      &:last-child {
        margin-bottom: 0;
      }
    }
  }
  &__bottom {

  }
}
.catalog__info {
  padding: 12px 0;
  width: 100%;
}
</style>