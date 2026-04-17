from flask import Blueprint

# Creamos el blueprint para las consultas
consultas_bp = Blueprint('consultas', __name__, template_folder='../templates/consultas')

from . import routes