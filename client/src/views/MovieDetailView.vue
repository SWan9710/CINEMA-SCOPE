<template>
  <div class="detail-main" style="background-color:#323232">
    <h1 style="color:white; margin:1em 0;">DETAIL MOVIE</h1>
    <div class="detail-top" style="margin-top:1.5em">
      <div class="top-left">
        <img class="poster-img" :src="`https://image.tmdb.org/t/p/w500${this.movies.movie.poster_path}`" alt="">
      </div>
      <div class="top-right d-flex flex-column justify-content-start">
        <div class="detail-txt d-flex flex-column">
          <div style="margin:1em 0;" class="d-flex justify-content-between">
            <div style="width:20%; text-align:start;">제 목</div>
            <div style="width:80%; text-align:end;">{{ movies.movie.title }}</div>
          </div>
          <div style="margin:1em 0;" class="d-flex justify-content-end">
            <div style="width:20%; text-align:start;">평 점</div>
            <div style="width:80%; text-align:end;" >{{ movies.movie.vote_average }}</div>
          </div>
          <div style="margin:1em 0;" class="d-flex justify-content-between">
            <div style="width:20% text-align:start;">장 르</div>
            <div style="width:80%; text-align:end;">
              <span class="text-white" v-for="genre in this.genresList" :key="genre.id" :genre="genre">
                <span v-if="movies.movie.genres.includes(genre.id)">
                  {{genre.name}}
                </span>
              </span>
            </div>
          </div>
          <div style="margin:1em 0;" class="d-flex justify-content-between">
            <div style="width:20%; text-align:start;">개봉일</div>
            <div style="width:80%; text-align:end;">{{ movies.movie.release_date }}</div>
          </div>
        </div>
        <div class="d-flex justify-content-start" style="color:white; margin-bottom:1em; font-size:1.5em;">내 용</div>
        <div class="text-white">
          {{ movies.movie.overview.slice(0, 220) }}
          <span v-if="movies.movie.overview.length > 22" class="showMore" @click="showMore()">...</span>
        </div>
      </div>
    </div>
    <div class="detail-mid">
      <div class="detail-mid-left">
        <div @click="movieLike(movies.movie.id)" :class="movies.movie.like_users.includes(currentUser.pk) ? 'like' : 'dislike' " />
        <button class="steel-btn text-white" @click="click">스틸컷</button>
      </div>
      <div></div>
    </div>
    <!-- 모달창 -->
    <div id="modal" class="modal-overlay">
      <div class="modal-window">
        <div class="modal-page">
          <div class="backdrop-img" :style="`background-image: url(https://image.tmdb.org/t/p/w500${this.movies.movie.backdrop_path})`"></div>
          <div @click="close" class="close-area">&nbsp;x&nbsp;</div>
        </div>
      </div>
    </div>
    
    <!-- 수정해야함 -->
    <div :class="movieState ? 'view' : 'noview'">
      <!-- 트레일러 영상 들고오는 부분 있어야함 -->
      <!-- 그부분 v-if로 영상 유무에 따라 예고편 보여줄지 말지 결정 -->
      <iframe  style="width:80%;height:500px;" v-if="this.trUrl" :src="'https://www.youtube.com/embed/'+this.trUrl+'?autoplay=1&mute=1'" frameborder="0"></iframe>
    </div>
      
      <div class="postem-img" :style="`background-image: url(https://image.tmdb.org/t/p/w500${this.movies.movie.poster_path})`"></div>


    <!-- 여기까지 -->

    <div>
      <div class="d-flex justify-content-start" style="margin: 0 6em; border-bottom: solid white 1px;">
        <div class="movie-review" style="color:white">MOVIE REVIEWS</div>
      </div>
      <!-- 마우스로 클릭하면 글자 사라지게 하기 -->
      <div class="review-list">
        <form @submit.prevent="reviewCreate" id="reviewCreate" style="width:500px; height:50px">
          <textarea class="p-2" id="content" v-model="inputContent" placeholder="리뷰를 작성해 주세요"/>
        </form>
        <button class="review-btn" v-if="isLogIn" form="reviewCreate">작성하기</button>
      </div>

      <div style="margin:0 6em;">
        <div class="d-flex justify-content-between" style="color:white; border-bottom: solid white 1px; padding:1em 0;">
          <div class="d-flex">
            <div style="margin:0 2.5em; text-align:center">번호</div>
            <div style="margin:0 2.5em; text-align:center">내용</div>
          </div>
          <div style="margin-right: 2.5em;">작성자</div>
        </div>
      </div>
      <!-- 전체 리뷰 목록 가져오기 -->
      <ReviewItem
        v-for="review in movies.movie.reviews"
        :key="review.id"
        :review="review"
        :username="$route.params.username"
      />
    </div>
  </div>
</template>

