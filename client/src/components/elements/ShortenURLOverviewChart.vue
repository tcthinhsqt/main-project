<template>
  <div class="row">
    <div class="col-xl-12">
      <div class="card bg-default">
        <div class="card-header bg-transparent">
          <div class="row align-items-center">
            <div class="col">
              <h6 class="text-light text-uppercase ls-1 mb-1"></h6>
              <h5 class="h3 text-white mb-0">Tổng quan</h5>
            </div>
            <div class="col">
              <ul class="nav nav-pills justify-content-end">
                <li class="nav-item mr-2 mr-md-0">
                  <a href="#" class="nav-link py-2 px-3 active" data-toggle="tab">
                    <span class="d-none d-md-block">Lượt đánh giá</span>
                    <span class="d-md-none"><i class="bi bi-calendar"></i></span>
                  </a>
                </li>
                <!--                <li class="nav-item">-->
                <!--                  <a href="#" class="nav-link py-2 px-3" data-toggle="tab">-->
                <!--                    <span class="d-none d-md-block">Ngày đánh giá</span>-->
                <!--                    <span class="d-md-none"><i class="bi bi-graph-up"></i></span>-->
                <!--                  </a>-->
                <!--                </li>-->
              </ul>
            </div>
          </div>
        </div>
        <div class="card-body">
          <ShortenURLBarChart v-if="loaded" :chartdata="chartdata" :options="options"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";
import ShortenURLBarChart from "./ShortenURLBarChart";

export default {
  name: "ShortenURLOverviewChart",
  components: {ShortenURLBarChart},
  data() {
    return {
      chartdata: null,
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          yAxes: [{
            ticks: {
              min: 0,
              stepSize: 1,
              reverse: false,
              beginAtZero: true
            }
          }],
        },
      },
      loaded: false,
    }
  },
  async created() {
    this.loaded = false;
    await this.setData();
    this.loaded = true;
  },
  computed: {
    ...mapState('validation', ['data', 'errors']),
  },
  methods: {
    ...mapMutations('validation', ['resetErrors']),
    ...mapActions('validation', ['getStatisticData']),
    async setData() {
      this.resetErrors();
      await this.getStatisticData();
      if (!this.errors) {
        this.chartdata = {
          labels: ["1 sao", "2 sao", "3 sao", "4 sao", "5 sao"],
          datasets: [{
            label: 'Số lượt đánh giá',
            data: this.data.rate,
            backgroundColor: [
              'rgba(153, 102, 255, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(153, 102, 255, 1)',
            ],
          }],
        };
      } else {
        alert("Failed!!!");
      }
    },
  },
}
</script>
