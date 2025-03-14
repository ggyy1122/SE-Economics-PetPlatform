// AppNavbar.vue - 导航栏组件，提供“精选”和“社区”选项

<template>
  <div class="navbar">
    <ul>
      <!-- 选中时加上 active 类名，并监听点击事件 -->
      <li :class="{ active: selected === 'featured' }" @click="select('featured')">精选</li>
      <li :class="{ active: selected === 'community' }" @click="select('community')">社区</li>
      <!-- 根据 isLoggedIn 来显示“我的”或“登录”按钮 -->
      <li :class="{ active: selected === 'profile' }" v-if="isLoggedIn" @click="select('profile')">我的</li>
      <li :class="{ active: selected === 'login' }" v-else @click="select('login')">登录</li>
    </ul>
  </div>
</template>


<script>
import { mapState } from "vuex";
export default {
  name: "AppNavbar",
  props: ["selected"],  // 通过 props 接收父组件的 selected 值
  computed: {
    ...mapState(['isLoggedIn']),  // 获取 Vuex 中的登录状态
 
  },
  watch: {
    isLoggedIn(newVal) {
      console.log("isLoggedIn 变化了:", newVal);
      this.$forceUpdate(); // 强制组件刷新
    },
  },
  methods: {
    select(option) {
      this.$emit("update:selected", option);  // 触发事件通知父组件更新 selected
    },
  },
  mounted() {
    // 在组件加载时，检查用户登录状态
    this.$store.dispatch('checkLoginStatus');
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


