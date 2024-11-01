from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_required

from Aplicacion import db

from .models import Tarea


bp = Blueprint('tarea', __name__, url_prefix='/tarea')


@bp.route('/ver-tarea/<int:proyecto_id>', methods=['GET', 'POST'])
@login_required
def ver_tarea(proyecto_id):
    tareas = Tarea.query.filter_by(proyecto_id=proyecto_id).all()
    return render_template('tareas/tarea.html', tareas=tareas, proyecto_id=proyecto_id)



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
        return redirect(url_for('tarea.ver_tarea', proyecto_id=proyecto_id))
    
    return render_template('tareas/register.html', proyecto_id=proyecto_id)



def tener_id(id):
    tarea_id = Tarea.query.get_or_404(id)
    return tarea_id



@bp.route('/actualizar-tarea/<int:id>', methods=['GET', 'POST'])
@login_required
def actualizar_tarea(id):
    
    id_tarea = tener_id(id)
    
    if request.method == "POST":
        id_tarea.title = request.form["title"]
        id_tarea.desc = request.form["desc"]
        id_tarea.state = request.form["state"]
        
        db.session.commit()
        
        return redirect(url_for('tarea.ver_tarea', proyecto_id=id_tarea.proyecto_id))
    
    return render_template('tareas/update.html', id_tarea=id_tarea)


@bp.route('/eliminar-tarea/<int:id>')
@login_required
def eliminar_tarea(id):
    
    tarea = tener_id(id)
    
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('tarea.ver_tarea', proyecto_id=tarea.proyecto_id))