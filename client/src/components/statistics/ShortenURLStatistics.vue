<template>
  <div class="header bg-info pb-6 pt-7">
    <div class="container">
      <div class="header-body">
        <ShortenURLBreadcrumb :breadcrumbs="breadcrumbs"/>
        <!-- Card stats -->
        <div class="row justify-content-center">
          <ShortenURLStatistic v-for="statisticItem in statisticList" :key="statisticItem.id"
                               :statisticItem="statisticItem"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ShortenURLBreadcrumb from "../elements/ShortenURLBreadcrumb";
import ShortenURLStatistic from "./ShortenURLStatistic";

export default {
  name: "ShortenURLStatistics",
  components: {ShortenURLStatistic, ShortenURLBreadcrumb},
  data() {
    return {
      statisticList: [
        {
          id: 1,
          name: "Total Use",
          statistic: "897",
          icon: "<i class=\"bi bi-calculator\"></i>",
          statusIcon: "<i class=\"bi bi-arrow-up\"></i>",
          status: "3,48%",
          backgroundIcon: "icon icon-shape bg-gradient-red text-white rounded-circle shadow"
        },
        {
          id: 2,
          name: "Rating",
          statistic: "4.5",
          icon: "<i class=\"bi bi-graph-up\"></i>",
          statusIcon: "<i class=\"bi bi-arrow-up\"></i>",
          status: "3,68%",
          backgroundIcon: "icon icon-shape bg-gradient-green text-white rounded-circle shadow"
        },
      ],
      breadcrumbs: [
        {routeName: 'home', pageName: 'Home'},
        {routeName: 'information', pageName: 'Information'},
      ],
    }
  }
}
</script>
