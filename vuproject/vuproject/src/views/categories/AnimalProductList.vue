<template>
    <div class="category-page">
      <h2>{{ categoryName }} 商品</h2>
  
      <!-- 子类导航 -->
      <div class="category-nav">
        <div 
          v-for="category in categories" 
          :key="category.value"
          class="nav-item"
          :class="{ active: activeCategory === category.value }"
          @mouseenter="filterProducts(category.value)"
        >
          {{ category.label }}
        </div>
      </div>
  
      <!-- 商品展示 -->
      <div class="product-list">
        <div 
          v-for="product in paginatedProducts[activeCategory]" 
          :key="product.id" 
          class="product"
          @click="openProductPage(product.id)"  
        >
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
          <p>￥{{ product.price }}</p>
        </div>
      </div>
  
      <!-- 分页 -->
      <div class="pagination" v-if="paginatedProducts[activeCategory]">
        <button 
          @click="changePage(activeCategory, currentPage[activeCategory] - 1)" 
          :disabled="currentPage[activeCategory] <= 1"
        >上一页</button>
        <span>第 {{ currentPage[activeCategory] }} 页</span>
        <button 
          @click="changePage(activeCategory, currentPage[activeCategory] + 1)" 
          :disabled="currentPage[activeCategory] >= totalPages[activeCategory]"
        >下一页</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'CategoryPage',
    props: {
      categoryName: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        categories: [
          { label: '主粮', value: '主粮' },
          { label: '零食', value: '零食' },
          { label: '玩具', value: '玩具' }
        ],
        activeCategory: '主粮', // 默认选择第一个分类
        products: [],
        filteredProducts: [],
        // 每个分类的分页状态
        currentPage: {
          '主粮': 1,
          '零食': 1,
          '玩具': 1
        },
        productsPerPage: 12,
        totalPages: {
          '主粮': 1,
          '零食': 1,
          '玩具': 1
        },
        paginatedProducts: {
          '主粮': [],
          '零食': [],
          '玩具': []
        }
      };
    },
    mounted() {
      this.fetchProducts();  // 加载初始商品数据
    },
    methods: {
      async fetchProducts() {
        try {
          const res = await axios.get(`http://127.0.0.1:8000/api/products/?animals__name=${this.categoryName}`);
          this.products = res.data.results || [];
          this.filteredProducts = this.products;
          this.filterProducts(this.activeCategory); // 初始化分类商品
        } catch (err) {
          console.error(`获取 ${this.categoryName} 商品失败`, err);
        }
      },
      // 打开商品详情页
      openProductPage(productId) {
        window.open(`/product/${productId}`, "_blank");
      },
      async filterProducts(category) {
        this.activeCategory = category;
        try {
          const res = await axios.get(`http://127.0.0.1:8000/api/products/?animals__name=${this.categoryName}&categories__name=${category}`);
          this.filteredProducts = res.data.results || [];
          this.totalPages[category] = Math.ceil(this.filteredProducts.length / this.productsPerPage); // 更新总页数
          this.paginateProducts(category); // 加载当前页商品
        } catch (err) {
          console.error(`筛选 ${this.categoryName} 商品失败`, err);
          this.filteredProducts = [];
        }
      },
      paginateProducts(category) {
        const start = (this.currentPage[category] - 1) * this.productsPerPage;
        const end = start + this.productsPerPage;
        this.paginatedProducts[category] = this.filteredProducts.slice(start, end);
      },
      changePage(category, pageNumber) {
        if (pageNumber >= 1 && pageNumber <= this.totalPages[category]) {
          this.currentPage[category] = pageNumber;
          this.paginateProducts(category); // 更新当前分类的商品
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .category-nav {
    display: flex;
    gap: 12px;
    margin-bottom: 16px;
    padding: 0 10px;
  }
  
  .nav-item {
    padding: 6px 12px;
    background-color: #eee;
    border-radius: 20px;
    cursor: pointer;
    transition: 0.3s;
  }
  
  .nav-item:hover {
    background-color: #ddd;
  }
  
  .nav-item.active {
    background-color: #ff6b00;
    color: white;
  }
  
  .product-list {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    padding: 0 10px;
  }
  
  .product {
    width: 180px;
    border: 1px solid #ddd;
    border-radius: 6px;
    padding: 10px;
    text-align: center;
    transition: box-shadow 0.3s ease;
  }
  
  .product:hover {
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  .product img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 6px;
  }
  
  .pagination {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 20px;
  }
  
  .pagination button {
    padding: 6px 12px;
    border: none;
    background-color: #ff6b00;
    color: white;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .pagination button:disabled {
    background-color: #ddd;
    cursor: not-allowed;
  }
  
  .pagination button:hover:not(:disabled) {
    background-color: #e65c00;
  }
  </style>
  