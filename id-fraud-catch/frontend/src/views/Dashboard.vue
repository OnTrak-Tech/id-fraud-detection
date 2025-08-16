<template>
  <div class="dashboard">
    <header class="header">
      <h1>🛡️ ID Fraud Detection System</h1>
      <div class="status-indicator" :class="{ online: isConnected }">
        {{ isConnected ? '🟢 Live' : '🔴 Offline' }}
      </div>
    </header>

    <div class="stats-grid">
      <div class="stat-card">
        <h3>Total Cases</h3>
        <div class="stat-number">{{ fraudCases.length }}</div>
      </div>
      <div class="stat-card">
        <h3>Active Alerts</h3>
        <div class="stat-number alert">{{ activeAlerts }}</div>
      </div>
      <div class="stat-card">
        <h3>Transactions Today</h3>
        <div class="stat-number">{{ transactionsToday }}</div>
      </div>
    </div>

    <div class="content-grid">
      <div class="chart-container">
        <h3>Fraud Cases Trend</h3>
        <canvas id="fraudChart"></canvas>
      </div>

      <div class="cases-list">
        <h3>Recent Fraud Cases</h3>
        <div class="case-item" v-for="fraudCase in fraudCases" :key="fraudCase.id">
          <div class="case-status" :class="fraudCase.status.toLowerCase()">{{ fraudCase.status }}</div>
          <div class="case-info">
            <div>Case #{{ fraudCase.id }}</div>
            <div class="case-date">{{ formatDate(fraudCase.created_at) }}</div>
          </div>
        </div>
        <div v-if="fraudCases.length === 0" class="no-cases">No fraud cases detected</div>
      </div>
    </div>

    <div class="transaction-form">
      <h3>Add Test Transaction</h3>
      <form @submit.prevent="addTransaction">
        <input v-model="newTransaction.user_id" type="number" placeholder="User ID" required>
        <input v-model="newTransaction.amount" type="number" step="0.01" placeholder="Amount" required>
        <input v-model="newTransaction.location" type="text" placeholder="Location" required>
        <button type="submit">Add Transaction</button>
      </form>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, getCurrentInstance } from 'vue';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

export default {
  name: 'Dashboard',
  setup() {
    const { proxy } = getCurrentInstance();
    const fraudCases = ref([]);
    const isConnected = ref(false);
    const activeAlerts = ref(0);
    const transactionsToday = ref(0);
    const newTransaction = ref({
      user_id: '',
      amount: '',
      location: ''
    });

    const loadFraudCases = async () => {
      try {
        const response = await proxy.$http.get('/api/fraud_cases');
        fraudCases.value = response.data;
        activeAlerts.value = response.data.filter(c => c.status === 'Open').length;
      } catch (error) {
        console.error('Failed to load fraud cases:', error);
      }
    };

    const addTransaction = async () => {
      try {
        const transaction = {
          ...newTransaction.value,
          timestamp: new Date().toISOString()
        };
        await proxy.$http.post('/api/transactions', transaction);
        newTransaction.value = { user_id: '', amount: '', location: '' };
        transactionsToday.value++;
      } catch (error) {
        console.error('Failed to add transaction:', error);
      }
    };

    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString();
    };

    onMounted(() => {
      loadFraudCases();
      
      // Initialize chart
      const ctx = document.getElementById('fraudChart').getContext('2d');
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
          datasets: [{
            label: 'Fraud Cases',
            data: [12, 19, 8, 15, 22, 18],
            borderColor: '#e74c3c',
            backgroundColor: 'rgba(231, 76, 60, 0.1)',
            tension: 0.4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      });

      // Socket.IO connection
      proxy.$socket.on('connect', () => {
        isConnected.value = true;
      });

      proxy.$socket.on('disconnect', () => {
        isConnected.value = false;
      });

      proxy.$socket.on('new_transaction', (data) => {
        transactionsToday.value++;
      });
    });

    return {
      fraudCases,
      isConnected,
      activeAlerts,
      transactionsToday,
      newTransaction,
      addTransaction,
      formatDate
    };
  }
};
</script>

<style scoped>
.dashboard {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 10px;
}

.header h1 {
  margin: 0;
  font-size: 2rem;
}

.status-indicator {
  padding: 8px 16px;
  border-radius: 20px;
  background: rgba(255,255,255,0.2);
  font-weight: bold;
}

.status-indicator.online {
  background: rgba(46, 204, 113, 0.3);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  text-align: center;
}

.stat-card h3 {
  margin: 0 0 10px 0;
  color: #666;
  font-size: 0.9rem;
  text-transform: uppercase;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: bold;
  color: #2c3e50;
}

.stat-number.alert {
  color: #e74c3c;
}

.content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
  margin-bottom: 30px;
}

.chart-container {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  height: 400px;
}

.chart-container h3 {
  margin: 0 0 20px 0;
  color: #2c3e50;
}

.cases-list {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.cases-list h3 {
  margin: 0 0 20px 0;
  color: #2c3e50;
}

.case-item {
  display: flex;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #eee;
}

.case-status {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: bold;
  margin-right: 10px;
}

.case-status.open {
  background: #e74c3c;
  color: white;
}

.case-status.closed {
  background: #27ae60;
  color: white;
}

.case-info {
  flex: 1;
}

.case-date {
  font-size: 0.8rem;
  color: #666;
}

.no-cases {
  text-align: center;
  color: #666;
  font-style: italic;
}

.transaction-form {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.transaction-form h3 {
  margin: 0 0 20px 0;
  color: #2c3e50;
}

.transaction-form form {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.transaction-form input {
  flex: 1;
  min-width: 150px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.transaction-form button {
  padding: 10px 20px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
}

.transaction-form button:hover {
  background: #2980b9;
}

@media (max-width: 768px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
  
  .transaction-form form {
    flex-direction: column;
  }
}
</style>
