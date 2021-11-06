<template>
    <footer id="footer" class="mt-5">
        <div class="footer-top">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4 col-md-6">
                        <div class="footer-info">
                            <h3>HỆ THỐNG TRẢ LỜI CÂU HỎI TỰ ĐỘNG</h3>
                            <b class="pb-3"><em>Nhanh chóng - Cập nhật - Đáp ứng đa dạng</em></b>
                            <p>
                                12 Nguyễn Văn Bảo, Phường 4, Quận Gò Vấp 
                                <br>
                                Thành phố Hồ Chí Minh, Việt Nam
                                <br><br>
                                <strong>Số điện thoại:</strong> +84 12 445 678<br>
                                <strong>Địa chỉ email:</strong> trancongthinh1999@gmail.com<br>
                            </p>
                            <div class="social-links mt-3">
                                <a href="#" class="twitter"><i class="bx bxl-twitter"></i></a>
                                <a href="#" class="facebook"><i class="bx bxl-facebook"></i></a>
                                <a href="#" class="instagram"><i class="bx bxl-instagram"></i></a>
                                <a href="#" class="google-plus"><i class="bx bxl-skype"></i></a>
                                <a href="#" class="linkedin"><i class="bx bxl-linkedin"></i></a>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-2 col-md-6 footer-links">
                        <h4>Các liên kết</h4>
                        <ul>
                            <li><i class="bx bx-chevron-right"></i> <a href="#">Trang chủ</a></li>
                            <li><i class="bx bx-chevron-right"></i> <a href="#">Liên hệ</a></li>
                            <li><i class="bx bx-chevron-right"></i> <a href="#">Các dịch vụ</a></li>
                            <li><i class="bx bx-chevron-right"></i> <a href="#">Điều khoản dịch vụ</a></li>
                            <li><i class="bx bx-chevron-right"></i> <a href="#">Chính sách bảo mật</a></li>
                        </ul>
                    </div>

                    <div class="col-lg-2 col-md-6 footer-links">
                        <h4>Các dịch vụ</h4>
                        <ul>
                            <li><i class="bx bx-chevron-right"></i> <a href="#">Web Design</a></li>
                            <li><i class="bx bx-chevron-right"></i> <a href="#">Web Development</a></li>
                            <li><i class="bx bx-chevron-right"></i> <a href="#">Product Management</a></li>
                            <li><i class="bx bx-chevron-right"></i> <a href="#">Marketing</a></li>
                            <li><i class="bx bx-chevron-right"></i> <a href="#">Graphic Design</a></li>
                        </ul>
                    </div>

                    <div class="col-lg-4 col-md-6 footer-newsletter">
                        <h4>Bảng tin của chúng tôi</h4>
                        <form action="" method="post" @submit.prevent="">
                            <input type="email" name="email"><input type="submit" value="Đăng ký">
                        </form>

                    </div>

                </div>
            </div>
        </div>

        <div class="container">
            <div class="copyright">
                &copy; Bản quyền thuộc về <strong><span>HỆ THỐNG TRẢ LỜI CÂU HỎI - IUH</span></strong>. Bản quyền đã được đăng ký
            </div>
        </div>
    </footer>
</template>

<script>
export default {
    name: "ShortenURLFooter"
}
</script>
