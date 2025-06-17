<template>
  <div class="dashboard">
    <!-- 左侧导航栏 -->
    <nav class="sidebar">
      <router-link to="/dashboard/home">我的</router-link>

      <!-- 交易管理折叠项 -->
      <el-collapse v-model="activeNames">
        <el-collapse-item title="交易管理" name="1">
          <router-link to="/dashboard/favorites">我的收藏</router-link>
          <router-link to="/dashboard/orders">商城订单</router-link>
        </el-collapse-item>
      </el-collapse>

      <router-link to="/dashboard/ordershistory">历史订单</router-link>
      <router-link to="/dashboard/messages">消息管理</router-link>
      <router-link to="/dashboard/settings">个人设置</router-link>
    </nav>

    <!-- 右侧内容区域 -->
    <main class="content">
      <router-view /> <!-- 这里会显示子页面内容 -->
    </main>
  </div>
</template>

<script>
export default {
  name: "ProfileSection",
  data() {
    return {
      activeNames: [], // 控制折叠面板展开/收起
    };
  },
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
/* 确保整个折叠面板背景一致 */
:deep(.el-collapse) {
  background: #333 !important;
  border: none !important;
}

/* 确保折叠项的标题背景、边框一致 */
:deep(.el-collapse-item__header) {
  background: #333 !important;
  color: white !important;
  border: none !important;
  padding: 10px;
}

/* 确保折叠内容区域背景一致 */
:deep(.el-collapse-item__wrap) {
  background: #333 !important;
  border: none !important;
}

/* 确保折叠内容本身没有边框 */
:deep(.el-collapse-item__content) {
  background: #333 !important;
  color: white !important;
  padding-left: 20px;
  border: none !important;
}

/* 移除可能导致边框的默认阴影或轮廓 */
:deep(.el-collapse-item) {
  border: none !important;
  box-shadow: none !important;
}

/* 鼠标悬停时的样式 */
:deep(.el-collapse-item__header:hover) {
  background: #17afcd !important;
}



/* 让折叠标题和导航栏的字体一致 */
:deep(.el-collapse-item__header) {
  font-size: 16px !important;  /* 确保字体大小一致 */
  font-family: inherit !important; /* 继承父级字体 */
  color: white !important; /* 颜色和导航栏一致 */
  font-weight: normal !important; /* 确保不是加粗的 */
  padding: 10px;
}

/* 让折叠内容的字体也一致 */
:deep(.el-collapse-item__content) {
  font-size: 16px !important;
  font-family: inherit !important;
  color: white !important;
}
/* 解决折叠标题点击后出现的蓝色边框问题 */
:deep(.el-collapse-item__header:focus),
:deep(.el-collapse-item__header:focus-visible) {
  outline: none !important;
  box-shadow: none !important;
}
</style>
