<template>
    <div class="category-page">
      <h2>小宠商品</h2>
  
      <!-- 小宠子类导航 -->
      <div class="subcategory-nav">
        <button v-for="sub in smallSubcategories" :key="sub" class="nav-button">
          {{ sub }}
        </button>
      </div>
  
      <!-- 商品展示 -->
      <div class="product-list">
        <div v-for="product in smallProducts" :key="product.id" class="product">
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
          <p>￥{{ product.price }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SmallProducts',
    data() {
      return {
        smallSubcategories: ['小宠粮', '玩具', '衣服', '玩具'],
        smallProducts: [] // 待接入数据
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
  