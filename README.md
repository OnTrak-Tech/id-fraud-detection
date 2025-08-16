# ID Fraud Detection System

A real-time fraud detection system for monitoring and analyzing suspicious transactions with a modern web interface.

## 🏗️ Architecture

### Backend (Flask)
- **Framework**: Flask with SQLAlchemy ORM
- **Database**: PostgreSQL
- **Real-time**: WebSocket support via Flask-SocketIO
- **Security**: CSRF protection, rate limiting, CORS
- **Caching**: Redis for session storage and rate limiting

### Frontend (Vue.js)
- **Framework**: Vue 3 with Composition API
- **UI**: Responsive dashboard with real-time updates
- **Charts**: Chart.js for data visualization
- **Security**: DOMPurify for XSS protection

## 📁 Project Structure

```
id-fraud-detection/
└── id-fraud-catch/
    ├── backend/
    │   ├── app.py          # Flask application setup
    │   ├── config.py       # Configuration management
    │   ├── models.py       # Database models
    │   ├── routes.py       # API endpoints
    │   └── requirements.txt
    ├── frontend/
    │   ├── src/
    │   │   ├── views/Dashboard.vue
    │   │   ├── router/index.js
    │   │   ├── App.vue
    │   │   └── main.js
    │   └── package.json
    └── database/
        └── init.sql        # Database schema
```

## 🚀 Features

- **Real-time Monitoring**: Live transaction tracking with WebSocket updates
- **Fraud Case Management**: Track and manage fraud cases with status updates
- **Interactive Dashboard**: Visual analytics with charts and statistics
- **Security**: CSRF protection, rate limiting, input sanitization
- **Responsive Design**: Mobile-friendly interface

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL
- Redis

### Backend Setup

1. Navigate to backend directory:
```bash
cd id-fraud-catch/backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://username:password@localhost/fraud_detection
```

4. Initialize database:
```bash
psql -U username -d fraud_detection -f ../database/init.sql
```

5. Start Redis server:
```bash
redis-server
```

6. Run the application:
```bash
python app.py
```

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd id-fraud-catch/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run serve
```

## 📊 Database Schema

### Users Table
- `id`: Primary key
- `name`: User full name
- `email`: Unique email address

### Transactions Table
- `id`: Primary key
- `user_id`: Foreign key to users
- `amount`: Transaction amount
- `location`: Transaction location
- `timestamp`: Transaction datetime

### Fraud Cases Table
- `id`: Primary key
- `transaction_id`: Foreign key to transactions
- `status`: Case status (Open/Closed)
- `created_at`: Case creation datetime

## 🔌 API Endpoints

### Users
- `POST /api/users` - Create new user

### Transactions
- `POST /api/transactions` - Add new transaction

### Fraud Cases
- `GET /api/fraud_cases` - Retrieve all fraud cases

## 🔒 Security Features

- **CSRF Protection**: Prevents cross-site request forgery
- **Rate Limiting**: Redis-based request throttling
- **CORS**: Configured for localhost development
- **Content Security Policy**: XSS protection headers
- **Input Sanitization**: DOMPurify on frontend
- **Secure Cookies**: HTTPOnly, Secure, SameSite attributes

## 🌐 Real-time Features

- **WebSocket Connection**: Live transaction updates
- **Connection Status**: Visual indicator for real-time connectivity
- **Auto-refresh**: Dashboard updates without page reload

## 🎨 Dashboard Features

- **Statistics Cards**: Total cases, active alerts, daily transactions
- **Fraud Trend Chart**: Visual representation of fraud patterns
- **Case Management**: List and track fraud case statuses
- **Transaction Testing**: Add test transactions for system validation

## 🚀 Production Deployment

### Backend
```bash
gunicorn --worker-class eventlet -w 1 app:app
```

### Frontend
```bash
npm run build
```

## 🔧 Configuration

### Environment Variables
- `SECRET_KEY`: Flask secret key for sessions
- `DATABASE_URL`: PostgreSQL connection string

### Default Ports
- Backend: `5000`
- Frontend: `8080`
- Redis: `6379`
- PostgreSQL: `5432`

## 📝 Development

### Adding New Features
1. Backend: Add models in `models.py`, routes in `routes.py`
2. Frontend: Create components in `src/components/`, add routes in `router/index.js`
3. Database: Update `init.sql` for schema changes

### Testing Transactions
Use the dashboard form to add test transactions and monitor real-time updates.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request
