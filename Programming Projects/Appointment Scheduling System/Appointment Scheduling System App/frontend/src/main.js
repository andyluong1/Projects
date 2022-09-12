import { createApp } from 'vue'
import App from './App.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import VueGoogleMaps from '@fawmi/vue-google-maps'
import router from './router'

const app = createApp(App)
app.use(router)
app.use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyBcTzfiN7TtMe2Rob15eRvxBWX9qUGYWU8',
    },
})
app.mount('#app')
