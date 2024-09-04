<template>
  <div>
    <router-link :to="{name: 'MovieView'}">
      <img class="main-logo" src="../assets/logo.png" alt="" style="margin:2em 0;">
    </router-link>
    <h1 style="color:white; margin-bottom:0.5em;">SIGN UP</h1>
    <div class="signup-main" style="margin-bottom:3em;">
      <form @submit.prevent="signUp" id='signUpForm'>

        <div class="signup-form">
          <div class="d-flex flex-column justify-content-center align-items-center" style="width:50%; margin-top:1em; margin-left:6em; border-bottom:solid white 1px;">
            <!-- 이미지파일넣기 -->
            <img class="input-img" :src="imageUrl.url" alt="baseuser" style="width:100px; height:100px;"><br>
            <label class="img-btn">
              이미지 선택
              <input class="upload-file" type="file" @change="changeUserImage">
            </label>
          </div>

          <div class="d-flex flex-column justify-content-center" style="width:50%; margin-right:6em; margin-top:1em; border-bottom:solid white 1px;">
            <!-- 이메일 입력창 -->
            <div class="signup">
              <img src="../assets/email.png" alt="" style="width:35px; heigth:100%; margin-right:0.5em;">
              <input
                style="color: white;"
                class="signup-input"
                id="email"
                placeholder="이메일 주소 입력"
                type="email"
                v-model="credentials.email"
                required
                autofocus
              ><br><br>
            </div>

            <div class="signup">
              <!-- 유저아이디 -->
              <img src="../assets/usericon.png" alt="" style="width:35px; heigth:100%; margin-right:0.5em;">
              <input class="signup-input" type="text" placeholder="아이디를 입력하세요" id="inputId" required v-model="credentials.username"><br><br>
            </div>

            <!-- 유저 비밀번호 -->
            <div class="signup">
              <img src="../assets/password.png" alt="" style="width:35px; heigth:100%; margin-right:0.5em;">
              <input
                class="signup-input"
                type="password" 
                placeholder="비밀번호를 입력하세요" 
                id="inputPw" 
                required 
                v-model="credentials.password1"
                minlength="8"
                maxlength="12"
              ><br><br>
            </div>

            <!-- 비밀번호 확인 -->
            <div class="signup">
              <img src="../assets/check.png" alt="" style="width:30px; heigth:100%; margin-right:0.5em;">
              <input
                class="signup-input"
                type="password" 
                placeholder="비밀번호를 확인해주세요" 
                id="checkPw" 
                required 
                v-model="credentials.password2" 
                minlength="8"
                maxlength="12"
              ><br><br>
            </div>
          </div>
        </div>

        <!-- 좋아하는 장르 선택 -->
        <div class="select-genre">
          <div class="genre-title" style="color:white;">좋아하는 장르를 선택해 주세요</div>
          <div class="check-genre">
            <span class="genre-box" v-for="(genre,idx) in genres" :key="genre.id">
              <input
                class="input-genre"
                :id="genre+idx" 
                type="checkbox"  
                :value="genre.id" 
                v-model="genre_likes"
                @click="check"
                >
              <label :for="genre+idx">{{genre.name}}</label>
            </span>
          </div>
        </div>
      </form>
      <AccountErrorListVue v-if="authError" />
      <button class="btn btn-secondary rounded-pill" style="color:white; width:200px; margin-bottom:1.5em; margin-right:1.5em" form="signUpForm" type="submit" >회원가입</button>
      <button @click="goHome" class="btn btn-outline-secondary rounded-pill" style="color:white; width:200px; margin-bottom:1.5em;">돌아가기</button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import AccountErrorListVue from '../components/AccountErrorList.vue'

