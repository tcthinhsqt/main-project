<template>
    <div class="modal left fade" id="modalUpdate" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 id="myModalLabel">Chỉnh sửa</h1>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                        aria-hidden="true"><i class="bi bi-x-lg"></i></span></button>
                </div>
                <div class="text-center pt-4 pb-4">
                    <a href="#">
                        short.url
                        <span>/1sdas8df1</span>
                    </a>
                    <div class="pt-2">
                        <button id="copyBtn" type="button" class="btn btn-primary btn-sm"><i
                            class="bi bi-clipboard"></i> Sao chép
                        </button>
                        <button id="redirectBtn" type="button" class="btn btn-danger btn-sm"><i
                            class="bi bi-box-arrow-in-right"></i> Đi đến
                        </button>
                    </div>
                </div>
                <div class="modal-body">
                    <form>
                        <div class="form-group">
                            <label for="title">Tiêu đề</label>
                            <input type="text" class="form-control" id="title" aria-describedby="emailHelp"
                                   placeholder="Thêm một tiêu đề">
                        </div>
                        <div class="form-group">
                            <label for="select-domain">Chọn tên miền</label>
                            <select class="form-control form-select" aria-label="Default select example"
                                    id="select-domain">
                                <option selected>short.url</option>
                            </select>
                        </div>
                        <div class="form-group form-check">
                            <input type="checkbox" class="form-check-input" id="choose-back-half"
                                   v-model="isCustomizeBackHalf">
                            <label class="form-check-label" for="choose-back-half">Tùy chỉnh phần còn lại</label>
                        </div>
                        <div class="form-group" v-show="isCustomizeBackHalf">
                            <input type="text" class="form-control" id="backHalfInput" aria-describedby="longURLHelp"
                                   placeholder="Nhập phần còn lại">
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="submit" class="btn btn-success" id="edit">Lưu</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ShortenURLFormUpdate",
    data() {
        return {
            isCustomizeBackHalf: false,
        }
    }
}
</script>

<style scoped>
#edit {
    width: 100% !important;
    height: 3rem !important;
}

#copyBtn, #redirectBtn {
    width: 30% !important;
}

.text-center {
    border-bottom: 1px solid lightgray;
}
</style>
