# ID Fraud Detection System

## Overview
The ID Fraud Detection System is a multi-layered application designed to detect and prevent fraudulent activities involving ID cards, biometric data, and transactions. It features a real-time dashboard, secure APIs, and a robust backend powered by Flask, PostgreSQL, and Vue.js.

## Features
- **Data Acquisition**: Collects ID documents, biometric data, and transaction streams.
- **Fraud Detection**: Uses rule-based systems, anomaly detection, and predictive modeling.
- **Real-Time Alerts**: Notifies users of suspicious activities.
- **Case Management**: Tracks and resolves fraud cases.
- **Secure Architecture**: Implements best practices for security, including CSRF protection, rate limiting, and secure WebSocket connections.

## Project Structure
```
id-fraud-catch/
├── backend/                # Flask backend
│   ├── app.py              # Main Flask app
│   ├── config.py           # Configuration (e.g., database URI)
│   ├── models.py           # Database models
│   ├── routes.py           # API routes
│   ├── requirements.txt    # Python dependencies
│   └── .env                # Environment variables
├── frontend/               # Vue.js frontend
│   ├── public/             # Static assets
│   ├── src/                # Vue.js source code
│   │   ├── components/     # Vue components
│   │   ├── views/          # Pages
│   │   ├── App.vue         # Main Vue app
│   │   └── main.js         # Vue entry point
│   └── package.json        # JavaScript dependencies
├── database/               # Database setup
│   └── init.sql            # SQL script to initialize the database
└── README.md               # Project documentation
```

## Prerequisites
- **Backend**:
  - Python 3.9+
  - PostgreSQL 12+
- **Frontend**:
  - Node.js 16+
  - npm 7+

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/id-fraud-catch.git
cd id-fraud-catch
```

### 2. Backend Setup
#### Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

#### Configure Environment Variables
Create a `.env` file in the `backend/` directory:
```
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://username:password@localhost/id_fraud_catch
```

#### Initialize the Database
```bash
psql -U username -d id_fraud_catch -f ../database/init.sql
```

#### Run the Backend Server
```bash
python app.py
```

### 3. Frontend Setup
#### Install Dependencies
```bash
cd frontend
npm install
```

#### Run the Frontend Server
```bash
npm run serve
```

### 4. Access the Application
- Frontend: `http://localhost:8080`
- Backend: `http://localhost:5000`

## Security Features
- **CSRF Protection**: Prevents cross-site request forgery attacks.
- **Rate Limiting**: Limits the number of requests to prevent abuse.
- **Content Security Policy (CSP)**: Restricts resource loading to trusted sources.
- **Secure WebSocket Connections**: Uses `wss://` for real-time updates.
- **Environment Variables**: Stores sensitive data securely.

## API Endpoints
### Transactions
- **POST** `/api/transactions`
  - Adds a new transaction.
  - **Request Body**:
    ```json
    {
      "user_id": 1,
      "amount": 100.0,
      "location": "New York",
      "timestamp": "2025-08-16T12:00:00"
    }
    ```
  - **Response**:
    ```json
    {
      "message": "Transaction added successfully"
    }
    ```

### Fraud Cases
- **GET** `/api/fraud_cases`
  - Retrieves all fraud cases.
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "status": "Open",
        "created_at": "2025-08-16T12:00:00"
      }
    ]
    ```

## Real-Time Updates
The application uses WebSocket connections to provide real-time updates for new transactions and fraud cases. Ensure secure WebSocket connections (`wss://`) in production.

## Deployment
### Backend
- Use a production-ready WSGI server like **Gunicorn**.
- Example:
  ```bash
  gunicorn -w 4 -b 0.0.0.0:5000 app:app
  ```

### Frontend
- Build the frontend for production:
  ```bash
  npm run build
  ```
- Serve the static files using a web server like **Nginx**.

### Database
- Use a managed PostgreSQL service or secure your local instance.

## Contributing
Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Flask**: For the backend framework.
- **Vue.js**: For the frontend framework.
- **PostgreSQL**: For the database.
- **Chart.js**: For data visualization.
- **Socket.IO**: For real-time updates.
