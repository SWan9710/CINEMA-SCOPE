<template>
  <div>
    <div class="d-flex flex-direction-row mb-2 align-items-center">
      <div class="comment">
        {{comment.pk}}
      </div>
      <div class="comment-content">
        {{comment.content}}
      </div>
      <div class="comment">
        {{comment.user.username}}
      </div>
      <div class="comment">
        <div style="cursor:default" class="btn p-1">
          <div style="cursor:pointer" @click="likeComment" :class="comment.liked_users.includes(currentUser.pk) ? 'like' : 'dislike' " />
        </div>
      </div>
      <div class="comment">
        <div>{{comment.liked_users.length}}</div>
      </div>
      <div class="comment">
        <!-- 인증된 유저한테만 보이기 -->
        <button class="btn btn-danger p-1 rounded-pill"
          v-if="payload.username === currentUser.username"
          @click="commentDelete">삭제</button>
        </div>
      </div>
    </div>
    
    
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'CommentItem',
  props: {
    comment: Object,
    username: {
      required: true
    },
    idx: [Number, String]
  },
  data() {
    return {
      payload: {
        content: this.comment.content,
        username: this.comment.user.username
      }
    }
  },
  computed: {
    ...mapGetters(['currentUser'])
  },
  methods: {
    commentDelete() {
      const payload = {
        articlePk: this.comment.article,
        commentPk: this.comment.pk
      }
      this.$store.dispatch('commentDelete', payload)
    },
    likeComment(event) {
      const payload = {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        idx: this.idx
      }
      this.$store.dispatch('likeComment',payload)
      event.target.classList.toggle('like')
      event.target.classList.toggle('dislike')
    }
  },
}

</script>

<style scoped>

.like {
  background-image: url("../assets/images/like-txt.png");
  background-repeat: no-repeat;
  background-size: cover;
  width: 25px;
  height: 25px;
}

.dislike{
  background-image: url("../assets/images/emptyHeart.png");
  background-repeat: no-repeat;
  background-size: cover;
  width: 25px;
  height: 25px;
}

.comment {
  width: 10%;
}

.comment-content {
  width: 50%;
}



</style>