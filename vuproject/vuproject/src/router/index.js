import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import ProductDetail from '@/views/ProductDetail.vue';
import ProfileSection from '@/components/ProfileSection.vue';
import DashboardHome from '@/views/DashboardHome.vue'; 
import FundsSection from '@/views/FundsSection.vue';
import MessagesSection from '@/views/MessageSection.vue';
import SettingsSection from '@/views/SettingsSection.vue';
import MyFavorites from '@/views/MyFavorites.vue';  // 引入我的收藏组件
import ShopOrders from '@/views/ShopOrders.vue';    // 引入商城订单组件

const routes = [
  { path: '/', component: HomePage },
  { path: '/product/:id', component: ProductDetail, props: true },

  {
    path: '/dashboard',
    component: ProfileSection, // ProfileSection 是包含左侧导航栏的主组件
    redirect: '/dashboard/home', // 默认重定向到 /dashboard/home
    children: [
      { path: 'home', component: DashboardHome },
      { path: 'favorites', component: MyFavorites }, // 我的收藏
      { path: 'orders', component: ShopOrders }, // 商城订单,
      { path: 'funds', component: FundsSection },
      { path: 'messages', component: MessagesSection },
      { path: 'settings', component: SettingsSection },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
