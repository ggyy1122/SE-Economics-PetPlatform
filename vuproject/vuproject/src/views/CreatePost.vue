<template>
  <div class="create-post">
    <div class="post-form">
      <h1>创建帖子</h1>

      <div class="form-group">
        <label for="title">标题</label>
        <input
          v-model="title"
          id="title"
          type="text"
          placeholder="请输入标题"
        />
      </div>

      <div class="form-group">
        <label for="text">内容</label>
        <textarea
          v-model="text"
          id="text"
          rows="6"
          placeholder="请输入内容"
        ></textarea>
      </div>

      <div class="form-group">
        <label for="tags">标签</label>
        <select
          v-model="selectedTags"
          multiple
        >
          <option
            v-for="tag in tags"
            :key="tag.id"
            :value="tag.id"
          >{{ tag.name }}</option>
        </select>
      </div>

      <div class="form-group">
        <label>图片（可选）</label>
        <input
          type="file"
          @change="handleImageUpload"
        />
      </div>

      <div class="form-group">
        <label>视频（可选）</label>
        <input
          type="file"
          @change="handleVideoUpload"
        />
      </div>

      <div class="form-group">
        <button @click="submitPost">提交帖子</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      title: "",
      text: "",
      selectedTags: [],
      imageFile: null,
      videoFile: null,
      tags: [],
    };
  },
  mounted() {
    this.fetchTags();
  },
  methods: {
    async fetchTags() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/posts/tags/");
        this.tags = res.data;
      } catch (err) {
        console.error("获取标签失败：", err);
      }
    },
    handleImageUpload(event) {
      this.imageFile = event.target.files[0];
    },
    handleVideoUpload(event) {
      this.videoFile = event.target.files[0];
    },
    async submitPost() {
      if (!this.title && !this.text) {
        alert("标题和内容不能全部为空！");
        return;
      }

      const formData = new FormData();
      formData.append("title", this.title);
      formData.append("text", this.text);

      this.selectedTags.forEach((tagId) => {
        formData.append("tags", tagId);
      });

      if (this.imageFile) {
        formData.append("image", this.imageFile);
      }

      if (this.videoFile) {
        formData.append("video", this.videoFile);
      }

      try {
        await axios.post("http://127.0.0.1:8000/api/posts/create/", formData, {
          withCredentials: true,
        });
        alert("帖子提交成功！");
        this.$router.push("/community"); // 成功后跳转回社区页
      } catch (error) {
        console.error("提交帖子失败：", error);
        if (error.response?.data?.error) {
          alert("提交失败：" + error.response.data.error);
        } else {
          alert("提交失败，请检查是否已登录或数据是否完整！");
        }
      }
    },
  },
};
</script>

<style scoped>
.create-post {
  padding: 30px;
  max-width: 700px;
  margin: auto;
}

.post-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group label {
  font-weight: bold;
}

input,
textarea,
select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  padding: 12px;
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
</style>
