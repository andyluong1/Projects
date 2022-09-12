import { createRouter, createWebHistory } from 'vue-router'
import login from '../views/login.vue'
import dashboard from '../views/dashboard.vue'
import staticPages from '../views/staticPages.vue'

const routes = [
    {
        path: '/login',
        name: 'login',
        component: login
    },
    {
        path: '/',
        name: 'smileArchitectsOfHouston',
        component: staticPages
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        component: dashboard,
        beforeEnter: (to, from, next) => {
            if (window.sessionStorage.getItem('authenticated') == 'true') 
            {
                next()
            }
            else {
                next({ name: 'login'})
            }
        }
    }
];

const router = createRouter ({
    history: createWebHistory(), routes
});

export default router