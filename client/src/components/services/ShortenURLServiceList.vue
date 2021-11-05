<template>
    <div class="row">
        <ShortenURLServiceItem v-for="service in services" v-bind:key="service.id" v-bind:service="service"/>
    </div>
</template>

<script>
import ShortenURLServiceItem from "./ShortenURLServiceItem";

export default {
    name      : "ShortenURLServiceList",
    components: {ShortenURLServiceItem},
    props     : {
        services: {
            type    : Array,
            Defaults: function () {
                return [];
            }
        }
    }
}
</script>
