<template>
    <div>
      <h2>我的收藏</h2>
  
      <!-- 商品列表 -->
      <div class="favorites-container">
        <table>
          <thead>
            <tr>
              <th>商品信息</th>
              <th>价格</th>
              <th>库存</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="product in currentPageProducts" :key="product.id">
              <td class="product-info">
                <div class="product-image">
                  <img :src="product.image || 'https://via.placeholder.com/50'" alt="product image" />
                </div>
                <div class="product-name">
                  <h3>{{ product.name || '未知商品' }}</h3>
                </div>
              </td>
              <td class="product-price">
                <p>{{ product.price ?? '未知' }}</p>
              </td>
              <td class="product-stock">
                <p>{{ product.stock ?? '未知' }}</p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
  
      <!-- 分页按钮 -->
      <div class="pagination">
        <button @click="changePage(currentPage - 1)" :disabled="currentPage <= 1">上一页</button>
        <span>{{ currentPage }} / {{ totalPages || 1 }}</span>
        <button @click="changePage(currentPage + 1)" :disabled="currentPage >= totalPages">下一页</button>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      favoriteProducts: [], // 存储收藏商品数据
      currentPage: 1, // 当前页码
      itemsPerPage: 10, // 每页展示的商品数
    };
  },
  computed: {
    currentPageProducts() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      return this.favoriteProducts.slice(start, start + this.itemsPerPage);
    },
    totalPages() {
      return this.favoriteProducts.length > 0 ? Math.ceil(this.favoriteProducts.length / this.itemsPerPage) : 1;
    },
  },
  methods: {
    async fetchFavorites() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/favorites/get_favorites/', {
          withCredentials: true, // 允许携带 Cookies
        });
        this.favoriteProducts = response.data;
      } catch (error) {
        console.error("获取收藏商品失败", error.response || error);
        alert("获取收藏商品失败，请重新登录！");
      }
    },
    changePage(page) {
      if (page >= 1 && page <= this.totalPages) {
        this.currentPage = page;
      }
    },
  },
  mounted() {
    this.fetchFavorites();
  },
};
</script>

<style scoped>
.favorites-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.favorite-item {
  width: 30%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-sizing: border-box;
}

.product-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.product-image img {
  width: 50px;
  height: 50px;
  object-fit: cover;
  border-radius: 5px;
}

.pagination {
  margin-top: 20px;
  text-align: center;
}

.pagination button {
  padding: 10px;
  margin: 0 10px;
  border: none;
  background-color: #007BFF;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.pagination button:disabled {
  background-color: #d6d6d6;
  cursor: not-allowed;
}
</style>
