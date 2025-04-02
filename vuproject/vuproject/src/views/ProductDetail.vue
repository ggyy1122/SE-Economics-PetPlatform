<template>
  <div class="product-detail">
    <div class="product-info">
      <!-- 商品图片部分 -->
      <div class="product-image">
        <img
          :src="product.image"
          :alt="product.name"
          v-if="product.image"
        />
        <div
          v-else
          class="placeholder"
        >图片加载失败</div>
      </div>

      <!-- 商品详情部分 -->
      <div class="product-description">
        <h1>{{ product.name }}</h1>
        <p class="price">价格: ￥{{ product.price }}</p>
        <p class="stock">库存: {{ product.stock }} 件</p>
        <p class="description">{{ product.description }}</p>
        <div class="button-group">
          <button class="buy-button">立即购买</button>
          <button
            class="order-button"
            @click="addToCart(product.id)"
          >加入购物车</button>
          <!-- 收藏按钮 -->
          <button
            class="favorite-button"
            :class="{ active: isFavorite }"
            @click="toggleFavorite"
          > {{ isFavorite ? '已收藏' : '收藏' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      product: {
        name: "",
        image: "",
        price: "",
        stock: "",
        description: "",
      },
      isFavorite: false, // 收藏状态
    };
  },
  async mounted() {
    const productId = this.$route.params.id;
    console.log("页面加载，获取商品 ID:", productId);
    await this.fetchProductDetails(productId); // 确保数据先加载
    await this.checkFavoriteStatus(productId); // 先查询收藏状态
    console.log("初始收藏状态:", this.isFavorite);
  },
  watch: {
    "$route.params.id": async function (newId) {
      await this.fetchProductDetails(newId);
      await this.checkFavoriteStatus(newId);
    },
  },
  methods: {
    async fetchProductDetails(id) {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/products/${id}/`
        );
        this.product = response.data;
      } catch (error) {
        console.error("获取商品详情失败:", error);
      }
    },

    async checkFavoriteStatus(productId) {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/favorites/check_status/?product_id=${productId}`,
          { withCredentials: true }
        );
        console.log("后端返回收藏状态：", response.data);

        if (response.data && response.data.is_favorited !== undefined) {
          this.isFavorite = response.data.is_favorited;
        } else {
          console.error("返回的数据格式不正确，缺少 is_favorited");
        }
      } catch (error) {
        console.error("检查收藏状态失败:", error);
      }
    },

    async toggleFavorite() {
      try {
        const url = this.isFavorite
          ? "http://127.0.0.1:8000/api/favorites/remove/"
          : "http://127.0.0.1:8000/api/favorites/add/";

        await axios.post(
          url,
          { product_id: this.product.id },
          { withCredentials: true }
        );

        this.isFavorite = !this.isFavorite; // 更新 UI 状态
      } catch (error) {
        console.error("收藏操作失败:", error);
      }
    },

    // 添加到购物车方法
    async addToCart(productId) {
      try {
        const response = await axios.post(
          `http://127.0.0.1:8000/api/cart/add/${productId}/`,
          { quantity: 1 },
          { withCredentials: true }
        );
        console.log("商品已添加到购物车:", response.data);
        alert("商品已添加到购物车！");
      } catch (error) {
        console.error("添加商品到购物车失败:", error);
        alert("添加商品到购物车失败！");
      }
    },
  },
};
</script>

<style scoped>
.product-detail {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.product-info {
  display: flex;
  max-width: 1000px;
  width: 100%;
}

.product-image {
  flex: 2; /* 图片占据左侧 2/3 空间 */
  margin-right: 20px;
}

.product-image img {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.product-description {
  flex: 1; /* 商品信息占据右侧 1/3 空间 */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.product-description h1 {
  font-size: 24px;
  color: #333;
  margin-bottom: 10px;
}

.product-description .price {
  font-size: 20px;
  color: #e67e22;
  margin-bottom: 10px;
}

.product-description .stock {
  font-size: 16px;
  color: #666;
  margin-bottom: 10px;
}

.product-description .description {
  font-size: 14px;
  color: #444;
  margin-bottom: 20px;
}

.button-group {
  display: flex;
  gap: 10px;
}

.buy-button,
.order-button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.buy-button {
  background-color: #ff4500;
  color: white;
}

.order-button {
  background-color: #ffcc00;
  color: white;
}

.buy-button:hover,
.order-button:hover {
  opacity: 0.9;
}

/* 收藏按钮样式 */
.favorite-button {
  border: none;
  padding: 10px 15px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  transition: background-color 0.3s, transform 0.2s;
  color: white;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* 添加阴影 */
  background-color: #ffb347; /* 未收藏状态（淡橙色） */
}

.favorite-button.active {
  background-color: #ff7f00; /* 已收藏状态（深橙色） */
}

.favorite-button:hover {
  transform: scale(1.05);
  filter: brightness(1.1);
}
</style>