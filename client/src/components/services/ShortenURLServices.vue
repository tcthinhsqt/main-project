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
                    title       : 'Dễ sử dụng',
                    description : 'ShortURL dễ dàng và nhanh chóng, hãy nhập liên kết dài để lấy liên kết rút gọn của bạn'
                },
                {
                    id          : 3,
                    dataOutDelay: '200',
                    icon        : "<i class='bx bx-shield'></i>",
                    title       : 'Bảo mật',
                    description : 'Nhanh chóng và an toàn, dịch vụ sử dụng giao thức HTTPS và mã hóa dữ liệu'
                },
                {
                    id          : 5,
                    dataOutDelay: '400',
                    icon        : "<i class='bx bx-donate-heart'></i>",
                    title       : 'Tin cậy',
                    description : 'Tất cả thông tin bạn nhận được từ hệ thống đều được kiểm soát chặt chẽ'
                }
            ]
        }
    }
}
</script>
