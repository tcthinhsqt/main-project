<template>
  <div>
    <div class="pt-3 mt-8" id="panel">
      <!-- Page content -->
      <div class="container">
        <ShortenURLManagement/>
        <div class="card border-0 mb-0">
          <div class="card-header bg-transparent">
            <h3 class="mb-0">Tạo bộ dữ liệu mới</h3>
          </div>
          <div class="card-body px-lg-5 py-lg-5">
            <ValidationObserver tag="form" @submit.prevent="" v-slot="{ invalid }">
              <div class="form-group" hidden>
                <input type="file" class="form-control-file" id="exampleFormControlFile1">
              </div>
              <ValidationProvider vid="username" name="username" rules="required"
                                  v-slot="{ errors }">
                <div class="form-group mb-3">
                  <div class="input-group input-group-merge input-group-alternative">
                    <div class="input-group-prepend">
                      <!--                      <span class="input-group-text"><i class="bi bi-file-earmark"></i></span>-->
                      <button @click.prevent="chooseFile" class="btn btn-primary" ref="files">
                        <i class="bi bi-file-earmark"></i>
                        Chọn file
                      </button>

                    </div>
                    <input id="display-name" type="text" class="form-control" v-model="filename" disabled>
                    <input id="files"
                           class="form-control"
                           placeholder="Chọn một file"
                           type="file"
                           :class="{'is-invalid': errors[0]}"
                           ref="files"
                           @change="displayName"
                           hidden
                    >
                  </div>
                </div>
                <div class="input-group invalid-feedback mt--2">
                  {{ errors[0] }}
                </div>
              </ValidationProvider>
              <br/>

              <div class="input-group invalid-feedback" v-if="false">
                Thông báo lỗi
              </div>
              <div class="text-center">
                <button type="submit" class="btn btn-primary my-4" :disabled="invalid">
                  <i class="bi bi-box-arrow-right"></i>
                  Phát sinh dữ liệu mới
                </button>
              </div>
              <ShortenURLLoading v-show="false"/>
            </ValidationObserver>
          </div>
        </div>


      </div>
    </div>
  </div>
</template>

<script>
import ShortenURLManagement from "../components/management/ShortenURLManagement";
import ShortenURLLoading from "../components/elements/ShortenURLLoading";

export default {
  name: "Admin",
  components: {ShortenURLLoading, ShortenURLManagement},
  data() {
    return {
      filename: '',
    }
  },
  methods: {
    async chooseFile() {
      await this.$refs.files.click();
    },
    displayName() {
      this.filename = this.$refs.files.files[0].name;
    }
  }
}
</script>

<style scoped>

</style>