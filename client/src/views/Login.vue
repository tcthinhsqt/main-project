<template>
  <div class="main-content">
    <!-- Header -->
    <div class="header bg-gradient-primary py-7 py-lg-8 pt-lg-2">
      <div class="container">
        <div class="header-body text-center mb-7">
          <div class="row justify-content-center">
            <div class="col-xl-5 col-lg-6 col-md-8 px-5">
              <h1 class="text-white">Đăng nhập để truy cập vào hệ thống</h1>
              <p class="text-lead text-white">Đăng nhập hoặc tạo tài khoản hoàn toàn miễn phí.</p>
            </div>
          </div>
          <div class="mb--6 pt-5">
            <router-link :to="{ name: 'home'}"><h1 class="back-home">◃TRỞ VỀ TRANG CHỦ</h1></router-link>
          </div>
        </div>
      </div>
      <div class="separator separator-bottom separator-skew zindex-100">
        <svg x="0" y="0" viewBox="0 0 2560 100" preserveAspectRatio="none" version="1.1"
             xmlns="http://www.w3.org/2000/svg">
          <polygon class="fill-default" points="2560 0 2560 100 0 100"></polygon>
        </svg>
      </div>
    </div>
    <!-- Page content -->
    <div class="container mt--8 pb-5">
      <div class="row justify-content-center">
        <div class="col-lg-5 col-md-7">
          <div class="card border-0 mb-0">
            <div class="card-header bg-transparent pb-5">
              <div class="text-muted text-center mt-2 mb-3"><small>Đăng nhập bằng tài khoản</small></div>
              <div class="btn-wrapper text-center">
                <a href="#" class="btn btn-neutral btn-icon">
                  <span class="btn-inner--icon"><img src="../assets/img/icons/common/google.svg"></span>
                  <span class="btn-inner--text">Google</span>
                </a>
              </div>
            </div>
            <div class="card-body px-lg-5 py-lg-5">
              <div class="text-center text-muted mb-4">
                <small>Hoặc đăng nhập bằng thông tin xác thực của chúng tôi</small>
              </div>
              <ValidationObserver tag="form" @submit.prevent="submitLogin" v-slot="{ invalid }">
                <ValidationProvider vid="username" name="username" rules="required"
                                    v-slot="{ errors }">
                  <div class="form-group mb-3">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                                                    <span class="input-group-text"><i
                                                        class="bi bi-person-fill"></i></span>
                      </div>
                      <input class="form-control"
                             placeholder="Email hoặc MSSV, MGV"
                             type="text"
                             :class="{'is-invalid': errors[0]}"
                             v-model="credentials.username"
                      >
                    </div>
                  </div>
                  <div class="input-group invalid-feedback mt--2">
                    {{ errors[0] }}
                  </div>
                </ValidationProvider>
                <br/>
                <ValidationProvider vid="password" name="password" rules="required"
                                    v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                        <span class="input-group-text"><i class="bi bi-key-fill"></i></span>
                      </div>
                      <input class="form-control"
                             placeholder="Mật khẩu của bạn"
                             type="password"
                             :class="{'is-invalid': errors[0]}"
                             v-model="credentials.password">
                    </div>
                  </div>
                  <div class="input-group invalid-feedback mt--3">
                    {{ errors[0] }}
                  </div>
                </ValidationProvider>
                <br/>
                <div class="custom-control custom-control-alternative custom-checkbox">
                  <input class="custom-control-input" id=" customCheckLogin" type="checkbox"
                         v-model="credentials.is_remember">
                  <label class="custom-control-label" for=" customCheckLogin">
                    <span class="text-muted">Giữ trạng thái đăng nhập cho lần sau</span>
                  </label>
                </div>
                <div class="input-group invalid-feedback" v-if="responseErrors">
                  {{ responseErrors.message }}
                </div>
                <div class="text-center">
                  <button type="submit" class="btn btn-primary my-4" :disabled="invalid">Đăng nhập
                  </button>
                </div>
                <ShortenURLLoading v-show="$store.state.isLoading"/>
              </ValidationObserver>
            </div>
          </div>
          <div class="row mt-3">
            <div class="col-6">
              <a href="#" class="text-light"><small>Quên mật khẩu?</small></a>
            </div>
            <div class="col-6 text-right">
              <router-link :to="{ name: 'register' }">
                <small>Tạo tài khoản mới</small>
              </router-link>
            </div>
          </div>
        </div>
      </div>
      <br/><br/><br/>
    </div>
  </div>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";
import ShortenURLLoading from "../components/elements/ShortenURLLoading.vue";

export default {
  name: "Login",
  components: {ShortenURLLoading},
  data() {
    return {
      credentials: {
        username: "",
        password: "",
        is_remember: false,
      },
    }
  },
  created() {
    this.resetErrors();
  },
  computed: {
    ...mapState('auth', ['responseErrors']),
  },
  methods : {
    ...mapMutations('auth', ['resetErrors']),
    ...mapActions('auth', ['login']),
    async submitLogin() {
      this.resetErrors();
      await this.login(this.credentials);
      if (!this.responseErrors) {
        await this.$router.push({name: 'home'});
      }
    },
  }
}
</script>

<style scoped>
.main-content {
  background-color: #172b4d;
}

.btn {
  width: 40% !important;
  height: 100% !important;
}

.back-home {
  color: white;
}

a:hover {
  text-decoration: none;
}
</style>
