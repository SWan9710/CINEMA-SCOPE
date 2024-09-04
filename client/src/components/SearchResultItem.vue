<template>
  <div class="card col-md-3" style="width: 20rem; height:30rem; margin:17.5px; padding-top: 12px; background-color:black">
    <router-link :to="{name: 'MovieDetailView', params:{movie:searchResult}}">
      <div class="poster-img" :style="`background-image: url(https://image.tmdb.org/t/p/w500${this.searchResult.poster_path})`">
        <div class="poster-index" style="color:white">
        &nbsp;{{ idx + 1 }}&nbsp;<span>{{this.searchResult.title}}</span></div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'SearchResultItem',
  props: {
    searchResult: Object,
    idx: [Number, String]
  },
}
</script>

<style scoped>
.movie{
  margin: 0 6em;
  margin-top: 1.5em;
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
  font-size: 2em;
  width: 100%;
  height: 100%;
  background: linear-gradient(to top, black, transparent);
  position: relative !important;
  justify-content: left !important;
  display: flex;
  align-items: end;
}

.poster-index > span {
  font-size: 0.5em;
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

</style>