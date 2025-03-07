<template>
    <div>
      <h2>精选内容</h2>
      <div class="product-list">
        <div v-for="product in products" :key="product.id" class="product">
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
          <p>价格: ￥{{ product.price }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        products: [
          { id: 1, name: "商品A", price: 99, image: "https://via.placeholder.com/150" },
          { id: 2, name: "商品B", price: 199, image: "https://via.placeholder.com/150" },
          { id: 3, name: "商品C", price: 299, image: "https://via.placeholder.com/150" },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .product-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
  }
  
  .product {
    width: 150px;
    text-align: center;
  }
  
  .product img {
    width: 100%;
    border-radius: 10px;
  }
  </style>
  