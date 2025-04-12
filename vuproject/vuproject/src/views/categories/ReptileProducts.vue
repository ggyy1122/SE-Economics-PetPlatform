<template>
    <div class="category-page">
      <h2>爬虫商品</h2>
  
      <!-- 爬虫子类导航 -->
      <div class="subcategory-nav">
        <button v-for="sub in reptileSubcategories" :key="sub" class="nav-button">
          {{ sub }}
        </button>
      </div>
  
      <!-- 商品展示 -->
      <div class="product-list">
        <div v-for="product in reptileProducts" :key="product.id" class="product">
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
          <p>￥{{ product.price }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ReptileProducts',
    data() {
      return {
        reptileSubcategories: ['爬虫粮', '栖息地', '温控设备', '水盆'],
        reptileProducts: [] // 待接入数据
      };
    }
  };
  </script>
  
  <style scoped>
  .subcategory-nav {
    display: flex;
    gap: 12px;
    margin-bottom: 16px;
  }
  
  .nav-button {
    padding: 6px 12px;
    border: none;
    background-color: #eee;
    cursor: pointer;
    border-radius: 4px;
  }
  
  .product-list {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
  }
  
  .product {
    width: 180px;
    border: 1px solid #ddd;
    border-radius: 6px;
    padding: 10px;
    text-align: center;
  }
  </style>
  