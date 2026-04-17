from flask import Blueprint, render_template, request, flash
from models import db, Alumnos, Maestros, Curso

from . import consultas_bp
# --- 1. CURSOS POR ALUMNO ---
@consultas_bp.route("/cursos_por_alumno", methods=["GET", "POST"])
def cursos_por_alumno():
    alumnos = Alumnos.query.all()
    resultados = None
    seleccionado = None

    if request.method == "POST":
        alumno_id = request.form.get("alumno_id")
        if alumno_id:
            seleccionado = Alumnos.query.get(alumno_id)
            resultados = seleccionado.cursos # Magia de SQLAlchemy
        else:
            flash("Selecciona un alumno", "warning")

    return render_template("consultas/cursos_alumno.html", alumnos=alumnos, resultados=resultados, seleccionado=seleccionado)

# --- 2. CURSOS POR MAESTRO ---
@consultas_bp.route("/cursos_por_maestro", methods=["GET", "POST"])
def cursos_por_maestro():
    maestros = Maestros.query.all()
    resultados = None
    seleccionado = None

    if request.method == "POST":
        matricula = request.form.get("matricula")
        if matricula:
            seleccionado = Maestros.query.get(matricula)
            resultados = seleccionado.cursos 
        else:
            flash("Selecciona un maestro", "warning")

    return render_template("consultas/cursos_maestro.html", maestros=maestros, resultados=resultados, seleccionado=seleccionado)

# --- 3. ALUMNOS POR CURSO ---
@consultas_bp.route("/alumnos_por_curso", methods=["GET", "POST"])
def alumnos_por_curso():
    cursos = Curso.query.all()
    resultados = None
    seleccionado = None

    if request.method == "POST":
        curso_id = request.form.get("curso_id")
        if curso_id:
            seleccionado = Curso.query.get(curso_id)
            resultados = seleccionado.alumnos
        else:
            flash("Selecciona un curso", "warning")

    return render_template("consultas/alumnos_curso.html", cursos=cursos, resultados=resultados, seleccionado=seleccionado)