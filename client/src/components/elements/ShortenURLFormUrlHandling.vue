<template>
  <section id="asking" class="about">
    <div class="container">
      <div class="row no-gutters">
        <div class="section-title" data-aos="fade-in" data-aos-delay="100">
          <h2>Let's ask about something you want to know about IUH</h2>
          <p>Easy to use - Easy to learn</p>
        </div>
        <div class="col-xl-12 d-flex align-items-stretch">
          <div class="col-lg-12 icon-box" data-aos="fade-up" data-aos-delay="100">
            <ValidationObserver tag="form" @submit.prevent="submitCreateShortenUrl" ref="urlFormCreate"
                                v-slot="{ invalid }">
              <ValidationProvider vid="question" name="Question" rules="required" v-slot="{ errors }">
                <div class="row justify-content-center">
                  <div class="col-md-8 form-group">
                    <input type="text" name="question" class="form-control" id="question"
                           placeholder="Put your question here" v-model="question"
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
                  ASKING
                </button>
              </div>
              <ShortenURLLoading v-show="false"/>
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
                        <textarea class="form-control" disabled="true" v-model="answer"></textarea>
                        <span class="form-label">Your answer</span>
                      </div>
                    </div>
                    <div class="col-md-2 d-flex flex-column">
                      <div class="form-btn">
                        <button type="button" class="submit-btn"
                                @click.prevent="copyToClipboard">
                          <i class="bi bi-clipboard"></i>
                          Copy
                        </button>
                      </div>
                      <div class="form-btn">
                        <button class="submit-btn" data-toggle="modal" data-target="#modalCreate">
                          <i class="bi bi-pencil-square"></i>
                          Evaluate
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
import ShortenURLLoading from "./ShortenURLLoading.vue";

export default {
  name: "ShortenURLFormUrlHandling",
  components: {ShortenURLLoading},
  data() {
    return {
      question: null,
      isShowResult: false,
      isDisableShortenBtn: false,
      answer: 'Đây là một câu trả lời rất dài rất dài rất dài rất dài rất dài rất dài rất dài rất dài' +
          'dài lắm luôn quá dài tôi là ai ai là tôi chấm chấm chấm',
    }
  },
  methods: {
    copyToClipboard() {
      navigator.clipboard.writeText(this.answer).then(function () {
        alert('Copied');
      }, function () {
        alert('Cannot copy');
      });
    },
    closeResult() {
      this.isShowResult = false;
      this.isDisableShortenBtn = false;
    },
    handleClickShortenInput() {
      this.isDisableShortenBtn = false;
    },
    async submitCreateShortenUrl() {
      this.isShowResult = true;
      this.isDisableShortenBtn = true;
    },
  },
}
</script>

<style scoped>
textarea {
  resize: none;
}
</style>
