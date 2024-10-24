import logging
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_admin import Admin
from flask import redirect
from lib.routes.register import register_routes
from lib.models.profile import Profile 
from lib.models.views import ProfileView
from lib.middlelayer.userauth import init_auth_service
from app_factor import create_app, db


def configure_admin(app):

    admin = Admin(app, name='Super App', template_mode='bootstrap4')
    admin.add_view(ProfileView(Profile, db.session))

def main():
    # Cria a aplicação Flask
    app = create_app()
    
    # Configura o Flask-Admin
    configure_admin(app)

    # Registra as rotas
    register_routes(app)

    init_auth_service(db)

    # Executa a aplicação
    app.run(host="0.0.0.0", debug=True, port=8080)

if __name__ == "__main__":
    main()
