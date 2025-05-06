<template>
  <div class="post-detail container mx-auto p-10 bg-gradient-to-r from-gray-50 to-gray-100 rounded-xl shadow-md mt-12 space-y-12">
    <!-- 标题 -->
    <h1 class="text-4xl font-semibold text-gray-900 text-center leading-tight">{{ post.title }}</h1>

    <!-- 作者信息 -->
    <div class="flex items-center justify-between text-sm text-gray-600 border-b pb-6 mb-6">
      <div class="flex items-center space-x-4">
        <span>👤 <span class="text-indigo-600 font-medium">{{ post.user }}</span></span>
        <span>🕒 发布时间：{{ formatDate(post.created_at) }}</span>
      </div>
      <div class="text-gray-500">阅读量：{{ post.view_count || 0 }}</div>
    </div>

    <!-- 图片 -->
    <div v-if="post.content?.image" class="bg-white p-8 rounded-2xl shadow-lg">
      <img :src="post.content.image" class="w-full rounded-2xl border-2 border-gray-200" alt="Post Image" />
    </div>

    <!-- 正文内容 -->
    <div class="bg-white p-8 rounded-2xl shadow-md mt-8 text-lg leading-relaxed text-gray-800 whitespace-pre-line">
      <div v-html="post.content?.text"></div>
    </div>

    <!-- 标签部分 -->
    <div v-if="post.tags?.length" class="bg-white p-8 rounded-2xl shadow-md mt-8">
      <h3 class="text-xl font-semibold text-gray-700 mb-6">📎 标签</h3>
      <div class="flex flex-wrap gap-6">
        <span
          v-for="tag in post.tags"
          :key="tag.id"
          class="bg-indigo-100 text-indigo-700 px-5 py-2 rounded-full text-sm font-medium shadow-sm hover:bg-indigo-200 transition-all"
        >
          #{{ tag.name }}
        </span>
      </div>
    </div>

    <!-- 评论区 -->
    <div class="bg-white p-8 rounded-2xl shadow-md mt-8">
      <h3 class="text-2xl font-semibold text-gray-800 mb-8">🗨️ 评论</h3>

      <!-- 评论列表 -->
      <div v-if="comments.length" class="space-y-8 mb-8">
        <div v-for="comment in comments" :key="comment.id" class="p-8 border rounded-2xl bg-gray-50 shadow-md">
          <div class="flex items-center justify-between mb-6">
            <div class="text-sm text-gray-600">👤 {{ comment.user }} ｜ 🕒 {{ formatDate(comment.created_at) }}</div>
            <button class="text-sm text-indigo-600 hover:underline transition-all">举报</button>
          </div>
          <div class="text-gray-800 whitespace-pre-line">{{ comment.text }}</div>
          <img v-if="comment.image" :src="comment.image" class="mt-6 w-60 rounded-2xl border-2 shadow-md" alt="评论图片" />
        </div>
      </div>
      <div v-else class="text-gray-500">暂无评论，快来抢沙发！</div>

      <!-- 发表评论 -->
      <div class="mt-10">
        <textarea
          v-model="newCommentText"
          placeholder="写下你的评论..."
          class="w-full p-6 border-2 rounded-2xl resize-none focus:outline-none focus:ring-2 focus:ring-indigo-500 text-gray-800 shadow-sm"
          rows="4"
        ></textarea>
        <button
          @click="submitComment"
          class="mt-6 bg-indigo-600 text-white px-8 py-3 rounded-2xl hover:bg-indigo-700 transition-all"
        >
          发布评论
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PostDetail",
  data() {
    return {
      post: {},
      comments: [],
      newCommentText: "",
    };
  },
  async mounted() {
    const id = this.$route.params.id;
    await this.fetchPost(id);
    await this.fetchComments(id);
  },
  methods: {
    async fetchPost(id) {
      try {
        const res = await axios.get(`http://127.0.0.1:8000/api/posts/${id}/`, {
          withCredentials: true,
        });
        this.post = res.data;
      } catch (error) {
        console.error("获取帖子详情失败:", error);
      }
    },

    async fetchComments(postId) {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/post_comment/post/${postId}/`
        );
        this.comments = response.data;
      } catch (error) {
        console.error("获取评论失败:", error);
      }
    },

    async submitComment() {
      if (!this.newCommentText.trim()) {
        alert("评论内容不能为空！");
        return;
      }

      try {
        const postId = this.$route.params.id;
        const response = await axios.post(
          `http://127.0.0.1:8000/api/post_comment/add/${postId}/`,
          { text: this.newCommentText },
          { withCredentials: true }
        );
        console.log("评论提交成功:", response.data);
        this.comments.push(response.data);
        this.newCommentText = "";
      } catch (error) {
        console.error("提交评论失败:", error);
        alert("提交评论失败！");
      }
    },

    formatDate(dateStr) {
      if (!dateStr) return "";
      const date = new Date(dateStr);
      return date.toLocaleDateString("zh-CN", {
        year: "numeric",
        month: "short",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
      });
    },
  },
};
</script>

<style scoped>
.post-detail {
  font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  background-color: #f9fafb;
  padding: 24px;
  border-radius: 18px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
}

/* 标题样式 */
.post-detail h1 {
  font-size: 36px;
  font-weight: 700;
  color: #2d3748;
  letter-spacing: -1px;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 4px solid #4c51bf; /* 底部添加一条蓝色边框 */
}

/* 作者信息 */
.post-detail .border-b {
  border-color: #e2e8f0;
}

/* 正文文本 */
.post-detail .text-gray-600 {
  color: #4a5568;
}

.post-detail .text-gray-800 {
  color: #2d3748;
}

.post-detail .text-gray-500 {
  color: #a0aec0;
}

/* 图片部分 */
.post-detail img {
  width: 100%;
  max-width: 400px; /* 限制最大宽度 */
  height: auto; /* 保持图片比例 */
  border-radius: 12px;
  margin-top: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

/* 评论部分 */
.post-detail .border-t {
  border-top: 2px solid #e2e8f0;
}

.post-detail .bg-gray-50 {
  background-color: #f7fafc;
}

/* 评论卡片 */
.post-detail .comment-card {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  margin-bottom: 20px;
}

.post-detail .comment-card .text-gray-600 {
  font-size: 14px;
  margin-bottom: 8px;
  color: #6b7280;
}

.post-detail .comment-card .text-gray-800 {
  color: #1a202c;
  font-size: 16px;
}

.post-detail .comment-card img {
  margin-top: 12px;
  border-radius: 8px;
  width: 100%;
  max-width: 150px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* 评论输入框 */
.post-detail textarea {
  width: 100%;
  padding: 14px;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
  font-size: 16px;
  color: #2d3748;
  background-color: #fff;
  margin-top: 20px;
  resize: none;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  transition: border-color 0.3s;
}

.post-detail textarea:focus {
  border-color: #4c51bf;
  outline: none;
}

/* 评论按钮 */
.post-detail button {
  margin-top: 12px;
  padding: 12px 24px;
  background-color: #4c51bf;
  color: white;
  font-weight: 600;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s;
}

.post-detail button:hover {
  background-color: #434190;
}

/* 标签部分 */
.post-detail .tags {
  margin-top: 20px;
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.post-detail .tags span {
  background-color: #ebf4ff;
  color: #4c51bf;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  transition: background-color 0.3s, color 0.3s;
}

.post-detail .tags span:hover {
  background-color: #4c51bf;
  color: white;
}

</style>
