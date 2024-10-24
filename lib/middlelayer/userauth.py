# lib/middlelayer/userauth.py
from flask import g, request, current_app, Response
from werkzeug.security import check_password_hash
from lib.service.profile_service import ProfileService
from flask_httpauth import HTTPBasicAuth
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import HTTPException
import logging

log = logging.getLogger(__name__)
auth = HTTPBasicAuth()
profile_service = None

def init_auth_service(db):
    global profile_service
    profile_service = ProfileService(db)  # Inicializa o serviço com o db

@auth.verify_password
def verify_password(username, password):
    user = Profile.query.filter_by(username=username).first()
    log.info(f"Verificando usuário: {username}, encontrado: {user is not None}")
    if user and check_password_hash(user.password, password):
        g.current_user = user
        return True
    return False

class MyModelView(ModelView):
    def is_accessible(self):
        if profile_service is None:
            raise AuthException('Serviço de autenticação não inicializado.')

        auth_data = request.authorization  # Obter dados de autenticação

        if auth_data and auth_data.username and auth_data.password:
            username = auth_data.username
            password = auth_data.password
            
            # Validar usuário com o profile_service
            if (profile_service.validate_authentication(username, password) and
                username in current_app.config.get('ADMINISTRATORS', [])):
                return True
            
        return False  # Retorna False se não autenticado

class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "Você não pôde ser autenticado. Por favor, atualize a página.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))
