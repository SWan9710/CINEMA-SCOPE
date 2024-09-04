import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

// 훈석햄 컴퓨터로 요청보내기
// const API_URL = 'https://de84-59-20-195-24.ngrok-free.app/api/v1/movies/popularity/'
const API_URL = 'http://127.0.0.1:8000/api/v1/movies/popularity'

Vue.use(Vuex)

export default {
  state: {
    movieList: null,
    movies: null,
    genreMovies: null,
    releaseMovies: null,
    detailMovie: null,
    genresList: null,
    randomMovies: null,
    userLikeMovies: null,
    movieLike: [],
  },
  getters: {
    movies: state => state.movies,
    genresList: state => state.genresList
  },
  mutations: {
    GET_MOVIE_LIST(state, movies) {
      state.movieList = movies
    },
    SET_MOVIE(state, movies) {
      state.movies = movies
    },
    GET_GENRES(state, genres) {
      state.genresList = genres
    },
    GET_GENRE_MOVIES(state, movies) {
      state.genreMovies = movies
    },
    GET_RELEASE_MOVIES(state, movies) {
      state.releaseMovies = movies
    },
    GET_USER_LIKE_MOVIES(state, movies) {
      state.userLikeMovies = movies
    },
    SET_REVIEW(state, reviews) {
      state.movies.movie.reviews = reviews
    },
    GET_RANDOM_MOVIES(state, movies) {
      state.randomMovies = movies
    },
    MOVIE_LIKE(state, movie_id) {
      state.movieLike.push(movie_id)
    },
    MOVIE_DIS_LIKE(state, movie_id) {
      for(let i = 0; i < state.movieLike.length; i++) {
        if(state.movieLike[i] === movie_id)  {
          state.movieLike.splice(i, 1);
          i--;
        }
      }
    },
    RESET_MOVIELIKE(state) {
      state.movieLike = []
    }
  },
  actions: {
    // 전체 영화 정보 들고오기
    getMovieList(context) {
      axios({
        method: 'get', 
        url: `${API_URL}`,
      })
      .then(res => {
        context.commit('GET_MOVIE_LIST',res.data)
      })
    },
    // props 받은 영화 정보 저장하기
    setMovie(context, payload) {
      context.commit('SET_MOVIE', payload)
    },
    // 전체 장르 데이터 들고오기
    getGenres(context) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/v1/genres/'
      })
      .then(res => {
        context.commit('GET_GENRES', res.data)
      })
    },
    // 장르별 영화 들고오기
    getGenreMovies(context, payload) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/popularity/${payload}`
      })
      .then(res => {
        context.commit('GET_GENRE_MOVIES', res.data)
      })
    },
    // 개봉일 순으로 영화 들고오기
    getReleaseMovies(context) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/v1/movies/release_date/'
      })
      .then(res => {
        context.commit('GET_RELEASE_MOVIES',res.data)
      })
    },
    // 유저가 좋아요한 영화 랜덤 20개 요청
    getUserLikeMovies(context, userPK) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/userLikes/${userPK}/`
      })
      .then(res => {
        context.commit('GET_USER_LIKE_MOVIES',res.data)
      })
    },
    // 영화에 대한 리뷰 생성
    reviewCreate(context, payload) {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/movies/${payload.moviePk}/reviews/`,
        data: payload,
        headers: {
          Authorization: `Token ${this.state.accounts.token}`
        }
      })
      .then(res => {
        context.commit('SET_REVIEW', res.data)
      })
    },
    // 리뷰 수정
    reviewUpdate(context, payload) {
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/api/v1/movies/${payload.moviePk}/reviews/${payload.reviewPk}/`,
        data: payload,
        headers: {
          Authorization: `Token ${this.state.accounts.token}`
        }
      })
      .then(res => {
        router.push({
          name: 'MovieDetailView', 
          params: {
            movie: this.state.movies.movies.movie,
            moviePk: payload.moviePk
          }})
        context.commit('SET_REVIEW',res.data)
      })
    },
    //리뷰 삭제
    reviewDelete(context, payload) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/api/v1/movies/${payload.moviePk}/reviews/${payload.reviewPk}`,
        data: {},
        headers: {
          Authorization: `Token ${this.state.accounts.token}`
        }
      })
      .then(res => {
        context.commit('SET_REVIEW', res.data)
        router.go(0)
      })
    },
    // Tinder Random Movie 받아오기
    getRandomMovies(context) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/random/`,
        headers: {
          Authorization: `Token ${this.state.accounts.token}`
        }
      })
      .then(res => {
        context.commit('GET_RANDOM_MOVIES', res.data)
      })
    },
    // 영화에 대한 좋아요
    movieLike(context, movie_id) {
      context.commit('MOVIE_LIKE', movie_id)
    },
    // 영화에 대한 좋아요 취소
    movieDisLike(context, movie_id) {
      context.commit('MOVIE_DIS_LIKE', movie_id)
    },
    // 좋아요 토글버튼
    movieLikeToggle(context, movie_id) {
      axios({
          method: 'post',
          url: `http://127.0.0.1:8000/api/v1/movies/${movie_id}/toggleLikes/`,
          data: movie_id,
          headers: {
            Authorization: `Token ${this.state.accounts.token}`
          }
        })
        .then((res) => {
          context.commit('SET_MOVIE', {movie:res.data})
        })
    },
    // 좋아요 한 영화 저장
    saveMovieLike(context, movie_id_list) {
      movie_id_list.forEach(element => {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/api/v1/movies/${element}/likes/`,
          data: element,
          headers: {
            Authorization: `Token ${this.state.accounts.token}`
          }
        })
      });
      context.commit('RESET_MOVIELIKE')
        router.push({
          name: 'WishListView', 
          params: {
            username:this.state.accounts.currentUser.username
          }
        })
    },
    // 좋아요한 영화 빼기
    movieRemove(context, payload) {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/movies/${payload.movie_id}/dislikes/`,
        data: payload.movie_id,
        headers: {
          Authorization: `Token ${this.state.accounts.token}`
        }
      })
      .then(() => {
        context.dispatch('getUserProfile', payload)
      })
    }
  },
}
