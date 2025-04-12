<template>
    <div class="category-page">
      <h2>全部商品</h2>
  
      <!-- 商品外框容器 -->
      <div class="product-container">
        <div
          v-for="product in paginatedProducts"
          :key="product.id"
          class="product"
          @click="openProductPage(product.id)"
        >
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
          <p>￥{{ product.price }}</p>
        </div>
      </div>
  
      <!-- 翻页按钮 -->
      <div class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1">上一页</button>
        <span>第 {{ currentPage }} 页 / 共 {{ totalPages }} 页</span>
        <button @click="nextPage" :disabled="currentPage === totalPages">下一页</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "AllProducts",
    data() {
      return {
        products: [],
        currentPage: 1,
        pageSize: 28,
      };
    },
    computed: {
      totalPages() {
        return Math.ceil(this.products.length / this.pageSize);
      },
      paginatedProducts() {
        const start = (this.currentPage - 1) * this.pageSize;
        return this.products.slice(start, start + this.pageSize);
      },
    },
    mounted() {
      this.fetchAllProducts();
    },
    methods: {
      async fetchAllProducts() {
        try {
          const res = await axios.get("http://127.0.0.1:8000/api/products/");
          this.products = res.data.results || [];
        } catch (error) {
          console.error("❌ 获取商品失败:", error);
        }
      },
      openProductPage(productId) {
        window.open(`/product/${productId}`, "_blank");
      },
      nextPage() {
        if (this.currentPage < this.totalPages) {
          this.currentPage++;
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      },
      prevPage() {
        if (this.currentPage > 1) {
          this.currentPage--;
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .category-page {
    padding: 20px;
    text-align: center;
  }
  
  .product-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* 每行4个 */
    gap: 16px;
    max-width: 1120px;
    margin: 0 auto 20px auto;
    min-height: 800px;
  }
  
  .product {
    padding: 10px;
    border-radius: 6px;
    background-color: #fff;
    transition: transform 0.3s;
    cursor: pointer;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
  }
  
  .product:hover {
    transform: translateY(-5px);
  }
  
  .product img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 6px;
  }
  
  .product h3 {
    font-size: 1em;
    margin: 10px 0;
    color: #333;
  }
  
  .product p {
    color: #f60;
    font-weight: bold;
  }
  
  .pagination {
    margin-top: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 16px;
  }
  
  .pagination button {
    padding: 8px 16px;
    background-color: #409eff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .pagination button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  </style>
  