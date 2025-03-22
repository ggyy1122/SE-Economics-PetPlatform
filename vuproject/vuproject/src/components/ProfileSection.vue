<template>
  <div class="dashboard">
    <!-- 左侧导航栏 -->
    <nav class="sidebar">
       <!-- 添加返回首页的按钮 -->
      <router-link to="/">返回首页</router-link> <!-- 这是返回首页的链接 -->
      <router-link to="/dashboard/home">我的</router-link>
      <router-link to="/dashboard/transactions">交易管理</router-link>
      <router-link to="/dashboard/funds">资金管理</router-link>
      <router-link to="/dashboard/messages">消息管理</router-link>
      <router-link to="/dashboard/settings">个人设置</router-link>
    </nav>

    <!-- 右侧内容区域 -->
    <main class="content">
      <router-view /> 
    </main>
  </div>
</template>

<script>
export default {
  name: "ProfileSection",
  mounted() {
    this.$router.push('/dashboard/home'); // 页面加载时自动跳转到 home
  }
};

</script>

<style scoped>
.dashboard {
  display: flex;
  height: 100vh;
}

/* 左侧导航栏 */
.sidebar {
  width: 200px;
  background: #333;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.sidebar a {
  color: white;
  text-decoration: none;
  padding: 10px;
  margin: 5px 0;
  display: block;
  border-radius: 5px;
  transition: background 0.3s;
}

.sidebar a:hover {
  background: #17afcd;
}

/* 右侧内容区域 */
.content {
  flex: 1;
  padding: 20px;
  background: #f8f8f8;
}
</style>
