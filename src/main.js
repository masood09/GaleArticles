import Vue from 'vue'
import App from './App.vue'
import List from './components/List.vue'
import Detail from './components/Detail.vue'
import Search from './components/Search.vue'

import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

Vue.config.devtools = false

Vue.use(VueResource)
Vue.use(VueRouter)

Vue.filter('linebreaks', function (value) {
  return value.replace(/(?:\r\n|\r|\n)/g, '<br>')
})

Vue.filter('truncatewords_html', function (value, count) {
  return value.split(' ').splice(0, count).join(' ')
})

const router = new VueRouter()

router.map({
  '/article': {
    component: List
  },
  '/article/:articleId': {
    name: 'articleDetail',
    component: Detail
  },
  '/search': {
    name: 'search',
    component: Search
  }
})

router.redirect({
  '/': '/article'
})

router.start(App, '#app')
