from flask import Blueprint

# Creamos el blueprint para los alumnos
alumnos_bp = Blueprint('alumnos', __name__, template_folder='../templates/alumnos')

from . import routes