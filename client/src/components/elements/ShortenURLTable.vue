<template>
    <div class="table-responsive">
        <table class="table align-items-center table-flush">
            <thead class="thead-light">
            <tr>
                <th scope="col" v-for="(item, index) in data.header" :key="index">{{ item }}</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in data.data" :key="item.id">
                <td v-for="(value, key) in item" :key="key">{{ value }}</td>
                <td v-if="data.name==='short-url'">
                    <button class="btn btn-outline-danger" data-toggle="modal" data-target="#modalUpdate">
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
export default {
    name : "ShortenURLTable",
    props: {
        data: {
            type   : Object,
            default: null,
        }
    },
}
</script>
<style scoped>
.btn {
    width: 100% !important;
}
</style>
