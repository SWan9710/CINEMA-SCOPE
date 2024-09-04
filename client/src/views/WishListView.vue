<template>
  <div>
    <h3 class="text-white">내가 찜한 것들</h3>
    <div class="d-flex justify-content-between flex-wrap">
      <div class="row m-5" style="width:200px; height:300px;" v-for="(movie,idx) in profile.like_movie" :key="movie.id">
        <div>
          <p @click="goDetail(movie)" @mouseout="out(idx)" @mouseover="hover(idx)" :class="`pic pic${idx}`" :style="{'background-image': `url(https://image.tmdb.org/t/p/w500${movie.poster_path})`}" alt="이미지가 없습니다." />
          <img @click="click(movie)" @mouseover="hover(idx)" :class="`nope-img nope-img${idx}`" src="@/assets/images/logoImage2.png" alt="">
          <p class="text-white">{{movie.title}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'WishListView',
  methods: {
    getUserProfile() {
      const username = {username : this.$route.params.username}
      this.$store.dispatch('getUserProfile',username)
    },
    hover(idx) {
      const pic = document.querySelector(`.pic${idx}`)
      const nopeImg = document.querySelector(`.nope-img${idx}`)
      pic.classList.add('pic-hover')
      nopeImg.classList.add('img-hover')
      nopeImg.classList.remove('nope-img')
    },
    out(idx) {
      const pic = document.querySelector(`.pic${idx}`)
      const nopeImg = document.querySelector(`.nope-img${idx}`)
      pic.classList.remove('pic-hover')
      nopeImg.classList.remove('img-hover')
      nopeImg.classList.add('nope-img')
    },
    click(movie) {
      const payload = {
        movie_id: movie.id,
        username: this.$route.params.username
      }
      this.$store.dispatch('movieRemove', payload)
    },
    goDetail(movie) {
      this.$router.push({
        name: 'MovieDetailView', params: {movie: movie, moviePk: movie.id}
      })
    }
  },
  created() {
    this.getUserProfile()
  },
  computed: {
    ...mapGetters(['profile'])
  },
}

</script>

<style scoped>

.pic {
  cursor: pointer;
  width: 200px;
  height: 300px;
  background-size: cover;
  background-position: center;
  border: solid white 1px;
  border-radius: 1em;
}

.pic-hover {
  opacity: 0.7;
  scale: 1.3;
  transition: 0.5s;
}

.img-hover {
  padding: 3px;
  background-color: white;
  border-radius: 50%;
  cursor: pointer;
  display: block;
  position: relative;
  bottom: 300px;
  width: 24%;
  margin-top: 20%;
  margin-left: 45%;
  transition: 0.5s;
}

.nope-img {
  cursor: pointer;
  position: relative;
  width: 20%;
  height: 0%;
  visibility: hidden;
}

</style>