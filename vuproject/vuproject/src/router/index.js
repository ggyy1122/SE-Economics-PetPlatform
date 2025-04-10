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
import PostDetail from '../views/PostDetail.vue';
import CreatePost from '@/views/CreatePost.vue';
import Community from '@/components/CommunitySection.vue'; // 引入社区页面

const routes = [
  { path: '/', name: 'HomePage', component: HomePage },
  { path: '/product/:id', component: ProductDetail, props: true },
  { path: '/post/:id', name: 'PostDetail', component: PostDetail },
  { path: '/create-post', name: 'CreatePost', component: CreatePost },
  { path: '/community', name: 'Community', component: Community },  // 确保有 Community 路由
  {
    path: '/dashboard',
    component: ProfileSection,
    redirect: '/dashboard/home',
    children: [
      { path: 'home', component: DashboardHome },
      { path: 'favorites', component: MyFavorites },
      { path: 'orders', component: ShopOrders },
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

