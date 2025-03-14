//确保vue正确使用路由
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // 引入 router
import store from './store/store';
const app = createApp(App);

app.use(store); // 注册 Vuex
app.use(router); // 如果有 Vue Router
app.mount("#app")