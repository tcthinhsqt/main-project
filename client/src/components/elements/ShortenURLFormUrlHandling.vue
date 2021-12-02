<template>
  <section id="asking" class="about">
    <div class="container">
      <div class="row no-gutters">
        <div class="section-title" data-aos="fade-in" data-aos-delay="100">
          <h2>Hãy hỏi về những điều bạn muốn biết về IUH</h2>
          <p>Nhanh chóng - Cập nhật thường xuyên - Đáp ứng đa dạng nhu cầu</p>
        </div>
        <div class="col-xl-12 d-flex align-items-stretch">
          <div class="col-lg-12 icon-box" data-aos="fade-up" data-aos-delay="100">
            <ValidationObserver tag="form" @submit.prevent="submitCreateShortenUrl" ref="urlFormCreate"
                                v-slot="{ invalid }">
              <ValidationProvider vid="question" name="Question" rules="required" v-slot="{ errors }">
                <div class="row justify-content-center">
                  <div class="col-md-8 form-group">
                    <input type="text" name="question" class="form-control" id="question"
                           placeholder="Nhập câu hỏi của bạn ở đây" v-model="question"
                           :class="{'is-invalid': errors[0]}"
                           @click.prevent="handleClickShortenInput"
                    >
                    <div class="invalid-feedback">
                      {{ errors[0] }}
                    </div>
                  </div>
                </div>
              </ValidationProvider>
              <div class="text-center">
                <button type="submit" class="btn-shorten" :disabled="isDisableShortenBtn || invalid">
                  Đặt câu hỏi
                </button>
              </div>
              <ShortenURLLoading v-show="$store.state.isLoading"/>
            </ValidationObserver>
          </div>
        </div>

        <div id="booking" class="section" v-show="isShowResult">
          <div class="section-center">
            <div class="container">
              <div class="row">
                <div class="booking-form">
                  <h1 class="bi bi-x" @click.prevent="closeResult" id="title-form"></h1>
                  <form class="d-flex" @submit.prevent="">
                    <div class="col-md-10">
                      <div class="form-group">
                        <textarea class="form-control" disabled="true" v-model="data.answer"></textarea>
                        <span class="form-label">Câu trả lời của bạn</span>
                      </div>
                    </div>
                    <div class="col-md-2 d-flex flex-column">
                      <div class="form-btn">
                        <button type="button" class="submit-btn"
                                @click.prevent="copyToClipboard">
                          <i class="bi bi-clipboard"></i>
                          Sao chép
                        </button>
                      </div>
                      <div class="form-btn">
                        <button class="submit-btn" data-toggle="modal" data-target="#modalCreate">
                          <i class="bi bi-pencil-square"></i>
                          Đánh giá
                        </button>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";
import ShortenURLLoading from "./ShortenURLLoading.vue";

export default {
  name: "ShortenURLFormUrlHandling",
  components: {ShortenURLLoading},
  data() {
    return {
      question: null,
      isShowResult: false,
      isDisableShortenBtn: false
    }
  },
  computed: {
    ...mapState('QA', ['errors', 'data']),
    ...mapState('auth', ['user']),
  },
  methods: {
    ...mapActions('QA', ['createAnswer']),
    ...mapMutations('QA', ['resetErrors', 'setAnswer']),
    copyToClipboard() {
      navigator.clipboard.writeText(this.data.answer).then(function () {
        alert('Sao chép thành công');
      }, function () {
        alert('Không thể sao chép');
      });
    },
    closeResult() {
      this.isShowResult = false;
      this.isDisableShortenBtn = false;
      this.setAnswer({
        question: null,
        answer: null
      })
    },
    handleClickShortenInput() {
      this.isDisableShortenBtn = false;
    },
    async submitCreateShortenUrl() {
      this.resetErrors();
      await this.createAnswer({cauHoi: this.question, id: this.user ? this.user.id : 0});
      if (this.errors === null) {
        this.isShowResult = true;
        this.isDisableShortenBtn = true;
      } else {
        this.isShowResult = false;
        this.$refs.urlFormCreate.setErrors(this.errors);
      }
    },
  },
}
</script>

<style scoped>
textarea {
  resize: none;
}
</style>
