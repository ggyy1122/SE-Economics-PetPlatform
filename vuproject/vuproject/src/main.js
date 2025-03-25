import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // 引入 Vue Router
import store from './store/store'; // 引入 Vuex
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

const app = createApp(App);
app.use(store);   // 注册 Vuex
app.use(router);  // 注册 Vue Router
app.use(ElementPlus); // 注册 Element Plus

app.mount("#app"); // 挂载应用
