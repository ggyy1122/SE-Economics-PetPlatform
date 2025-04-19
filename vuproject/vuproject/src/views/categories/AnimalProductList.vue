<template>
    <div class="category-page">
      <h2>{{ categoryName }} 商品</h2>
  
      <!-- 子类导航：点击切换路由 -->
      <div class="category-nav">
        <router-link
          v-for="category in categories"
          :key="category.value"
          :to="`/category/${categoryPath}/${category.path}`"
          class="nav-item"
          :class="{ active: isActiveCategory(category.path) }"
        >
          {{ category.label }}
        </router-link>
      </div>
  
      <!-- 商品展示 -->
      <div class="product-list">
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
  
      <!-- 分页 -->
      <div class="pagination" v-if="totalPages > 1">
        <button @click="changePage(currentPage - 1)" :disabled="currentPage <= 1">上一页</button>
        <span>第 {{ currentPage }} 页</span>
        <button @click="changePage(currentPage + 1)" :disabled="currentPage >= totalPages">下一页</button>
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
      },
      subCategory: {
        type: String,
        required: false,
        default: ''
      }
    },
    data() {
      return {
        categories: [
          { label: '主粮', value: '主粮', path: 'food' },
          { label: '零食', value: '零食', path: 'snack' },
          { label: '玩具', value: '玩具', path: 'toy' }
        ],
        currentPage: 1,
        productsPerPage: 12,
        products: [],
        paginatedProducts: [],
        totalPages: 1
      };
    },
    computed: {
        categoryPath() {
  const map = {
    '狗': 'dog',
    '猫': 'cat',
    '小宠': 'small',
    '水族': 'aquatic',
    '爬虫': 'reptile',
    '全部商品': 'all'
  };
  return map[this.categoryName] || this.categoryName.toLowerCase();
}

    },
    watch: {
      '$route.fullPath': {
        handler() {
          this.currentPage = 1;
          this.fetchProducts();
        },
        immediate: true
      }
    },
    methods: {
      isActiveCategory(path) {
        return this.$route.path.includes(`/${path}`);
      },
      async fetchProducts() {
        try {
          const categoryParam = this.subCategory || this.routeSubCategory();
          const res = await axios.get(
            `http://127.0.0.1:8000/api/products/?animals__name=${this.categoryName}&categories__name=${categoryParam}`
          );
          this.products = res.data.results || [];
          this.totalPages = Math.ceil(this.products.length / this.productsPerPage);
          this.paginateProducts();
        } catch (err) {
          console.error(`获取 ${this.categoryName} 商品失败`, err);
          this.products = [];
          this.paginatedProducts = [];
        }
      },
      paginateProducts() {
        const start = (this.currentPage - 1) * this.productsPerPage;
        const end = start + this.productsPerPage;
        this.paginatedProducts = this.products.slice(start, end);
      },
      changePage(page) {
        if (page >= 1 && page <= this.totalPages) {
          this.currentPage = page;
          this.paginateProducts();
        }
      },
      openProductPage(productId) {
        window.open(`/product/${productId}`, '_blank');
      },
      routeSubCategory() {
  const pathParts = this.$route.path.split('/');
  const lastPart = pathParts[pathParts.length - 1];
  const mapping = {
    food: '主粮',
    snack: '零食',
    toy: '玩具'
  };
  return mapping[lastPart] || '';
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
    text-decoration: none;
    color: inherit;
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
  