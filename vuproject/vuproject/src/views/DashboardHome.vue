<!-- src/views/DashboardHome.vue -->
<template>
    <div class="profile">
      <h2>我的</h2>
      <p>欢迎, {{ username }}</p>
      <button @click="logout">退出登录</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: "用户", // 这里可以从后端获取
      };
    },
    methods: {
      logout() {
        fetch("http://127.0.0.1:8000/api/person/logout/", {
          method: "POST",
          credentials: "include",
        })
          .then(() => {
            alert("退出成功");
            window.location.href = "/";
            this.$store.dispatch("checkLoginStatus");
          })
          .catch(error => console.error("退出失败", error));
      }
    }
  };
  </script>
  
  <style scoped>
  .profile {
    padding: 20px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  button {
    background: red;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
  }
  </style>
  