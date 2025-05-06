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
  margin: 30px auto;
  padding: 30px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.avatar-container {
  margin-bottom: 20px;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 3px solid #ececec;
  object-fit: cover;
  transition: transform 0.3s ease-in-out;
}

.avatar:hover {
  transform: scale(1.05);
}

h1.username {
  font-size: 30px;
  font-weight: 600;
  margin-bottom: 15px;
  color: #2d3748;
}

.info-group {
  margin-bottom: 20px;
  text-align: left;
  font-size: 18px;
}

label {
  font-weight: 600;
  margin-bottom: 5px;
  color: #555;
}

p {
  font-size: 16px;
  color: #888;
}

@media (max-width: 768px) {
  .profile-display {
    padding: 20px;
  }

  h1.username {
    font-size: 26px;
  }

  .info-group {
    font-size: 14px;
  }

  .avatar {
    width: 100px;
    height: 100px;
  }
}
</style>
