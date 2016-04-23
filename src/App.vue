<template>
  <sidebar></sidebar>

  <router-view></router-view>

  <what_to_read_next></what_to_read_next>

  <component_footer></component_footer>
</template>

<style lang="sass">
  @import '../scss/styles';
</style>

<script>
  import Sidebar from './components/Sidebar.vue'
  import WhatToReadNext from './components/WhatToReadNext.vue'
  import Footer from './components/Footer.vue'

  export default {
    components: {
      'sidebar': Sidebar,
      'what_to_read_next': WhatToReadNext,
      'component_footer': Footer
    }
  }
</script>
