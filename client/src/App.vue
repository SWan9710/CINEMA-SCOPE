<template>
  <div id="app">
    <NavBarView /> <!-- 상단고정 걸기 -->
    <footer :class="pageState ? 'start-app' : 'none-start-app'">
      <button class="top-button rounded-pill" @click="goTop">Top</button>
    </footer>
  </div>
</template>
<script>
import NavBarView from './views/NavBarView'

export default {
  components: {
    NavBarView
  },
  methods: {
    goTop() {
      window.scrollTo({top: 0})
    },
  },
  computed: {
    pageState() {
      return this.$store.state.pageState
    }
  },
}
</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
* {
  font-family: 'Jeju Gothic'
}
</style>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
* {
  margin: 0;
  padding: 0;
  font-family: 'Jeju Gothic', sans-serif;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

footer {
  position: fixed;
  bottom: 3%;
  right: 2%;
}
.none-start-app {
  display: none;
}

.top-button {
  border: none;
  font-size: 1.2em;
  padding: 0 0.5em;
  background: white
}
</style>
