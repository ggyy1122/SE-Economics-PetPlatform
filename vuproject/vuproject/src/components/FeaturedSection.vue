<template>
  <div>
    <h2>精选内容</h2>
    <div class="product-list">
      <div v-for="product in products" :key="product.id" class="product">
        <!-- 改用 @click 事件，在新标签页打开商品详情 -->
        <div @click="openProductPage(product.id)" style="cursor: pointer">
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
        </div>
        <p class="price">价格: ￥{{ product.price }}</p>
        <p class="stock">库存: {{ product.stock }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      products: [], // 存储商品列表
    };
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/products/");
        this.products = response.data; // 获取商品数据
      } catch (error) {
        console.error("获取商品失败:", error);
      }
    },
    openProductPage(productId) {
      // 在新标签页打开商品详情页
      window.open(`/product/${productId}`, "_blank");
    },
  },
};
</script>

<style scoped>
.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); /* 自适应布局，每个商品占一个宽度最小为200px */
  gap: 20px;
  padding: 20px; /* 为产品列表添加内边距 */
}

.product {
  background-color: #fff; /* 商品卡片背景色 */
  border-radius: 10px; /* 圆角 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  padding: 15px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* 动画效果 */
}

.product:hover {
  transform: translateY(-5px); /* 鼠标悬停时卡片上移 */
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15); /* 悬停时加深阴影 */
}

.product img {
  width: 100%;
  height: 200px; /* 统一商品图片的高度 */
  object-fit: cover; /* 确保图片填充区域，按比例缩放 */
  border-radius: 10px;
}

.product h3 {
  font-size: 1.2em;
  margin: 10px 0;
  color: #333;
}

.product .price {
  font-size: 1.1em;
  font-weight: bold;
  color: #f60; /* 价格颜色 */
}

.product .stock {
  font-size: 0.9em;
  color: #888; /* 库存颜色 */
}
</style>
