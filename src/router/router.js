
import {createRouter, createWebHistory} from 'vue-router';
import profileView from '@/views/profileView.vue';
import catalogView from '@/views/catalogView.vue';
import myBooksView from "@/views/myBooksView.vue";
import catalogItemView from "@/views/catalogItemView.vue";
import errorView from "@/views/errorView.vue";
import authView from "@/views/authView.vue";

const routes = [
    {
        path: '/',
        name: 'Index',
        component: profileView,
        redirect: '/auth'
    },
    {
        path: '/auth',
        name: 'Auth',
        component: authView,
        meta: {
            isAuthPage: true,
        }
    },
    {
        path: '/profile',
        name: 'Profile',
        component: profileView
    },
    {
        path: '/catalog',
        name: 'Catalog',
        component: catalogView
    },
    {
        path: '/catalog/:id',
        name: 'CatalogItem',
        component: catalogItemView
    },
    {
        path: '/my-books',
        name: 'My Books',
        component: myBooksView
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'Error page',
        component: errorView
    },
]

const router = createRouter ( {
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;