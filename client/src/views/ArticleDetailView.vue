<template>
  <div class="detail-main" style="background-color:#323232">
    <div class="container detail-txt d-flex flex-column">
      <div style="margin:1em 3em;" class="d-flex justify-content-between">
        <div style="width:100%; font-size:2em;">{{articles.article.pk}}번째 게시물</div>
      </div>
      <div style="margin:1em 3em; border:none; border-bottom:solid white 1px;" class="content-body d-flex justify-content-between">
        <div class="content-title">작성자</div>
        <div class="content-content">제목</div>
          <div class="content-title">작성일</div>
      </div>
      <div style="margin:0 3em; border-bottom:solid white 1px;" class="content-body d-flex justify-content-between">
        <div class="content-title">{{articles.article.user.username}}</div>
        <div class="content-content">{{articles.article.title}}</div>
        <div class="content-title">{{articles.article.created_at.slice(0, 10)}}</div>
      </div>
      <div style="margin:0.5em 3em;" class="content-body d-flex justify-content-start">
        <div class="content-title">내용</div>
      </div>

      <div style="margin: 0 3em;" class="content-body">
        <p style="padding: 0 1em; word-wrap: break-word;">{{articles.article.content}}</p>
      </div>
 
      <div style="margin:1em 3em;" class="content-body d-flex justify-content-center">
        <div style="margin:0 2em">좋아요</div>
        <div style="margin:0 2em">{{articles.article.liked_users.length}}</div>
      </div>
        <div style="margin:auto;">마지막 수정 날짜</div>
        <div style="margin:auto; margin-bottom:1em;">{{articles.article.updated_at}}</div>
    </div>

    <div style="margin:0 6em;">
      <div style="border-top: 1px solid white;">
        <div style="cursor:default" class="btn m-3 w-25">
          <div style="cursor:pointer" @click="likeArticle" :class="articles.article.liked_users.includes(currentUser.pk) ? 'like' : 'dislike' " />
        </div>
        <button class="btn btn-outline-secondary m-3 w-25 rounded-pill" style="font-size:1.25em;" @click="goHome">돌아가기</button>
      </div>
      <!-- 사용자 정보 따라 버튼 다르게 보여야함 -->
      <div class="AuthUser" v-if="articles.article.user.username === currentUser.username">
        <button class="btn btn-primary m-3 w-25 rounded-pill" style="background-color:darkgray; border:none; font-size:1.25em; " @click="upDateArticle">수정</button> 
        <button class="btn btn-danger m-3 w-25 rounded-pill" style="font-size:1.25em;" @click="deleteArticle">삭제</button>
      </div>
    </div>
    <hr>
    <div style="margin:0 6em;">
      <h1 class="text-white">댓글 목록</h1>
      <form class="container" @submit.prevent="commentCreate">
        <textarea class="p-3" id="content" v-model="inputContent" placeholder="댓글을 작성해 주세요" style="border-radius:1em;"/>
      </form>
      <button class="btn btn-success mb-4 w-25 rounded-pill" style="background-color:gray; border:none; font-size:1.25em;" @click="commentCreate">작성하기</button>
      <!-- 전체 댓글목록 -->
      <div class="container review text-white">
        <div class="d-flex flex-direction-row">
          <div class="comment">
            번호
          </div>
          <div class="comment-content">
            내용
          </div>
          <div class="comment">
            작성자
          </div>
          <div class="comment">
            좋아요
          </div>
          <div class="comment">
            개수
          </div>
          <div class="comment">
            삭제
          </div>
      </div>
        <CommentItem class="pt-4" style="border-top: 1px solid white; font-size:0.7em;"
          v-for="(comment,idx) in articles.article.comments"
          :key="comment.pk"
          :comment="comment"
          :username="$route.params.username"
          :idx="idx"
        />
    </div>
    </div>
  </div>
</template>

<script>
import CommentItem from '../components/CommentItem'
import {mapGetters} from 'vuex'

export default {
  name: 'ArticleDetailView',
  data() {
    return {
      commentsList: null,
      inputContent: '',
    }
  },
  components: {
    CommentItem
  },
  props: {
    article: [Object, String]
  },
  methods: {
    setArticle() {
      const payload = {
        article: this.article
      }
      this.$store.dispatch('setArticle', payload)
    },
    upDateArticle() {
      this.$router.push({name: 'ArticleUpdate', params: {article: this.article, articlePk: this.article.pk}})
    },
    deleteArticle() {
      const payload = this.articles.article.pk
      this.$store.dispatch('articleDelete', payload)
    },
    goHome() {
      this.$router.push({name: 'CommunityView'})
    },
    likeArticle(event) {
      const payload = this.articles.article.pk
      this.$store.dispatch('likeArticle', payload)
      event.target.classList.toggle('like')
      event.target.classList.toggle('dislike')
    },
    // 게시물의 댓글 생성
    commentCreate() {
      const payload = {
        articlePk: this.articles.article.pk,
        content: this.inputContent,
      }
      if (payload.content === '') {
        alert('댓글을 입력하세요')
      } else {
        this.$store.dispatch('commentCreate', payload)
        this.inputContent = ''
      }
    },
    click() {
      console.log('---')
    }
  },
  computed: {
    ...mapGetters(['articles','currentUser']),
  },
  created() {
    if (typeof(this.article) === 'object') {
      this.setArticle()
    }
  }
}
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
* {
  font-family: 'Jeju Gothic'
}
p {
  margin: 0;
}
.like {
  background-image: url("../assets/images/like-txt.png");
  background-repeat: no-repeat;
  background-size: cover;
  margin: auto;
  width: 40px;
  height: 40px;
  border: none !important;
}

.dislike{
  background-image: url("../assets/images/emptyHeart.png");
  background-repeat: no-repeat;
  background-size: cover;
  margin: auto;
  width: 40px;
  height: 40px;
  border: none !important;
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
  height: 100%;
}
.detail-txt {
  color: white;
  font-size: 1.5em;
}

.content-body {
  padding: 5px;
  width: 80%
}

.content-title {
  width: 30%;
  
}
.content-content {
  width: 70%;
}

.AuthUser {
  border-top: 1px solid white;
  border-bottom: 1px solid white;
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

.review {
  font-size: 1.3em;
}

.comment {
  width: 10%;
}

.comment-content {
  width: 50%;
}
</style>