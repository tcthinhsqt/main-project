<template>
  <nav id="navbar" class="navbar">
    <ul>
      <li>
        <ul>
          <li v-for="(item, key) in navbar[$route.name]" :key="key">
            <a :href="item.href" class="nav-link scrollto">{{ item.content }}</a>
          </li>
        </ul>
      </li>
      <li class="dropdown" v-if="user">
        <a href="#">
          <span>{{ name }}</span>
          <i class="bi bi-chevron-down"></i>
        </a>
        <ul>
          <li>
            <router-link :to="{ name: 'information' }">Thống kê về ứng dụng</router-link>
          </li>
          <li v-if="user.id === 1">
            <router-link :to="{ name: 'admin' }">Manager</router-link>
          </li>
          <li>
            <router-link :to="{ name: 'profile' }">Hồ sơ người dùng</router-link>
          </li>
          <li><a @click="handleLogout" class="log-out">Đăng xuất</a></li>
        </ul>
      </li>
      <li class="dropdown" v-else>
        <a href="#">
          <span>Account</span>
          <i class="bi bi-chevron-down"></i>
        </a>
        <ul>
          <li>
            <router-link :to="{ name: 'information' }">Thống kê về ứng dụng</router-link>
          </li>
          <li>
            <router-link :to="{ name: 'login' }">Đăng nhập</router-link>
          </li>
          <li>
            <router-link :to="{ name: 'register' }">Đăng ký</router-link>
          </li>
        </ul>
      </li>
    </ul>
    <i class="bi bi-list mobile-nav-toggle"></i>
  </nav>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";

export default {
  name: "ShortenURLSubHeader",
  data() {
    return {
      navbar: {
        home: [
          {href: '#hero', content: 'Trang chủ'},
          {href: '#asking', content: 'Đặt câu hỏi'},
          {href: '#services', content: 'Các dịch vụ'},
        ],
        information: [
          {href: '#statistic', content: 'Tổng quan'},
        ],
        profile: [
          {href: '#editProfile', content: 'Chỉnh sửa hồ sơ'},
          {href: '#changePassword', content: 'Đổi mật khẩu'},
        ]
      },
    }
  },
  created() {
    this.setDisplayName();
  },
  computed: {
    ...mapState('auth', ['responseErrors', 'user', 'name']),
  },
  methods: {
    ...mapMutations('auth', ['resetErrors', 'setDisplayName']),
    ...mapActions('auth', ['logout']),
    async handleLogout() {
      this.resetErrors();
      await this.logout();
      if (this.responseErrors === null) {
        await this.$router.push({name: 'login'});
      } else {
        alert(this.responseErrors.message);
      }
    }
  }
}
</script>

<style scoped>
.log-out:hover {
  cursor: pointer;
}
</style>
