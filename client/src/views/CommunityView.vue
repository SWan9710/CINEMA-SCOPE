<template>
  <div>
    <h1 style="color:white">이야기 게시판</h1>
    
    <div class="article-list" style="background-color: #535353; margin: 0 6em; padding-bottom:3em; padding-top: 1em;">
      <div class="button d-flex justify-content-end" style="margin:0 6em;">
        <button @click="moveCreate">+게시물생성</button>
      </div>
      <div style="margin:0 6em;">
        <div class="d-flex justify-content-between" style="color:white; border-bottom: solid white 1px; padding:1em 0;">
          <div class="d-flex">
            <div style="margin:0 2.5em; text-align:center">번호</div>
            <div style="margin:0 2.5em; text-align:center">내용</div>
          </div>
          <div>
            <div style="margin-right: 2.5em;">작성자</div>
          </div>
        </div>
      </div>
        
      <CommunityItem 
        v-for="article in articles"
        :key="article.id"
        :article="article"
      />
    </div>
  </div>
</template>

<script>
import CommunityItem from '../components/CommunityItem'

export default {
  name: 'CommunityView',
  components: {
    CommunityItem
  },
  methods: {
    getArticleList() {
      this.$store.dispatch('getArticleList')
    },
    moveCreate() {
      this.$router.push({name: 'ArticleCreate'})
    }
  },
  created() {
    this.getArticleList()
  },
  computed: {
    articles() {
      return this.$store.state.community.articleList
    }
  }
}
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
* {
  font-family: 'Jeju Gothic'
}

.article-list{
  margin: 1em 6em;
  border: solid white 1px;
  border-radius: 1em;
}
button {
  border: none;
  background-color: transparent;
  color: white ;
  border-radius: 10em;
  width: 100px;
}
button:hover {
  background-color: #353535;
}
</style>