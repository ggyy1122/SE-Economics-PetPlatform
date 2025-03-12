<!--
  2025-3-7:主页 商城和社区导航栏
  2025-3-12:主页  登录导航栏
  -->
  <template>
    <div class="home">
      <!-- 渲染 AppNavbar，传递并监听选中的选项 -->
   
    <AppNavbar :selected="selected" @update:selected="handleSelection" />

    
    <!-- 根据选中的值，显示广告、精选内容、社区内容等 -->
    <AdCarousel v-if="selected === 'featured'" />
    <FeaturedSection v-if="selected === 'featured'" />
    <CommunitySection v-if="selected === 'community'" />

    <!-- 如果选中 'login'，则显示登录弹窗 -->
    <LoginPopup :isVisible="selected === 'login'" @close="handleCloseLogin" />

    </div>
  </template>
  
  <script>
  import AppNavbar from "@/components/AppNavbar.vue";
  import AdCarousel from "@/components/AdCarousel.vue"; // 引入广告组件
  import FeaturedSection from "@/components/FeaturedSection.vue";
  import CommunitySection from "@/components/CommunitySection.vue";
  import LoginPopup from "@/components/LoginSection.vue";
  
  export default {
    components: { AppNavbar, AdCarousel, FeaturedSection, CommunitySection ,LoginPopup},
    data() {
      return {
        selected: "featured", // 初始显示 FeaturedSection
      };
    },
    methods: {
  handleSelection(option) {
    console.log("✅ handleSelection 被调用，选项：", option);
    this.selected = option; // 直接切换页面或弹窗
  },
  handleCloseLogin() {
    console.log("✅ 1111111111111111111111111", );
  this.selected = "featured"; // 关闭弹窗时，重置选中状态
}

}


  };
  </script>
  