<script>
import ReviewItem from '@/components/ReviewItem'
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'MovieDetailView',  
  props: {
    movie: [Object,String],
    moviePk: [Number,String]
  },
  components: {
    ReviewItem
  },
  data() {
    return {
      trUrl: null,
      inputContent: '',
      movieState: true,
    }
  },
  methods: {
    setMovie() {
      const payload = {
        movie: this.movie
      }
      this.$store.dispatch('setMovie', payload)
    },
    // 장르 받아오기
    getGenres() {
      this.$store.dispatch('getGenres')
    },
    // 예고편 영상 가져오기
    getTrailerMovie() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movies.movie.movie_id}/videos?language=ko-KR`,
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMzFjMDk5ZTk1Mjk3ZWVhZTIzMTA2NzQ5NDE5ODBlYyIsInN1YiI6IjYzZDMzOTNmZTcyZmU4MDA4ZTYxOTBjZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.nb96UwhqMkwXWbkrunw4gdvedywBY8lP4eYZkT84ZoY'
        }
      })
      .then(res => {
        if (res.data.results) {
          this.movieState = true
          this.trUrl = res.data.results[0].key
          for (const element of res.data.results) {
            if (element.name.includes('메인')) {
              this.trUrl = element.key
              break
            } else if (element.name.includes('예고편')) {
              this.trUrl = element.key
              break
            }
          }
        } else {
          this.movieState = false
        }
      })
      .catch(() => {
        console.log('비디오에 대한 정보가 없습니다.')
      })
    },
    // 리뷰생성
    reviewCreate() {
      if (this.isLogIn) {
        const payload = {
          moviePk: this.movies.movie.id,
          content: this.inputContent,
        }
        if (payload.content === '') {
          alert('내용을 입력하세요')
        } else {
          this.$store.dispatch('reviewCreate', payload)
          this.inputContent = ''
        }
      } else {
        alert('리뷰를 작성하려면 로그인을 하세요')
        this.$router.push({name: 'LoginView'})
      }
    },
    movieLike(movie_id) {
      this.$store.dispatch('movieLikeToggle', movie_id)
    },
    click() {
      const modal = document.getElementById("modal")
      modal.style.display = 'flex'
    },
    close() {
      const modal = document.getElementById("modal")
      modal.style.display = 'none'
    },
    showMore() {
      const target = document.querySelector('.showMore')
      if (target.innerText === '...') {
        target.innerText = this.movies.movie.overview.slice(220,)
      } else {
        target.innerText = '...'
      }
    }
  },
  created() {
    // 단일 영화 정보 받아오기
    if (typeof(this.movie) === 'object') {
      this.setMovie()
    }
    this.getGenres() // 장르데이터 뽑기
    // window.scrollTo({top: 0}) // 스크롤 상단이동
    this.getTrailerMovie()
  },
  computed: {
    ...mapGetters(['movies', 'genresList', 'isLogIn', 'currentUser']),
  }

}
</script>

<style scoped>
p {
  margin: 0;
}
.like {
  background-image: url("../assets/images/like-txt.png");
  background-repeat: no-repeat;
  background-size: cover;
  width: 50px;
  height: 50px;
}

.dislike{
  background-image: url("../assets/images/emptyHeart.png");
  background-repeat: no-repeat;
  background-size: cover;
  width: 50px;
  height: 50px;
}

.view {
  display: block;
}
.noview {
  display: none;
}
.detail-main {
  border: solid white 1px;
  border-radius: 1em;
  margin:auto;
  margin-bottom: 3em;
  padding-bottom: 3em;
  width: 1000px;
}
.poster-img {
  width: 100%;
  height: 600px;
}
.detail-top {
  width: 800px;
  display: flex;
  justify-content: center;
  margin: 0 6em;
}
.top-left {
  width:50%;
  margin-right:0.5em;
}
.top-right {
  width:50%;
  margin-left:0.5em;
}
.detail-txt {
  color: white;
  font-size: 1.5em;
  margin: 1em 0;
}
.steel-btn {
  border: none;
  font-size: 1.5em;
  background-color: #535353;
  width: 200px;
  height: 50px;
  border-radius: 10em;
}
.detail-mid{
  margin: 1em 6em;
  border-bottom:solid white 1px;
}
.detail-mid-left {
  display: flex;
  margin: 1em 0;
  justify-content: space-around;
  width: 50%;
}
.backdrop-img {
  margin: auto;
  background-repeat: no-repeat;
  background-size: contain;
  width: 1600px;
  height: 400px;
}
.modal-window {
  width: 80%;
  margin: 0.5em 6em;
}
.modal-page {
  display: flex;
  justify-content: space-between;
  margin: 1.5em 6em;
}
.close-area {
  cursor: pointer;
  width: 50px;
  height: 50px;
  font-size: 2em;
  color:black;
  opacity: 0.7;
  position: relative;
  left: -6%;
}
.close-area:hover {
  color: white;
  transition: 0.5s;
}

#modal.modal-overlay {
  display: none;
  margin: auto;
  justify-content: center;
}
.movie-review {
  font-size: 2em;
}
.review-list{
  width: 100%;
  margin: 1em 6em;
  display: flex;
  justify-content: start;
  align-items: center;
}

textarea {
  resize: none;
  width: 100%;
  height: 100%;
  border: none;
  background-color: darkgray;
  color: white;
}
textarea::placeholder{
  color: white;
}
.review-btn {
  border: none;
  margin-left: 3em;
  height: 50px;
  border-radius: 10em;
  width: 150px;
  font-size: 1.2em;
  background-color: darkgray;
  color: white;
}

.showMore:hover {
  cursor: pointer;
}

</style>