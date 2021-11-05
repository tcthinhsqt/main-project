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
      <li class="dropdown"><a href="#"><span>Account</span><i class="bi bi-chevron-down"></i></a>
        <ul v-if="true">
          <li>
            <router-link :to="{ name: 'information' }">Information</router-link>
          </li>
          <li>
            <router-link :to="{ name: 'login' }">Login</router-link>
          </li>
          <li>
            <router-link :to="{ name: 'register' }">Register</router-link>
          </li>
        </ul>
        <ul v-else>
          <li>
            <router-link :to="{ name: 'information' }">Information</router-link>
          </li>
          <li>
            <router-link :to="{ name: 'profile' }">Profile</router-link>
          </li>
          <li><a href="#" class="log-out">Log out</a></li>
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
          {href: '#hero', content: 'Home'},
          {href: '#asking', content: 'Asking'},
          {href: '#services', content: 'Services'},
        ],
        information: [
          {href: '#statistic', content: 'Overview'},
        ],
        profile: [
          {href: '#editProfile', content: 'Edit Profile'},
          {href: '#changePassword', content: 'Change Password'},
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
