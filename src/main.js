import Vue from 'vue'
import App from './App.vue'
import List from './components/List.vue'

import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(VueRouter)

const router = new VueRouter()

router.map({
  '/blog': {
    component: List
  }
})

router.redirect({
  '*': '/blog'
})

router.start(App, '#app')
