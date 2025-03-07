<template>
  <div id="app">
    <!-- 渲染 HomePage 组件 -->
    <HomePage />
  </div>
</template>

<script>
// 导入 HomePage 组件
import HomePage from "./views/HomePage.vue";

export default {
  components: {
    HomePage, // 注册 HomePage 组件
  },
};
</script>
