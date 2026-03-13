from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos, Maestros 
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf = CSRFProtect(app)



@app.route("/", methods=["GET","POST"])
@app.route("/index")
def index():
    create_alumno = forms.UserForm(request.form)
    # select * alumnos alumnos
    alumno = Alumnos.query.all()
    return render_template("index.html", form=create_alumno, alumno=alumno)
    

@app.route("/usuarios", methods=["GET","POST"])
def usuario():
    mat = 0
    nom = ''
    apa = ''
    ama = ''
    edad = 0
    email = ''
    usuarios_clas = forms.UserForm(request.form)
    
    if request.method == 'POST':
        mat = usuarios_clas.matricula.data
        nom = usuarios_clas.nombre.data
        apa = usuarios_clas.apaterno.data
        ama = usuarios_clas.amaterno.data
        edad = usuarios_clas.edad.data
        email = usuarios_clas.correo.data
    
    return render_template('usuarios.html', form=usuarios_clas, mat=mat,
                           nom=nom, apa=apa, ama=ama, edad=edad, email=email)



@app.route("/maestros", methods=["GET","POST"])
def maestros():
    create_maestro = forms.MaestroForm(request.form)
    
    maestro = Maestros.query.all()
    return render_template("maestros.html", form=create_maestro, maestro=maestro)

@app.route("/datos_maestros", methods=["GET","POST"])
def datos_maestro():
    mat = 0
    nom = ''
    ape = ''
    esp = ''
    correo = ''
    maestros_clas = forms.MaestroForm(request.form)
    
    if request.method == 'POST':
        mat = maestros_clas.matricula.data
        nom = maestros_clas.nombre.data
        ape = maestros_clas.apellidos.data
        esp = maestros_clas.especialidad.data
        correo = maestros_clas.email.data
    
    return render_template('datos_maestros.html', form=maestros_clas, mat=mat,
                           nom=nom, ape=ape, esp=esp, correo=correo)



if __name__ == '__main__':
   
    with app.app_context():
        db.create_all()
    
    
    app.run(debug=True)