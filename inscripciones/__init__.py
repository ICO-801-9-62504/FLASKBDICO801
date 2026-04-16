from flask import Blueprint

# Creamos el blueprint para las inscripciones
ins_bp = Blueprint('inscripciones', __name__, template_folder='../templates/inscripciones')

from . import routes