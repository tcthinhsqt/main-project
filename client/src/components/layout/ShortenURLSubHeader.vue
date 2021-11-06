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
      <li class="dropdown"><a href="#"><span>Xem thêm</span><i class="bi bi-chevron-down"></i></a>
        <ul v-if="true">
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
        <ul v-else>
          <li>
            <router-link :to="{ name: 'information' }">Thống kê</router-link>
          </li>
          <li>
            <router-link :to="{ name: 'profile' }">Hồ sơ người dùng</router-link>
          </li>
          <li><a href="#" class="log-out">Đăng xuất</a></li>
        </ul>
      </li>
    </ul>
    <i class="bi bi-list mobile-nav-toggle"></i>
  </nav>
</template>

<script>
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
      }
    }
  },
}
</script>

<style scoped>
.log-out:hover {
  cursor: pointer;
}
</style>
