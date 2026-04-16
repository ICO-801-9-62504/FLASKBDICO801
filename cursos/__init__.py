from flask import Blueprint

# Quitamos el template_folder para que use el estándar de Flask
cursos_bp = Blueprint('cursos', __name__)

from . import routes