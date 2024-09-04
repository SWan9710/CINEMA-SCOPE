<template>
  <div style="margin:0 6em;">
    <div class="d-flex justify-content-between" style="color:white; border-bottom: solid white 1px; padding:1em 0;">
      <router-link class="d-flex" :to="{name:'ArticleDetail', params: {article: article, articleComments: article.comments}}">
        <div style="margin:0 2.5em; text-align:center">{{article.pk}}</div>
        <div style="margin:0 2.5em; text-align:center">{{article.title}}</div>
      </router-link>
      <div>
        <router-link :to="{name: 'ProfileView',params:{username:article.user.username}}">
          <div style="margin-right: 2.5em;">{{article.user.username}}</div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommunityList',
  props: {
    article: Object,
  },
}
</script>

<style scoped>

a {
  text-decoration: none;
  color: white;
}
a:hover {
  text-decoration: underline;
}
</style>