<template>
    <div>
        <h1>메인 페이지</h1>
        <div v-if="productIsEmpty" class="product-list">
            <div v-for="product in products" :key="product.id" class="product-card">
                <img :src="product.image" alt="">
                <strong>{{ product.title }}</strong>
                <p>가격: ${{ product.price }}</p>
                <button @click="goDetail(product)">상세 페이지로 이동</button>
                <button @click="addCart(product)">장바구니에 추가</button>
            </div>
        </div>
        <div v-else>
            <strong>로딩 중이거나, 상품정보가 없습니다.</strong>
        </div>
    </div>
</template>

<script setup>
    import { ref,computed } from 'vue'
    import { useRouter } from 'vue-router'
    import axios from 'axios'

    const router = useRouter()
    const products = ref ([]) 
    const storeURL = "https://fakestoreapi.com/products"

    axios.get(storeURL)
        .then((response)=>{
            // console.log(response)
            products.value = response.data
        }) .catch((error)=>{
            console.error(error)
        })
    const productIsEmpty = computed(()=>{
        return products.value.length > 0 ? true : false
    })

    const goDetail = (product) => {
        router.push(`/${product.id}`)
    }
    
    const addCart = (product) => {
        //하나의 데이터만 저장하기
        //문제점: 덮어쓰기 된다.
        // localStorage.setItem('cart',JSON.stringify(product))
    
        //여러 데이터 저장하기
        // 중복 체크
        const ex
    }
</script>

<style scoped>
    .product-list {
        display:flex;
        flex-wrap:wrap;
        gap:10px;
    }

</style>

<style>
    .product-card {
        border :1px solid black;
        width : 200px;
    }
    .product-card img {
        width:200px;
        height: 200px;
        object-fit: fill;
    }
</style>