<template>
  <div class="navbar">
    <div class="nav-left">
      <span class="city">
        <span class="location-icon">📍</span>
        上海市
      </span>
      <ul>
        <li :class="{ active: selected === 'featured' }" @click="select('featured')">精选</li>
        <li :class="{ active: selected === 'community' }" @click="select('community')">社区</li>
      </ul>
    </div>

    <div class="nav-right">
      <ul>
        <li 
          :class="{ active: selected === 'profile' }" 
          v-if="isLoggedIn" 
          @click="select('profile')"
        >
          我的
        </li>
        <template v-else>
          <li :class="{ active: selected === 'login' }" @click="select('login')">登录</li>
          <li :class="{ active: selected === 'register' }" @click="select('register')">注册</li>
        </template>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "AppNavbar",
  props: ["selected"],
  computed: {
    ...mapState(["isLoggedIn"]),
  },
  methods: {
    select(option) {
      this.$emit("update:selected", option);
    },
  },
  mounted() {
    this.$store.dispatch("checkLoginStatus");
  },
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #fff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.nav-left, .nav-right {
  display: flex;
  align-items: center;
}

.city {
  margin-right: 20px;
  font-size: 16px;
  display: flex;
  align-items: center;
}

.location-icon {
  margin-right: 5px;
}

ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  margin: 0 10px;
  padding: 8px 12px;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s;
}

li:hover {
  background-color: #f5f5f5;
}

li.active {
  background-color: #409EFF;
  color: white;
}

li.active:hover {
  background-color: #3a8ee6;
}
</style>