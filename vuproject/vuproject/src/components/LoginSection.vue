<!-- 2025-3-12: 登录弹窗
      2025-3-13: 登录弹窗
  -->
<template>
  <div v-if="isVisible" class="popup-overlay">
    <div class="popup">
      <button class="close-btn" @click="closePopup">×</button>
      <div class="header">
        <h2>{{ isRegister ? "欢迎注册" : "欢迎登录" }}</h2>
        <div class="divider"></div>
      </div>
      
      <div class="form-group">
        <input 
          v-model="username" 
          type="text" 
          placeholder="用户名"
          class="custom-input"
        >
        <input 
          v-model="password" 
          type="password" 
          placeholder="密码"
          class="custom-input"
        >
      </div>

      <button 
        @click="submit" 
        class="submit-btn"
        :disabled="processing"
      >
        <span v-if="!processing">{{ isRegister ? "立即注册" : "立即登录" }}</span>
        <div v-else class="loader"></div>
      </button>

      <p class="toggle-text" @click="isRegister = !isRegister">
        {{ isRegister ? "已有账号？马上登录" : "没有账号？快速注册" }}
      </p>
    </div>
  </div>
</template>



<script>
export default {

  props: ['isVisible'],
  data() {
    return {
      isRegister: false, // 控制是注册还是登录
      username: "", // 用户名
      password: "", // 密码
      processing: false // 防止重复提交
    };
  },
  methods: {
    closePopup() {
      this.$emit('close');
    },
    async submit() {
      this.processing = true;
      try {
        const url = this.isRegister 
          ? "http://127.0.0.1:8000/api/person/register/" 
          : "http://127.0.0.1:8000/api/person/login/";

          const response = await fetch(url, {
              method: "POST",
             headers: { "Content-Type": "application/json" },
              credentials: "include",  // 关键：让浏览器携带 cookie
              body: JSON.stringify({ 
               name: this.username, 
             password: this.password 
  }),
});

        const data = await response.json();
        
        if (response.ok) {
          this.$store.dispatch("checkLoginStatus");
          alert(data.message || "操作成功！");
          this.$emit('success');
        } else {
          alert(data.error || data.message || "操作失败，请重试");
        }
      } catch (error) {
        alert("网络请求失败");
      } finally {
        this.processing = false;
      }
    }
  }
};
</script>


<style scoped>
/* 基础样式 */
:root {
  --primary-color: #409EFF;
  --success-color: #67C23A;
  --danger-color: #F56C6C;
  --text-color: #606266;
}

.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
  backdrop-filter: blur(2px);
}

.popup {
  background: white;
  padding: 40px 30px 30px;
  border-radius: 12px;
  width: 380px;
  position: relative;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  animation: slideIn 0.3s ease-out;
}

.header {
  text-align: center;
  margin-bottom: 30px;
}

h2 {
  color: var(--text-color);
  font-size: 24px;
  margin-bottom: 15px;
}

.divider {
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--primary-color), transparent);
  margin: 0 auto;
  width: 80%;
}

/* 输入框样式 */
.form-group {
  margin: 25px 25px;
}

.custom-input {
  width: 100%;
  padding: 12px 15px;
  margin: 10px 0;
  border: 1px solid #DCDFE6;
  border-radius: 6px;
  transition: all 0.3s;
  font-size: 14px;
}

.custom-input:focus {
  border-color: var(--primary-color);
  box-shadow: 0 0 8px rgba(64, 158, 255, 0.2);
}

/* 按钮样式 */
.submit-btn {
  width: 100%;
  padding: 12px;
  background: var(--primary-color);
  color: rgba(9, 10, 10, 0.902);
  border: none;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s;
}

.submit-btn:hover {
  opacity: 0.9;
  transform: translateY(-1px);
}

.submit-btn:disabled {
  background: #c0c4cc;
  cursor: not-allowed;
}

/* 关闭按钮 */
.close-btn {
  position: absolute;
  top: 15px;
  right: 15px;
  background: none;
  border: none;
  font-size: 24px;
  color: var(--text-color);
  cursor: pointer;
  transition: all 0.3s;
  padding: 5px;
  line-height: 1;
}

.close-btn:hover {
  color: var(--danger-color);
  transform: rotate(90deg);
}

/* 切换文字 */
.toggle-text {
  color: var(--text-color);
  font-size: 14px;
  margin-top: 20px;
  cursor: pointer;
  transition: all 0.3s;
}

.toggle-text:hover {
  color: var(--primary-color);
  text-decoration: underline;
}

/* 加载动画 */
.loader {
  width: 20px;
  height: 20px;
  margin: 0 auto;
  border: 3px solid #f3f3f3;
  border-top: 3px solid var(--primary-color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes slideIn {
  from { transform: translateY(-20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

@media (max-width: 480px) {
  .popup {
    width: 90%;
    padding: 30px 20px;
  }
}
</style>