<template>
  <div class="main-content">
    <!-- Header -->
    <div class="header bg-gradient-primary py-7 py-lg-8 pt-lg-2">
      <div class="container">
        <div class="header-body text-center mb-7">
          <div class="row justify-content-center">
            <div class="col-xl-5 col-lg-6 col-md-8 px-5">
              <h1 class="text-white">Đăng ký tài khoản</h1>
              <p class="text-lead text-white">Tạo tài khoản đăng nhập hoàn toàn miễn phí.</p>
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
        <div class="col-lg-6 col-md-8">
          <div class="card border-0 mb-0">
            <div class="card-header bg-transparent pb-5">
              <div class="text-muted text-center mt-2 mb-4"><small>Đăng nhập bằng tài khoản</small></div>
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
              <ValidationObserver ref="register" @submit.prevent="submitRegisterForm" tag="form"
                                  v-slot="{ invalid }">
                <ValidationProvider vid="id" name="Id" rules="required|numeric|min:8"
                                    v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                        <span class="input-group-text"><i class="bi bi-align-middle"></i></span>
                      </div>
                      <input class="form-control"
                             placeholder="Mã số sinh viên hoặc mã giảng viên"
                             type="text"
                             :class="{'is-invalid': errors[0]}"
                             v-model="userDataForm.id"
                             autocomplete="off"
                      >
                    </div>
                    <div class="input-group invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </ValidationProvider>
                <ValidationProvider vid="name" name="Name" rules="required|min:6"
                                    v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                        <span class="input-group-text"><i class="bi bi-person-fill"></i></span>
                      </div>
                      <input class="form-control"
                             placeholder="Họ và tên"
                             type="text"
                             :class="{'is-invalid': errors[0]}"
                             v-model="userDataForm.name"
                             autocomplete="off"
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
                             placeholder="Địa chỉ email"
                             type="email"
                             :class="{'is-invalid': errors[0]}"
                             v-model="userDataForm.email"
                             autocomplete="off"
                      >
                    </div>
                    <div class="input-group invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </ValidationProvider>
                <ValidationProvider vid="password" name="Password" rules="required|min:6" v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                        <span class="input-group-text"><i class="bi bi-key-fill"></i></span>
                      </div>
                      <input class="form-control"
                             placeholder="Mật khẩu"
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
                             placeholder="Nhập lại mật khẩu"
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
                <ValidationProvider vid="birthday" name="Birthday" rules="required" v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                        <span class="input-group-text"><i class="bi bi-calendar3"></i></span>
                      </div>
                      <input class="form-control"
                             type="date"
                             :class="{'is-invalid': errors[0]}"
                             v-model="userDataForm.birthday"
                      >
                    </div>
                    <div class="input-group invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </ValidationProvider>
                <ValidationProvider vid="gender" name="Gender"
                                    rules="required"
                                    v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                        <span class="input-group-text"><i class="bi bi-gender-ambiguous"></i></span>
                      </div>
                      <select class="form-control" v-model="userDataForm.gender" :class="{'is-invalid': errors[0]}">
                        <option value=1>Nam</option>
                        <option value=2>Nữ</option>
                        <option value=0 selected>Khác</option>
                      </select>
                    </div>
                    <div class="input-group invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </ValidationProvider>
                <ValidationProvider vid="address" name="Address" v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                        <span class="input-group-text"><i class="bi bi-geo-alt-fill"></i></span>
                      </div>
                      <input class="form-control"
                             placeholder="Địa chỉ"
                             type="text"
                             :class="{'is-invalid': errors[0]}"
                             v-model="userDataForm.address"
                             autocomplete="off"
                      >
                    </div>
                    <div class="input-group invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </ValidationProvider>
                <ValidationProvider vid="faculty" name="Faculty" v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                        <span class="input-group-text"><i class="bi bi-building"></i></span>
                      </div>
                          <select id="input-faculty" class="form-control" v-model="userDataForm.faculty"
                                  :class="{'is-invalid': errors[0]}">
                            <option v-for="(value, index) in facultys" :key="index" :value="value">{{ value }}</option>
                          </select>
                    </div>
                    <div class="input-group invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </ValidationProvider>
                <ValidationProvider vid="degree" name="Degree" v-slot="{ errors }">
                  <div class="form-group">
                    <div class="input-group input-group-merge input-group-alternative">
                      <div class="input-group-prepend">
                        <span class="input-group-text"><i class="bi bi-award-fill"></i></span>
                      </div>
                      <select class="form-control" v-model="userDataForm.degree" :class="{'is-invalid': errors[0]}">
                        <option value="Đại học">Đại học</option>
                        <option value="Cao đẳng">Cao đẳng</option>
                        <option value="Khác">Khác</option>
                      </select>
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
                          <span class="text-muted">Tôi đồng ý với <a href="#!">Điều khoản dịch vụ</a></span>
                        </label>
                      </div>
                    </div>
                    <div class="input-group invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </ValidationProvider>
                <div class="input-group invalid-feedback" v-if="responseErrors">
                  {{ responseErrors.message ? responseErrors.message : '' }}
                </div>
                <div class="text-center">
                  <button type="submit" class="btn btn-primary mt-4" :disabled="invalid">
                    Tạo tài khoản
                  </button>
                </div>
              </ValidationObserver>
              <ShortenURLLoading v-show="$store.state.isLoading"/>
            </div>
          </div>
          <div class="row mt-2">
            <div class="col-12 text-center">
              <p class="text-white">
                <small>Bạn đã có tài khoản?</small>
                <router-link :to="{ name: 'login' }">
                  <small>Đăng nhập</small>
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
import {mapActions, mapMutations, mapState} from "vuex";
import ShortenURLLoading from "../components/elements/ShortenURLLoading.vue";

export default {
  name: "Register",
  components: {ShortenURLLoading},
  data() {
    return {
      userDataForm: {
        id: "",
        name: "",
        birthday: "",
        gender: "",
        address: "",
        email: "",
        password: "",
        password_confirmation: "",
        faculty: "",
        degree: ""
      },
      isAgree: false,
      facultys: [
        'Khoa Công nghệ Cơ khí',
        'Khoa Công nghệ Thông tin',
        'Khoa Công nghệ Điện',
        'Khoa Công nghệ Điện tử',
        'Khoa Công nghệ Động lực',
        'Khoa Công nghệ Nhiệt lạnh',
        'Khoa Công nghệ may - Thời trang',
        'Khoa Công nghệ Hóa học',
        'Khoa Kế toán - Kiểm toán',
        'Khoa Khoa học cơ bản',
        'Khoa Lý luận Chính trị',
        'Khoa Ngoại ngữ',
        'Khoa Quản trị Kinh doanh',
        'Khoa Tài chính - Ngân hàng',
        'Khoa Thương mại - Du lịch',
        'Khoa Kỹ thuật - Xây dựng',
        'Khoa Luật',
      ],
    }
  },
  computed: mapState('auth', ['responseErrors']),
  methods: {
    ...mapMutations('auth', ['resetErrors']),
    ...mapActions('auth', ['register']),
    async submitRegisterForm() {
      this.resetErrors();
      await this.register(this.userDataForm);
      if (this.responseErrors === null) {
        await this.$router.push({name: 'login'});
      } else {
        this.$refs.register.setErrors(this.responseErrors);
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
