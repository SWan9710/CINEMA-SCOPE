<template>
  <div>
    <router-link :to="{name: 'MovieDetailView', params: {movie: movie, moviePk: movie.id}}">
      <div class="poster-img" :style="`background-image: url(https://image.tmdb.org/t/p/w500${movie.poster_path})`" alt="">
        <div class="poster-index">&nbsp;{{index + 1}}<span>&nbsp;{{movie.title}}</span></div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
    name: 'MovieListItem',
    props: {
      movie: Object,
      index: [Number, String],
    },
}
</script>

<style scoped>
div {
  background-color: gray;
  display: flex;
  justify-content: center;
}
.poster-index {
  position: relative !important;
  justify-content: left !important;
  width: 100%;
  height: 100%;
  font-size: 2em;
  background: linear-gradient(to top, black, transparent);
  align-items: flex-end;
  color: white
}
.poster-index > span {
  font-size: 0.5em;
}
.poster-img {
  background-repeat: no-repeat;
  background-size: 200px 300px;
  margin-top: 3em;
  border-radius: 10px;
  width: 200px;
  height: 300px;
}

a:hover > .poster-img > .poster-index {
  display: none;
}

a:hover > .poster-img {
  transform: scale(1.3);
  transition: 0.5s;
}

a {
  margin:auto;
  text-decoration: none;
  display: flex;
  flex-flow: column;
  justify-content: center;
  align-items: center;
  padding-bottom: 3em;
}
</style>