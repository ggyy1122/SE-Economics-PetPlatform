<template>
  <div class="product-detail">
    <!-- 商品信息部分 -->
    <div class="product-info">
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

      <div class="product-description">
        <h1>{{ product.name }}</h1>
        <p class="price">价格: ￥{{ product.price }}</p>
        <p class="stock">库存: {{ product.stock }} 件</p>
        <p class="description">{{ product.description }}</p>
        <div class="button-group">
          <button class="buy-button" @click="handleBuyNow">立即购买</button>
          <button
            class="order-button"
            @click="addToCart(product.id)"
          >加入购物车</button>
          <button
            class="favorite-button"
            :class="{ active: isFavorite }"
            @click="toggleFavorite"
          > {{ isFavorite ? '已收藏' : '收藏' }}
          </button>
        </div>
      </div>
    </div>

    <!-- 评论部分 -->
    <div class="product-comments">
      <h2>用户评论</h2>
      <ul>
        <li
          v-for="comment in comments"
          :key="comment.id"
        >
          <p><strong>用户 {{ comment.user }}:</strong></p>
          <p>{{ comment.text }}</p>
          <p class="comment-time">{{ new Date(comment.created_at).toLocaleString() }}</p>
        </li>
      </ul>

      <!-- 添加评论部分 -->
      <div class="add-comment">
        <textarea
          v-model="newCommentText"
          placeholder="写下你的评论..."
          rows="4"
        ></textarea>
        <button @click="submitComment">提交评论</button>
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
      isFavorite: false,
      comments: [],
      newCommentText: "", // 用于存储用户输入的评论内容
    };
  },
  async mounted() {
    const productId = this.$route.params.id;
    await this.fetchProductDetails(productId);
    await this.checkFavoriteStatus(productId);
    await this.fetchComments(productId);
  },
  watch: {
    "$route.params.id": async function (newId) {
      await this.fetchProductDetails(newId);
      await this.checkFavoriteStatus(newId);
      await this.fetchComments(newId);
    },
  },
  methods: {
    async handleBuyNow() {
      try {
        // 调用支付API创建支付订单
        const response = await axios.post(
          `http://127.0.0.1:8000/api/pay/create_payment/?amount=${this.product.price}`,
          { product_id: this.product.id },
          { withCredentials: true }
        );
        
        // 从响应中获取支付URL
        const payUrl = response.data.pay_url;
        
        // 在新窗口打开支付页面
        window.open(payUrl, '_blank');
        
        // 可以在这里添加支付状态检查逻辑
        // this.checkPaymentStatus(response.data.out_trade_no);
        
      } catch (error) {
        console.error("创建支付订单失败:", error);
        alert("创建支付订单失败，请稍后重试");
      }
    },
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

    async fetchComments(productId) {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/comments/product/${productId}/`
        );
        this.comments = response.data;
      } catch (error) {
        console.error("获取评论失败:", error);
      }
    },

    async submitComment() {
      if (!this.newCommentText.trim()) {
        alert("评论内容不能为空！");
        return;
      }

      try {
        const productId = this.$route.params.id;
        const response = await axios.post(
          `http://127.0.0.1:8000/api/comments/add/${productId}/`,
          { text: this.newCommentText },
          { withCredentials: true }
        );
        console.log("评论提交成功:", response.data);
        this.comments.push(response.data); // 更新评论列表
        this.newCommentText = ""; // 清空评论输入框
      } catch (error) {
        console.error("提交评论失败:", error);
        alert("提交评论失败！");
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

        this.isFavorite = !this.isFavorite;
      } catch (error) {
        console.error("收藏操作失败:", error);
      }
    },

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
  flex-direction: column; /* 纵向排列 */
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
  margin-bottom: 20px; /* 上下间距 */
}

.product-image {
  flex: 2; /* 图片占 2/3 */
  margin-right: 20px;
  position: relative;
}

.product-image img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 图片阴影 */
}

.product-description {
  flex: 1; /* 描述占 1/3 */
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
  gap: 12px;
  margin-top: 20px;
}

.buy-button,
.order-button {
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: transform 0.2s ease, opacity 0.2s ease;
}

.buy-button {
  background-color: #ff4500;
  color: white;
  box-shadow: 0 4px 8px rgba(255, 69, 0, 0.1);
}

.order-button {
  background-color: #ffcc00;
  color: white;
  box-shadow: 0 4px 8px rgba(255, 204, 0, 0.1);
}

.buy-button:hover,
.order-button:hover {
  opacity: 0.9;
  transform: scale(1.05);
}

/* 收藏按钮 */
.favorite-button {
  border: none;
  padding: 10px 15px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  transition: background-color 0.3s, transform 0.2s;
  color: white;
  background-color: #ffb347; /* 未收藏状态 */
  box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2); /* 阴影 */
}

.favorite-button.active {
  background-color: #ff7f00; /* 已收藏状态 */
}

.favorite-button:hover {
  transform: scale(1.05);
  filter: brightness(1.1);
}

.add-comment {
  margin-top: 30px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.add-comment textarea {
  width: 100%;
  max-width: 600px;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 8px;
  resize: vertical;
  margin-bottom: 10px;
  font-size: 16px;
}

.add-comment button {
  padding: 12px 24px;
  background-color: #ff4500;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.add-comment button:hover {
  background-color: #e43e00;
  transform: scale(1.05);
}

/* 评论区 */
.product-comments {
  width: 100%;
  max-width: 1000px;
  margin-top: 40px;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.product-comments h2 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
}

.product-comments ul {
  list-style-type: none;
  padding: 0;
}

.product-comments li {
  margin-bottom: 20px;
  border-bottom: 1px solid #eee;
  padding-bottom: 10px;
}

.product-comments .comment-time {
  font-size: 12px;
  color: #aaa;
  margin-top: 5px;
}

.product-comments p {
  font-size: 14px;
  color: #444;
}

.product-comments strong {
  color: #e67e22;
}
</style>
