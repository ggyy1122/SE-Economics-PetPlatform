<template>
  <div class="cart-page">
    <h2>我的购物车</h2>

    <!-- 购物车有商品时显示 -->
    <div v-if="cartItems.length > 0">
      <div
        v-for="item in cartItems"
        :key="item.product_id"
        class="cart-item"
      >
        <p>{{ item.product }}</p>

        <p>
          数量:
          <input
            v-model.number="item.quantity"
            @change="updateCartItem(item.product_id, item.quantity)"
            type="number"
            min="1"
          />
        </p>

        <p>价格: {{ item.total_price }} 元</p>

        <button @click="removeFromCart(item.product_id)">删除</button>
      </div>
      <h3>总价: {{ totalPrice }} 元</h3>
    </div>

    <!-- 购物车为空时显示 -->
    <div v-else>
      <p>购物车是空的</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cartItems: [], // 购物车商品列表
      totalPrice: 0, // 购物车总价
    };
  },
  created() {
    this.fetchCart();
  },
  methods: {
    // 获取购物车信息
    async fetchCart() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/cart/cart/", {
          method: "GET",
          credentials: "include",
        });
        if (!response.ok) {
          throw new Error(`获取购物车失败，状态码：${response.status}`);
        }

        const data = await response.json();
        console.log("购物车数据：", data);

        // 确保 cartItems 和 totalPrice 正确赋值，避免 undefined 错误
        this.cartItems = Array.isArray(data.cart) ? data.cart : [];
        this.totalPrice = data.total_price ?? 0;
      } catch (error) {
        console.error("获取购物车信息失败", error);
      }
    },

    // 更新购物车商品数量
    async updateCartItem(productId, quantity) {
      if (quantity < 1) {
        alert("数量不能小于 1！");
        return;
      }

      try {
        const response = await fetch(
          `http://127.0.0.1:8000/api/cart/update/${productId}/`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            credentials: "include",
            body: JSON.stringify({ quantity }),
          }
        );

        if (!response.ok) {
          throw new Error(`更新商品失败，状态码：${response.status}`);
        }

        const data = await response.json();
        alert(data.message || "商品数量已更新");

        // 重新加载购物车
        this.fetchCart();
      } catch (error) {
        console.error("更新购物车失败", error);
        alert("更新商品数量失败，请稍后再试！");
      }
    },

    // 从购物车中移除商品
    async removeFromCart(productId) {
      // 检查 productId 是否有效
      if (!productId) {
        alert("商品 ID 不存在，无法删除！");
        return;
      }

      console.log("正在删除的商品 ID:", productId); // 输出 productId，检查是否有效

      try {
        const response = await fetch(
          `http://127.0.0.1:8000/api/cart/remove/${productId}/`,
          {
            method: "POST",
            credentials: "include",
          }
        );

        if (!response.ok) {
          throw new Error(`删除商品失败，状态码：${response.status}`);
        }

        const data = await response.json();
        alert(data.message || "商品已从购物车移除");

        // 重新获取购物车信息，确保前端与后端数据同步
        this.fetchCart();
      } catch (error) {
        console.error("从购物车移除商品失败", error);
        alert("删除商品失败，请稍后再试！");
      }
    },
  },
};
</script>

<style scoped>
.cart-page {
  padding: 20px;
}

.cart-item {
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
}

button {
  background-color: red;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}

input {
  width: 50px;
}
</style>