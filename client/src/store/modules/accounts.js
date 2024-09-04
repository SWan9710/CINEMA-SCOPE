import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

// 훈석햄 컴퓨터로 요청보내기
// const API_URL = 'https://de84-59-20-195-24.ngrok-free.app/api/v1/movies/popularity/'

const API_URL = "http://127.0.0.1:8000"
Vue.use(Vuex)

export default {
  state: {
    token: null,
    authError: null,
    profile: {},
    currentUser: null,
    profileEdit: {},
  },
  getters: {
    isLogIn: state => !!state.token,
    currentUser: state => state.currentUser,
    nowUserProfile: state => state.nowUserProfile,
    profile: state => state.profile,
    authError: state => state.authError,
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.token = token
    },
    SET_AUTH_ERROR(state, error) {
      state.authError = error
    },
    SET_PROFILE(state, profile) {
      state.profile = profile
    },
    SET_CURRENT_USER(state, user) {
      state.currentUser = user
    },
    SET_PROFILE_EDIT(state, user) {
      state.profileEdit = user
    },
  },
  actions: {
    // 회원가입
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: payload
      })
      .then(res => {
        context.commit('SET_TOKEN', res.data.key)
        context.commit('SET_PROFILE', res.data)
        context.dispatch('setCurrentUser')
        router.push({
          name: 'MovieView'
        })
      })
      .catch(err => {
        context.commit('SET_AUTH_ERROR', err.response.data)
      })
    },
    // 로그인
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: payload
      })
      .then(res => {
        context.commit('SET_TOKEN', res.data.key)
        context.commit('SET_PROFILE', res.data)
        context.dispatch('setCurrentUser')
        router.push({name: 'MovieView'})
      })
      .catch(err => {
        context.commit('SET_AUTH_ERROR', err.response.data)
      })
    },
    // 로그아웃
    logOut(context) {
      if(confirm('로그아웃 하시겠습니까?')) {
        axios({
          method: 'post',
          url: `${API_URL}/accounts/logout/`,
          headers: {
            Authorization : `Token ${this.state.accounts.token}`
          }
        })
        .then(res => {
          if(res) {
            context.commit('SET_TOKEN', '')
            context.commit('SET_PROFILE', res.data)
            context.commit('SET_CURRENT_USER', null)
            context.commit('GET_USER_LIKE_MOVIES', null)
            router.push({name: 'LoginView'})
          }
        })
        .catch(err => {
          context.commit('SET_AUTH_ERROR', err.response.data)
        })
      }
    },
    // 유저 정보 저장하기
    setCurrentUser(context) {
      if (this.getters.isLogIn) {
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
            Authorization : `Token ${this.state.accounts.token}`
          }
        })
        .then(res => {
          context.commit('SET_CURRENT_USER', res.data)
          localStorage.setItem('currentUser', JSON.stringify(res.data))
        })
        .catch(() => {
          router.push({name: 'LoginView'})
        })
      }
    },
    // 회원가입 및 유저 활동정보 불러오기
    getUserProfile(context, payload) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v3/profile/${payload.username}`,
        headers: {
          Authorization : `Token ${this.state.accounts.token}`
        }
      })
      .then (res => {
        context.commit('SET_PROFILE', res.data)
      })
    },
    // 회원정보 수정
    profileUpdate(context, payload) {
      axios({
        method: 'put',
        url: `${API_URL}/api/v3/profile/${payload.username}/`,
        data: {
          username: payload.username,
          genre_likes: payload.genre_likes,
          email: payload.email,
          profile_img: payload.profile_img
        },
        headers: {
          Authorization : `Token ${this.state.accounts.token}`
        }
      })
      .then(res => {
        context.commit('SET_PROFILE', res.data)
        context.commit('SET_PROFILE_EDIT', res.data)
        context.dispatch('setCurrentUser')
        router.go(-1)
      })
    },
    // 팔로우 언팔로우
    followProfile(context, userPk) {
      axios({
        method: 'post',
        url: `${API_URL}/api/v3/${userPk}/follow/`,
        headers: {
          Authorization : `Token ${this.state.accounts.token}`
        }
      })
      .then(res => {
        context.commit('SET_PROFILE', res.data)
      })
    }
  },
}
