<template>
  <div>
    <div class="header pb-6 d-flex align-items-center pt-7">
      <!-- Mask -->
      <span class="mask bg-gradient-default opacity-8"></span>
      <!-- Header container -->
      <div class="container">
        <div class="header-body">
          <ShortenURLBreadcrumb :breadcrumbs="breadcrumbs"/>
        </div>
        <div class="d-flex align-items-center">
          <div class="row">
            <div class="col-lg-12 col-md-12">
              <h1 class="display-2 text-white">Xin chào<br>{{ name }}</h1>
              <p class="text-white mt-0 mb-5">
                Đây là trang hồ sơ của bạn. Nơi bạn có thể quản lý thông tin cá nhân và tài khoản đã đăng ký
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="container mt--6" v-if="user">
      <div class="row">
        <div class="col-xl-12 order-xl-1">
          <div class="card">
            <div class="card-header">
              <div class="row align-items-center">
                <div class="col-8">
                  <h3 class="mb-0">Chỉnh sửa hồ sơ cá nhân</h3>
                </div>
              </div>
            </div>
            <div class="card-body">
              <ValidationObserver ref="updateProfile" @submit.prevent="updateProfileUser" tag="form"
                                  v-slot="{ invalid }">
                <h6 class="heading-small text-muted mb-4">Thông tin cá nhân</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-lg-6">
                      <div class="form-group">
                        <label class="form-control-label" for="input-email">MSSV-MSGV:</label>
                        <input type="text" id="input-email" class="form-control" v-model="user.id" disabled>
                      </div>
                    </div>
                    <div class="col-lg-6">
                      <ValidationProvider vid="name" name="Name" rules="required|min:5" v-slot="{ errors }">
                        <div class="form-group">
                          <label class="form-control-label" for="input-username">Họ và tên:</label>
                          <input class="form-control"
                                 placeholder="Họ và tên"
                                 id="input-username"
                                 type="text"
                                 :class="{'is-invalid': errors[0]}"
                                 v-model="user.name"
                                 autocomplete="off"
                                 :disabled="user.name === 'Admin'"
                          >
                          <div class="input-group invalid-feedback">
                            {{ errors[0] }}
                          </div>
                        </div>
                      </ValidationProvider>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6">
                      <ValidationProvider vid="email" name="Email" rules="required|email" v-slot="{ errors }">
                        <div class="form-group">
                          <label class="form-control-label" for="input-first-name">Email:</label>
                          <input class="form-control"
                                 placeholder="Địa chỉ email"
                                 id="input-first-name"
                                 type="email"
                                 :class="{'is-invalid': errors[0]}"
                                 v-model="user.email"
                                 autocomplete="off"
                          >
                          <div class="input-group invalid-feedback">
                            {{ errors[0] }}
                          </div>
                        </div>
                      </ValidationProvider>
                    </div>
                    <div class="col-lg-6">
                      <ValidationProvider vid="birthday" name="Birthday" rules="required" v-slot="{ errors }">
                        <div class="form-group">
                          <label class="form-control-label" for="birthday">Ngày sinh (mm/dd/yyyy):</label>
                          <input class="form-control"
                                 id="birthday"
                                 type="date"
                                 :class="{'is-invalid': errors[0]}"
                                 v-model="birthday"
                          >
                          <div class="input-group invalid-feedback">
                            {{ errors[0] }}
                          </div>
                        </div>
                      </ValidationProvider>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6">
                      <div class="form-group">
                        <label class="form-control-label">Gender:</label>
                        <select class="form-control" v-model="user.gender">
                          <option value=1>Nam</option>
                          <option value=2>Nữ</option>
                          <option value=0>Khác</option>
                        </select>
                      </div>
                    </div>
                    <div class="col-lg-6">
                      <div class="form-group">
                        <label class="form-control-label" for="input-address">Địa chỉ:</label>
                        <input type="text" id="input-address" class="form-control"
                               placeholder="Nhập địa chỉ" v-model="user.address">
                      </div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6">
                      <ValidationProvider vid="faculty" name="Faculty" v-slot="{ errors }">
                        <div class="form-group">
                          <label class="form-control-label">Khoa:</label>
                          <select id="input-faculty" class="form-control" v-model="user.faculty"
                                  :class="{'is-invalid': errors[0]}">
                            <option v-for="(value, index) in facultys" :key="index" :value="value">{{ value }}</option>
                          </select>
                          <div class="input-group invalid-feedback">
                            {{ errors[0] }}
                          </div>
                        </div>
                      </ValidationProvider>
                    </div>
                    <div class="col-lg-6">
                      <ValidationProvider vid="degree" name="Degree" v-slot="{ errors }">
                        <div class="form-group">
                          <label class="form-control-label">Bậc học:</label>
                          <select id="input-degree" class="form-control" v-model="user.degree"
                                  :class="{'is-invalid': errors[0]}">
                            <option value="Đại học">Đại học</option>
                            <option value="Cao đẳng">Cao đẳng</option>
                            <option value="Khác">Khác</option>
                          </select>
                          <div class="input-group invalid-feedback">
                            {{ errors[0] }}
                          </div>
                        </div>
                      </ValidationProvider>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6">
                      <div class="form-group">
                        <label class="form-control-label" for="input-registration-date">Ngày đăng ký
                          (mm/dd/yyyy):</label>
                        <input type="date" class="form-control" id="input-registration-date"
                               :value="registrationDate" disabled>
                      </div>
                    </div>
                  </div>
                  <div class="row mt-3">
                    <div class="col-lg-6">
                      <div class="form-group text-center">
                        <button type="submit" class="btn btn-warning" :disabled="invalid">
                          Cập nhật hồ sơ
                        </button>
                        <ShortenURLLoading v-show="$store.state.isLoading"/>
                      </div>
                    </div>
                  </div>
                </div>
              </ValidationObserver>
              <hr class="my-4"/>
              <!-- Address -->
              <ValidationObserver ref="changePassword" @submit.prevent="changePasswordUser" tag="form"
                                  v-slot="{ invalid }">
                <h6 class="heading-small text-muted mb-4">Đổi mật khẩu</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-md-6">
                      <ValidationProvider vid="password" name="Password" rules="required" v-slot="{ errors }">
                        <div class="form-group">
                          <label class="form-control-label" for="input-current-password">Mật khẩu hiện tại:</label>
                          <input class="form-control"
                                 id="input-current-password"
                                 type="password"
                                 :class="{'is-invalid': errors[0]}"
                                 v-model="changePasswordForm.password"
                          >
                          <div class="input-group invalid-feedback">
                            {{ errors[0] }}
                          </div>
                        </div>
                      </ValidationProvider>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6">
                      <ValidationProvider vid="new_password" name="New Password" rules="required|min:6"
                                          v-slot="{ errors }">
                        <div class="form-group">
                          <label class="form-control-label" for="input-new-password">Mật khẩu mới:</label>
                          <input class="form-control"
                                 id="input-new-password"
                                 type="password"
                                 :class="{'is-invalid': errors[0]}"
                                 v-model="changePasswordForm.new_password"
                          >
                          <div class="input-group invalid-feedback">
                            {{ errors[0] }}
                          </div>
                        </div>
                      </ValidationProvider>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6">
                      <ValidationProvider vid="confirm_password" name="Password Confirmation"
                                          rules="required|confirmed:new_password"
                                          v-slot="{ errors }">
                        <div class="form-group">
                          <label class="form-control-label" for="input-confirm-password">Xác nhận mật khẩu:</label>
                          <input class="form-control"
                                 placeholder="Nhập lại mật khẩu"
                                 id="input-confirm-password"
                                 type="password"
                                 :class="{'is-invalid': errors[0]}"
                                 v-model="changePasswordForm.password_confirmation"
                          >
                          <div class="input-group invalid-feedback">
                            {{ errors[0] }}
                          </div>
                        </div>
                      </ValidationProvider>
                    </div>
                  </div>
                  <div class="row mt-3">
                    <div class="col-lg-6">
                      <div class="form-group">
                        <button type="submit" class="btn btn-warning" :disabled="invalid">Đổi mật khẩu</button>
                      </div>
                    </div>
                  </div>
                </div>
              </ValidationObserver>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";
