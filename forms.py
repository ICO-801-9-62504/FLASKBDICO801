from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, EmailField, PasswordField, SubmitField

class UserForm(Form):
    id = IntegerField("ID")  # Este es el nombre que Jinja2 buscará
    nombre = StringField("Nombre")
    apaterno = StringField("APaterno")
    amaterno = StringField("AMaterno")
    edad = IntegerField("Edad")
    correo = EmailField("Correo")

class MaestroForm(FlaskForm):
    id = IntegerField("Matricula")
    nombre = StringField("Nombre")
    apellidos = StringField("Apellidos")
    especialidad = StringField("Especialidad")
    email = EmailField("Email")