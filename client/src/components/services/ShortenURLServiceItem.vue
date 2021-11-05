<template>
    <div class="col-md-6 col-lg-4 d-flex align-items-stretch mb-5 mb-lg-3">
        <div class="icon-box" data-aos="fade-up" :data-aos-delay="service.dataOutDelay">
            <div class="icon">
                <div v-html="service.icon"></div>
            </div>
            <h4 class="title"><a href="">{{ service.title }}</a></h4>
            <p class="description">{{ service.description }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name : "ShortenURLServiceItem",
    props: {
        service: {
            type   : Object,
            default: function () {
                return {id: null, dataOutDelay: '', icon: "", title: '', description: ''};
            }
        }
    }
}
</script>
