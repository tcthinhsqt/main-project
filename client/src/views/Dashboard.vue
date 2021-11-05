<template>
    <div>
        <div class="main-content pt-3" id="panel">
            <ShortenURLStatistics/>
            <!-- Page content -->
            <div class="container mt--6">
                <ShortenURLOverviewChart/>
            </div>
        </div>
        <ShortenURLFormUpdate/>
        <ShortenURLDetail/>
        <ShortenURLBackToTop/>
    </div>
</template>

<script>
import ShortenURLBackToTop     from "../components/elements/ShortenURLBackToTop";
import ShortenURLFormUpdate    from "../components/management/ShortenURLFormUpdate";
import ShortenURLOverviewChart from "../components/elements/ShortenURLOverviewChart";
import ShortenURLStatistics    from "../components/statistics/ShortenURLStatistics";
import ShortenURLDetail        from "../components/management/ShortenURLDetail";

export default {
    name      : "Dashboard",
    components: {
        ShortenURLDetail,
        ShortenURLStatistics,
        ShortenURLOverviewChart,
        ShortenURLFormUpdate,
        ShortenURLBackToTop,
    },
}
</script>
