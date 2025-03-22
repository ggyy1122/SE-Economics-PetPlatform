import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import ProductDetail from '@/views/ProductDetail.vue';
import ProfileSection from '@/components/ProfileSection.vue';
import DashboardHome from '@/views/DashboardHome.vue'; 
import TransactionsSection from '@/views/TransactionsSection.vue';
import FundsSection from '@/views/FundsSection.vue';
import MessagesSection from '@/views/MessageSection.vue';
import SettingsSection from '@/views/SettingsSection.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/product/:id', component: ProductDetail, props: true },

  {
    path: '/dashboard',
    component: ProfileSection, // ProfileSection 是包含左侧导航栏的主组件
    redirect: '/dashboard/home', // 默认重定向到 /dashboard/home
    children: [
      { path: 'home', component: DashboardHome },
      { path: 'transactions', component: TransactionsSection },
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
