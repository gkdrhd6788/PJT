<template>
  <header>
    <nav v-if="store.isLogin">
      <form @submit.prevent="store.logOut" >
        <input type="submit" value="logOut">
      </form>
    </nav>
    <nav v-else>
      <RouterLink :to ="{name:'SignUpView'}" > SignUp   </RouterLink>|
      <RouterLink :to ="{name:'LogInView'}" > LogIn   </RouterLink>|
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
  import { RouterView, RouterLink } from 'vue-router'
  import { useCounterStore } from '@/stores/counter';

  const store = useCounterStore()
</script>
<style scoped>
</style>