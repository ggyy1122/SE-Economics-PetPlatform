<template>
  <div class="category-page">
    <h2>全部商品</h2>

    <!-- 商品外框容器 -->
    <div class="product-container">
      <ProductCard
        v-for="product in paginatedProducts"
        :key="product.id"
        :product="product"
        @click="openProductPage(product.id)"
      />
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
import ProductCard from "@/components/ProductCard.vue"; // 路径根据你项目结构调整

export default {
  name: "AllProducts",
  components: {
    ProductCard
  },
  data() {
    return {
      products: [],
      currentPage: 1,
      pageSize: 25,
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
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 100vh;
}

.product-container {
  display: grid;
  gap: 16px;
  max-width: 100%;
  margin: 0 auto 20px auto;
  flex-grow: 1;
  grid-template-columns: repeat(5, 1fr); /* 固定每行 5 个 */
}


/* ProductCard 自带尺寸的话就不需要额外定义 .product 的宽高了 */

.pagination {
  margin-top: 20px;
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
