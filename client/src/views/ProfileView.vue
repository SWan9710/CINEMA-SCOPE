<template>
  <div v-if="profile" class="profile-main" style="margin: 0 6em;">
    <h1 style="margin-top:1.5em;">PROFILE</h1>

    <div class="profile-top">
      <div class="profile-top-left">
        <div class="profile-top-img">
          <img :src="profile.profile_img" alt="유저이미지" class="rounded-circle">
        </div>
        <div class="profile-name">
          {{this.$route.params.username}}
        </div>

        <div class="profile-top-edit">
          <router-link 
            :to="{
              name: 'ProfileEditView', 
              params:{username:profile.username, userInfo: profile}}"
          ><button id="profile-edit-btn" class="btn btn-dark rounded-pill" v-if="$route.params.username === this.currentUser.username">회원정보수정</button>
          </router-link>
        </div>
      </div>

        
      <div class="profile-top-right">
        <!-- 라우터 푸쉬 걸어주기 -->
        
        <button @click="click" id="btn-modal" class="right1">
          <h3>{{profile.articles ? profile.articles.length : 0}}</h3>
          게시물
        </button>
        <div id="lorem-ipsum"></div>        

        <div class="right2">
          <h3>{{ profile.followers ? profile.followers.length : 0 }}</h3>
          팔로워
        </div>

        <div class="right3">
          <h3>{{ profile.followings.length ? profile.followings.length : 0 }}</h3>
          팔로잉
        </div>
      </div>
    </div>

    <div class="profile-mid">
      <div class="follow-btn" >
        <button
          :class="unFollowButton ? 'btn btn-primary rounded-pill' : 'btn btn-secondary rounded-pill'"
          v-if="$route.params.username !== this.currentUser.username"
          @click="followProfile();
          unFollowButton = !unFollowButton
          "
        >
          <span v-if="unFollowButton">팔로우</span>
          <span v-if="!unFollowButton">언팔로우</span>
        </button>
      </div>
      
      <div class="genre">
        <div class="like-genre-txt">
          좋아하는 장르
        </div>
        <div class="like-genre">
          <span class="like-genre-item" v-for="(genre, index) in this.genres_list" :key="index">
          {{genre}}
          </span> 
        </div>
      </div>
    </div>
    
    <div id="modal" class="modal-overlay">
      <div class="modal-window">
        <div class="modal-page">
          <span class="like-article">작성한 게시물</span>
          <button @click="close" class="close-area">X</button>
        </div>
        <div class="modal-title">
          <div class="d-flex">
            <div style="margin-left:1.5em; margin-right:3em;">글 번호</div>
            <div>제목</div>
          </div>
            <div style="margin-right:1em;">좋아요</div>
        </div>
        <div class="modal-item" v-for="article in profile.articles" :key="article.id" :article="article">
          <div class="d-flex">
            <div style="padding-right:3em; margin-left:1.5em; border-right: solid white; color:white;">{{article.pk}}</div>
            <router-link :to="{name: 'ArticleDetail', params:{article:article, articleComments: article.comments}}">
              <div style="margin-left:1.5em; color:white">
                {{article.title}}
              </div>
            </router-link>
          </div>
          <div style="margin-right:1em; padding-left:1em; border-left:solid white; color:white">{{article.liked_users.length}}</div>
        </div>
      </div>
    </div>


    <div class="movie">
      <p class="movie-txt" style="color:white; margin-bottom:2em;" >좋아하는 영화</p>

      <div style="margin:0 6em;">
        <div class="row d-flex justify-content-between flex-wrap">
          <div v-for="(movie, index) in profile.like_movie" :key="movie.id" :movie="movie" :index="index" class="card col-md-3" style="width: 20rem; height:30rem; margin:17.5px; padding-top: 12px; background-color:black">
            <router-link :to="{name: 'MovieDetailView', params:{movie:movie, moviePk:movie.id}}">
              <div class="poster-img" :style="`background-image: url(https://image.tmdb.org/t/p/w500${movie.poster_path})`">
                <div class="poster-index" style="color:white">
                  <span>{{index+1}}</span>&nbsp;&nbsp;<span style="font-size:1.5em">{{movie.title}}</span></div>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'ProfileView',
  data() {
    return {
      genres_list: [],
      all_genres: null,
      unFollowButton: true,
    }
  },
  methods: {
    getUserProfile() {
      const username = {username : this.$route.params.username}
      this.$store.dispatch('getUserProfile',username)
    },
    followProfile() {
      this.$store.dispatch('followProfile', this.profile.pk)
    },
    click() {
      const modal = document.getElementById("modal")
      modal.style.display = 'flex'
    },
    close() {
      const modal = document.getElementById("modal")
      modal.style.display = 'none'
    }
  },
  created() {
    this.getUserProfile() // axios 요청으로 유저가 좋아요한 정보들 불러오기
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/genres/'
    })
    .then(res => {
      this.all_genres = res.data
    })
  }, 
  computed: {
    ...mapGetters(['nowUserProfile']),
    profile() {
      return this.$store.state.accounts.profile
    },
    currentUser() {
      return this.$store.state.accounts.currentUser
    },
  },
  watch: {
    profile: {
      handler() {
        if (this.all_genres) {
          const gen_list = JSON.parse(this.profile.genre_likes)
        this.genres_list = gen_list.genre_likes.map((item) => {
          for (let i = 0; i < this.all_genres.length; i++) {
            if (parseInt(item) === this.all_genres[i].id) {
              return this.all_genres[i].name
            }
          }
        })
        }
      }
    }
  }
}
</script>


