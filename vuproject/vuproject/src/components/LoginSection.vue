<!--
  2025-3-12:  登录弹窗
  -->
<template>
    <div v-if="isVisible" class="popup-overlay">
      <div class="popup">
        <h2>{{ isRegister ? "注册" : "登录" }}</h2>
        <input v-model="username" type="text" placeholder="用户名" />
        <input v-model="password" type="password" placeholder="密码" />
        <button @click="submit">{{ isRegister ? "注册" : "登录" }}</button>
        <p @click="isRegister = !isRegister">
          {{ isRegister ? "已有账号？点击登录" : "没有账号？点击注册" }}
        </p>
        <button class="close" @click="$emit('close')">×</button> <!-- 触发关闭事件 -->
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['isVisible'], // 接收控制弹窗是否显示的状态
    data() {
      return {
        isRegister: false,
        username: "",
        password: "",
      };
    },
    methods: {
      closePopup() {
        this.$emit("close"); // 触发关闭事件
      },
      async submit() {
  const url = this.isRegister ? "http://127.0.0.1:8000/api/users/register/" : "http://127.0.0.1:8000/api/users/login/";

  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username: this.username, password: this.password }),
  });

  const data = await response.json();
  console.log(data);  // 打印返回的响应数据，查看错误信息

  if (data.success) {
    alert(this.isRegister ? "注册成功！" : "登录成功！");
    this.closePopup();
  } else {
    alert(data.message);
  }
}

    },
  };
  </script>
  
  <style scoped>
  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .popup {
    background: white;
    padding: 20px;
    border-radius: 5px;
    width: 300px;
    text-align: center;
  }
  
  input {
    display: block;
    width: 100%;
    margin: 10px 0;
    padding: 8px;
  }
  
  button {
    padding: 10px;
    margin: 10px 0;
    width: 100%;
  }
  
  .close {
    background: none;
    border: none;
    font-size: 20px;
    cursor: pointer;
  }
  </style>
  