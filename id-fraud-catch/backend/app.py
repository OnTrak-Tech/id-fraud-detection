from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_cors import CORS
from config import Config
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="http://localhost:8080")
CORS(app, origins=["http://localhost:8080"])
csrf = CSRFProtect(app)
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="redis://localhost:6379"
)

# Set secure session cookie attributes
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

# Import routes
from routes import *

@app.after_request
def set_csp(response):
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self';"
    return response

@app.errorhandler(500)
def internal_error(error):
    return {"error": "An internal error occurred"}, 500

@app.errorhandler(404)
def not_found_error(error):
    return {"error": "Resource not found"}, 404

if __name__ == "__main__":
    socketio.run(app, debug=True)
