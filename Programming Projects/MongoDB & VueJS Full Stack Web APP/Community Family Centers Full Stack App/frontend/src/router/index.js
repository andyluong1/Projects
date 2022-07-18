import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import ProgramChart from '@/views/ProgramChart'

// Define some routes
// Each route maps to a component
const routes = [
  {
    path: '/Home',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',

    component: () => import('../views/About.vue')
  },
  {
    path: '/create',
    name: 'createClient',
    component: () => import('../components/CreateComponent')
  },
  {
    path: '/view',
    name: 'view',
    component: () => import('../components/ListComponent')
  },
  {
    path: '/edit/:id',
    name: 'editClient',
    component: () => import('../components/EditComponent')
  },
  {
    path: '/programs',
    name: 'programs',
    component: () => import('../components/ProgramComponent')
  },
  
  {
    path: '/editProgram/:id',
    name: 'editProgram',
    component: () => import('../components/EditProgramComponent')
  },
  {
    path: '/addProgram/:id',
    name: 'addProgram',
    component: () => import('../components/AddProgramComponent')
  },
  {
     path: '/ProgramChart',
     name: 'ProgramChart',
     component: ProgramChart
   },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
