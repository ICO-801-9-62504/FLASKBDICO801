from flask import render_template, request, redirect, url_for
from models import db, Maestros
import forms
from sqlalchemy.exc import IntegrityError
from maestros import maestros_bp 

@maestros_bp.route("/maestros")
def maestros():
    lista_maestros = Maestros.query.all()
    # Asegúrate de que en maestros.html uses {{ teacher.matricula }}
    return render_template("maestros/maestros.html", maestros=lista_maestros)

@maestros_bp.route('/registrar_maestro', methods=['GET', 'POST'])
def registrar():
    form = forms.MaestroForm()
    if form.validate_on_submit():
        try:
            nuevo = Maestros(
                matricula=form.id.data,
                nombre=form.nombre.data,
                apellidos=form.apellidos.data,
                especialidad=form.especialidad.data,
                email=form.email.data
            )
            db.session.add(nuevo)
            db.session.commit()
            return redirect(url_for('maestros.maestros'))
        except IntegrityError:
            db.session.rollback()
            return "Error: La matrícula ya existe."
            
    return render_template("maestros/registrar_maestro.html", form=form)

@maestros_bp.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modificar(id):
    maestre = Maestros.query.get_or_404(id)
    # Llenamos el formulario con los datos del objeto
    form = forms.MaestroForm(obj=maestre)
    
    if request.method == 'POST':
        # Forzamos a que ignore el error del ID porque ya lo tenemos en la URL
        # Actualizamos los datos manualmente del request.form
        maestre.nombre = request.form.get('nombre')
        maestre.apellidos = request.form.get('apellidos')
        maestre.especialidad = request.form.get('especialidad')
        maestre.email = request.form.get('email')
        
        try:
            db.session.commit()
            return redirect(url_for('maestros.maestros'))
        except Exception as e:
            db.session.rollback()
            return f"Error al actualizar: {e}"
            
    return render_template("maestros/editar_maestro.html", form=form, maestro=maestre)

@maestros_bp.route('/detalles/<int:id>')
def detalles(id):
    maestre = Maestros.query.get_or_404(id)
    return render_template("maestros/detalles_maestro.html", maestro=maestre)

@maestros_bp.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar(id):
    maestre = Maestros.query.get_or_404(id)
    
    # 1. Tienes que crear el formulario aquí
    form = forms.MaestroForm(obj=maestre)
    
    if request.method == 'POST':
        db.session.delete(maestre)
        db.session.commit()
        return redirect(url_for('maestros.maestros'))
    
    # 2. ¡IMPORTANTE! Tienes que pasar 'form=form' en el render_template
    # Antes solo tenías maestro=maestre, por eso fallaba
    return render_template("maestros/eliminar_maestro.html", maestro=maestre, form=form)