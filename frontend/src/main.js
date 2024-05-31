import './assets/css/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'

// アプリケーションインスタンスを作成
const app = createApp(App)

// ルーターを統合
app.use(router)

// アプリケーションをマウント
app.mount('#app')
