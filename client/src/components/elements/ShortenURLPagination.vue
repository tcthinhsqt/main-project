<template>
  <nav aria-label="Page navigation example" class="d-flex justify-content-end mt-2 mr-2">
    <ul class="pagination">
      <li class="page-item" :class="{disabled: isFirstPage}">
        <a type="button" class="page-link" @click.prevent="changePage(pagination.first.start)">
          <span aria-hidden="true">&laquo;</span>
          <span class="sr-only">First</span>
        </a>
      </li>
      <li class="page-item" :class="{disabled: isFirstPage}">
        <a type="button" class="page-link"
           @click.prevent="changePage(pagination.previous.start)">
          <span aria-hidden="true">&lsaquo;</span>
          <span class="sr-only">Previous</span>
        </a>
      </li>
      <li v-for="page in pageList" class="page-item"
          :key="page"
          :class="{disabled: page === pagination.current_page}"
      >
        <a type="button"
           class="page-link"
           :class="{'border border-primary text-primary': page === pagination.current_page}"
           @click.prevent="changePage(((page-1)*pagination.limit) + 1)">
          {{ page }}
        </a>
      </li>
      <li class="page-item" :class="{disabled: isLastPage}">
        <a type="button" class="page-link"
           @click.prevent="changePage(pagination.next.start)">
          <span aria-hidden="true">&rsaquo;</span>
          <span class="sr-only">Next</span>
        </a>
      </li>
      <li class="page-item" :class="{disabled: isLastPage}">
        <a type="button" class="page-link"
           @click.prevent="changePage(pagination.last.start)">
          <span aria-hidden="true">&raquo;</span>
          <span class="sr-only">Last</span>
        </a>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "ShortenURLPagination",
  props: {
    pagination: {
      type: Object,
      default: null,
    },
  },
  computed: {
    pageList() {
      const pages = [];
      if (this.pagination) {
        for (let index = 1; index <= this.pagination.total_page; index++) {
          if (Math.abs(this.pagination.current_page - index) < 5
              || (index < 10 && this.pagination.current_page < 6)
              || (index > this.pagination.total_page - 9 && this.pagination.current_page > this.pagination.total_page - 5)
          ) {
            pages.push(index);
          }
        }
      }
      return pages;
    },
    isFirstPage() {
      return this.pagination.current_page === 1;
    },
    isLastPage() {
      return this.pagination.current_page === this.pagination.total_page;
    },
  },
  methods: {
    async changePage(page) {
      this.$emit('change-page', page);
    },
  }
}
</script>
