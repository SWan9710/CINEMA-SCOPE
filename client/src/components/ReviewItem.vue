<template>
  <div>
    <div style="margin:0 6em;">
      <div class="d-flex justify-content-between" style="color:white; border-bottom: solid white 1px; padding:1em 0;">
        <div class="d-flex">
          <div style="margin:0 3em; text-align:center">{{review.id}}</div>
          <div style="margin:0 3em; text-align:center">{{review.content}}</div>
        </div>

        <div class="d-flex">
          <router-link :to="{name: 'ProfileView',params:{username:review.user.username}}"><div>{{review.user.username}}</div></router-link>
          <div v-if="payload.username === currentUser.username">
            <button @click="reviewDelete">삭제</button></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'ReviewItem',
  props: {
    review: Object
  },
  data() {
    return {
      payload: {
        content: this.review.content,
        username: this.review.user.username
      },
    }
  },
  methods: {
    reviewUpdate() {
      this.$router.push({name: 'ReviewUpdateView', params:{review:this.review}})
    },
    reviewDelete() {
      const payload = {
        moviePk: this.review.movie,
        reviewPk: this.review.id
      }
      this.$store.dispatch('reviewDelete', payload)
    }
  },
  computed: {
    ...mapGetters(['currentUser'])
  }
}
</script>

<style scoped>
button {
  border: none;
  background-color: transparent;
  color:white;
  font-size: 1em;
}
button:hover{
  background-color: darkgray;
  border-radius: 2em;
}

a {
  text-decoration: none;
  color: white;
}
a:hover {
  text-decoration: underline;
}
</style>