<template>
    <div class="category-page">
      <h2>🐶 狗狗商品</h2>
  
      <!-- 狗狗子类导航 -->
      <div class="dog-category-nav">
        <div 
          v-for="category in dogCategories" 
          :key="category.value"
          class="nav-item"
          :class="{ active: activeDogCategory === category.value }"
          @mouseenter="filterDogProducts(category.value)"
        >
          {{ category.label }}
        </div>
      </div>
  
      <!-- 商品展示 -->
      <div class="product-list">
        <div 
          v-for="product in paginatedDogProducts[activeDogCategory]" 
          :key="product.id" 
          class="product"
        >
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
          <p>￥{{ product.price }}</p>
        </div>
      </div>
  
      <!-- 分页 -->
      <div class="pagination" v-if="paginatedDogProducts[activeDogCategory]">
        <button 
          @click="changePage(activeDogCategory, currentPage[activeDogCategory] - 1)" 
          :disabled="currentPage[activeDogCategory] <= 1"
        >上一页</button>
        <span>第 {{ currentPage[activeDogCategory] }} 页</span>
        <button 
          @click="changePage(activeDogCategory, currentPage[activeDogCategory] + 1)" 
          :disabled="currentPage[activeDogCategory] >= totalPages[activeDogCategory]"
        >下一页</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'DogProducts',
    data() {
      return {
        dogCategories: [
          { label: '主粮', value: '主粮' },
          { label: '零食', value: '零食' },
          { label: '玩具', value: '玩具' }
        ],
        activeDogCategory: '主粮', // 默认选择第一个分类
        dogProducts: [],
        filteredDogProducts: [],
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
        paginatedDogProducts: {
          '主粮': [],
          '零食': [],
          '玩具': []
        }
      };
    },
    mounted() {
      this.fetchAllDogProducts();  // 加载初始商品数据
    },
    methods: {
      async fetchAllDogProducts() {
        try {
          const res = await axios.get('http://127.0.0.1:8000/api/products/?animals__name=狗');
          this.dogProducts = res.data.results || [];
          this.filteredDogProducts = this.dogProducts;
          this.filterDogProducts(this.activeDogCategory); // 初始化分类商品
        } catch (err) {
          console.error('获取狗狗商品失败', err);
        }
      },
      async filterDogProducts(category) {
        this.activeDogCategory = category;
        try {
          const res = await axios.get(`http://127.0.0.1:8000/api/products/?animals__name=狗&categories__name=${category}`);
          this.filteredDogProducts = res.data.results || [];
          this.totalPages[category] = Math.ceil(this.filteredDogProducts.length / this.productsPerPage); // 更新总页数
          this.paginateProducts(category); // 加载当前页商品
        } catch (err) {
          console.error('筛选狗狗商品失败', err);
          this.filteredDogProducts = [];
        }
      },
      paginateProducts(category) {
        const start = (this.currentPage[category] - 1) * this.productsPerPage;
        const end = start + this.productsPerPage;
        this.paginatedDogProducts[category] = this.filteredDogProducts.slice(start, end);
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
  .dog-category-nav {
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
  