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
import { generateAnimalCategoryRoutes } from '@/router/categoryGenerator.js'
const animalCategoryConfigs = [
  {
    pathBase: 'dog',
    categoryName: '狗',
    subCategories: ['food', 'snack', 'toy'],
    defaultSub: 'food'
  },
  {
    pathBase: 'cat',
    categoryName: '猫',
    subCategories: ['food', 'snack', 'toy'],
    defaultSub: 'food'
  },
  {
    pathBase: 'small',
    categoryName: '小宠',
    subCategories: ['food', 'snack', 'toy'],
    defaultSub: 'food'
  },
  {
    pathBase: 'aquatic',
    categoryName: '水族',
    subCategories: ['food', 'snack', 'toy'],
    defaultSub: 'food'
  },
  {
    pathBase: 'reptile',
    categoryName: '爬虫',
    subCategories: ['food', 'snack', 'toy'],
    defaultSub: 'food'
  }
];

const animalCategoryRoutes = generateAnimalCategoryRoutes(animalCategoryConfigs);
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
  {
    path: '/category',
    component: () => import('@/views/CategoryPage.vue'), // 导航栏 + router-view
    children: [
      {
        path: 'all',
        name: 'all',
        component: () => import('@/views/categories/AllProducts.vue') // 显示所有商品
      },
      ...animalCategoryRoutes
      
    ]
  }
  
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;