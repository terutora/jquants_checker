import { createRouter, createWebHistory } from 'vue-router'; 
import App from '@/App.vue';
import MessageComponent from '@/components/MessageComponent.vue';  
import NotFound from '@/components/NotFound.vue';
import ErrorPage from '@/components/ErrorPage.vue'; // Errorコンポーネントの名前を変更

const routes = [
    { path: '/', name: 'App', component: App},
    { path: '/message', name: 'MessagePage', component: MessageComponent},
    { path: '/notfound', name: 'NotFound', component: NotFound}, 
    { path: '/error', name: 'ErrorPage', component: ErrorPage} 
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
