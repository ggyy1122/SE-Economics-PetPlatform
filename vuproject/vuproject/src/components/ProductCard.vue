<template>
    <div class="product" @click="openProductPage(product.id)">
      <img :src="product.image" :alt="product.name" />
      <h3>{{ product.name }}</h3>
      <p class="price">价格: ￥{{ product.price }}</p>
      <div class="info-line">
        <span class="stock">库存: {{ product.stock }}</span>
        <!-- 如果收藏数大于0，显示收藏数 -->
        <span v-if="product.favorite_count > 0" class="favorites">❤️ 收藏: {{ formattedFavoriteCount }}</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      product: {
        type: Object,
        default: () => ({
          stock: 0,
          favorite_count: 0,  // 确保给出默认值
        }),
      },
    },
    computed: {
      formattedFavoriteCount() {
        const count = this.product.favorite_count;
        if (count >= 10000) {
          return Math.floor(count / 1000) + '万+';
        } else if (count >= 1000) {
          return count + '+';
        } else {
          return count;
        }
      },
    },
    methods: {
      openProductPage(productId) {
        window.open(`/product/${productId}`, "_blank");
      },
    },
  };
  </script>
  
  <style scoped>
  .product {
    width: 200px;
    height: 320px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 15px;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    cursor: pointer;
  }
  
  .product:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  }
  
  .product img {
    width: 100%;
    height: 160px;
    object-fit: cover;
    border-radius: 10px;
  }
  
  .product h3 {
    font-size: 1.1em;
    margin: 8px 0;
    color: #333;
    height: 2.6em;
    overflow: hidden;
  }
  
  .product .price {
    font-size: 1em;
    font-weight: bold;
    color: #f60;
    margin-bottom: 8px;
  }
  
  .info-line {
    display: flex;
    justify-content: space-between;
    font-size: 0.9em;
    color: #888;
  }
  </style>
  