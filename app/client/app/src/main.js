import Vue from 'vue'
import Vuex from 'vuex'
import router from './router.js'
import store from './store'
import App from './App.vue'
import './filters.js'
import Mixins from './mixins.js'
import backend from './store/backend'

Vue.mixin(Mixins)

let vue = new Vue({
  el: '#vue-app',
  router,
  store,
  template: '<App/>',
  mixins: [Mixins],
  components: { App, backend }
})
