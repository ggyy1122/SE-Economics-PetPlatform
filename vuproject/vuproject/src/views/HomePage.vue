<template>
  <div class="home" :style="pageStyle">
    <AppNavbar @update:selected="handleSelection" />

    <div v-if="selected === 'featured'">
      <h2>精选内容</h2>
      <div class="product-list">
        <div v-for="product in products" :key="product.id" class="product">
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
          <p>价格: ￥{{ product.price }}</p>
        </div>
      </div>
    </div>

    <div v-else>
      <h2>社区</h2>
    </div>
  </div>
</template>

<script>
import AppNavbar from "@/components/AppNavbar.vue";

export default {
  components: {
    AppNavbar,
  },
  data() {
    return {
      selected: "featured",
      products: [
        { id: 1, name: "商品A", price: 99, image: "https://via.placeholder.com/150" },
        { id: 2, name: "商品B", price: 199, image: "https://via.placeholder.com/150" },
        { id: 3, name: "商品C", price: 299, image: "https://via.placeholder.com/150" },
      ],
    };
  },
  computed: {
    pageStyle() {
      return {
        backgroundColor: this.selected === "featured" ? "lightblue" : "lightgreen",
        transition: "background-color 0.5s ease",
      };
    },
  },
  methods: {
    handleSelection(option) {
      this.selected = option;
    },
  },
};
</script>

<style scoped>
.home {
  padding: 20px;
}

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.product {
  width: 150px;
  text-align: center;
}

.product img {
  width: 100%;
  border-radius: 10px;
}
</style>