export default {
  name: 'SignUpView',
  components: {
    AccountErrorListVue
  },
  data() {
    return {
      credentials: {
        username: "",
        password1: "",
        password2: "",
        //  장르 추가
        genre_likes: null,
        email: "",
        profile_img: null,
      },
      genre_likes: [],
      profile_img: '',
      imageUrl: {
        url: "https://png.pngtree.com/png-vector/20191115/ourmid/pngtree-beautiful-profile-line-vector-icon-png-image_1990469.jpg"
      },
      ifFlag: false
    }
  },
  methods: {
    signUp() {
      this.genre_likes = this.genre_likes.map((item) => {
        return item.toString()
      })
      const trans_genre_likes = {
        genre_likes: this.genre_likes
      }
      this.credentials.genre_likes = JSON.stringify(trans_genre_likes)
      if (this.credentials.inputPw !== this.credentials.checkPw) {
        alert('비밀번호가 일치하지 않습니다.')
      } else {
        this.$store.dispatch('signUp', this.credentials)
      }
    },
    // 장르 데이터 받아오기
    getGenres() {
      this.$store.dispatch('getGenres')
    },
    // 유저 이미지 넣기
    changeUserImage(event) {
      let credentials = this.credentials
      let imageUrl = this.imageUrl
      let reader = new FileReader();
      reader.onload = function (event) {
        credentials.profile_img = event.target.result;
        imageUrl.url = event.target.result;
      };

      // reader.addEventListener('load', function() {
      //   this.imageUrl = reader.result;
      // }, false)

      if (event.target.files.length > 0) {
        reader.readAsDataURL(event.target.files[0]);
      } else {
        this.imageUrl = "https://png.pngtree.com/png-vector/20191115/ourmid/pngtree-beautiful-profile-line-vector-icon-png-image_1990469.jpg"
      }
    },
    check() {
      if (this.genre_likes.length >= 3) {
        if (event.target.checked === true) {
          event.target.checked = false
          alert('최대 3개까지 선택 가능 합니다.')
        }
      }
    },
    destroyedPageStatement() {
      this.$store.state.pageState =true
    },
    mountedPageStatement() {
      this.$store.state.pageState =false
    },
    goHome() {
      this.$router.push({name:"MovieView"})
    }
  },
  created() {
    this.getGenres()
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
    genres() {
      return this.$store.state.movies.genresList
    },

  },
}
</script>

<style scoped>
.upload-file {
  display: none;
}
.signup-main{
  background-color: #353535;
  margin:0 6em;
  border: solid white 1px;
  border-radius: 1em;
}

#signUpForm {
  margin:auto;
}
.signup{
  border-bottom: white solid 1px;
  margin-top: 1.5em;
  margin-bottom: 1.5em;
  width: 100%;
  height: 40px;
  background-color: #535353;
}
.signup-input {
  border: none;
  width: 90%;
  height: 90%;
  background-color: #535353;
}
.select-genre{
  border: solid white 1px;
  border-radius: 1em;
  position: relative;
  margin: 3em 6em;
}
.genre-title {
  position: absolute;
  top: -20px;
  font-size: 1.5em;
  left: 50%;
  width:70%;
  transform: translate(-50%);
  background-color: #353535;
}
.check-genre {
  padding: 2em 0;
}
.genre-box {
  margin: 1em 5em;
}
.genre-box > label {
  display:inline-block; 
  width:100px; 
  line-height:50px;
  color: white;
  font-size: 1.2em; 
}
.genre-box > label:hover {
  cursor: pointer;
}
input[type="checkbox"] {
  width: 1rem;
  height: 1rem;
  border-radius: 50%;
  border: 1px solid #999;
  appearance: none;
  cursor: pointer;
  transition: background 0.2s;
}

input[type="checkbox"]:checked {
    background: white;
    border: none;
}
.signup-form{
  display: flex;
}
input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0 1000px #535353 inset;
  -webkit-text-fill-color: white
}
input {
  color: white
}
input[type=password] {
  font-family: "나눔고딕 ExtraBold";
}
.input-img {
  width: 60% !important;
  height: 60% !important;
  border-radius: 50%;
  margin-bottom: 2em;
}
.img-btn {
  color: white;
  background-color: gray;
  padding: 0.5em 2em;
  font-size: 1.2em;
  border-radius: 10em;
}
.img-btn:hover {
  background-color: #535353;
  cursor: pointer;
}
</style>