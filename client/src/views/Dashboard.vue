<template>
    <div>
        <div class="main-content pt-3" id="panel">
            <ShortenURLStatistics/>
            <!-- Page content -->
            <div class="container mt--6">
                <ShortenURLOverviewChart/>
            </div>
        </div>
        <ShortenURLBackToTop/>
    </div>
</template>

<script>
import ShortenURLBackToTop     from "../components/elements/ShortenURLBackToTop";
import ShortenURLOverviewChart from "../components/elements/ShortenURLOverviewChart";
import ShortenURLStatistics    from "../components/statistics/ShortenURLStatistics";

export default {
    name      : "Dashboard",
    components: {
        ShortenURLStatistics,
        ShortenURLOverviewChart,
        ShortenURLBackToTop,
    },
}
</script>
