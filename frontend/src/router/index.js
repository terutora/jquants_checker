import { createRouter, createWebHistory } from 'vue-router';  // Vue Routerの関数をインポート
import MessageComponent from '@/components/MessageComponent.vue';  // 表示するメッセージを持つコンポーネントをインポート

const routes = [
  {
    path: '/message',  // 新しいページのパスを指定
    name: 'Message',
    component: MessageComponent  // 表示するメッセージを持つコンポーネントを指定
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
