from flask import Blueprint

# Creamos el objeto primero
maestros_bp = Blueprint('maestros', __name__)

# IMPORTANTE: La importación de routes va al final 
# para que el objeto maestros_bp ya exista cuando routes lo busque.
from . import routes