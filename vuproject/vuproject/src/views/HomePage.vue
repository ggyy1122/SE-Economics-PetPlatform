<!--
  2025-3-7:主页
  -->
  <template>
    <div class="home">
      <!-- 导航栏 -->
      <AppNavbar @update:selected="handleSelection" />
  
      <!-- 广告部分 -->
      <AdCarousel />
  
      <!-- 根据 selected 显示内容 -->
      <FeaturedSection v-if="selected === 'featured'" />
      <CommunitySection v-else />
    </div>
  </template>
  
  <script>
  import AppNavbar from "@/components/AppNavbar.vue";
  import AdCarousel from "@/components/AdCarousel.vue"; // 引入广告组件
  import FeaturedSection from "@/components/FeaturedSection.vue";
  import CommunitySection from "@/components/CommunitySection.vue";
  
  export default {
    components: { AppNavbar, AdCarousel, FeaturedSection, CommunitySection },
    data() {
      return {
        selected: "featured", // 初始显示 FeaturedSection
      };
    },
    methods: {
      handleSelection(option) {
        this.selected = option; // 更新 selected 的值
      },
    },
  };
  </script>
  
