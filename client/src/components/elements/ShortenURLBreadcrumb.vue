<template>
    <div class="row align-items-center py-4">
        <div class="col-lg-6 col-7">
            <nav aria-label="breadcrumb" class="d-none d-md-inline-block md-4">
                <ol class="breadcrumb breadcrumb-links breadcrumb-dark">
                    <li class="breadcrumb-item" v-for="(item, index) in breadcrumbs" :key="index">
                        <router-link :to="{name: item.routeName}">
                            <i class="bi bi-house-door-fill" v-if="item.routeName === 'home'"></i>
                            {{ item.pageName }}
                        </router-link>
                    </li>
                </ol>
            </nav>
        </div>
    </div>
</template>

<script>
export default {
    name : "ShortenURLBreadcrumb",
    props: {
        breadcrumbs: {
            type   : Array,
            default: null,
        }
    }
}
</script>