<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
* {
  font-family: 'Jeju Gothic', sans-serif;
}
.modal-window {
  border: solid white 1px;
  border-radius: 1em;
  width: 80%;
  margin: 6em;
}
.modal-item {
  background-color: darkgray;
  display: flex;
  justify-content: space-between;
  width: 80%;
  margin: auto;
  margin-top: 1em;
  margin-bottom: 1em;
  padding: 1em;
  font-size: 1.5em;
  border-radius: 10em;
}
.modal-title {
  display: flex;
  justify-content: space-between;
  width: 80%;
  margin: auto;
  font-size: 1.5em;
  color:white
}
.modal-page {
  display: flex;
  justify-content: space-between;
  margin: 1.5em 6em;
  padding-bottom: 1em;
  border-bottom: solid white 1px;
}
.close-area {
  border: none;
  width: 10%;
  height: 50px;
  font-size: 2em;
  color: white;
  background-color: #353535;
}

.like-article {
  font-size: 3em;
  color: white;
}


#modal.modal-overlay {
  display: none;
  margin: auto;
  justify-content: center;
}

.profile-main{
  background-color: #353535;
  border: solid white 1px;
}

h1 {
  color: white
}

.profile-top {
  display: flex;
  justify-content: space-around;
  margin: 0 6em;
}

.profile-top-img {
  width: 200px;
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.profile-name {
  color: white;
  margin-top: 0.5em;
  font-size: 1.5em;
}

.profile-top-img > img {
  width: 100%;
  height: 100%;
}

.profile-top-edit {
  margin-top: 0.5em;
  height: 3em;
}

.profile-top-edit > a {
  border: none;
  width: 80%;
  height: 80%;
}

#profile-edit-btn {
  width: 80%;
  height: 80%;
}

.profile-top-right {
  display: flex;
  justify-content: space-between;
  color: white;
}
.right1 {
  margin:2em;
  font-size: 2em;
  border: none;
  background-color: #353535;
  color: white
}
.right2 {
  margin:2em;
  font-size: 2em;
  display: flex;
  flex-flow: column;
  justify-content: center;
}
.right3 {
  margin:2em;
  font-size: 2em;
  display: flex;
  flex-flow: column;
  justify-content: center;
}

.profile-mid {
  color:white;
  display: flex;
  justify-content: space-around;
  border-top: white solid 1px;
  border-bottom: white solid 1px;
  margin: 0 6em;
  
}
.genre{
  display: flex;
  flex-flow: column;
  justify-content: center;
  background-color: gray;
  width: 500px;
  height: 150px;
  border-radius: 1em;
  margin: 1.5em 0;
}

.like-genre-txt {
  margin: 0.5em;
  margin-top: 0;
  font-size: 2em;
}

.like-genre {
  font-size: 1.5em;
}

.like-genre-item {
  background-color: darkgray;
  border-radius: 5em;
  font-size: 1em;
  margin:0 0.3em;
  padding: 0.2em 0.5em;
  text-align: center;
}

.follow-btn {
  width: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top:1.5em;
}

.follow-btn > button {
  width: 100%;
  height: 50px;
  
}

.follow-btn > button > span {
  font-size: 1.5em;
}

.poster-img {
  background-repeat: no-repeat;
  background-size: 294px 460px;
  border-radius: 10px;
  width: 294px;
  height: 460px;
  border-radius: 10px;
}

.poster-index {
  width: 100%;
  height: 100%;
  background: linear-gradient(to top, black, transparent);
  position: relative !important;
  justify-content: left !important;
  display: flex;
  align-items: end;
}

.poster-index > span {
  font-size: 2em;
}

a {
  text-decoration: none;
}
a:hover > .poster-img {
  transform: scale(1.2);
  transition: 0.5s;
}
a:hover > .poster-img > .poster-index {
  display: none;
}

.movie-txt {
  display: flex;
  margin: 0 6em;
  font-size: 2em;
}
.movie{
  margin: 0 6em;
  margin-top: 1.5em;
}

</style>