import Vue from 'vue'
import VueRouter from 'vue-router'
import StartView from '../views/StartView'
import MovieDetailView from '../views/MovieDetailView.vue'
import SearchResultView from '../views/SearchResultView.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from '../views/SignUpView.vue'
import CommunityView from '../views/CommunityView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import ArticleDetailView from '../views/ArticleDetailView.vue'
import ArticleUpdateView from '../views/ArticleUpdateView.vue'
import ProfileView from '../views/ProfileView.vue'
import ProfileEditView from '../views/ProfileEditView.vue'
import TinderMainView from '../views/TinderMainView.vue'
import WishListView from '../views/WishListView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'StartView',
    component: StartView
  },
  {
    path: '/movie',
    name: 'MovieView',
    // route level code-splitting
    // this generates a separate chunk (MovieView.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "MovieView" */ '../views/MovieView')
  },
  {
    path: '/movies/:movie/:moviePk/',
    name: 'MovieDetailView',
    component: MovieDetailView,
    props: true,
  },
  {
    path: '/movies/searchresult/:keyword/',
    name: 'SearchResultView',
    component: SearchResultView,
    props: true,
  },
  {
    path: '/login/',
    name: 'LoginView',
    component: LoginView,
    props: true,
  },
  {
    path: '/signup/',
    name: 'SignUpView',
    component: SignUpView,
  },
  {
    path: '/community/',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/article/create/',
    name: 'ArticleCreate',
    component: ArticleCreateView
  },
  {
    path: '/articles/:article/',
    name: 'ArticleDetail',
    component: ArticleDetailView,
    props: true
  },
  {
    path: '/articles/:articlePk/update/',
    name: 'ArticleUpdate',
    component: ArticleUpdateView,
    props: true
  },
  {
    path: '/profile/:username/',
    name: 'ProfileView',
    component: ProfileView,
    props: true
  },
  {
    path: '/profile/:username/:userInfo/',
    name: 'ProfileEditView',
    component: ProfileEditView,
    props: true
  },
  {
    path:'/tinder/',
    name: 'TinderMainView',
    component: TinderMainView,
    props: true
  },
  {
    path: '/wishlist/:username/',
    name: 'WishListView',
    component: WishListView,
    props: true
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
