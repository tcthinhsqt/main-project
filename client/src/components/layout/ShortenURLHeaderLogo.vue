<template>
    <div class="logo">
        <h1 class="text-light">
            <router-link :to="{ name: 'home'}"><span>HỆ THỐNG TRẢ LỜI CÂU HỎI - IUH</span></router-link>
        </h1>
        <!-- Uncomment below if you prefer to use an image logo -->
        <!--<a href="#"><img src="logo.png" alt="" class="img-fluid"></a>-->
    </div>
</template>

<script>
export default {
    name: "ShortenURLHeaderLogo"
}
</script>
