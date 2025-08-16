from flask import request, jsonify
from app import app, db, socketio, csrf
from models import User, Transaction, FraudCase
from datetime import datetime

@app.route('/')
def home():
    return "Welcome to the ID Fraud Detection System!"

@app.route('/api/users', methods=['POST'])
@csrf.exempt
def add_user():
    data = request.json
    user = User(
        name=data['name'],
        email=data['email']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully', 'id': user.id}), 201

@app.route('/api/transactions', methods=['POST'])
@csrf.exempt
def add_transaction():
    data = request.json
    transaction = Transaction(
        user_id=data['user_id'],
        amount=data['amount'],
        location=data['location'],
        timestamp=data['timestamp']
    )
    db.session.add(transaction)
    db.session.commit()

    # Emit real-time update
    socketio.emit('new_transaction', {'id': transaction.id, 'amount': transaction.amount})

    return jsonify({'message': 'Transaction added successfully'}), 201

@app.route('/api/fraud_cases', methods=['GET'])
def get_fraud_cases():
    cases = FraudCase.query.all()
    return jsonify([{'id': case.id, 'status': case.status, 'created_at': case.created_at.isoformat()} for case in cases])