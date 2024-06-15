import { createRouter, createWebHistory } from 'vue-router'; 
import Home from '@/components/Home.vue';
import MessageComponent from '@/components/MessageComponent.vue';  
import NotFound from '@/components/NotFound.vue';
import ErrorPage from '@/components/ErrorPage.vue';
import DataHandler from '@/components/DataHandler.vue';

const routes = [
    { path: '/', name: 'HomePage', component: Home},
    { path: '/message', name: 'MessagePage', component: MessageComponent},
    { path: '/notfound', name: 'NotFound', component: NotFound}, 
    { path: '/error', name: 'ErrorPage', component: ErrorPage},
    { path: '/datahandler', name: 'DataHandler', component: DataHandler},
    { path: '/:pathMatch(.*)*', redirect: '/notfound'} 
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
