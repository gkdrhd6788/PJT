<template>
    <div>
        Home
    </div>
</template>

<script setup>
  import axios from 'axios'
  const token = import.meta.env.VITE_TMDB_TOKEN
  const videos = ref([])

  const searchVideo = function(keyword){
      const url = 'https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1'

      const options = {
        method: 'GET',
        headers: {
            accept: 'application/json',
            Authorization: `Bearer ${token}`
        }
        };

      const params = {
        key: key,
        part: 'snippet',
        q: keyword,
        type: 'video',
      }

      //youtube 요청
    axios({
        method:'get',
        url,
        params,
    })
        .then(res=>{
            console.log(res.data)
            videos.value = res.data.items
            saveData( videos.value)
        })
        .catch(err=> console.log(err))
  }
</script>

<style scoped>

</style>