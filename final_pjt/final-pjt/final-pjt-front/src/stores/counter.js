import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios  from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)

  const isLogin = computed(()=>{
    if (token.value===null){
      return false
    } else {
      return true
    }
  })


  const signUp = function(payload){
    const { username, password1, password2 } = payload
    axios({
      method : 'post',
      url : `${API_URL}/accounts/signup/`,
      data : {
        username,
        password1,
        password2,
      }
    })
      .then(res=>{
        const password = password1
        logIn({username,password})
        console.log(res)
        console.log('회원가입 완료')
      })
      .catch(err=>{
        console.log(err)
      })
  }


  const logIn = function(payload){
    const { username, password } = payload
    axios({
      method : 'post',
      url : `${API_URL}/accounts/login/`,
      data : {
        username,
        password,
      }
    })
      .then(res=>{
        console.log(res)
        token.value = res.data.key
        console.log('로그인 완료')
      })
      .catch(err=>{
        console.log(err)
      })}

  const logOut = function(){
    axios({
      method:'post',
      url : `${API_URL}/accounts/logout/`,
    })
    .then((res)=>{
      token.value = null
      console.log('로그아웃 성공')
      console.log(res)
      router.push({name:'logIn'})
    })
    .catch((err)=>{
      console.log(err)
    })
  }
  
  return { signUp,logIn, logOut,isLogin,token }
},{persist:true})
