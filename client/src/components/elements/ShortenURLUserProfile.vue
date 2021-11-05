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
                            <h1 class="display-2 text-white">Hello {{ name }}</h1>
                            <p class="text-white mt-0 mb-5">
                                This is your profile page. You can see the progress you've
                                made with your work and manage your projects or assigned tasks
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
                                    <h3 class="mb-0">Edit profile </h3>
                                </div>
                            </div>
                        </div>
                        <div class="card-body">
                            <form>
                                <h6 class="heading-small text-muted mb-4">User information</h6>
                                <div class="pl-lg-4">
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label" for="input-username">Username</label>
                                                <input type="text" id="input-username" class="form-control"
                                                       placeholder="Username" value="lucky.jesse">
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label" for="input-email">Email
                                                    address</label>
                                                <input type="email" id="input-email" class="form-control"
                                                       placeholder="jesse@example.com">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label" for="input-first-name">Display
                                                    name</label>
                                                <input type="text" id="input-first-name" class="form-control"
                                                       placeholder="First name" value="Thinh">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row mt-3">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <button type="button" class="btn btn-outline-warning">Update profile
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </form>
                            <hr class="my-4"/>
                            <!-- Address -->
                            <form>
                                <h6 class="heading-small text-muted mb-4">Change password</h6>
                                <div class="pl-lg-4">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <div class="form-group">
                                                <label class="form-control-label" for="input-current-password">Current
                                                    password</label>
                                                <input id="input-current-password" class="form-control" value=""
                                                       type="password">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label" for="input-new-password">New
                                                    password</label>
                                                <input type="password" id="input-new-password" class="form-control"
                                                       value="">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label" for="input-confirm-password">Confirm
                                                    new password</label>
                                                <input type="password" id="input-confirm-password" class="form-control"
                                                       value="">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row mt-3">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <button class="btn btn-outline-warning">Change password</button>
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
                {routeName: 'home', pageName: 'Home'},
                {routeName: 'profile', pageName: 'Profile'},
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
