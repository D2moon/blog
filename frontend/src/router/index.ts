import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage,
  },
  // 你可以在这里添加其他页面路由，例如关于页和联系页
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
