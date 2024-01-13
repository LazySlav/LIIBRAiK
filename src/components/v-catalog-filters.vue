<script>
import VInput from "@/components/v-input.vue";
import VButton from "@/components/v-button.vue";
export default {
  name: "v-catalog-filters",

  components: {
    VButton,
    VInput,
  },
  props: {

    // valueTitle: [String, Number],
    // valueAuthor: [String, Number],
    // valueYear: [String, Number],
    // valuePlace: [String, Number],
    // valueVolume: [String, Number],
  },
  data() {
    return {

      isValidForm: true,
      valueTitle: '',
    }
  },
  methods: {


    updateInput (event) {
      // this.valueTitle = value;
      // console.log(this.valueTitle);
      this.$emit('update:inputTitle', event.target.value);
    }
  }
}
</script>

<template>
  <div></div>
</template>

<style lang="scss">


</style>