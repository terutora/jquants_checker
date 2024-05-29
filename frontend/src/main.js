import './assets/css/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router';

createApp(App).mount('#app')

createApp.config.productionTip = false;

new createApp({
  router,  // Vue RouterをVueインスタンスに統合
  render: h => h(App),
}).$mount('#app');