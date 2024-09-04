<template>
    <div>
      <h1 style="color:white;">게시물 수정하기</h1>
      <div style="border:solid white 1px; margin:1em 6em; background-color:#353535;">
        <form @submit.prevent="articleCreate">
          <div class="article-info" style="color:white">{{article.pk}} 번째 게시물</div>
          <label for="title" style="color:white" id="title-label">제목</label>
          <input type="text" id="title" v-model="inputTitle" autofocus><br><br>

          <label for="content" style="color:white" id="content-label">내용</label>
          <textarea id="content" v-model="inputContent"/><br><br>
        </form>
        <button class="btn btn-secondary rounded-pill" style="margin-bottom: 1em; width:200px; height: 50px; font-size: 2em; padding: 0; margin-right:1em;" @click="articleUpdate">수정하기</button>
      <button class="btn btn-secondary rounded-pill" style="margin-bottom: 1em; width:200px; height: 50px; font-size: 2em; padding: 0;" @click="back">돌아가기</button>
      </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleUpdateView',
  props: {
    article: [Object, String],
    articlePk: [Number, String]
  },
  data() {
    return {
      inputTitle: this.article.title,
      inputContent: this.article.content
    }
  },
  methods: {
    articleUpdate() {
      const payload = {
        title: this.inputTitle,
        content: this.inputContent,
        articlePk: this.article.pk
      }
      this.$store.dispatch('articleUpdate', payload)
    },
    back() {
      this.$router.push({
        name: 'ArticleDetail',
        params: {
          article: this.article,
          articleComments: this.article.comments
        }
      })
    }
  },
}
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
* {
  font-family: 'Jeju Gothic'
}

.article-info{
  margin-top:1em;
  font-size: 2em;
}

#title {
  width: 80%;
  height: 80px;
  font-size: 2em;
  color: white;
  border: none;
  padding: 0;
  background-color: #353535;
  border-bottom: solid white 1px;
  padding: 1em 3em;
}
input::placeholder {
  color:white;
  background-color: #353535;
}

#title-label {
  position: relative;
  left: 3em;
}

#content {
  resize: none;
  width: 80%;
  height: 500px;
  font-size: 2em;
  color: white;
  border: none;
  padding: 0;
  background-color: #353535;
  padding: 1em 3em;
  border-bottom: solid white 1px;
}
#content-label {
  position: relative;
  left: 3em;
  top: -27.5em;
}
textarea::placeholder{
  color:white;
  background-color: #353535;
}


</style>