/* eslint-disable */
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}

declare module 'vue-router' {
  import { Router, RouteRecordRaw, RouterOptions } from 'vue-router/dist/vue-router'
  export * from 'vue-router/dist/vue-router'
  export { createRouter, createWebHistory, createWebHashHistory, createMemoryHistory, RouteRecordRaw }
}