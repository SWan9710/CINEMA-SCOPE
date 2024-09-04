import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

import movies from './modules/movies'
import accounts from './modules/accounts'
import community from './modules/community'

Vue.use(Vuex)

const persistedstate = createPersistedState({
  storage: window.localStorage
})
export default new Vuex.Store({
  plugins: [
    persistedstate
  ],
  state: {
    pageState : false
  },
  getters: {
  },
  mutations: {
    START_APP(state) {
      state.pageState = true
    }
  },
  actions: {
  },
  modules: {
    movies, accounts, community
  }
})
