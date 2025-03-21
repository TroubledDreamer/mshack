import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Import router

const app = createApp(App);
app.use(router); // Make sure router is used
app.mount('#app');
