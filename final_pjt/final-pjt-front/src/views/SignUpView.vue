<template>
  <div>
    <h1>SignUp</h1>
    <form @submit.prevent="signUp">
      <label for="id">ID</label>
      <input type="text" id='id' v-model.trim="username">
      <label for="password1">Password</label>
      <input type="password" id="password1" v-model.trim="password1">
      <label for="password2">Password 재확인</label>
      <input type="password" id="password2" v-model.trim="password2">
      <input type="submit" value="sign up">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'  

  const store = useCounterStore()

  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)

  const signUp = function(){
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
    }
    store.signUp(payload)
  }

</script>

<style scoped>

</style>