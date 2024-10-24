# lib/models/profile.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from database import db, configure_bd

def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)
    
    # Carrega as configurações a partir da classe Config
    Config.load_config(app)

    Config.log_configure()
    
    configure_bd(app)

    return app
