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
                <li class="nav-item">
                  <a href="#" class="nav-link py-2 px-3" data-toggle="tab">
                    <span class="d-none d-md-block">Ngày đánh giá</span>
                    <span class="d-md-none"><i class="bi bi-graph-up"></i></span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="card-body">
          <chartjs-bar :labels="labels" :datasets="datasets"></chartjs-bar>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ShortenURLOverviewChart",
  data() {
    return {
      labels: [1, 2, 3, 4, 5],
      datasets: [{
        label: 'Số lượt đánh giá',
        data: [65, 59, 80, 81, 56],
        backgroundColor: [
          'rgba(153, 102, 255, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(153, 102, 255, 1)',
        ],
      }],
    }
  }
}
</script>
