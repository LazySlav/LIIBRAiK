
<script>
import VBlock from "@/components/v-block.vue";
import VInput from "@/components/v-input.vue";
import VButton from "@/components/v-button.vue";
import router from "@/router/router";
import axios from 'axios';
export default {
  name: 'authView',
  components: {
    VBlock,
    VButton, VInput,
  },
  data () {
    return {
      loginInput: '',
      passwordInput: '',
      formValid: false,
    }
  },
  methods: {
    formSubmit(event) {
      if (this.loginInput === '' || this.passwordInput === '') {
        event.preventDefault();
        this.formValid = false;
      } else {
        this.formValid = true;
        router.push('/profile')
      }
    },

    async sendPostRequest() {
      try {
        const response = await axios.post('/auth/login', {}, {
          auth: {
            username: 'uname',
            password: 'pass',
          }
        });

        console.log('Ответ от сервера:', response.data);
        router.push('/profile')
      } catch (error) {
        console.error('Ошибка при отправке POST запроса:', error);

      }
    },
  }
}
</script>

<template>
  <div class="auth-view">
    <v-block class="auth-view__cont">
        <div class="auth-view__title">
          <h3>
            Авторизация
          </h3>
        </div>
        <form class="auth-view__form">
          <div class="auth-view__form-list">
            <v-input
              placeholder="Введите логин"
              id="loginInput"
              type="text"
              name="login"
              message="Поле должно быть заполнено!"
              v-model="loginInput"
            />
            <v-input
                placeholder="Введите пароль"
                id="passwordInput"
                type="password"
                name="password"
                message="Поле должно быть заполнено!"
                v-model="passwordInput"

            />
          </div>
          <div class="auth-view__form-bottom">
            <v-button
                class-color="primary"
                class-size="large"

                @click.prevent="sendPostRequest"
            >Войти</v-button>
          </div>
        </form>
    </v-block>
  </div>
</template>
<style lang="scss">
@import "@/assets/css/vars";

.auth-view {
  width: 100%;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  &__cont {
    width: 400px;
  }
  &__title {
    width: 100%;
    text-align: center;
    margin-bottom: $margin*6;
    h3 {
      padding: 0;
    }
  }
  &__form {
    width: 100%;
  }
  &__form-list {
    width: 100%;
    .v-input {
      width: 100%;
      margin-bottom: $margin*6;
      &:last-child {
        margin-bottom: 0;
      }
    }
  }
  &__form-bottom {
    width: 100%;
    display: flex;
    justify-content: center;
    margin-top: $margin*8;

    .v-button {
      width: 100%;
    }
  }
}
</style>