// AppNavbar.vue - 导航栏组件，提供“精选”和“社区”选项
<template>
  <div class="navbar">
    <ul>
      <!-- 选中时加上 active 类名，并监听点击事件 -->
      <li :class="{ active: selected === 'featured' }" @click="select('featured')">精选</li>
      <li :class="{ active: selected === 'community' }" @click="select('community')">社区</li>
      <li :class="{ active: selected === 'login' }" @click="select('login')">登录</li>
    </ul>
  </div>
</template>


<script>
export default {
  name: "AppNavbar",
  props: ["selected"],  // 通过 props 接收父组件的 selected 值
  methods: {
    select(option) {
      this.$emit("update:selected", option);  // 触发事件通知父组件更新 selected
    }
  }
};
</script>

<style scoped>
.navbar ul {
  list-style-type: none;
  display: flex;
  justify-content: space-around;
}

.navbar li {
  cursor: pointer;
  padding: 10px;
}

.navbar .active {
  font-weight: bold;
  color: #42b983;
}
</style>


