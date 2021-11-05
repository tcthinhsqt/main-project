<template>
    <section id="services" class="services">
        <div class="container">
            <ShortenURLServiceTitle/>
            <ShortenURLServiceList v-bind:services="services"/>
        </div>
    </section>
</template>

<script>

import ShortenURLServiceList  from "./ShortenURLServiceList";
import ShortenURLServiceTitle from "./ShortenURLServiceTitle";

export default {
    name      : "ShortenURLServices",
    components: {ShortenURLServiceTitle, ShortenURLServiceList},
    data() {
        return {
            services: [
                {
                    id          : 1,
                    dataOutDelay: '0',
                    icon        : "<i class='bi bi-book'></i>",
                    title       : 'Easy',
                    description : 'ShortURL is easy and fast, enter the long link to get your shortened link'
                },
                {
                    id          : 3,
                    dataOutDelay: '200',
                    icon        : "<i class='bx bx-shield'></i>",
                    title       : 'Secure',
                    description : 'It is fast and secure, our service have HTTPS protocol and data encryption'
                },
                {
                    id          : 5,
                    dataOutDelay: '400',
                    icon        : "<i class='bx bx-donate-heart'></i>",
                    title       : 'Reliable',
                    description : 'All links that try to disseminate spam, viruses and malware are deleted'
                }
            ]
        }
    }
}
</script>
