<template>
  <div>
    <!-- 火爆商品 -->
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
      <h2 style="margin: 0; padding: 0; border: none;">🔥 火爆商品</h2>
      <div style="flex-grow: 1;"></div>
      <button
        @click="goToAllCategory"
        style="margin-right: 40px; padding: 8px 16px; background-color: #F95D0F; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 14px;"
      >
        🛒 进入商城
      </button>
    </div>
    <div class="product-list">
      <ProductCard
        v-for="product in hotProducts"
        :key="product.id"
        :product="product"
      />
    </div>

    <!-- 狗狗商品 -->
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
      <h2 style="margin: 0; padding: 0; border: none;">🐶 狗狗商品</h2>
      <div style="flex-grow: 1;"></div>
      <button
        @click="goToDogCategory"
        style="margin-right: 40px; padding: 8px 16px; background-color: #F95D0F; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 14px;"
      >
        🛒 狗狗商城
      </button>
    </div>

    <!-- 狗狗分类导航 -->
    <div class="category-nav">
      <div
        v-for="category in dogCategoriesWithAll"
        :key="category.value"
        class="nav-item"
        :class="{ active: activeDogCategory === category.value }"
        @mouseenter="filterProducts('dog', category.value)"
        @click="goToCategory('dog', category.value)"
      >
        {{ category.label }}
      </div>
    </div>

    <!-- 显示狗狗商品 -->
    <div class="product-list">
      <ProductCard
        v-for="product in filteredDogProducts.slice(0, 12)"
        :key="product.id"
        :product="product"
      />
    </div>

    <!-- 猫猫商品 -->
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
      <h2 style="margin: 0; padding: 0; border: none;">🐱 猫猫商品</h2>
      <div style="flex-grow: 1;"></div>
      <button
        @click="goToCatCategory"
        style="margin-right: 40px; padding: 8px 16px; background-color: #F95D0F; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 14px;"
      >
        🛒 猫猫商城
      </button>
    </div>

    <!-- 猫猫分类导航 -->
    <div class="category-nav">
      <div
        v-for="category in catCategoriesWithAll"
        :key="category.value"
        class="nav-item"
        :class="{ active: activeCatCategory === category.value }"
        @mouseenter="filterProducts('cat', category.value)"
        @click="goToCategory('cat', category.value)"
      >
        {{ category.label }}
      </div>
    </div>

    <!-- 显示猫猫商品 -->
    <div class="product-list">
      <ProductCard
        v-for="product in filteredCatProducts.slice(0, 12)"
        :key="product.id"
        :product="product"
      />
    </div>

    <!-- 小宠商品 -->
    <h2>🐹 小宠商品</h2>
    <div class="product-list">
      <ProductCard
        v-for="product in smallPetProducts"
        :key="product.id"
        :product="product"
      />
    </div>

    <!-- 水族商品 -->
    <h2>🐠 水族商品</h2>
    <div class="product-list">
      <ProductCard
        v-for="product in aquariumProducts"
        :key="product.id"
        :product="product"
      />
    </div>

    <!-- 爬虫商品 -->
    <h2>🦎 爬虫商品</h2>
    <div class="product-list">
      <ProductCard
        v-for="product in reptileProducts"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductCard from "@/components/ProductCard.vue"; // 请根据实际路径调整

export default {
  components: {
    ProductCard
  },
  data() {
    return {
      hotProducts: [],
      dogProducts: [],
      filteredDogProducts: [],
      catProducts: [],
      filteredCatProducts: [],
      smallPetProducts: [],
      aquariumProducts: [],
      reptileProducts: [],
      activeDogCategory: null,
      activeCatCategory: null,
      dogCategories: [
        { label: "主粮", value: "主粮" },
        { label: "零食", value: "零食" },
        { label: "玩具", value: "玩具" }
      ],
      catCategories: [
      { label: "主粮", value: "主粮" },
        { label: "零食", value: "零食" },
        { label: "玩具", value: "玩具" }
      ]
    };
  },
  mounted() {
    this.fetchAllProducts();
  },
  computed: {
    // 为狗狗分类添加“全部商品”
    dogCategoriesWithAll() {
      return [{ label: "全部商品", value: "全部商品" }, ...this.dogCategories];
    },
    // 为猫猫分类添加“全部商品”
    catCategoriesWithAll() {
      return [{ label: "全部商品", value: "全部商品" }, ...this.catCategories];
    }
  },
  methods: {
    goToAllCategory() {
      window.open(this.$router.resolve({ name: "all" }).href, "_blank");
    },
    goToCategory(animalType, category = null) {
      const categoryMapping = {
        "主粮": "food",
        "零食": "snack",
        "玩具": "toy",
        "全部商品": ""  // 为空表示跳转到所有商品
      };

      const path = categoryMapping[category] || "";  // 获取对应的路径，默认为空
      const routePath = path ? `/category/${animalType}/${path}` : `/category/${animalType}`;

      window.open(this.$router.resolve({ path: routePath }).href, "_blank");
    },
    async fetchAllProducts() {
      try {
        const hotRes = await axios.get("http://127.0.0.1:8000/api/products/?limit=12");
        this.hotProducts = hotRes.data.results || [];

        const dogRes = await axios.get("http://127.0.0.1:8000/api/products/?animals__name=狗");
        this.dogProducts = dogRes.data.results || [];
        this.filteredDogProducts = this.dogProducts;

        const catRes = await axios.get("http://127.0.0.1:8000/api/products/?animals__name=猫");
        this.catProducts = catRes.data.results || [];
        this.filteredCatProducts = this.catProducts;

        const smallPetRes = await axios.get("http://127.0.0.1:8000/api/products/?animals__name=小宠");
        this.smallPetProducts = smallPetRes.data.results || [];

        const aquariumRes = await axios.get("http://127.0.0.1:8000/api/products/?animals__name=水族");
        this.aquariumProducts = aquariumRes.data.results || [];

        const reptileRes = await axios.get("http://127.0.0.1:8000/api/products/?animals__name=爬虫");
        this.reptileProducts = reptileRes.data.results || [];
      } catch (error) {
        console.error("❌ 获取商品失败:", error);
      }
    },
    async filterProducts(animalType, category) {
      if (animalType === "dog") {
        this.activeDogCategory = category;
        if (category === "全部商品") {
          this.filteredDogProducts = this.dogProducts;
        } else {
          const res = await axios.get(`http://127.0.0.1:8000/api/products/?animals__name=狗&categories__name=${category}`);
          this.filteredDogProducts = res.data.results || [];
        }
      } else if (animalType === "cat") {
        this.activeCatCategory = category;
        if (category === "全部商品") {
          this.filteredCatProducts = this.catProducts;
        } else {
          const res = await axios.get(`http://127.0.0.1:8000/api/products/?animals__name=猫&categories__name=${category}`);
          this.filteredCatProducts = res.data.results || [];
        }
      }
    }
  }
};
</script>

<style scoped>
.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  padding: 20px;
  min-height: 200px;
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

.product-list:empty::before {
  content: "暂无商品，敬请期待";
  display: block;
  text-align: center;
  color: #999;
  padding: 50px 0;
}

.category-nav {
  display: flex;
  gap: 15px;
  padding: 0 20px 15px;
  border-bottom: 1px solid #eee;
  margin-bottom: 15px;
}

.category-nav .nav-item {
  cursor: pointer;
  color: #333;
  padding: 10px;
  transition: background-color 0.3s;
}

.category-nav .nav-item:hover {
  background-color: #f0f0f0;
}

.category-nav .active {
  font-weight: bold;
  color: #f95d0f;
}
</style>
