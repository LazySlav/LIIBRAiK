<template>
  <div class="app">
      <div class="app-top" v-if="!$route.meta.isAuthPage" >
        <div id="top" ref="to-top" class="to-top"></div>
        <VHeader />
        <div>
          <v-cont>
            <router-view />
          </v-cont>
        </div>
      </div>
      <div class="app-bottom" v-if="!$route.meta.isAuthPage" >
        <VFooter/>
      </div>
      <div class="app-auth"  v-if="$route.meta.isAuthPage" >
        <router-view />
      </div>
  </div>

</template>

<script>

import VHeader from "@/components/v-header.vue";
import VFooter from "@/components/v-footer.vue";
import VCont from "@/components/v-cont.vue";
export default {
  name: 'App',
  components: {
    VFooter,
    VHeader,
    VCont,
  }
}
</script>

<style lang="scss">
  @import '@/assets/css/main.scss';
  @import '@/assets/css/vars.scss';
  .app {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;
    width: 100%;
    min-height: 100vh;

    & > * {
      width: 100%;
    }
  }
  .app-top {
    width: 100%;
    padding: $padding*28 0 $padding*3 0;
  }
</style>
