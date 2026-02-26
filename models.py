from io import StringIO

from flask_sqlalchemy import SQLAlchemy #ORM
import datetime

db= SQLAlchemy()

class Alumnos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), primary_key=True)
    apaterno = db.Column(db.String(50), primary_key=True)
    amaterno= db.Column(db.String(50), primary_key=True)
    edad = db.Column(db.Integer, nullable=False)
    correo =db.Column(db,String(100), nullable= False)
    
    