<template>
    <div>
        <h1>UserView</h1>
        <h2> {{ userId }} 유저의 페이지입니다. </h2> 
        <!-- 내 프로필이면 안보이게 하기         -->
        <userLike />
        <!-- <button @click="goHome">홈으로!</button> -->
        
    </div>
</template>

<script setup>
    import userLike from '@/components/userLike.vue'
    import { ref } from 'vue'   //이렇게 할 수도 있음
    import { useRoute,useRouter,onBeforeRouteUpdate} from 'vue-router'; 
    const route = useRoute()
    const userId = ref(route.params.id)

    //프로그래밍 방식 네비게이션
    const router = useRouter()
//     const goHome = function(){
//       router.push({ name : 'home' })
//     }

</script>

<style scoped>

</style>