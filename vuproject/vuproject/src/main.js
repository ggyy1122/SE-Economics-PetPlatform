//确保vue正确使用路由
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // 引入 router

const app = createApp(App);

app.use(router); // 挂载 router
app.mount('#app');
