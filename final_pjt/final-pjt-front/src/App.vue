<template>
  <header>
    <nav v-if="store.isLogin">
      <form @submit.prevent="store.logOut" >
        <input type="submit" value="logOut">
      </form>
      <RouterLink :to ="{name:'MyLikeView', params:{id:UserId}}"> 내가 찜한 콘텐츠 </RouterLink>|
      <RouterLink :to="{name:'UserView',params:{id:UserId}}">내 프로필 보기</RouterLink>
      

    </nav>
    <nav v-else>
      <RouterLink :to ="{name:'SignUpView'}" > SignUp   </RouterLink>|
      <RouterLink :to ="{name:'LogInView'}" > LogIn   </RouterLink>|
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { ref } from "vue"
import { RouterView, RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter';
const UserId = ref(1) //  원래 백엔드에서 받아와야하는데 테스트하는 것

  const store = useCounterStore()
</script>
<style scoped>
</style>