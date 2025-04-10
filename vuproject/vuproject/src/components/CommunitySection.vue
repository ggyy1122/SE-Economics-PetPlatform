<!--
  时间: [2025-3-7]
  描述: [主页的社区模块]
-->
<template>
  <div class="community-section">
    <h2>社区</h2>

    <!-- 发布新帖子按钮 -->
    <div class="add-post-button">
      <button @click="goToCreatePostPage">发布新帖子</button>
    </div>

    <div
      v-if="posts.length"
      class="post-list"
    >
      <div
        v-for="post in posts"
        :key="post.id"
        class="post"
        @click="goToPost(post.id)"
      >
        <img
          v-if="post.content?.image"
          :src="post.content.image"
          alt="Post Cover"
        />
        <h3>{{ post.title }}</h3>
        <p class="author">作者：{{ post.user }}</p>
      </div>
    </div>

    <div
      v-else
      class="empty-message"
    >暂无帖子内容</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CommunitySection",
  data() {
    return {
      posts: [],
    };
  },
  methods: {
    async fetchPosts() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/posts/");
        this.posts = res.data;
        console.log("获取帖子成功:", this.posts);
      } catch (err) {
        console.error("获取帖子失败:", err);
      }
    },
    goToPost(postId) {
      this.$router.push({ name: "PostDetail", params: { id: postId } });
    },
    goToCreatePostPage() {
      // 使用路由跳转到创建帖子页面
      this.$router.push({ name: "CreatePost" });
    },
  },
  mounted() {
    this.fetchPosts();
  },
};
</script>

<style scoped>
.community-section {
  padding: 20px;
}

h2 {
  margin-top: 30px;
  margin-bottom: 15px;
  padding-left: 10px;
  font-size: 1.5em;
  color: #333;
  border-bottom: 2px solid #eee;
  padding-bottom: 10px;
}

.add-post-button {
  text-align: center;
  margin-top: 20px;
}

.add-post-button button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.add-post-button button:hover {
  background-color: #45a049;
}

.post-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  min-height: 200px;
}

.post {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 15px;
  text-align: center;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.post:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.post img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px;
}

.post h3 {
  font-size: 1.2em;
  margin: 10px 0;
  color: #333;
}

.post .author {
  font-size: 0.95em;
  color: #666;
}

.empty-message {
  text-align: center;
  color: #999;
  padding: 50px 0;
}
</style>

