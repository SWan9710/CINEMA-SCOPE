<template>
  <div class="home">
    <MovieList />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'MovieView',
  data() {
    return {
      keyword: null,
    }
  },
  components: {
    MovieList
  },
}
</script>

<style>


</style>
