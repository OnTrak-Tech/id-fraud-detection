CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    email VARCHAR(128) UNIQUE NOT NULL
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    amount FLOAT NOT NULL,
    location VARCHAR(128) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

CREATE TABLE fraud_cases (
    id SERIAL PRIMARY KEY,
    transaction_id INTEGER REFERENCES transactions(id),
    status VARCHAR(64) DEFAULT 'Open',
    created_at TIMESTAMP NOT NULL
);
