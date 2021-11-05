<template>
  <div class="main-content">
    <!-- Header -->
    <div class="header bg-gradient-primary py-7 py-lg-8 pt-lg-2">
      <div class="container">
        <div class="header-body text-center mb-7">
          <div class="row justify-content-center">
            <div class="col-xl-5 col-lg-6 col-md-8 px-5">
              <h1 class="text-white">Create an account</h1>
              <p class="text-lead text-white">Login or create new account in your project for free.</p>
            </div>
          </div>
          <div class="mb--6 pt-5">
            <router-link :to="{ name: 'home'}"><h1 class="back-home">◃BACK HOME</h1></router-link>
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
        <div class="col-lg-6 col-md-8">
          <div class="card border-0 mb-0">
            <div class="card-header bg-transparent pb-5">
              <div class="text-muted text-center mt-2 mb-4"><small>Sign in with</small></div>
              <div class="btn-wrapper text-center">
                <a href="#" class="btn btn-neutral btn-icon">
                  <span class="btn-inner--icon"><img src="../assets/img/icons/common/google.svg"></span>
                  <span class="btn-inner--text">Google</span>
                </a>
              </div>
            </div>
            <div class="card-body px-lg-5 py-lg-5">
              <div class="text-center text-muted mb-4">
                <small>Or sign up with credentials</small>
              </div>
              <ValidationObserver ref="register" @submit.prevent="submitRegisterForm" tag="form"
                                  v-slot="{ invalid }">
                <ValidationProvider vid="username" name="Username" rules="required|alpha|min:5"
                                    v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                        <span class="input-group-text"><i class="bi bi-person-fill"></i></span>
                      </div>
                      <input class="form-control"
                             placeholder="Username"
                             type="text"
                             :class="{'is-invalid': errors[0]}"
                             v-model="userDataForm.username"
                      >
                    </div>
                    <div class="input-group invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </ValidationProvider>
                <ValidationProvider vid="email" name="Email" rules="required|email" v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                                                <span class="input-group-text"><i
                                                    class="bi bi-envelope-fill"></i></span>
                      </div>
                      <input class="form-control"
                             placeholder="Email"
                             type="email"
                             :class="{'is-invalid': errors[0]}"
                             v-model="userDataForm.email"
                      >
                    </div>
                    <div class="input-group invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </ValidationProvider>
                <ValidationProvider vid="password" name="Password" rules="required" v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                        <span class="input-group-text"><i class="bi bi-key-fill"></i></span>
                      </div>
                      <input class="form-control"
                             placeholder="Password"
                             type="password"
                             :class="{'is-invalid': errors[0]}"
                             v-model="userDataForm.password"
                      >
                    </div>
                    <div class="input-group invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </ValidationProvider>
                <ValidationProvider vid="password_confirmation" name="Verify Password"
                                    rules="required|confirmed:password"
                                    v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                        <span class="input-group-text"><i class="bi bi-key-fill"></i></span>
                      </div>
                      <input class="form-control"
                             placeholder="Verify password"
                             type="password"
                             :class="{'is-invalid': errors[0]}"
                             v-model="userDataForm.password_confirmation"
                      >
                    </div>
                    <div class="input-group invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </ValidationProvider>
                <ValidationProvider ref="agree" name="Agree Policy"
                                    :rules="{ required: { allowFalse: false } }"
                                    v-slot="{ errors }">
                  <div class="row my-4">
                    <div class="col-12">
                      <div class="custom-control custom-control-alternative custom-checkbox">
                        <input
                            class="custom-control-input"
                            id="customCheckRegister"
                            type="checkbox"
                            :class="{'is-invalid': errors[0]}"
                            v-model="isAgree"
                        >
                        <label class="custom-control-label" for="customCheckRegister">
                          <span class="text-muted">I agree with the <a href="#!">Privacy Policy</a></span>
                        </label>
                      </div>
                    </div>
                    <div class="input-group invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </ValidationProvider>
                <div class="text-center">
                  <button type="submit" class="btn btn-primary mt-4" :disabled="invalid">Create
                    account
                  </button>
                </div>
              </ValidationObserver>
              <ShortenURLLoading v-show="false"/>
            </div>
          </div>
          <div class="row mt-2">
            <div class="col-12 text-center">
              <p class="text-white">
                <small>Already have an account?</small>
                <router-link :to="{ name: 'login' }">
                  <small> Login</small>
                </router-link>
              </p>
            </div>
          </div>
        </div>
      </div>
      <br/><br/><br/>
    </div>
  </div>
</template>

<script>
import ShortenURLLoading from "../components/elements/ShortenURLLoading.vue";

export default {
  name: "Register",
  components: {ShortenURLLoading},
  data() {
    return {
      userDataForm: {
        username: "",
        email: "",
        password: "",
        password_confirmation: "",
      },
      isAgree: false,
    }
  },
  methods: {
    async submitRegisterForm() {
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
