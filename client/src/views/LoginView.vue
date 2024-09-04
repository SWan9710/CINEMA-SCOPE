<template>
  <div class="main-login">
    <router-link :to="{name: 'MovieView'}">
      <img class="main-logo" src="../assets/logo.png" alt="">
    </router-link>
    <div class="login">
      <h1>LOGIN</h1>
      <form @submit.prevent="login">
        <div>
          <input type="text" placeholder="아이디" v-model="inputId" id="id" autofocus>
          <br><br>
          <input type="password" placeholder="비밀번호" v-model="inputPw" id="password" @keyup.enter="logIn">
        </div><br><br>
      </form>
      <AccountErrorListVue v-if="authError" />
      <div class="login-btn">
        <button class="btn btn-secondary rounded-pill" @click="logIn">로그인</button>
        <button class="btn btn-outline-secondary rounded-pill" @click="signUp">회원가입</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import AccountErrorListVue from '../components/AccountErrorList.vue'

export default {
  name: 'LoginView',
  components: {
    AccountErrorListVue
  },
  data() {
    return {
      inputId: '',
      inputPw: ''
    }
  },
  methods: {
    logIn() {
      const inputId = this.inputId
      const inputPw = this.inputPw

      const payload = {
        username: inputId,
        password: inputPw,
      }
      if (payload.inputId === '') {
        alert('아이디를 입력하세요')
      } else if (payload.inputPw === '') {
        alert('비밀번호를 입력하세요')
      } else {
        this.$store.dispatch('logIn', payload)
      }
    },
    signUp() {
      this.$router.push({name: 'SignUpView'})
    },
    destroyedPageStatement() {
      this.$store.state.pageState =true
    },
    mountedPageStatement() {
      this.$store.state.pageState =false
    },
  },
  created() {

    this.$store.commit('SET_AUTH_ERROR', null)
  },
  destroyed() {
    this.destroyedPageStatement()
  },
  mounted() {
    this.mountedPageStatement()
  },
  computed: {
    ...mapGetters(['authError']),
  },
}
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
* {
  font-family: 'Jeju Gothic'
}

.login {
  border: solid white 1px;
  border-radius: 1em;
  padding: 3em;
  width: 50%;
  height: 500px;
  margin: auto;
  background-color: #353535;
}
.main-logo {
  margin-top: 6em;
  margin-bottom: 2em;
}
input {
  outline-style: none;
  width: 60%;
  height: 50px;
  background-color: #353535;
  border: none;
  border-bottom: solid white 1px;
  color: white;
  font-size: 1.6em;
}
input::placeholder {
  color: white;
}
.login-btn {
  display: flex;
  flex-flow: column;
  width: 60%;
  margin: auto
}
.login-btn > button {
  margin-bottom: 1em;
  font-size: 2em;
}

h1 {
  color: white;
  margin-bottom:1em;
  font-size: 2em;
}
input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0 1000px #353535 inset;
  -webkit-text-fill-color: white
}
input {
  color: white
}
input[type=password] {
  font-family: "나눔고딕 ExtraBold";
}
</style>