<template>
  <div>
    <section>
      <span class="text" v-for="(word, idx) in startWords1" :key="idx"
        >{{ word }}&nbsp;</span>
      <img class="text text-Image" src="../assets/images/logoImage.png" alt="O">
      <span class="text" v-for="word in startWords2" :key="word"
      >{{ word }}&nbsp;</span>
    </section>
  </div>
</template>

<script>
import VueAnime from "vue-animejs";
import Vue from "vue";
Vue.use(VueAnime);

export default {
  name: "StartView",
  data() {
    return {
      startWords1: "CINEMA   SC",
      startWords2: "PE"
    };
  },
  created() {
    setTimeout(() => {
      this.$store.commit("START_APP")
      this.$router.push({ path: "/movie" })}, 3000);
  },
  mounted() {
    this.$anime({
      targets: ".text",
      width: "100%",
      easing: "easeInOutExpo",
      direction: "alternate",
    });
    
  },
};
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Jeju Gothic', sans-serif;
}
section {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: black;
  overflow: hidden;
}
section .text {
  position: relative;
  font-size: 7em;
  text-align: center;
  color: white;
  -webkit-box-reflect: below -0.6em linear-gradient(transparent, #0004);
}
section .text span {
  position: relative;
}

.text-image {
  width: 300px;
  height: 300px
}
</style>