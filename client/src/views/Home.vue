<template>
  <div>
    <div>
      <ShortenURLContent/>
      <main id="main">
        <ShortenURLFormUrlHandling/>
        <ShortenURLServices/>
      </main>
    </div>
    <ShortenURLFormCreate/>
    <ShortenURLBackToTop/>
  </div>
</template>

<script>
import ShortenURLFormCreate    from "../components/management/ShortenURLFormCreate";
import ShortenURLContent from "../components/elements/ShortenURLContent";
import ShortenURLFormUrlHandling from "../components/elements/ShortenURLFormUrlHandling";
import ShortenURLServices from "../components/services/ShortenURLServices";
import ShortenURLBackToTop from "../components/elements/ShortenURLBackToTop";

export default {
  name: "Home",
  components: {
    ShortenURLBackToTop,
    ShortenURLServices,
    ShortenURLFormUrlHandling,
    ShortenURLContent,
    ShortenURLFormCreate
  },
};
</script>
