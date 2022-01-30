import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'

const app = createApp(App)
// app.use(VueGoodTablePlugin)
app.config.globalProperties.axios=axios
axios.defaults.baseURL = 'http://localhost:5000/'
app.mount('#app')