<template>
    <div>
        Detail
        {{  $route.params.id }} -{{ videoId }} -{{ $route.query }}
    </div>
    <div>
        <iframe id="ytplayer" type="text/html" width="640" height="360"
        :src="videoUrl"
        frameborder="0"></iframe>
    </div>
</template>

<script setup>
    import { ref,computed } from 'vue'
    // 여기서 쓰려면 이렇게 가져와야
    import { useRoute } from 'vue-router';
    const route = useRoute()
    const videoId = ref(route.params.id)
    const videoUrl = computed(()=> `https://www.youtube.com/embed/${videoId.value}`)

</script>

<style scoped>

</style>