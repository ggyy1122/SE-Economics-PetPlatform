<template>
  <div class="profile-display">
    <div class="avatar-container">
      <img
        :src="userInfo.avatar ? 'http://127.0.0.1:8000' + userInfo.avatar : defaultAvatar"
        alt="用户头像"
        class="avatar"
      />
    </div>

    <h1 class="username">{{ userInfo.name || '用户名' }}</h1>

    <div class="info-group">
      <label>邮箱</label>
      <p>{{ userInfo.email || '未设置' }}</p>
    </div>

    <div class="info-group">
      <label>电话</label>
      <p>{{ userInfo.phone || '未设置' }}</p>
    </div>

    <div class="info-group">
      <label>性别</label>
      <p>{{ userInfo.gender === 'male' ? '男' : userInfo.gender === 'female' ? '女' : '其他' }}</p>
    </div>

    <div class="info-group">
      <label>生日</label>
      <p>{{ userInfo.birthday || '未设置' }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      userInfo: {
        name: "",
        email: "",
        phone: "",
        gender: "male",
        birthday: "",
        avatar: null,
      },
      defaultAvatar: "http://127.0.0.1:8000/static/default-avatar.jpg", // 默认头像路径
    };
  },
  mounted() {
    this.loadUserInfo();
  },
  methods: {
    async loadUserInfo() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/person/user/", {
          withCredentials: true,
        });
        this.userInfo = res.data || {};
      } catch (err) {
        console.error("加载用户信息失败", err);
      }
    },
  },
};
</script>

<style scoped>
.profile-display {
  max-width: 600px;
  margin: 0 auto;
  padding: 30px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.avatar-container {
  margin-bottom: 20px;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 2px solid #ddd;
  object-fit: cover;
}

h1.username {
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 15px;
  color: #333;
}

.info-group {
  margin-bottom: 15px;
  text-align: left;
  font-size: 16px;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
  color: #555;
}

p {
  font-size: 16px;
  color: #777;
}
</style>
