<template>
  <div class="cart-page">
    <h2>🛒 我的购物车</h2>

    <div v-if="cartItems.length > 0" class="cart-grid">
      <div
        v-for="item in cartItems"
        :key="item.product_id"
        class="cart-item"
      >
        <div class="item-info">
          <h3 class="item-title">{{ item.product }}</h3>

          <div class="item-quantity">
            <label>数量</label>
            <input
              v-model.number="item.quantity"
              @change="updateCartItem(item.product_id, item.quantity)"
              type="number"
              min="1"
            />
          </div>

          <p class="price">价格: <strong>{{ item.total_price }} 元</strong></p>

          <button @click="removeFromCart(item.product_id)">删除</button>
        </div>
      </div>
    </div>

    <div v-else class="empty-cart">
      <p>🈳 购物车是空的</p>
    </div>

    <div v-if="cartItems.length > 0" class="total-bar">
      🧾 总价: <span>{{ totalPrice }} 元</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cartItems: [],
      totalPrice: 0,
    };
  },
  created() {
    this.fetchCart();
  },
  methods: {
    async fetchCart() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/cart/cart/", {
          method: "GET",
          credentials: "include",
        });
        const data = await response.json();
        this.cartItems = Array.isArray(data.cart) ? data.cart : [];
        this.totalPrice = data.total_price ?? 0;
      } catch (error) {
        console.error("获取购物车信息失败", error);
      }
    },
    async updateCartItem(productId, quantity) {
      if (quantity < 1) return alert("数量不能小于 1！");
      try {
        const res = await fetch(
          `http://127.0.0.1:8000/api/cart/update/${productId}/`,
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            credentials: "include",
            body: JSON.stringify({ quantity }),
          }
        );
        const data = await res.json();
        alert(data.message || "商品数量已更新");
        this.fetchCart();
      } catch {
        alert("更新商品数量失败，请稍后再试！");
      }
    },
    async removeFromCart(productId) {
      if (!productId) return alert("商品 ID 不存在！");
      try {
        const res = await fetch(
          `http://127.0.0.1:8000/api/cart/remove/${productId}/`,
          {
            method: "POST",
            credentials: "include",
          }
        );
        const data = await res.json();
        alert(data.message || "商品已移除");
        this.fetchCart();
      } catch {
        alert("删除失败，请稍后再试！");
      }
    },
  },
};
</script>

<style scoped>
.cart-page {
  max-width: 1000px;
  margin: 50px auto;
  padding: 30px;
  background: #fdfdfd;
  border-radius: 16px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.05);
  font-family: 'Segoe UI', sans-serif;
}

.cart-page h2 {
  font-size: 32px;
  color: #222;
  text-align: center;
  margin-bottom: 40px;
}

.cart-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

.cart-item {
  background: white;
  border-radius: 14px;
  padding: 20px;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.06);
  transition: transform 0.2s ease;
}

.cart-item:hover {
  transform: translateY(-4px);
}

.item-title {
  font-size: 20px;
  margin-bottom: 12px;
  color: #333;
}

.item-quantity {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

input[type="number"] {
  width: 60px;
  padding: 6px 8px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
  box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
}

.price {
  font-size: 16px;
  color: #555;
  margin-bottom: 16px;
}

button {
  background-color: #ff4d4f;
  color: white;
  border: none;
  padding: 6px 14px;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

button:hover {
  background-color: #d9363e;
}

.empty-cart {
  text-align: center;
  font-size: 18px;
  color: #888;
}

.total-bar {
  margin-top: 40px;
  padding: 20px;
  background: #fff6f0;
  border-radius: 12px;
  font-size: 20px;
  color: #333;
  font-weight: bold;
  text-align: right;
}

.total-bar span {
  color: #fa541c;
}
</style>