import ShortenURLBreadcrumb from "./ShortenURLBreadcrumb";
import ShortenURLLoading from "./ShortenURLLoading";

export default {
  name: "ShortenURLUserProfile",
  components: {ShortenURLLoading, ShortenURLBreadcrumb},
  data() {
    return {
      breadcrumbs: [
        {routeName: 'home', pageName: 'Trang chủ'},
        {routeName: 'profile', pageName: 'Hồ sơ người dùng'},
      ],
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
      changePasswordForm: {
        password: '',
        new_password: '',
        password_confirmation: '',
      },
    }
  },
  created() {
    this.setDisplayName();
  },
  computed: {
    ...mapState('auth', ['responseErrors', 'user', 'name']),
    birthday: {
      get() {
        let today = new Date(this.user.birthday);
        let dd = String(today.getDate()).padStart(2, '0');
        let mm = String(today.getMonth() + 1).padStart(2, '0');
        let yyyy = today.getFullYear();

        today = yyyy + '-' + mm + '-' + dd;
        return today;
      },
      set(value) {
        this.setBirthday(value);
      }
    },
    registrationDate() {
      let today = new Date(this.user.registration_date);
      let dd = String(today.getDate()).padStart(2, '0');
      let mm = String(today.getMonth() + 1).padStart(2, '0');
      let yyyy = today.getFullYear();

      today = yyyy + '-' + mm + '-' + dd;
      return today;
      // return today.toISOString().split('T')[0];
    }
  },
  methods: {
    ...mapMutations('auth', ['setDisplayName', 'setBirthday', 'resetErrors']),
    ...mapActions('auth', ['updateUser', 'changePassword']),
    async updateProfileUser() {
      this.resetErrors();
      await this.updateUser(this.user);
      if (!this.responseErrors) {
        alert('Cập nhật hồ sơ thành công!!!')
      } else {
        alert(this.responseErrors.message)
      }
    },
    async changePasswordUser() {
      this.resetErrors();
      await this.changePassword({form: this.changePasswordForm, id: this.user.id});
      if (!this.responseErrors) {
        alert('Cập nhật mật khẩu thành công!!!')
      } else {
        alert(this.responseErrors.message)
      }
    },
  },
}
</script>

<style scoped>
.btn {
  width: 30% !important;
}

.header {
  min-height: 500px;
  background-color: #2a2958;
  background-size: cover;
  background-position: center top;
}
</style>
