<template>
  <div>
    <div v-if="!flag">
      <h3 style="color:white">검색중 입니다...</h3>
    </div>
    <div v-else>
      <h1 style="color:white">"{{keyword}}"에 대한 검색 결과 입니다.</h1>
      <div class="row">
        <SearchResultItem
          v-for="(searchResult, idx) in searchResults"
          :key="searchResult.id"
          :search-result="searchResult" :idx="idx"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchResultItem from '../components/SearchResultItem'

export default {
  name: 'SearchResultView',
  data() {
    return {
      searchResults: null,
      flag: false,
    }
  },
  components: {
    SearchResultItem
  },
  props: {
    keyword: String,
  },
  created() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/movies/search/${this.keyword}/`
    })
    .then(res => {
      this.searchResults = res.data
      this.flag = !this.flag
    })
  }
}
</script>

<style>

</style>