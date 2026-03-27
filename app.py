from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from config import DevelopmentConfig
import forms

from models import db, Alumnos, Maestros
from forms import UserForm, MaestroForm

# 1. IMPORTAMOS EL MÓDULO (BLUEPRINT) DEL PROFE
from maestros import maestros_bp

# 2. INICIALIZAMOS LA APP 
app = Flask(__name__)  
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

# 3. CONECTAMOS EL MÓDULO A TU APP PRINCIPAL
app.register_blueprint(maestros_bp)

# ==========================================
# RUTAS PRINCIPALES
# ==========================================

@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
    # Menú principal (solo muestra los botones de alumnos y maestros)
    return render_template("index.html")

# Cambiamos el nombre de la función a vista_alumnos para evitar el error con el modelo Alumnos
@app.route("/alumnos", methods=["GET", "POST"])
def vista_alumnos(): 
    create_form = forms.UserForm(request.form)
    
    # Mandamos a los alumnos a la nueva tabla
    lista_alumnos = Alumnos.query.all()
    return render_template("Alumnos.html", form=create_form, alumno=lista_alumnos)

# NUEVA RUTA: Para el formulario de insertar alumno
@app.route("/insertar_alumno", methods=["GET", "POST"])
def insertar_alumno():
    create_form = forms.UserForm(request.form)
    
    if request.method == "POST":
        alum = Alumnos(
            nombre=create_form.nombre.data,
            amaterno=create_form.amaterno.data,
            apaterno=create_form.apaterno.data,
            edad=create_form.edad.data,
            correo=create_form.correo.data,
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for("vista_alumnos"))
        
    return render_template("insertar_alumno.html", form=create_form)

@app.route("/detalles", methods=["GET", "POST"])
def detalles():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        nombre = alum1.nombre
        apaterno = alum1.apaterno
        amaterno = alum1.amaterno
        edad = alum1.edad
        correo = alum1.correo

    return render_template(
        "detalles.html",
        id=id,
        nombre=nombre,
        apaterno=apaterno,
        amaterno=amaterno,
        edad=edad,
        correo=correo,
    )

@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get("id")
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.amaterno.data = alum1.amaterno
        create_form.edad.data = alum1.edad
        create_form.correo.data = alum1.correo

    if request.method == "POST":
        id = request.args.get("id")
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum1.id = id
        alum1.nombre = create_form.nombre.data
        alum1.apaterno = create_form.apaterno.data
        alum1.amaterno = create_form.amaterno.data
        alum1.edad = create_form.edad.data
        alum1.correo = create_form.correo.data
        db.session.add(alum1)
        db.session.commit()
        # Modificado: ahora redirige a vista_alumnos
        return redirect(url_for("vista_alumnos"))
    
    return render_template("modificar.html", form=create_form)

@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get("id")
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.amaterno.data = alum1.amaterno
        create_form.edad.data = alum1.edad
        create_form.correo.data = alum1.correo
        
    if request.method == "POST":
        id = request.form.get("id")
        alum = Alumnos.query.get_or_404(id)
        db.session.delete(alum)
        db.session.commit()
        # Modificado: ahora redirige a vista_alumnos
        return redirect(url_for("vista_alumnos"))
    
    return render_template("eliminar.html", form=create_form)

# ==========================================
# INICIO DE LA APLICACIÓN
# ==========================================
if __name__ == "__main__":
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)