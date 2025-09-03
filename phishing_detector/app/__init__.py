import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from .extensions import db , migrate

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
# We start the configuration here -----------
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, 'aegis.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    

    # --- Logging Configuration ---

    #Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Handlers for logging to file and console
    file_handler = RotatingFileHandler(
        os.path.join(app.instance_path, 'aegis.log'),
        maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s'))

    # Add both handlers to the logger
    app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('AegisPhish system startup')
    # --- End of Logging Configuration ---
    db.init_app(app)
    migrate.init_app(app,db)
    from . import models
    # -- Routes --
    @app.route('/')
    def index():
        app.logger.info('Root endpoint was reached.')
        return "Welcome to AegisPhish!"

    @app.route('/health')
    def health_check():
        app.logger.info('Health check endpoint was reached.')
        return 'AegisPhish System Status: Nominal.'

    return app
