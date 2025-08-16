import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { io } from 'socket.io-client';
import axios from 'axios';
import DOMPurify from 'dompurify';

// Configure axios base URL
axios.defaults.baseURL = 'http://localhost:5000';

// Initialize Socket.IO client
const socket = io('http://localhost:5000');

const app = createApp(App);
app.config.globalProperties.$socket = socket;
app.config.globalProperties.$http = axios;
app.config.globalProperties.$sanitize = DOMPurify.sanitize;

app.use(router);
app.mount('#app');
