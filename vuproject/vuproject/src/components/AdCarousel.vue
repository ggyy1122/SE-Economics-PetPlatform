<!--2025-3-9：实现主页广告的轮播-->
<template>
  <div v-if="ads.length" class="ad-carousel">
    <div class="carousel-container">
      <img :src="ads[currentIndex].image" alt="广告" class="ad-image" />
    </div>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      ads: [], // 存放广告数据
      currentIndex: 0, // 当前显示的广告索引
      adInterval: null // 保存定时器的引用
    };
  },
  mounted() {
    console.log('组件挂载完成，开始获取广告数据...');
    this.fetchAds();
    // 确保定时器的上下文指向正确
    this.adInterval = setInterval(() => {
      console.log('切换广告，当前索引：', this.currentIndex);
      this.nextAd();
    }, 3000); // 每3秒切换广告
  },
  beforeUnmount() { // 修正为 Vue 3 的 beforeUnmount
    // 在组件销毁前清除定时器，避免内存泄漏
    if (this.adInterval) {
      console.log('清除广告切换定时器...');
      clearInterval(this.adInterval);
    }
  },
  methods: {
    async fetchAds() {
      try {
        console.log('请求广告数据...');
        const response = await axios.get('http://127.0.0.1:8000/api/ads/homepage/');
        console.log('获取到的广告数据:', response.data);
        this.ads = response.data;

        // 拼接完整的图片 URL
        this.ads.forEach(ad => {
          console.log('拼接广告图片路径:', ad.image_url);
          ad.image = "http://127.0.0.1:8000/media/" + ad.image_url; // 拼接成完整路径
        });

        // 预加载广告图片
        this.ads.forEach(ad => {
          const img = new Image();
          img.src = ad.image;
          console.log('预加载图片:', img.src);
        });
      } catch (error) {
        console.error('获取广告失败:', error);
      }
    },
    nextAd() {
      if (this.ads.length > 0) {
        console.log('广告切换，当前索引:', this.currentIndex);
        this.currentIndex = (this.currentIndex + 1) % this.ads.length;
      }
    }
  }
};
</script>

<style scoped>
.ad-carousel {
  width: 100%;
  height: 400px; /* 根据需求设置高度 */
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px; /* 广告和商品之间的间距 */
}

.carousel-container {
  width: 100%;
  display: flex;
  justify-content: center;
}

.ad-image {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 保证图片填满容器，且按比例压缩 */
}
</style>




