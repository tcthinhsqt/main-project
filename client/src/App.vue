<template>
  <div>
    <ShortenURLHeader v-if="!isLoginOrRegister"/>
    <router-view/>
    <ShortenURLFooter v-if="!isLoginOrRegister"/>
  </div>
</template>

<script>
import {generatePageTitle} from './services/generator';
import ShortenURLFooter from "./components/layout/ShortenURLFooter.vue";
import ShortenURLHeader from "./components/layout/ShortenURLHeader.vue";

export default {
  name: "App",
  components: {ShortenURLHeader, ShortenURLFooter,},
  mounted() {
    document.title = generatePageTitle(this.$route);
  },
  computed: {
    isLoginOrRegister() {
      return this.$route.name === 'login' || this.$route.name === 'register' || this.$route.name === 'error' || this.$route.name === 'page_not_found';
    }
  },
  watch: {
    $route(to) {
      document.title = generatePageTitle(to);
    },
  },
};
</script>
<style>
@import '~bootstrap/dist/css/bootstrap.css';
@import '~bootstrap/dist/css/bootstrap.min.css';
@import '~aos/dist/aos.css';
@import './assets/css/style.css';
@import './assets/vendor/bootstrap/css/bootstrap.min.css';
@import './assets/vendor/bootstrap-icons/bootstrap-icons.css';
@import './assets/vendor/boxicons/css/boxicons.min.css';
@import './assets/vendor/glightbox/css/glightbox.min.css';
@import './assets/vendor/swiper/swiper-bundle.min.css';
@import './assets/css/argon.css';
@import './asset2/css/app.css';
</style>
