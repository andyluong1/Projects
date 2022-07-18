import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue3 from 'bootstrap-vue-3'
import VueChartkick from 'vue-chartkick'
import 'chartkick/chart.js'


import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

// Establishing a Vue instance
const app = createApp(App)
app.use(BootstrapVue3)
app.use(router)
app.mount('#app')
app.use(VueChartkick)