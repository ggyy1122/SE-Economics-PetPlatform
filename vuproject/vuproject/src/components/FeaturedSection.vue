<template>
  <div>
    <!-- 火爆商品区域 (保持不变) -->
    <!-- 商品标题和按钮一行 -->
    <div
  style="display: flex; align-items: center; margin-bottom: 10px;"
>
<h2 style="margin: 0; padding: 0; border: none;">🔥 火爆商品</h2>
  <div style="flex-grow: 1;"></div> <!-- 占位让按钮往右 -->
  <button
    @click="goToAllCategory"
    style="margin-right: 40px; padding: 8px 16px; background-color: #F95D0F; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 14px;"
  >
    🛒 进入商城
  </button>
</div>


    <div class="product-list">
      <div v-for="product in hotProducts" :key="product.id" class="product">
        <div @click="openProductPage(product.id)" style="cursor: pointer">
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
        </div>
        <p class="price">价格: ￥{{ product.price }}</p>
        <p class="stock">库存: {{ product.stock }}</p>
      </div>
    </div>

    <!-- 修改后的狗狗商品区域 -->
<div
  style="display: flex; align-items: center; margin-bottom: 10px;"
><h2 style="margin: 0; padding: 0; border: none;">🐶 狗狗商品</h2>
  <div style="flex-grow: 1;"></div> <!-- 占位让按钮往右 -->
  <button
    @click="goToDogCategory"
    style="margin-right: 40px; padding: 8px 16px; background-color: #F95D0F; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 14px;"
  >
    🛒 狗狗商城
  </button>
</div>
<div class="dog-category-nav">
  <div 
    v-for="category in dogCategories" 
    :key="category.value"
    class="nav-item"
    :class="{ active: activeDogCategory === category.value }"
    @mouseenter="filterDogProducts(category.value)"
  >
    {{ category.label }}
  </div>
</div>
<div class="product-list">
  <div v-for="product in filteredDogProducts.slice(0, 12)" :key="product.id" class="product">
    <div @click="openProductPage(product.id)" style="cursor: pointer">
      <img :src="product.image" :alt="product.name" />
      <h3>{{ product.name }}</h3>
    </div>
    <p class="price">价格: ￥{{ product.price }}</p>
    <p class="stock">库存: {{ product.stock }}</p>
  </div>
</div>


    <!-- 以下所有其他区域保持不变 -->
    <h2>🐱 猫猫商品</h2>
    <div class="product-list">
      <div v-for="product in catProducts" :key="product.id" class="product">
        <div @click="openProductPage(product.id)" style="cursor: pointer">
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
        </div>
        <p class="price">价格: ￥{{ product.price }}</p>
        <p class="stock">库存: {{ product.stock }}</p>
      </div>
    </div>

    <h2>🐹 小宠商品</h2>
    <div class="product-list">
      <div v-for="product in smallPetProducts" :key="product.id" class="product">
        <div @click="openProductPage(product.id)" style="cursor: pointer">
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
        </div>
        <p class="price">价格: ￥{{ product.price }}</p>
        <p class="stock">库存: {{ product.stock }}</p>
      </div>
    </div>

    <h2>🐠 水族商品</h2>
    <div class="product-list">
      <div v-for="product in aquariumProducts" :key="product.id" class="product">
        <div @click="openProductPage(product.id)" style="cursor: pointer">
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
        </div>
        <p class="price">价格: ￥{{ product.price }}</p>
        <p class="stock">库存: {{ product.stock }}</p>
      </div>
    </div>

    <h2>🦎 爬虫商品</h2>
    <div class="product-list">
      <div v-for="product in reptileProducts" :key="product.id" class="product">
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
      hotProducts: [],
      dogProducts: [], // 存储所有狗狗商品
      filteredDogProducts: [], // 存储筛选后的狗狗商品
      catProducts: [],
      smallPetProducts: [],
      aquariumProducts: [],
      reptileProducts: [],
      activeDogCategory: null, // 当前激活的狗狗分类
      dogCategories: [ // 狗狗分类导航选项
        { label: '主粮', value: '主粮' },
        { label: '零食', value: '零食' },
        { label: '玩具', value: '玩具' }
      ]
    };
  },
  mounted() {
    this.fetchAllProducts();
  },
  methods: {
    goToAllCategory() {
      window.open(this.$router.resolve({ name: 'all' }).href, '_blank');
    },
    goToDogCategory(){
      window.open(this.$router.resolve({ name: 'dog' }).href, '_blank');
    },
    async fetchAllProducts() {
      try {
        // 火爆商品
        const hotRes = await axios.get("http://127.0.0.1:8000/api/products/?limit=12");
        this.hotProducts = hotRes.data.results || [];
        
        // 狗狗商品 - 获取所有狗狗商品
        const dogRes = await axios.get("http://127.0.0.1:8000/api/products/?animals__name=狗");
        this.dogProducts = dogRes.data.results || [];
        this.filteredDogProducts = this.dogProducts; // 初始显示全部
        
        // 其他商品保持不变...
        const catRes = await axios.get("http://127.0.0.1:8000/api/products/?animals__name=猫");
        this.catProducts = catRes.data.results || [];
        
        this.smallPetProducts = [];
        this.aquariumProducts = [];
        this.reptileProducts = [];
        
      } catch (error) {
        console.error("❌ 获取商品失败:", error);
        // 错误处理保持不变...
      }
    },
    
    // 新增方法：筛选狗狗商品
    async filterDogProducts(category) {
      this.activeDogCategory = category;
      try {
        const res = await axios.get(`http://127.0.0.1:8000/api/products/?animals__name=狗&categories__name=${category}`);
        this.filteredDogProducts = res.data.results || [];
      } catch (error) {
        console.error("筛选狗狗商品失败:", error);
        this.filteredDogProducts = [];
      }
    },
    
    openProductPage(productId) {
      window.open(`/product/${productId}`, "_blank");
    }
  }
};
</script>

<style scoped></style>

<style scoped>
.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  padding: 20px;
  min-height: 200px; /* 确保即使没有商品也有一定高度 */
}

.product {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 15px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.product:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.product img {
  width: 100%;
  height: 200px;
  object-fit: cover;
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
  color: #f60;
}

.product .stock {
  font-size: 0.9em;
  color: #888;
}

h2 {
  margin-top: 30px;
  margin-bottom: 15px;
  padding-left: 20px;
  font-size: 1.5em;
  color: #333;
  border-bottom: 2px solid #eee;
  padding-bottom: 10px;
}

/* 空状态提示 */
.product-list:empty::before {
  content: "暂无商品，敬请期待";
  display: block;
  text-align: center;
  color: #999;
  padding: 50px 0;
}

/* 原有样式全部保留，只新增以下样式 */

.dog-category-nav {
  display: flex;
  gap: 15px;
  padding: 0 20px 15px;
  border-bottom: 1px solid #eee;
  margin-bottom: 15px;
}

.dog-category-nav .nav-item {
  padding: 8px 15px;
  cursor: pointer;
  border-radius: 15px;
  transition: all 0.3s ease;
}

.dog-category-nav .nav-item:hover {
  background-color: #f5f5f5;
}

.dog-category-nav .nav-item.active {
  background-color: #ff6b00;
  color: white;
}
</style>