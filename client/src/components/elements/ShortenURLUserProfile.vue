<template>
    <div>
        <div class="header pb-6 d-flex align-items-center pt-7">
            <!-- Mask -->
            <span class="mask bg-gradient-default opacity-8"></span>
            <!-- Header container -->
            <div class="container">
                <div class="header-body">
                    <ShortenURLBreadcrumb :breadcrumbs="breadcrumbs"/>
                </div>
                <div class="d-flex align-items-center">
                    <div class="row">
                        <div class="col-lg-7 col-md-10">
                            <h1 class="display-2 text-white">Xin chào {{ name }}</h1>
                            <p class="text-white mt-0 mb-5">
                                Đây là trang hồ sơ của bạn. Nơi bạn có thể quản lý thông tin cá nhân và tài khoản đã đăng ký
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container mt--6">
            <div class="row">
                <div class="col-xl-12 order-xl-1">
                    <div class="card">
                        <div class="card-header">
                            <div class="row align-items-center">
                                <div class="col-8">
                                    <h3 class="mb-0">Chỉnh sửa hồ sơ cá nhân</h3>
                                </div>
                            </div>
                        </div>
                        <div class="card-body">
                            <form>
                                <h6 class="heading-small text-muted mb-4">Thông tin cá nhân</h6>
                                <div class="pl-lg-4">
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label" for="input-username">Họ và tên:</label>
                                                <input type="text" id="input-username" class="form-control"
                                                       placeholder="Nhập họ tên của bạn" value="lucky.jesse">
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label" for="input-email">Địa chỉ email:</label>
                                                <input type="email" id="input-email" class="form-control"
                                                       placeholder="jesse@example.com">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label" for="input-first-name">Tên hiển thị:</label>
                                                <input type="text" id="input-first-name" class="form-control"
                                                       placeholder="Tên hiển thị của bạn" value="Thinh">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row mt-3">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <button type="button" class="btn btn-outline-warning">Cập nhật hồ sơ
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </form>
                            <hr class="my-4"/>
                            <!-- Address -->
                            <form>
                                <h6 class="heading-small text-muted mb-4">Đổi mật khẩu</h6>
                                <div class="pl-lg-4">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <div class="form-group">
                                                <label class="form-control-label" for="input-current-password">Mật khẩu hiện tại:</label>
                                                <input id="input-current-password" class="form-control" value=""
                                                       type="password">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label" for="input-new-password">Mật khẩu mới:</label>
                                                <input type="password" id="input-new-password" class="form-control"
                                                       value="">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label" for="input-confirm-password">Xác nhận mật khẩu:</label>
                                                <input type="password" id="input-confirm-password" class="form-control"
                                                       value="">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row mt-3">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <button class="btn btn-outline-warning">Đổi mật khẩu</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import ShortenURLBreadcrumb from "./ShortenURLBreadcrumb";

export default {
    name      : "ShortenURLUserProfile",
    components: {ShortenURLBreadcrumb},
    data() {
        return {
            name       : 'Thinh',
            breadcrumbs: [
                {routeName: 'home', pageName: 'Trang chủ'},
                {routeName: 'profile', pageName: 'Hồ sơ người dùng'},
            ],
        }
    }
}
</script>

<style scoped>
.btn {
    width: 30% !important;
}

.header {
    min-height: 500px;
    background-color: #2a2958;
    background-size: cover;
    background-position: center top;
}
</style>
