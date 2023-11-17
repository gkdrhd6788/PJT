import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
  ]
})

router.beforeEach((to,from)=>{
  const store = useCounterStore()
  // if (to.name === 'ArticleView' && !store.isLogin) {
  //   window.alert('로그인이 필요합니다.')
  //   return { name : 'LogInView'}
  // }
  if ((to.name === 'SignUpView' || to.name=='LogInView') && (store.isLogin)){
    window.alert('이미 로그인 했습니다.')
    return { name: 'ArticleView'}
  }
})




export default router
