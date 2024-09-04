import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

// 훈석햄 컴퓨터로 요청보내기
// const API_URL = 'https://de84-59-20-195-24.ngrok-free.app/api/v1/movies/popularity/'

const API_URL = "http://127.0.0.1:8000/api/v2/"
Vue.use(Vuex)

export default {
  state: {
    articleList: null,
    article: null,
  },
  getters: {
    articles: state => state.article
  },
  mutations: {
    GET_ARTICLE_LIST(state, articles) {
      state.articleList = articles
    },
    SET_ARTICLE(state, article) {
      state.article = article
    },
    SET_ARTICLE_COMMENT(state, comments) {
      state.article.article.comments = comments
    },
    SET_ARTICLE_LIKE(state, liked_users) {
      state.article.article.liked_users = liked_users
    },
    SET_ARTICLE_COMMENT_LIKE(state, payload) {
      state.article.article.comments[payload.idx].liked_users = payload.liked_users
    }
  },
  actions: {
    // 전체 게시글 조회
    getArticleList(context) {
      axios({
        method: 'get',
        url: API_URL
      })
      .then(res => {
        context.commit('GET_ARTICLE_LIST', res.data)
      })
    },
    // 게시글 생성
    articleCreate(context, payload) {
      axios({
        method: 'post',
        url: API_URL,
        data: payload,
        headers: {
          Authorization : `Token ${this.state.accounts.token}`
        }
      })
      .then(res => {
        context.commit('SET_ARTICLE', res.data)
        router.push({
          name: 'ArticleDetail', 
          params: {
            article: this.state.community.article
          }})
      })
    },
    // 게시글 수정 요청
    articleUpdate(context, payload) {
      const PK = payload.articlePk
      axios({
        method: 'put',
        url: `${API_URL}${PK}/`,
        data: {
          title: payload.title, 
          content: payload.content
        },
        headers: {
          Authorization : `Token ${this.state.accounts.token}`
        }
      })
      .then(res => {
        context.commit('SET_ARTICLE',res.data)
        router.push({
          name: 'ArticleDetail', 
          params: {
            article: this.state.community.article
          }})
        })
    },
    // 게시글 삭제 요청
    articleDelete(context, pk) {
      const PK = pk
      axios({
        method: 'delete',
        url: `${API_URL}${PK}/`,
        data: pk,
        headers: {
          Authorization : `Token ${this.state.accounts.token}`
        }
      })
      .then(() => {
        context.commit('SET_ARTICLE', {})
        router.push({name: 'CommunityView'})
      })
    },
    // 게시글 좋아요
    likeArticle(context, payload) {
      const PK = payload
      axios({
        method: 'post',
        url: `${API_URL}${PK}/like/`,
        headers: {
          Authorization : `Token ${this.state.accounts.token}`
        }
      })
      .then(res => {
        context.commit('SET_ARTICLE_LIKE', res.data.liked_users)
      })
    },
    // 게시글 댓글 생성
    commentCreate(context, payload) {
      const PK = payload.articlePk
      axios({
        method: 'post',
        url: `${API_URL}${PK}/comments/`,
        data: payload,
        headers: {
          Authorization : `Token ${this.state.accounts.token}`
        }
      })
      .then(res => {
        context.commit('SET_ARTICLE_COMMENT', res.data)
      })
    },
    // 게시글 댓글 삭제
    commentDelete(context, payload) {
      if (confirm('정말 삭제하시겠습니까?')) {
        const ARTICLE_PK = payload.articlePk
        const COMMENT_PK = payload.commentPk
        axios({
          method: 'delete',
          url: `${API_URL}${ARTICLE_PK}/comments/${COMMENT_PK}/`,
          data: {},
          headers: {
            Authorization : `Token ${this.state.accounts.token}`
          }
        })
        .then(res => {
          context.commit('SET_ARTICLE_COMMENT', res.data)
        })
      }
    },
    // 게시글 좋아요 
    likeComment(context, payload) {
      const ARTICLE_PK = payload.articlePk
      const COMMENT_PK = payload.commentPk
      axios({
        method: 'post',
        url: `${API_URL}${ARTICLE_PK}/comments/${COMMENT_PK}/like/`,
        headers: {
          Authorization : `Token ${this.state.accounts.token}`
        }
      })
      .then(res => {
        const total = {
          liked_users: res.data.liked_users,
          idx: payload.idx
        }
        context.commit('SET_ARTICLE_COMMENT_LIKE', total)
      })
    },
    setArticle(context, payload) {
      context.commit('SET_ARTICLE', payload)
    }
  },
}
