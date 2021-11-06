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
              <input type="search" id="form1" class="form-control input-search"
                     placeholder="Tìm kiếm đánh giá"/>
            </div>
            <div class="col text-right">
              <ul class="nav nav-pills justify-content-end">
                <li class="nav-item">
                  <a type="button" class="nav-link py-2 px-3 active">
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
        <ShortenURLTable :data="shortenURLData"/>
      </div>
    </div>
  </div>
</template>

<script>
import ShortenURLTable from "../elements/ShortenURLTable";

export default {
  name: "ShortenURLManagement",
  components: {ShortenURLTable},
  data() {
    return {
      shortenURLData: {
        name: 'short-url',
        header: ['Câu hỏi', 'Câu trả lời', 'Đánh giá', 'Phản hồi', ''],
        data: [
          {
            question: 'Câu hỏi 1',
            answer: 'Câu trả lời 1',
            rating: 5,
            feedback: "Feedback 1",
          },
          {
            question: 'Câu hỏi 2',
            answer: 'Câu trả lời 2',
            rating: 4,
            feedback: "Feedback 2",
          },
          {
            question: 'Câu hỏi 3',
            answer: 'Câu trả lời 3',
            rating: 4,
            feedback: "Feedback 3",
          },
          {
            question: 'Câu hỏi 4',
            answer: 'Câu trả lời 4',
            rating: 3,
            feedback: "Feedback 4",
          },
          {
            question: 'Câu hỏi 5',
            answer: 'Câu trả lời 5',
            rating: 5,
            feedback: "Feedback 5",
          },
        ],
      },
    }
  },
}
</script>
