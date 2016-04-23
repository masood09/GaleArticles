<template>
  <sidebar></sidebar>

  <router-view></router-view>

  <component_footer></component_footer>
</template>

<style lang="sass">
  @import '../scss/styles';
</style>

<script>
  import Sidebar from './components/Sidebar.vue'
  import Footer from './components/Footer.vue'

  export default {
    components: {
      'sidebar': Sidebar,
      'component_footer': Footer
    }
  }
</script>
