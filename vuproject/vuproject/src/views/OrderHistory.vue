<template>
  <div class="order-history">
    <h2>历史订单</h2>

    <div v-if="loading" class="loading">订单加载中...</div>
    <div v-else>
      <div v-if="error" class="error">{{ error }}</div>
      <div v-else>
        <div v-if="orders.length === 0" class="empty">暂无订单</div>
        <ul v-else class="order-list">
          <li v-for="order in orders" :key="order.out_trade_no" class="order-item">
            <div class="order-info">
              <div><strong>订单号：</strong>{{ order.out_trade_no }}</div>
              <div><strong>金额：</strong>￥{{ order.amount.toFixed(2) }}</div>
              <div><strong>创建时间：</strong>{{ formatTime(order.created_at) }}</div>
            </div>
            <div class="order-items">
              <strong>商品列表：</strong>
              <ul>
                <li v-for="(item, index) in order.items" :key="index">
                  {{ item.product_name }} × {{ item.quantity }}
                </li>
              </ul>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const orders = ref([])
const loading = ref(false)
const error = ref("")

function formatTime(datetime) {
  const date = new Date(datetime)
  return date.toLocaleString("zh-CN", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit"
  }).replace(/\//g, '-')
}

async function fetchOrders() {
  loading.value = true
  error.value = ""
  try {
    const res = await fetch("http://127.0.0.1:8000/api/order/orders/user/", {
      method: "GET",
      credentials: "include",
    })
    if (!res.ok) {
      if (res.status === 401) {
        error.value = "用户未登录，请先登录"
      } else {
        error.value = `请求失败，状态码：${res.status}`
      }
      orders.value = []
      return
    }
    const data = await res.json()
    orders.value = data.orders || []
  } catch (e) {
    error.value = "订单获取失败，请稍后重试"
    console.error(e)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchOrders()
})
</script>

<style scoped>
.order-history {
  max-width: 700px;
  margin: 20px auto;
  font-family: Arial, sans-serif;
}

.loading, .error, .empty {
  text-align: center;
  margin: 20px 0;
  font-size: 16px;
  color: #666;
}
.error {
  color: red;
}

.order-list {
  list-style: none;
  padding: 0;
}

.order-item {
  border: 1px solid #e0e0e0;
  padding: 16px 20px;
  margin-bottom: 16px;
  border-radius: 10px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.order-info {
  display: grid;
  grid-template-columns: 1fr 1fr;
  row-gap: 8px;
  margin-bottom: 10px;
}

.order-info div:nth-child(3) {
  grid-column: span 2;
}

.order-items {
  background: #f5f5f5;
  padding: 10px;
  border-radius: 6px;
}
.order-items ul {
  margin: 6px 0 0 0;
  padding-left: 20px;
}
</style>
