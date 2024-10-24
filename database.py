from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicializa o SQLAlchemy
db = SQLAlchemy()

def configure_bd(app):
 
    # Adiciona configuração para uso do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('DATABASE')  # Alterar para pegar a variável correta do app.config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = app.config.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    
    # Inicializa o SQLAlchemy com o aplicativo
    db.init_app(app)

    with app.app_context():
        # Cria todas as tabelas
        db.create_all()