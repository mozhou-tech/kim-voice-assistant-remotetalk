import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from 'vuex/dist/logger'


import actions from './actions'
import getters from './getters'
import mutations from './mutations'

Vue.use(Vuex)

export default new Vuex.Store({

  plugins: [createLogger()],
  strict: process.env.NODE_ENV !== 'production',
  mutations,
  actions,
  getters,
  state: {
    isAuth: false,
    version: '1.0',
    resource: null,
    isLoading: false,
    deviceConversationLogs: [],
    chatItems: [],
    deviceStat: {},
    chatPollingOpen: false,
    statPollingOpen: false,
    title: 'KIM智能语音助理',
    lastConversationAt: 0
  }
})
