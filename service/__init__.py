"""
Package initialization for the Account Service
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from flask_cors import CORS

# Create the Flask app
app = Flask(__name__)
app.config.from_object("service.config")

# Initialize plugins
db = SQLAlchemy(app)

# Only enable Talisman in production (not during testing)
talisman = Talisman(
    app,
    force_https=False,
    strict_transport_security=False,
    session_cookie_secure=False
)

CORS(app)

# Import routes after app is created
from service import routes, models  # noqa: F401, E402
from service.common import log_handlers  # noqa: F401, E402

if __name__ == "__main__":
    log_handlers.init_logging(app, "gunicorn.error")
