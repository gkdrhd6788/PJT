<template>
    <div>
        <ul class="nav bg-dark justify-content-center">
            <li class="nav-item">
                <RouterLink :to="{name:'home'}" class="nav-link text-white">Home</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{name:'list'}" class="nav-link">MovieList</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{name:'search'}" class="nav-link">Searh</RouterLink>
            </li>
        </ul>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped>
/* .nav-link {

} */
</style>