<template>
  <div class="row" id="shortUrl">
    <div class="col-xl-12">
      <div class="card">
        <div class="card-header border-0">
          <div class="row align-items-center">
            <div class="col">
              <h3 class="mb-0">Đánh giá gần đây</h3>
            </div>
            <div class="col">
              <!--              <input type="search" id="form1" class="form-control input-search"-->
              <!--                     placeholder="Tìm kiếm đánh giá"/>-->
<!--              <select class="form-control" v-model="searchData">-->
<!--                <option value=0>Tất cả</option>-->
<!--                <option value=1>1</option>-->
<!--                <option value=2>2</option>-->
<!--                <option value=3>3</option>-->
<!--                <option value=4>4</option>-->
<!--                <option value=5>5</option>-->
<!--              </select>-->
            </div>
            <div class="col text-right">
              <ul class="nav nav-pills justify-content-end">
                <li class="nav-item">
                  <a type="button" class="nav-link py-2 px-3 active" @click.prevent="validationsToCsv">
                                        <span class="d-none d-md-block">
                                            <i class="bi bi-folder-symlink"></i>
                                            Xuất ra file CSV
                                        </span>
                    <span class="d-md-none"><i class="bi bi-plus-lg"></i></span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <ShortenURLTable :data="validations.results"
                         :header="header"
                         @get-data="getValidationListData"/>
        <ShortenURLPagination :pagination="validations"
                              @change-page="getValidationListData"
                              v-if="validations.total_page > 1"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ShortenURLTable from "../elements/ShortenURLTable";
import {mapActions, mapMutations, mapState} from "vuex";
import ShortenURLPagination from "../elements/ShortenURLPagination";

export default {
  name: "ShortenURLManagement",
  components: {ShortenURLPagination, ShortenURLTable},
  data() {
    return {
      header: ['Câu trả lời', 'Phản hồi', 'Id', 'Câu hỏi', 'Đánh giá', 'Mã người dùng', 'Người dùng', 'Ngày đánh giá', ''],
      // searchData: 0,
    }
  },
  computed: {
    ...mapState('validation', ['validations', 'errors']),
  },
  methods: {
    ...mapMutations('validation', ['resetErrors']),
    ...mapActions('validation', ['getFeedbacksData']),
    async getValidationListData(start, limit = 10) {
      this.resetErrors();
      await this.getFeedbacksData({start: start, limit: limit});
      if (this.errors) {
        alert('Failed get validations!!!');
      }
    },
    async validationsToCsv() {
      this.$store.commit('generation/resetErrors', null, {root: true});
      await this.$store.dispatch('generation/extractToCsv', null, {root: true});
      if (!this.$store.state.generation.errors) {
        const url = window.URL.createObjectURL(new Blob([this.$store.state.generation.extractData], {
          encoding: "UTF-8",
          type: "text/csv;charset=UTF-8"
        }));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'validations.csv');
        document.body.appendChild(link);
        link.click();
        link.remove();
      } else {
        alert('Không thể xuất ra file CSV!!!');
      }
    },
    // async searchValidations() {
    //   this.$store.commit('validation/resetErrors', null, {root: true});
    //   await this.$store.dispatch('validation/searchFeedback', this.searchData, {root: null});
    //   if(this.$store.state.validation.errors) {
    //     alert('Không thể thực hiện tìm kiếm!!!');
    //   }
    // },
  },
  created() {
    this.getValidationListData(1);
  }
}
</script>
