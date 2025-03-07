// AppNavbar.vue - 导航栏组件，提供“精选”和“社区”选项
<template>
  <div class="navbar">
    <ul>
      <!-- 选中时加上 active 类名，并监听点击事件 -->
      <li :class="{ active: selected === 'featured' }" @click="select('featured')">精选</li>
      <li :class="{ active: selected === 'community' }" @click="select('community')">社区</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "AppNavbar",
  data() {
    return {
      selected: "featured", // 默认选中“精选”
    };
  },
  methods: {
    select(option) {
      this.selected = option; // 更新内部选中状态
      this.$emit("update:selected", option); // 触发事件，通知父组件
    },
  },
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
