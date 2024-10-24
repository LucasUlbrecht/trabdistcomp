from flask import jsonify, redirect
from flask_login import login_required
from lib.models.profile import Profile
from werkzeug.exceptions import HTTPException
from lib.middlelayer.userauth import auth
import logging

log = logging.getLogger(__name__)

def register_routes(app):
    @app.route('/')
    @login_required  # Utilize o decorador correto para autenticação
    def index():
        user = auth.current_user()  # Acesse o usuário atual

        # Verifique se o usuário existe
        user_db = Profile.query.filter_by(username=user).first()  # Use filter_by para simplificar

        if user_db:
            message_info = f"Usuário {user}, acessou o index."
            response = {"success": message_info}
            log.info(message_info)
            return jsonify(response)
        else:
            return jsonify({"error": "Usuário não encontrado."}), 404  # Retorne um erro se não encontrar o usuário
