<template>
  <nav>
    <ul class="list-unstyled main-menu">
      <li class="text-right close__menu">
        <a @click="toggleSidebar()">
          X
        </a>
      </li>
      <li class="text-center image__menu">
        <a href="#">
          <img src="http://placehold.it/250x75" />
        </a>
      </li>
      <li class="text-center image__menu">
        <a href="#">
          <img src="http://placehold.it/250x75" />
        </a>
      </li>
      <li class="text-center image__menu">
        <a href="#">
          <img src="http://placehold.it/250x75" />
        </a>
      </li>
      <li class="text-center image__menu">
        <a href="#">
          <img src="http://placehold.it/250x75" />
        </a>
      </li>
    </ul>
  </nav>

  <a class="nav-expander fixed"
    @click="toggleSidebar()">
    <i class="fa fa-bars fa-lg white"></i>
  </a>
</template>

<script>
  import jQuery from 'jquery'

  export default {
    methods: {
      toggleSidebar () {
        jQuery('body').toggleClass('nav-expanded')
      }
    }
  }
</script>
