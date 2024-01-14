<script>
import VBreadcrumbs from "@/components/v-breadcrumbs.vue";
import VTable from "@/components/v-table.vue";
import VInput from "@/components/v-input.vue";
import VButton from "@/components/v-button.vue";
import VPagination from "@/components/v-pagination.vue";
import VSortingArrow from "@/components/v-sorting-arrow.vue";
import VPopupCreateBook from "@/components/v-popup-create-book.vue";
export default {
  name: 'catalogView',
  components: {
    VButton, VInput,
    VBreadcrumbs,
    VTable,
    VPagination,
    VSortingArrow,
    VPopupCreateBook,
  },
  data () {
    return {
      isAdmin: true,

      showPopup: false,

      pageTitle: 'Каталог',
      showAdvancedFilterCont: false,
      showAdvancedFilterLink: 'Расширенный поиск',

      paginationChange: 0,
      paginationCurrentPage: 1,
      paginationPageCount: 20,
      paginationDisplayCount: 7,

      valueTitle: '',
      isErrorTitle: false,
      valueAuthor: '',
      valueYear: '',
      valuePlace: '',
      valueVolume: '',

      valueTitleNew: '',
      valueAuthorNew: '',
      valueYearNew: '',
      valuePlaceNew: '',
      valueVolumeNew: '',
      valueIdNew: '',
      valueAvailabilityNew: Boolean,

      sortingValue: '',
      activeButton: null,

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
    formSubmit() {
      // console.log(this.valueTitle)
      // if (this.valueTitle === '') {
      //   event.preventDefault()
      // }
    },
    sorting(value) {
      console.log(value)
      this.sortingValue = value;

    },
    setActiveButton(buttonNumber) {
      this.activeButton = buttonNumber;
    },
    showDialog() {
      this.showPopup = true;
    },
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
                  @click.prevent="formSubmit"
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

      <div class="catalog__admin" v-if="isAdmin">
        <v-button
          @click="showDialog()"
          class-color="primary"
        >
          Добавить книгу
        </v-button>
      </div>

      <div class="catalog__info" v-if="catalogValues.length">
        <v-table>
          <thead>
          <tr>
            <th>
              <div class="v-table__block">
                Название
                <div class="sorting-block">
                  <v-sorting-arrow
                    v-model="sortingValue"
                    newValue="title-up"
                    :isActive="activeButton === 1"
                    @click="setActiveButton(1)"
                  />
                  <v-sorting-arrow
                      v-model="sortingValue"
                      newValue="title-down"
                      :isActive="activeButton === 2"
                      @click="setActiveButton(2)"
                  />
                </div>
              </div>

            </th>
            <th>
              <div class="v-table__block">
                Автор
                <div class="sorting-block">
                  <v-sorting-arrow
                      v-model="sortingValue"
                      newValue="author-up"
                      :isActive="activeButton === 3"
                      @click="setActiveButton(3)"
                  />
                  <v-sorting-arrow
                      v-model="sortingValue"
                      newValue="author-down"
                      :isActive="activeButton === 4"
                      @click="setActiveButton(4)"
                  />
                </div>
              </div>
            </th>
            <th>
              <div class="v-table__block">
                Год и место издания
                <div class="sorting-block">
                  <v-sorting-arrow
                      v-model="sortingValue"
                      newValue="year-up"
                      :isActive="activeButton === 5"
                      @click="setActiveButton(5)"
                  />
                  <v-sorting-arrow
                      v-model="sortingValue"
                      newValue="year-down"
                      :isActive="activeButton === 6"
                      @click="setActiveButton(6)"
                  />
                </div>
              </div>
            </th>
            <th>
              <div class="v-table__block">
                Объем
                <div class="sorting-block">
                  <v-sorting-arrow
                      v-model="sortingValue"
                      newValue="volume-up"
                      :isActive="activeButton === 7"
                      @click="setActiveButton(7)"
                  />
                  <v-sorting-arrow
                      v-model="sortingValue"
                      newValue="volume-down"
                      :isActive="activeButton === 8"
                      @click="setActiveButton(8)"
                  />
                </div>
              </div>
            </th>
            <th>
              <div class="v-table__block">
                Наличие
                <div class="sorting-block">
                  <v-sorting-arrow
                      v-model="sortingValue"
                      newValue="availability-up"
                      :isActive="activeButton === 9"
                      @click="setActiveButton(9)"
                  />
                  <v-sorting-arrow
                      v-model="sortingValue"
                      newValue="availability-down"
                      :isActive="activeButton === 10"
                      @click="setActiveButton(10)"
                  />
                </div>
              </div>
            </th>
            <th>
              <div class="v-table__block">
                Идентификатор
                <div class="sorting-block">
                  <v-sorting-arrow
                      v-model="sortingValue"
                      newValue="id-up"
                      :isActive="activeButton === 11"
                      @click="setActiveButton(11)"
                  />
                  <v-sorting-arrow
                      v-model="sortingValue"
                      newValue="id-down"
                      :isActive="activeButton === 12"
                      @click="setActiveButton(12)"
                  />
                </div>
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
      <div class="catalog__pagination">
        <v-pagination
          :currentPage=paginationCurrentPage
          :pageCount=paginationPageCount
          :displayCount=paginationDisplayCount
          v-model="paginationCurrentPage"
        />
      </div>
    </div>

  </div>
  <v-popup-create-book
      v-model:show-popup="showPopup"
      v-model:value-title-model="valueTitleNew"
      v-model:value-author-model="valueAuthorNew"
      v-model:value-year-model="valueYearNew"
      v-model:value-place-model="valuePlaceNew"
      v-model:value-volume-model="valueVolumeNew"
      v-model:value-id-model="valueIdNew"
  />
</template>

<style lang="scss">
@import "@/assets/css/vars";
.sorting-block {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 12px;
  position: absolute;
  right: $padding*2;
  top: 10px;
  transform: translateY(-50%);


}
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