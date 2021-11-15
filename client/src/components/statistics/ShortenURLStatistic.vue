<template>
    <div class="col-xl-6 col-md-6" id="statistic">
        <div class="card card-stats">
            <!-- Card body -->
            <div class="card-body">
                <div class="row">
                    <div class="col">
                        <h5 class="card-title text-uppercase text-muted mb-0">{{ statisticItem.name }}</h5>
                        <span class="h2 font-weight-bold mb-0">{{ statisticItem.statistic }}</span>
                    </div>
                    <div class="col-auto">
                        <div
                            :class="statisticItem.backgroundIcon">
                            <div v-html="statisticItem.icon"></div>
                        </div>
                    </div>
                </div>
<!--                <p class="mt-3 mb-0 text-sm">-->
<!--                    <span class="text-success mr-2"><span-->
<!--                        v-html="statisticItem.statusIcon"></span> {{ statisticItem.status }}</span>-->
<!--                    <span class="text-nowrap">So với tháng trước</span>-->
<!--                </p>-->
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name : "ShortenURLStatistic",
    props: {
        statisticItem: {
            type   : Object,
            default: null,
        }
    }
}
</script>
