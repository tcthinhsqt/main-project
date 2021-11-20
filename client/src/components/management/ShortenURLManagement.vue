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
        <ShortenURLTable :data="validations.results" :header="header" :fieldNotUse="fieldNotUse"/>
        <nav aria-label="Page navigation example" class="d-flex justify-content-end mt-2 mr-2">
          <ul class="pagination">
            <li class="page-item" :class="{disabled: isDisabledFirst}">
              <a type="button" class="page-link"
                 @click.prevent="getValidationListData(validations.first.start, validations.first.limit)">
                <span aria-hidden="true">&laquo;</span>
                <span class="sr-only">First</span>
              </a>
            </li>
            <li class="page-item" :class="{disabled: isDisabledFirst}">
              <a type="button" class="page-link"
                 @click.prevent="getValidationListData(validations.previous.start, validations.previous.limit)">
                <span aria-hidden="true">&lsaquo;</span>
                <span class="sr-only">Previous</span>
              </a>
            </li>
            <li v-for="page in validations.total_page" class="page-item" :key="page"
                :class="{active: page===validations.current_page}"
                v-if="Math.abs(validations.current_page - page)<5
                || (page < 10 && validations.current_page < 6)
                || (page > validations.total_page - 9 && validations.current_page > validations.total_page - 5)"
            >
              <a type="button" class="page-link"
                 @click.prevent="getValidationListData(((page-1)*validations.limit) + 1, validations.limit)"
                 :class="{disabled: page===validations.current_page}"
              >{{ page }}</a>
            </li>
            <li class="page-item" :class="{disabled: isDisabledLast}">
              <a type="button" class="page-link"
                 @click.prevent="getValidationListData(validations.next.start, validations.next.limit)">
                <span aria-hidden="true">&rsaquo;</span>
                <span class="sr-only">Next</span>
              </a>
            </li>
            <li class="page-item" :class="{disabled: isDisabledLast}">
              <a type="button" class="page-link"
                 @click.prevent="getValidationListData(validations.last.start, validations.last.limit)">
                <span aria-hidden="true">&raquo;</span>
                <span class="sr-only">Last</span>
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
import ShortenURLTable from "../elements/ShortenURLTable";
import {mapActions, mapMutations, mapState} from "vuex";

export default {
  name: "ShortenURLManagement",
  components: {ShortenURLTable},
  data() {
    return {
      header: ['Câu trả lời', 'Phản hồi', 'Câu hỏi', 'Đánh giá', 'Mã người dùng', 'Người dùng', 'Ngày đánh giá', ''],
      fieldNotUse: ['id'],
      isDisabledFirst: false,
      isDisabledLast: false,
      // searchData: 0,
    }
  },
  computed: {
    ...mapState('validation', ['validations', 'errors']),
  },
  methods: {
    ...mapMutations('validation', ['resetErrors']),
    ...mapActions('validation', ['getFeedbacksData']),
    async getValidationListData(start, limit) {
      this.resetErrors();
      await this.getFeedbacksData({start: start, limit: limit});
      this.isDisabledFirst = this.validations.current_page <= 1;
      this.isDisabledLast = this.validations.current_page >= this.validations.total_page;
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
    this.getValidationListData(1, 5);
  }
}
</script>
