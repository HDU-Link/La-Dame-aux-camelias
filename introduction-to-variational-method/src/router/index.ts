import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/example',
    name: 'example',
    component: () => import('../views/ExampleView.vue')
  },
  {
    path: '/numerical',
    name: 'numerical',
    component: () => import('../views/NumericalView.vue')
  },
  {
    path: '/code',
    name: 'code',
    component: () => import('../views/CodeView.vue')
  },
  {
    path: '/behavior',
    name: 'behavior',
    component: () => import('../views/BehaviorView.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
