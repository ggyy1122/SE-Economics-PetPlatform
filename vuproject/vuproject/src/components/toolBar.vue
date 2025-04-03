<template>
    <div class="nav-bar">
      <div class="nav-content">
        <span class="city">
          <span class="location-icon">📍</span>
          {{ currentCity }}
        </span>
        <button class="nav-btn" :class="{ active: activeTab === 'mall' }" @click="activeTab = 'mall'">商城</button>
        <button class="nav-btn" :class="{ active: activeTab === 'community' }" @click="activeTab = 'community'">社区</button>
        <div class="spacer"></div>
        <button class="nav-btn">登录</button>
        <button class="nav-btn">注册</button>
        <button class="nav-btn">我的</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const currentCity = "上海市";
  const activeTab = ref('mall');
  </script>
  
  <style scoped> /* 确保样式仅作用于当前组件 */
  .nav-bar {
    width: 100%;
    height: 36.67px; /* 直接使用像素单位 */
    background: white;
    border-bottom: 1px solid #f0f0f0;
    font-size: 13px; /* 设置基准字体（不影响外部） */
  }
  
  .nav-content {
    width: 1190px;
    height: 100%;
    margin: 0 auto;
    display: flex;
    align-items: center;
    padding: 0 15px;
    box-sizing: border-box;
  }
  
  .city {
    margin-right: 30px;
    display: flex;
    align-items: center;
  }
  
  .location-icon {
    margin-right: 5px;
    font-size: 12px; /* 图标略小于文字 */
  }
  
  .nav-btn {
    margin: 0 10px;
    background: transparent;
    border: none;
    padding: 0;
    color: #333;
    cursor: pointer;
    font-size: 13px; /* 显式声明字体大小 */
  }
  
  .nav-btn.active {
    color: #1890ff;
    position: relative;
  }
  .nav-btn.active::after {
    content: '';
    position: absolute;
    bottom: -1px;
    left: 0;
    width: 100%;
    height: 2px;
    background: #1890ff;
  }
  
  .spacer {
    flex-grow: 1;
  }
  
  .nav-btn:hover {
    color: #1890ff;
  }
  </style>