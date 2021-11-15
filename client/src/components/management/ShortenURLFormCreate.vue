<template>
  <div class="modal left fade" id="modalCreate" tabindex="5" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h1 id="myModalLabel">ĐÁNH GIÁ</h1>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
              aria-hidden="true"><i class="bi bi-x-lg"></i></span></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="handleFeedback" id="form">
            <div class="form-group">
              <label>Xếp hạng câu trả lời của chúng tôi:</label>
              <select class="form-control form-select" aria-label="Default select example"
                      id="select-domain" v-model="feedbackData.rate">
                <option v-for="item in ratingOption" :key="item" :selected="{selected: item === 1}">{{ item }}</option>
              </select>
            </div>
            <div class="form-group form-check">
              <input type="checkbox" class="form-check-input" id="choose-back-half"
                     v-model="isCustomizeBackHalf">
              <label class="form-check-label" for="choose-back-half">Góp ý cho chúng tôi</label>
            </div>
            <div class="form-group" v-if="isCustomizeBackHalf">
              <textarea class="form-control" v-model="feedbackData.feedback"
                        placeholder="Nhập thông tin góp ý của bạn" resize="none" rows="6"></textarea>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="submit" class="btn btn-warning" id="create" form="form">Gửi phản hồi</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";

export default {
  name: "ShortenURLFormCreate",
  data() {
    return {
      isCustomizeBackHalf: false,
      ratingOption: [1, 2, 3, 4, 5],
      feedbackData: {
        rate: 5,
        feedback: '',
      }
    }
  },
  computed: {
    ...mapState('QA', ['data', 'errors']),
    ...mapState('auth', ['user']),
  },
  methods: {
    ...mapMutations('QA', ['resetErrors']),
    ...mapActions('QA', ['sendFeedback']),
    async handleFeedback() {
      this.resetErrors();
      const feedbackData = {
        rate: this.feedbackData.rate,
        feedback: this.feedbackData.feedback,
        question: this.data.question,
        answer: this.data.answer
      };
      await this.sendFeedback({id: this.user ? this.user.id : null, feedbackData: feedbackData});
      if (!this.errors) {
        alert('Cám ơn bạn đã phản hồi cho chúng tôi!!!');
      } else {
        alert(this.errors.message);
      }
    }
  }
}
</script>

<style scoped>
#create {
  width: 100% !important;
  height: 3rem !important;

}
</style>
