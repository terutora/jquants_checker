import { createRouter, createWebHistory } from 'vue-router'; 
import Home from '@/components/Home.vue';
import MessageComponent from '@/components/MessageComponent.vue';  
import NotFound from '@/components/NotFound.vue';
import ErrorPage from '@/components/ErrorPage.vue';
import DataHandler from '@/components/DataHandler.vue';

const routes = [
    { path: '/jquants_checker/', name: 'HomePage', component: Home},
    { path: '/jquants_checker/message', name: 'MessagePage', component: MessageComponent},
    { path: '/jquants_checker/notfound', name: 'NotFound', component: NotFound}, 
    { path: '/jquants_checker/error', name: 'ErrorPage', component: ErrorPage},
    { path: '/jquants_checker/datahandler', name: 'DataHandler', component: DataHandler},
    { path: '/:pathMatch(.*)*', redirect: '/notfound'} 
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
