<template>
  <div style="background-color: #323232;">
    
    <!-- 장르별 영화 목록 -->
    <div class="main">
        <div class="genre">
            <p class="genre-explain">장르별 영화</p>
            <select class="genre-select rounded-pill" @change="getGenreMovies" id="genre-select-list" >
                <option 
                    v-for="genre in genres" 
                    :key="genre.id" 
                    :genre="genre" 
                    :value="genre.id"
                    size="4"
                >{{genre.name}}
                </option>
            </select>
        </div>

        <carousel class="m-5 mt-0" :perPage="5">
            <slide v-for="(genreMovie, index) in genreMovies" :key="genreMovie.id" style="height:100%">
                <MovieListItem :movie="genreMovie" :index="index"/>
            </slide>
        </carousel>
    </div>

    <!-- 개봉일 순 영화 목록 -->
    <div class="main">
        <div class="genre">
            <span class="movie-explain">최신 영화</span>
        </div>
        <carousel class="m-5" :perPage="5">
            <slide v-for="(releaseMovie, index) in releaseMovies" :key="releaseMovie.id" style="height:100%">
                <MovieListItem :movie="releaseMovie" :index="index" />
            </slide>
        </carousel>
    </div>

    <!-- 전체 영화 목록 -->
    <div class="main">
        <div class="genre">
            <span class="movie-explain">인기 영화</span>
        </div>
        <carousel class="m-5" :perPage="5">
            <slide v-for="(movie, index) in movies" :key="movie.id" style="height:100%">
                <MovieListItem :movie="movie" :index="index" />
            </slide>
        </carousel>
    </div>

    <div v-if="currentUser" class="main">
        <div class="genre">
            <span class="movie-explain">좋아요 한 영화</span>
        </div>
        <carousel class="m-5" :perPage="5">
            <slide v-for="(movie, index) in userLikeMovies" :key="movie.id" style="height:100%">
                <MovieListItem :movie="movie" :index="index" />
            </slide>
        </carousel>
    </div>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem'
import { Carousel, Slide } from 'vue-carousel'

export default {
    name: 'MovieList',
    components: {
        MovieListItem,
        Carousel,
        Slide
    },
    methods: {
        getMovieList() {
            this.$store.dispatch('getMovieList')
        },
        getGenres() {
            this.$store.dispatch('getGenres')
        },
        // 장르별 평점순 영화 요청
        getGenreMovies(event) {
            // 디폴트 값 으로 모험 장르인 12로 요청
            let payload = '12'
            if (event) {
                payload = event.target.value
            }
            this.$store.dispatch('getGenreMovies',payload)
        },
        // 개봉일 순으로 영화 요청
        getReleaseMovies() {
            this.$store.dispatch('getReleaseMovies')
        },
        // 유저가 있을 때
        getUserLikeMovies(userPK) {
            this.$store.dispatch('getUserLikeMovies', userPK)
        }
    },
    created() {
        this.getMovieList()
        this.getGenres()
        this.getGenreMovies()
        this.getReleaseMovies()
        if (this.currentUser) {
            this.getUserLikeMovies(this.currentUser.pk)
        }
    },
    computed: {
        movies() {
            return this.$store.state.movies.movieList
        },
        genres() {
            return this.$store.state.movies.genresList
        },
        genreMovies() {
            return this.$store.state.movies.genreMovies
        },
        releaseMovies() {
            return this.$store.state.movies.releaseMovies
        },
        userLikeMovies() {
            return this.$store.state.movies.userLikeMovies
        },
        currentUser() {
            return this.$store.state.accounts.currentUser
        }
    }
}
</script>

<style scoped>
.main {
    margin: 0 4em ;
}
.genre {
    display: flex;
    justify-content:space-between;
    align-items: center;
    margin-top: 50px;
    margin-left: 3em;
    margin-bottom: 0;
    padding-top: 2em;
}
.genre-label {
    color: white;
    margin-right: 1em;
    margin-bottom: 0;
}
.genre-select {
    background-color: black;
    color: white;
    text-align: center;
    width: 8em;
    height: 30px;
    margin-right: 3em;
}
.movie-explain {
    color:white;
    position: relative !important;
    display: flex;
    top: 40px;
    font-size: 2em;
}
.genre-explain {
    color: white;
    font-size: 2em;
}

</style>