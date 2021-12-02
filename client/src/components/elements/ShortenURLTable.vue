<template>
  <div class="table-responsive">
    <table class="table align-items-center table-flush">
      <thead class="thead-light">
      <tr>
        <th scope="col" v-for="(item, index) in header" :key="index">{{ item }}</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="item in data" :key="item.id">
        <td v-for="(value, key) in item" :key="key" class="column"
            data-toggle="tooltip"
            data-placement="top"
            :title="value"
        >
          {{ value }}
        </td>
        <td>
          <button class="btn btn-outline-danger" @click.prevent="deleteItem(item.id)">
            <span class="d-none d-md-block">
             <i class="bi bi-trash-fill"></i>
             Xóa
            </span>
            <span class="d-md-none"><i class="bi bi-pencil-fill"></i></span>
          </button>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";

export default {
  name: "ShortenURLTable",
  props: {
    data: {
      type: Array,
      default: null,
    },
    header: {
      type: Array,
      default: null,
    },
    fieldNotUse: {
      type: Array,
      default: null,
    },
  },
  computed: {
    ...mapState('validation', ['errors']),
  },
  methods: {
    ...mapMutations('validation', ['resetErrors']),
    ...mapActions('validation', ['deleteFeedback']),
    async deleteItem(id) {
      await this.deleteFeedback({id: id});
      if (!this.errors) {
        this.$emit('get-data', 1);
        alert('Xóa thành công!!!');
      } else {
        alert('Xóa thất bại!!!');
      }
    },
  }
}
</script>
<style scoped>
.btn {
  width: 100% !important;
}

td {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.column {
  max-width: 18rem;
}
</style>
