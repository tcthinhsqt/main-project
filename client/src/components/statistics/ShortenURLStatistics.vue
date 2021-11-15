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
import {mapActions, mapState} from "vuex";

export default {
  name: "ShortenURLStatistics",
  components: {ShortenURLStatistic, ShortenURLBreadcrumb},
  data() {
    return {
      statisticList: [
        {
          id: 1,
          name: "Tổng số lượt sử dụng",
          statistic: null,
          icon: "<i class=\"bi bi-calculator\"></i>",
          statusIcon: "<i class=\"bi bi-arrow-up\"></i>",
          backgroundIcon: "icon icon-shape bg-gradient-red text-white rounded-circle shadow"
        },
        {
          id: 2,
          name: "Xếp hạng",
          statistic: null,
          icon: "<i class=\"bi bi-graph-up\"></i>",
          statusIcon: "<i class=\"bi bi-arrow-up\"></i>",
          backgroundIcon: "icon icon-shape bg-gradient-green text-white rounded-circle shadow"
        },
      ],
      breadcrumbs: [
        {routeName: 'home', pageName: 'Trang chủ'},
        {routeName: 'information', pageName: 'Thống kê về ứng dụng'},
      ],
    }
  },
  created() {
    this.getData();
  },
  computed: {
    ...mapState('validation', ['errors', 'data']),
  },
  methods: {
    ...mapActions('validation', ['getStatisticData']),
    async getData() {
      await this.getStatisticData();
      if (!this.errors) {
        this.statisticList[0].statistic = this.data.totalUse;
        this.statisticList[1].statistic = this.data.averageRate;
      }
    }
  }
}
</script>
