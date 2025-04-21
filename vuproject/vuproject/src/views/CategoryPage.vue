<template>
  <div class="category-page">
    <!-- 分类导航栏 -->
    <nav class="category-nav">
      <router-link
        v-for="(item, index) in categories"
        :key="index"
        :to="item.route"
        class="nav-item"
        active-class="active"
      >
        {{ item.name }}
      </router-link>
    </nav>

    <!-- 子分类或商品展示区 -->
    <!-- ⭐️ 加了 key 属性，强制切换分类时重新加载组件 -->
    <router-view :key="$route.fullPath" />
  </div>
</template>

<script setup>
import { ref } from 'vue'

const categories = ref([
  { name: '全部商品', route: '/category/all' },
  { name: '狗狗', route: '/category/dog' },
  { name: '猫猫', route: '/category/cat' },
  { name: '小宠', route: '/category/small' },
  { name: '水族', route: '/category/aquatic' },
  { name: '爬虫', route: '/category/reptile' }
]);


</script>

<style scoped>
.category-nav {
  display: flex;
  gap: 16px;
  padding: 16px;
  background-color: #f9f9f9;
  border-bottom: 1px solid #ddd;
}

.nav-item {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.nav-item:hover {
  background-color: #eaeaea;
}

.active {
  background-color: #409EFF;
  color: white;
}
</style>
