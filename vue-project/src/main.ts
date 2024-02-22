import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import CanvasJSChart from '@canvasjs/vue-charts';
import router from './router.ts';

const app = createApp(App)
app.use(router)
app.use(CanvasJSChart)
app.mount('#app')

