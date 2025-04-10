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
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PostDetail",
  data() {
    return {
      post: {},
    };
  },
  async mounted() {
    const id = this.$route.params.id;
    try {
      const res = await axios.get(`http://127.0.0.1:8000/api/posts/${id}/`, {
        withCredentials: true,
      });
      this.post = res.data;
    } catch (error) {
      console.error("获取帖子详情失败:", error);
    }
  },
  methods: {
    formatDate(dateStr) {
      if (!dateStr) return "";
      const date = new Date(dateStr);
      return date.toLocaleDateString("zh-CN", {
        year: "numeric",
        month: "short",
        day: "numeric",
      });
    },
  },
};
</script>

<style scoped>
/* 可选字体增强 */
.post-detail {
  font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
}
</style>


