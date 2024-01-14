<script>
import VBreadcrumbs from "@/components/v-breadcrumbs.vue";
import VTable from "@/components/v-table.vue";
import VPopup from "@/components/v-popup.vue";
export default {
  name: 'myBooksView',
  components: {
    VTable,
    VBreadcrumbs,
    VPopup,
  },
  data () {
    return {
      pageTitle: 'Мои книги',
      dialogVisible: false,
      popupId: false,
      breadcrumbs: [
        {
          path: '/',
          name: 'Главная',
        },
        {
          path: '/my-books',
          name: 'Мои книги',
        },
      ],

      bookOnHands: [
        {
          id: 1,
          periodFrom: "20.20.2022",
          periodTo: "22.20.2022",
          name: "Геодезический мониторинг движений земной коры (по материалам Кавказского региона). В. Р. Ященко, Х. К. Ямбаев",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
          idBook: "РБ.6 Я 958",
        },
        {
          id: 2,
          periodFrom: "20.20.2022",
          periodTo: "22.20.2022",
          name: "Геодезический мониторинг движений земной коры (по материалам Кавказского региона). В. Р. Ященко, Х. К. Ямбаев",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
          idBook: "РБ.6 Я 958",
        },
        {
          id: 3,
          periodFrom: "20.20.2022",
          periodTo: "22.20.2022",
          name: "Геодезический мониторинг движений земной коры (по материалам Кавказского региона). В. Р. Ященко, Х. К. Ямбаев",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
          idBook: "РБ.6 Я 958",
        },
      ],
      booksInReserve: [
        {
          id: 1,
          periodFrom: "20.20.2022",
          periodTo: "22.20.2022",
          name: "Геодезический мониторинг движений земной коры (по материалам Кавказского региона). В. Р. Ященко, Х. К. Ямбаев",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
        },
        {
          id: 2,
          periodFrom: "20.20.2022",
          periodTo: "22.20.2022",
          name: "Книга 2",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
        },
        {
          id: 3,
          periodFrom: "20.20.2022",
          periodTo: "22.20.2022",
          name: "Книга 3",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
        },
        {
          id: 4,
          periodFrom: "20.20.2022",
          periodTo: "22.20.2022",
          name: "Книга 4",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
        },
        {
          id: 5,
          periodFrom: "20.20.2022",
          periodTo: "22.20.2022",
          name: "Книга 5",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
        },
        {
          id: 6,
          periodFrom: "20.20.2022",
          periodTo: "22.20.2022",
          name: "Книга 6",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
        },
        {
          id: 7,
          periodFrom: "20.20.2022",
          periodTo: "22.20.2022",
          name: "Книга 7",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
        },
        {
          id: 8,
          periodFrom: "20.20.2022",
          periodTo: "22.20.2022",
          name: "Книга 8",
          author: "Ященко В.Р. / Ямбаев Х.К.",
          year: 2007,
          place: "МИИГАиК М.",
        },
      ]
    }
  },
  methods: {
    showDialog(id) {
      this.popupId = id;
      this.dialogVisible = true;
    },
    removeBook(id) {
      this.booksInReserve = this.booksInReserve.filter(p => p.id !== id);
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
      <div class="catalog__block">
        <h2>У меня на руках</h2>
        <div class="catalog__info" v-if="bookOnHands.length">
          <v-table class="hands__table">
            <thead>
            <tr>
              <th>
                <div class="v-table__block">
                  Период с
                </div>
              </th>
              <th>
                <div class="v-table__block">
                  Период до
                </div>
              </th>
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
                  Идентификатор
                </div>
              </th>
            </tr>
            </thead>
            <tbody>
            <tr
                v-for="catalogValue in bookOnHands"
                :key="catalogValue.id"
            >
              <td >
                <div class="v-table__block">
                  {{ catalogValue.periodFrom }}
                </div>
              </td>
              <td >
                <div class="v-table__block">
                  {{ catalogValue.periodTo }}
                </div>
              </td>
              <td>
                <div class="v-table__block">
<!--                  <router-link :to="{path: '/catalog/' + catalogValue.id}">{{ catalogValue.name }}</router-link>-->
                  {{ catalogValue.name }}
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
                  {{ catalogValue.idBook }}
                </div>
              </td>
            </tr>
            </tbody>
          </v-table>
        </div>
        <p v-else>Список книг пуст</p>
      </div>
      <div class="catalog__block">
        <h2>Книги в резерве</h2>
        <div class="catalog__info" v-if="booksInReserve.length">
          <v-table class="hands__table reserve">
            <thead>
            <tr>
              <th>
                <div class="v-table__block">
                  В резерве с
                </div>
              </th>
              <th>
                <div class="v-table__block">
                  В резерве до
                </div>
              </th>
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
                  Отмена
                </div>
              </th>
            </tr>
            </thead>
            <tbody>
              <tr
                  v-for="catalogValue in booksInReserve"
                  :key="catalogValue.id"
              >
                <td >
                  <div class="v-table__block">
                    {{ catalogValue.periodFrom }}
                  </div>
                </td>
                <td >
                  <div class="v-table__block">
                    {{ catalogValue.periodTo }}
                  </div>
                </td>
                <td>
                  <div class="v-table__block">
                    <!--                  <router-link :to="{path: '/catalog/' + catalogValue.id}">{{ catalogValue.name }}</router-link>-->
                    {{ catalogValue.name }}
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
                    <button class="delete_button" @click="showDialog(catalogValue.id)">
                      <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M0.46967 0.46967C0.762563 0.176777 1.23744 0.176777 1.53033 0.46967L7 5.93934L12.4697 0.46967C12.7626 0.176777 13.2374 0.176777 13.5303 0.46967C13.8232 0.762563 13.8232 1.23744 13.5303 1.53033L8.06066 7L13.5303 12.4697C13.8232 12.7626 13.8232 13.2374 13.5303 13.5303C13.2374 13.8232 12.7626 13.8232 12.4697 13.5303L7 8.06066L1.53033 13.5303C1.23744 13.8232 0.762563 13.8232 0.46967 13.5303C0.176777 13.2374 0.176777 12.7626 0.46967 12.4697L5.93934 7L0.46967 1.53033C0.176777 1.23744 0.176777 0.762563 0.46967 0.46967Z" fill="#D74747"/>
                      </svg>
                    </button>
                  </div>

                </td>
              </tr>
            </tbody>
          </v-table>
        </div>
        <p v-else>Список книг пуст</p>
      </div>
    </div>

  </div>
  <v-popup
      :id="this.popupId"
      v-model:show-popup="dialogVisible"
      @remove="removeBook"
  />
</template>

<style lang="scss">
@import "../assets/css/_vars.scss";

.delete_button {
  width: 24px;
  height: 24px;
  border-radius: $border-radius;
  border: 2px solid $error-color-200;
  background: $error-color-100;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: auto;
  transition: .5s;
  &:hover {
    transition: .3s;
    background: $error-color-200;
    border-color: $error-color-300;
    cursor: pointer;
  }
  &:active {
    transition: .1s;
    background: $error-color-300;
    border-color: $error-color-400;

  }
}
.catalog__info {
  padding: 12px 0;
  width: 100%;
}
.reserve {
  th:nth-child(6) .v-table__block {
    text-align: right;
  }

}
.hands__table {
  th:nth-child(1) {
    width: 10%;
  }
  th:nth-child(2) {
    width: 10%;
  }
  th:nth-child(3) {
    width: 40%;
  }
  th:nth-child(4) {
    width: 15%;
  }
  th:nth-child(5) {
    width: 15%;
  }
  th:nth-child(6) {
    width: 10%;
  }
}
</style>