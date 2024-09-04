<template>
  <div style="background-color: black;">
    <div :class="pageState ? 'start-app' : 'none-start-app'" >

      <div class="nav-logo">
        <router-link :to="{name: 'MovieView'}">
          <img class="nav-img" src="../assets/logo.png" alt="">
        </router-link>
      </div>

      <div class="nav-item d-flex justify-content-between">
        <div class="nav-left">
          <router-link :to="{name: 'MovieView'}">MOVIES</router-link>
          <router-link :to="{name: 'CommunityView'}">COMMUNITY</router-link>
          <router-link v-if="currentUser" :to="{name: 'TinderMainView'}">PICK+</router-link>
          <router-link v-if="currentUser" :to="{name: 'WishListView', params: {username:this.$store.state.accounts.currentUser.username}}">WISH LIST</router-link>
        </div>

        <div class="nav-right">
          <!-- 로그인 상태 -->
          <span v-if="!currentUser">
            <router-link :to="{name: 'LoginView'}">LOG IN</router-link>
            <router-link :to="{name: 'SignUpView'}">SIGN UP</router-link>
          </span>
          <span v-if="currentUser">
            <button @click="logOut" style="color:white; background-color:black; border: none;">LOG OUT</button>
            <router-link :to="{name: 'ProfileView',params:{username:this.$store.state.accounts.currentUser.username}}">PROFILE</router-link>
          </span>
        </div>
      </div>

      <!-- 검색창 부분 -->
      <div align="center" class="mt-2">
        <input 
          class="search-input rounded-pill"
          type="text"
          placeholder="보고싶은 영화를 입력하세요"
          @keyup.enter="onSearch"
          v-model="keyword"
          style="width:800px; height: 50px; text-align:center"
        > 
      </div>
    </div>

    <router-view :key="$route.fullPath"/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'NavBarView',
  data() {
    return {
      keyword: null,
    }
  },
  computed: {
    ...mapGetters(['isLogIn', 'currentUser']),
    pageState() {
      return this.$store.state.pageState
    },
    profile() {
      return this.$store.state.accounts.profile
    }
  },
  methods: {
    logOut() {
      if (this.isLogIn) {
        this.$store.dispatch('logOut')
      } else {
        alert('잘못된 접근')
      }
    },
    onSearch() {
      if (this.keyword === null) {
        alert('검색어를 입력해 주세요')
      } else {
        this.$router.push({
          name: 'SearchResultView',
          params: {
            'keyword' : this.keyword
          }
        })
        this.keyword = null
      }
    },
  }
}
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
input::-webkit-input-placeholder{
  background-image: url(https://cdn1.iconfinder.com/data/icons/hawcons/32/698627-icon-111-search-256.png) ;
  background-size: contain;
  background-position: 10px center;
  background-repeat: no-repeat;
  text-align: center;
  text-indent: 0;
}

* {
  margin: 0;
  padding: 0;
  font-family: 'Jeju Gothic', sans-serif;
}

.nav-img {
  width: 400px;
  height: 50px;
}

.nav-left a {
  text-decoration: none;
  color: white;
  margin-right: 1em;
  margin-left: 1em;
  position: relative;
  padding: 6px 12px;
}

.nav-left a::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translate(-50%);
  width: 0%;
  height: 4px;
  background: white;
  transition: all 0.2s ease-out;
}

.nav-left a:hover::after {
  width: 100%
}

.nav-right a {
  text-decoration: none;
  color: white;
  margin-right: 1em;
  margin-left: 1em;
  position: relative;
  padding: 6px 12px;
}

.nav-right a::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translate(-50%);
  width: 0%;
  height: 4px;
  background: white;
  transition: all 0.2s ease-out;
}

.nav-right a:hover::after {
  width: 100%
}

.nav-right button {
  text-decoration: none;
  color: white;
  margin-right: 1em;
  margin-left: 1em;
  position: relative;
  padding: 6px 12px;
}

.nav-right button::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translate(-50%);
  width: 0%;
  height: 4px;
  background: white;
  transition: all 0.2s ease-out;
}

.nav-right button:hover::after {
  width: 100%
}






.nav-item{
  margin: 1em 0;
}

.start-app {
  margin: 30px 100px;
}

.none-start-app {
  display: none;
}
</style>