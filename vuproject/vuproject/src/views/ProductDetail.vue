<template>
    <div class="product-detail">
      <div class="product-info">
        <!-- 商品图片部分 -->
        <div class="product-image">
          <img :src="product.image" :alt="product.name" v-if="product.image" />
          <div v-else class="placeholder">图片加载失败</div>
        </div>
  
        <!-- 商品详情部分 -->
        <div class="product-description">
          <h1>{{ product.name }}</h1>
          <p class="price">价格: ￥{{ product.price }}</p>
          <p class="stock">库存: {{ product.stock }} 件</p>
          <p class="description">{{ product.description }}</p> <!-- 动态渲染商品描述 -->
          <button class="buy-button">立即购买</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        product: {
          name: "",
          image: "",
          price: "",
          stock: "",
          description: "",
        },
      };
    },
    mounted() {
      // 获取路由传递的商品 ID
      const productId = this.$route.params.id;
      this.fetchProductDetails(productId); // 请求商品详情
    },
    watch: {
      // 当路由中的商品 ID 发生变化时，重新获取商品详情
      '$route.params.id'(newId) {
        this.fetchProductDetails(newId);
      },
    },
    methods: {
      async fetchProductDetails(id) {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/products/${id}/`); // 动态根据 id 请求数据
          this.product = response.data; // 获取商品数据并赋值
        } catch (error) {
          console.error('获取商品详情失败:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .product-detail {
    display: flex;
    flex-direction: row;
    margin: 20px;
  }
  
  .product-info {
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  
  .product-image img {
    max-width: 400px;
    height: auto;
    object-fit: cover;
    border-radius: 8px;
  }
  
  .product-description {
    margin-left: 20px;
  }
  
  .product-description h1 {
    font-size: 2em;
    margin-bottom: 20px;
  }
  
  .product-description .price {
    font-size: 1.5em;
    color: #f60;
  }
  
  .product-description .stock {
    font-size: 1.2em;
    color: #888;
  }
  
  .product-description .description {
    font-size: 1em;
    margin: 20px 0;
  }
  
  .buy-button {
    background-color: #f60;
    color: white;
    padding: 10px 20px;
    font-size: 1.2em;
    border: none;
    border-radius: 8px;
    cursor: pointer;
  }
  
  .buy-button:hover {
    background-color: #e55a00;
  }
  </style>
  