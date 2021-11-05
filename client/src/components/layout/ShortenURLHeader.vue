<template>
    <header id="header" class="fixed-top header-transparent header-scrolled">
        <div class="container d-flex align-items-center justify-content-between">
            <ShortenURLHeaderLogo/>
            <ShortenURLSubHeader/>
        </div>
    </header>
</template>

<script>
import ShortenURLHeaderLogo from "./ShortenURLHeaderLogo";
import ShortenURLSubHeader  from "./ShortenURLSubHeader";

export default {
    name      : "ShortenURLHeader",
    components: {ShortenURLSubHeader, ShortenURLHeaderLogo},
}
</script>
