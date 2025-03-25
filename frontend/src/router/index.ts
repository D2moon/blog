import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import AboutPage from '../views/AboutPage.vue'
import ContactPage from '../views/ContactPage.vue'
import MarkdownRenderer from "../components/MarkdownRenderer.vue";


const routes = [
  { path: '/', component: HomePage },
  { path: '/about', component: AboutPage },
  { path: '/contact', component: ContactPage },
  { path: "/post", component: MarkdownRenderer },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
