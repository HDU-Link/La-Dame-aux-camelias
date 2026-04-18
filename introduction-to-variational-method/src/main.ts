import { createApp, provide } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from "vue-axios"
import router from './router'
import store from './store'
const app = createApp(App)
app.use(VueAxios, axios)
app.use(store).use(router).mount('#app')
app.provide('axios', app.config.globalProperties.axios)