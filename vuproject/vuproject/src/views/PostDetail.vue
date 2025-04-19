<template>
  <div class="post-detail max-w-3xl mx-auto p-6 bg-white shadow-xl rounded-2xl mt-8 space-y-6">
    <!-- 标题 -->
    <h1 class="text-4xl font-extrabold text-gray-800">{{ post.title }}</h1>

    <!-- 作者信息 -->
    <div class="text-sm text-gray-500 border-b pb-2">
      <span class="mr-4">👤 作者：<span class="text-blue-600 font-medium">{{ post.user }}</span></span>
      <span>🕒 发布时间：{{ formatDate(post.created_at) }}</span>
    </div>

    <!-- 图片 -->
    <img
      v-if="post.content?.image"
      :src="post.content.image"
      class="w-full rounded-xl border border-gray-200 shadow-sm"
      alt="Post Image"
    />

    <!-- 正文内容 -->
    <div
      class="text-lg leading-relaxed text-gray-800 whitespace-pre-line"
      v-html="post.content?.text"
    ></div>

    <!-- 标签部分 -->
    <div
      v-if="post.tags?.length"
      class="border-t pt-4"
    >
      <h3 class="text-base font-semibold text-gray-700 mb-2">📎 标签</h3>
      <div class="flex flex-wrap gap-3">
        <span
          v-for="tag in post.tags"
          :key="tag.id"
          class="bg-blue-100 text-blue-700 px-4 py-1 rounded-full text-sm font-medium shadow-sm hover:bg-blue-200 transition"
        >
          #{{ tag.name }}
        </span>
      </div>
    </div>

    <!-- 评论区 -->
    <div class="border-t pt-6">
      <h3 class="text-xl font-semibold text-gray-800 mb-4">🗨️ 评论</h3>

      <!-- 评论列表 -->
      <div
        v-if="comments.length"
        class="space-y-4 mb-6"
      >
        <div
          v-for="comment in comments"
          :key="comment.id"
          class="p-4 border rounded-xl bg-gray-50"
        >
          <div class="text-sm text-gray-600 mb-2">
            👤 {{ comment.user }} ｜ 🕒 {{ formatDate(comment.created_at) }}
          </div>
          <div class="text-gray-800 whitespace-pre-line">{{ comment.text }}</div>
          <img
            v-if="comment.image"
            :src="comment.image"
            class="mt-2 w-40 rounded border"
            alt="评论图片"
          />
        </div>
      </div>
      <div
        v-else
        class="text-gray-500"
      >暂无评论，快来抢沙发！</div>

      <!-- 发表评论 -->
      <div class="mt-6">
        <textarea
          v-model="newCommentText"
          placeholder="写下你的评论..."
          class="w-full p-3 border rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
          rows="3"
        ></textarea>
        <button
          @click="submitComment"
          class="mt-3 bg-blue-600 text-white px-5 py-2 rounded-xl hover:bg-blue-700 transition"
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
}
</style>
