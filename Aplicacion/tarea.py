from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_required

from Aplicacion import db

from .models import Tarea


bp = Blueprint('tarea', __name__, url_prefix='/tarea')


@bp.route('/ver-tarea', methods=['GET', 'POST'])
def ver_tarea():
    tareas = Tarea.query.all()
    return render_template('tareas/tarea.html', tareas=tareas)



@bp.route('/register-tarea/<int:proyecto_id>', methods=['GET', 'POST'])
@login_required
def register_tarea(proyecto_id):
    
    if request.method == 'POST':
        title = request.form["title"]
        desc = request.form["desc"]
        state = request.form["state"]
        
        tarea = Tarea(proyecto_id, title, desc, state)
        
        db.session.add(tarea)
        db.session.commit()
        return redirect('tarea.ver_tarea')
    
    return render_template('tareas/register.html', proyecto_id=proyecto_id)



def tener_id(id):
    tarea_id = Tarea.query.get_or_404(id)
    return tarea_id



@bp.route('/actualizar-tarea/<int:id>', methods=['GET', 'POST'])
@login_required
def actualizar_tarea(id):
    
    id_tarea = tener_id(id)
    
    if request.form == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        state = request.form["state"]
        
        db.session.commit()
        
        return redirect(url_for('tarea.ver_tarea'))
    
    return render_template('tareas/update.html')


@bp.route('/eliminar-tarea/<int:id>', methods=['GET', 'POST'])
def meliminar_tarea(id):
    
    tarea = tener_id(id)
    
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('tarea.ver_tarea'))