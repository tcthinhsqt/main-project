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
              <ValidationProvider vid="pattern" name="Pattern" rules="required"
                                  v-slot="{ errors }">
                <div class="form-group mb-3">
                  <div class="input-group input-group-merge input-group-alternative">
                    <div class="input-group-prepend">
                      <!--                      <span class="input-group-text"><i class="bi bi-file-earmark"></i></span>-->
                      <button @click.prevent="choosePatternFile"
                              class="btn btn-primary"
                              data-toggle="tooltip"
                              data-placement="top"
                              title="Must be .txt file"
                              ref="patternBtn">
                        <i class="bi bi-file-earmark"></i>
                        Chọn file mẫu
                      </button>

                    </div>
                    <input type="text" class="form-control"
                           placeholder="Must be .txt file"
                           v-model="patternFilename"
                           data-toggle="tooltip"
                           data-placement="top"
                           title="Must be .txt file"
                           disabled>
                    <input id="pattern"
                           class="form-control"
                           placeholder="Chọn một file"
                           type="file"
                           :class="{'is-invalid': errors[0]}"
                           ref="patternFile"
                           @change="displayPatternName"
                           name="pattern"
                           accept=".txt"
                           hidden
                    >
                  </div>
                </div>
                <div class="input-group invalid-feedback mt--2">
                  {{ errors[0] }}
                </div>
              </ValidationProvider>
              <ValidationProvider vid="content" name="Content" rules="required"
                                  v-slot="{ errors }">
                <div class="form-group mb-3">
                  <div class="input-group input-group-merge input-group-alternative">
                    <div class="input-group-prepend">
                      <!--                      <span class="input-group-text"><i class="bi bi-file-earmark"></i></span>-->
                      <button @click.prevent="chooseContentFile"
                              class="btn btn-primary"
                              data-toggle="tooltip"
                              data-placement="top"
                              title="Must be .csv file"
                              ref="contentBtn">
                        <i class="bi bi-file-earmark"></i>
                        Chọn file nội dung
                      </button>

                    </div>
                    <input type="text"
                           class="form-control"
                           placeholder="Must be .csv file"
                           v-model="contentFilename"
                           data-toggle="tooltip"
                           data-placement="top"
                           title="Must be .csv file"
                           disabled>
                    <input id="content"
                           class="form-control"
                           placeholder="Chọn một file"
                           type="file"
                           :class="{'is-invalid': errors[0]}"
                           ref="contentFile"
                           @change="displayContentName"
                           hidden
                           name="content"
                           accept="text/csv"
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
                <button type="submit"
                        class="btn btn-primary my-4"
                        @click.prevent="handleGenerateData"
                        :disabled="invalid">
                  <i class="bi bi-box-arrow-right"></i>
                  Phát sinh dữ liệu mới
                </button>
              </div>
              <ShortenURLLoading v-show="$store.state.isLoading"/>
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
import {mapActions, mapMutations, mapState} from "vuex";

export default {
  name: "Admin",
  components: {ShortenURLLoading, ShortenURLManagement},
  data() {
    return {
      patternFilename: '',
      contentFilename: '',
    }
  },
  computed: {
    ...mapState('generation', ['data', 'errors']),
  },
  methods: {
    ...mapMutations('generation', ['resetErrors']),
    ...mapActions('generation', ['generateData']),
    async choosePatternFile() {
      await this.$refs.patternFile.click();
    },
    async chooseContentFile() {
      await this.$refs.contentFile.click();
    },
    displayPatternName() {
      this.patternFilename = this.$refs.patternFile.files[0].name;
    },
    displayContentName() {
      this.contentFilename = this.$refs.contentFile.files[0].name;
    },
    async handleGenerateData() {
      this.resetErrors();
      const pattern = this.$refs.patternFile.files[0];
      const content = this.$refs.contentFile.files[0];
      let formData = new FormData();
      formData.append('pattern', pattern);
      formData.append('content', content);
      await this.generateData(formData);
      if (!this.errors) {
        const url = window.URL.createObjectURL(new Blob([this.data], {
          encoding: "UTF-8",
          type: "text/csv;charset=UTF-8"
        }));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'data.csv');
        document.body.appendChild(link);
        link.click();
      } else {
        alert('Tạo dữ liệu thất bại!!!');
      }
    },
  }
}
</script>

<style scoped>

</style>