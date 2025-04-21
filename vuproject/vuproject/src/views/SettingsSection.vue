<template>
  <div class="profile-update">
    <h1>修改个人信息</h1>

    <div class="form-group">
      <label>用户名</label>
      <input
        v-model="form.name"
        type="text"
        placeholder="请输入用户名"
      />
    </div>

    <div class="form-group">
      <label>邮箱</label>
      <input
        v-model="form.email"
        type="email"
        placeholder="请输入邮箱，如 example@domain.com"
      />
      <p
        v-if="emailError"
        class="error-msg"
      >{{ emailError }}</p>
    </div>

    <div class="form-group">
      <label>电话</label>
      <input
        v-model="form.phone"
        type="text"
        placeholder="请输入手机号，如 13812345678"
      />
      <p
        v-if="phoneError"
        class="error-msg"
      >{{ phoneError }}</p>
    </div>

    <div class="form-group">
      <label>性别</label>
      <select v-model="form.gender">
        <option value="male">男</option>
        <option value="female">女</option>
        <option value="other">其他</option>
      </select>
    </div>

    <div class="form-group">
      <label>生日</label>
      <input
        v-model="form.birthday"
        type="date"
        placeholder="请选择生日"
      />
    </div>

    <div class="form-group">
      <label>头像</label>
      <input
        type="file"
        accept="image/*"
        @change="handleAvatarUpload"
      />
      <div
        v-if="preview"
        class="avatar-preview"
      >
        <img
          :src="preview"
          alt="预览头像"
        />
      </div>
    </div>

    <div class="form-group button-group">
      <button @click="submitUpdate">提交修改</button>
    </div>

    <div class="form-group button-group">
      <button
        class="logout"
        @click="logout"
      >退出登录</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        name: "",
        email: "",
        phone: "",
        gender: "male", // 默认性别
        birthday: "", // 新增生日字段
      },
      avatarFile: null,
      preview: null,
      emailError: "",
      phoneError: "",
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
        this.form = {
          name: res.data.name || "",
          email: res.data.email || "",
          phone: res.data.phone || "",
          gender: res.data.gender || "male", // 加载性别字段
          birthday: res.data.birthday || "", // 加载生日字段
        };
        // 检查是否有头像返回，并设置头像的显示
        this.preview = res.data.avatar
          ? `http://127.0.0.1:8000${res.data.avatar}`
          : null;
      } catch (err) {
        console.error("加载用户信息失败", err);
      }
    },
    handleAvatarUpload(event) {
      this.avatarFile = event.target.files[0];
      if (this.avatarFile) {
        this.preview = URL.createObjectURL(this.avatarFile);
      }
    },
    validateEmail(email) {
      const regex = /^[\w.-]+@[a-zA-Z\d.-]+\.[a-zA-Z]{2,}$/;
      return regex.test(email);
    },
    validatePhone(phone) {
      const regex = /^1[3-9]\d{9}$/;
      return regex.test(phone);
    },
    async submitUpdate() {
      this.emailError = "";
      this.phoneError = "";

      if (!this.validateEmail(this.form.email)) {
        this.emailError = "请输入有效的邮箱地址，如 example@domain.com";
        return;
      }

      if (!this.validatePhone(this.form.phone)) {
        this.phoneError = "请输入正确的手机号格式，如 13812345678";
        return;
      }

      const formData = new FormData();
      formData.append("name", this.form.name);
      formData.append("email", this.form.email);
      formData.append("phone", this.form.phone);
      formData.append("gender", this.form.gender); // 提交性别
      formData.append("birthday", this.form.birthday); // 提交生日
      if (this.avatarFile) {
        formData.append("avatar", this.avatarFile);
      }

      try {
        await axios.post(
          "http://127.0.0.1:8000/api/person/user/update/",
          formData,
          {
            withCredentials: true,
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
        alert("信息更新成功！");
        this.loadUserInfo(); // 更新头像信息
      } catch (error) {
        console.error("更新失败", error);
        if (error.response?.data) {
          let msg = "更新失败：";
          for (const key in error.response.data) {
            msg += `\n${key}: ${error.response.data[key]}`;
          }
          alert(msg);
        } else {
          alert("更新失败，请检查网络或重试");
        }
      }
    },
    logout() {
      fetch("http://127.0.0.1:8000/api/person/logout/", {
        method: "POST",
        credentials: "include",
      })
        .then(() => {
          alert("退出成功");
          window.location.href = "/";
        })
        .catch((error) => console.error("退出失败", error));
    },
  },
};
</script>

<style scoped>
.profile-update {
  max-width: 600px;
  margin: auto;
  padding: 30px;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 20px;
}

input,
select {
  width: 100%;
  padding: 10px;
  border: 1px solid #bbb;
  border-radius: 5px;
  font-size: 16px;
}

button {
  padding: 12px 20px;
  background-color: #007bff;
  border: none;
  color: white;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.error-msg {
  color: red;
  font-size: 14px;
  margin-top: 5px;
}

.avatar-preview img {
  max-width: 100px;
  max-height: 100px;
  margin-top: 10px;
  border-radius: 8px;
}
</style>

  