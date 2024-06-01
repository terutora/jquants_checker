import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// アプリケーションインスタンスを作成
const app = createApp(App)

// ルーターを統合
app.use(router)

// アプリケーションをマウント
app.mount('#app')
