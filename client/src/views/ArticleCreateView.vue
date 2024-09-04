<template>
  <div>
    <h1 style="color:white">게시물 작성</h1>
    <div style="border:solid white 1px; margin: 0 6em;">
      <form @submit.prevent="articleCreate" style="margin-top:2em;">
          <input type="text" id="title" v-model="inputTitle" placeholder="제목을 작성하세요">
          <textarea id="content" v-model="inputContent" placeholder="내용을 입력하세요"/><br><br>
      </form>
      <button class="btn btn-secondary rounded-pill" style="margin-bottom: 1em; width:200px; height: 50px; font-size: 2em; padding: 0; margin-right:1em;" @click="articleCreate">생성</button>
      <button class="btn btn-secondary rounded-pill" style="margin-bottom: 1em; width:200px; height: 50px; font-size: 2em; padding: 0;" @click="back">돌아가기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleCreateView',
  data() {
    return {
      inputTitle: '',
      inputContent: ''
    }
  },
  methods: {
    articleCreate() {
      const payload = {
        title: this.inputTitle,
        content: this.inputContent,
      }
      if (payload.title === '') {
        alert('제목을 입력하세요')
      } else if (payload.content === '') {
        alert('내용을 입력하세요')
      } else {
        this.$store.dispatch('articleCreate', payload)
      }
    },
    back() {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
* {
  font-family: 'Jeju Gothic'
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
}
textarea::placeholder{
  color:white;
  background-color: #353535;
}

</style>