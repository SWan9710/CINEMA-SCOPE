<template>
  <div>
    <Tinder ref="tinder" key-name="poster_path" :queue.sync="queue" :offset-y="10" @submit="onSubmit">
      <template slot-scope="scope">
        <div
          class="pic"
          :style="{
            'background-image': `url(https://image.tmdb.org/t/p/w500${scope.data.poster_path})`
          }"
        >
          <div class="title">{{ scope.data.movie.title }}</div><br/>
        </div>
      </template>
      <img class="like-pointer" slot="like" src="../assets/images/like-txt.png" />
      <img class="nope-pointer" slot="nope" src="../assets/images/nope-txt.png" />
      <img class="super-pointer" slot="super" src="../assets/images/logoImage.png" />
      <img class="down-pointer" slot="down" src="../assets/images/rewind-txt.png" />
    </Tinder>
    <div class="btns">
      <img src="../assets/images/rewind.png" @click="decide('rewind')" />
      <img src="../assets/images/nope.png" @click="decide('nope')" />
      <img class="logoImage" src="../assets/images/logoImage2.png" @click="decide('super')" />
      <img src="../assets/images/like.png" @click="decide('like')" />
      <img src="../assets/images/home.png" @click="decide('help')" />
    </div>
  </div>
</template>

<script>
import Tinder from "vue-tinder";

export default {
  name: "TinderMainView",
  components: {
    Tinder
  },
  data: () => ({
    queue: [],
    offset: 0,
    history: []
  }),
  created() {
    this.$store.dispatch('getRandomMovies')
    this.pageStatement()
  },
  destroyed() {
    this.pageStatement()
  },
  watch: {
    randomMovies() {
      this.mock()
    }
  },
  computed: {
    randomMovies() {
      return this.$store.state.movies.randomMovies
    }
  },
  methods: {
    mock(count = 5, append = true) {
      const list = []
      for (let i = 0; i < count; i++) {
        list.push({ poster_path: this.randomMovies[this.offset].poster_path, movie: this.randomMovies[this.offset]})
        this.offset++
      }
      if (append) {
        this.queue = this.queue.concat(list)
      } else {
        this.queue.unshift(...list)
      }
    },
    onSubmit({ item, type }) {
      if (type === 'like') {
        this.$store.dispatch('movieLike', item.movie.id)
      } else if (type === 'super') {
        this.$store.dispatch('saveMovieLike', this.$store.state.movies.movieLike)
      } else if (type == 'nope') {
        this.$store.dispatch('movieDisLike', item.movie.id)
      }
      if (this.queue.length < 3) {
        this.mock()
      }
      this.history.push(item)
    },
    async decide(choice) {
      if (choice === 'rewind') {
        if (this.history.length) {
          this.$refs.tinder.rewind(
            this.history.splice(-Math.ceil(Math.random() * 3))
          )
        }
      } else if (choice === 'help') {
        this.$router.push({name: "MovieView"})
      } else if (choice === 'like') {
        this.$refs.tinder.decide(choice)
      } else if (choice === 'nope') {
        this.$refs.tinder.decide(choice)
      } else {
        this.$refs.tinder.decide(choice)
      }
    },
    pageStatement() {
      this.$store.state.pageState = !this.$store.state.pageState
    }
  },
}
</script>

<style scoped>
html,
body {
  height: 100%;
}

body {
  margin: 0;
  background-color: #20262e;
  overflow: hidden;
}

#app .vue-tinder {
  position: absolute;
  z-index: 1;
  left: 0;
  right: 0;
  top: 50px;
  margin: auto;
  width: calc(100% - 20px);
  height: calc(100% - 50px - 65px - 47px - 16px);
  min-width: 500px;
  max-width: 355px;
}

.nope-pointer,
.like-pointer {
  position: absolute;
  z-index: 1;
  top: 20px;
  width: 64px;
  height: 64px;
}

.nope-pointer {
  right: 10px;
}

.like-pointer {
  left: 10px;
}

.rewind-pointer {
  position: absolute;
  z-index: 1;
  top: 20px;
  right: 10px;
  width: 112px;
  height: 78px;
}

.logoImage{
  background-color: white;
  border-radius: 50%;
}

.pic {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  border: solid white 1px;
  border-radius: 1em;
}

.pic:hover {
  cursor: pointer;
  opacity: 0.7;
}

.pic:hover > .title {
  display: block;
  color:  black;
  background-color: white;
}

.title {
  width: 100%;
  display: none;
  font-size: 1.5em;
  font-family: 'Jeju Gothic', sans-serif;
}

.btns {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 30px;
  margin: auto;
  height: 65px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 300px;
  max-width: 355px;
}

.btns img {
  margin-right: 12px;
  box-shadow: 0 4px 9px rgba(0, 0, 0, 0.15);
  border-radius: 50%;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.btns img:nth-child(2n + 1) {
  width: 53px;
}

.btns img:nth-child(2n) {
  width: 65px;
}

.btns img:nth-last-child(1) {
  margin-right: 0;
}



</style>