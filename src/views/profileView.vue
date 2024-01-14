<script >
import VBreadcrumbs from "@/components/v-breadcrumbs.vue";
import VBlock from "@/components/v-block.vue";
import VButton from "@/components/v-button.vue";
export default {
  name: 'profileView',
  components: {
    VBreadcrumbs,
    VBlock,
    VButton
  },
  data () {
    return {
      pageTitle: 'Мой профиль',
      // pathToImg: 'img/profile__photo.png',
      // pathUniversal: '@/assets/',

      profile: [
        {
          title: 'Статус',
          value: 'Студент'
        },
        {
          title: 'Факультет, группа',
          value: '2022-ФГиИБ-ИСиТ-1б'
        },
        {
          title: 'Фамилия',
          value: 'Иванов'
        },
        {
          title: 'Имя',
          value: 'Иван'
        },
        {
          title: 'Отчество',
          value: 'Иванович'
        },
        {
          title: 'Логин',
          value: 'Ivanovvv'
        },
        {
          title: 'ID',
          value: 'u25928y4592'
        },
        {
          title: 'Номер читательского билет',
          value: '2394823049823094'
        },
      ],

      breadcrumbs: [
        {
          path: '/',
          name: 'Главная',
        },
        {
          path: '/profile',
          name: 'Профиль',
        },
      ],

    }
  }
}
</script>

<template>
  <div class="profile-view">
    <v-breadcrumbs :breadcrumbs="breadcrumbs" />
    <h1>
      {{ pageTitle }}
    </h1>
    <div class="profile-view__content">
      <div class="profile-view__row">
        <div class="profile-view__col">
          <div class="profile__photo">
            <div class="profile__photo-blur">
              <img src="@/assets/img/profile__photo2.jpeg" alt="">
            </div>
            <img src="@/assets/img/profile__photo2.jpeg" alt="">
          </div>
          <div class="profile__exit">
            <v-button
              class-color="error"
              class-size="mid"
            >Выйти</v-button>
          </div>
        </div>
        <div class="profile-view__col">
          <v-block class="profile__info">
            <div
                v-for="line in profile"
                :key="line.title"
                class="profile__info-line"
            >
              <div class="profile__info-text">
                {{ line.title }}
              </div>
              <div class="profile__info-text">
                {{ line.value }}
              </div>
            </div>
          </v-block>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
@import "@/assets/css/vars";

.profile__exit {
  margin-top: $margin*6;
}
.profile-view {
  width: 100%;
  &__content {
    width: 100%;
    padding: 12px 0;
  }
  &__row {
    width: 100%;
    display: flex;
    align-items: flex-start;
    justify-content: flex-start;
  }
  &__col {
    &:nth-child(1) {
      width: 240px;
      margin-right: $margin*6;
    }
    &:nth-child(2) {
      width: 420px;
    }
  }
}
.profile__photo {
  width: 100%;
  height: 320px;
  border: 2px solid $primary-color-200;
  border-radius: $border-radius*2;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 0;
  overflow: hidden;

  & > img {
    max-width: 100%;
    max-height: 100%;
  }
}
.profile__photo-blur {
  width: 100%;
  height: 100%;
  position: absolute;
  z-index: -1;
  &:after {
    content: '';
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: $primary-color-500;
    opacity: .2;
    z-index: 0;
  }
  & > img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: relative;

    filter: blur(3.5px);
  }
}
.profile__info {
  width: 100%;

  .profile__info-line {
    width: 100%;
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: $padding*2;

    &:last-child {
      margin-bottom: 0;
    }
  }
  .profile__info-text {
    width: 50%;
    @include text($size: $font-size-md, $color: $primary-color-900);
    &:first-child {
      font-weight: bold;
      padding-right: $padding*4;
    }
  }
}
</style>