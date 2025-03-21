import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: () => import('../views/LandingView.vue'),
    // props: route => ({ selectedCategory: route.params.selectedCategory || 'all' })
  },
  {
    path: '/learn',
    name: 'Learn',
    component: () => import('../views/LearnView.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/LoginView.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/ProfileView.vue')
  },
  {
    path: '/support',
    name: 'Support',
    component: () => import('../views/SupportView.vue')
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import('../views/HomeView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
