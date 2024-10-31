from flask import Flask, render_template, request, Blueprint, redirect, url_for, flash

from Aplicacion import db

from .models import Proyecto, User

from flask_login import login_required, current_user

bp = Blueprint("proyecto", __name__, url_prefix="/proyecto")



@bp.route('/ver-proyectos', methods=['GET', 'POST'])
@login_required
def ver_proyectos():
    proyectos = Proyecto.query.filter_by(created_by=current_user.id).all()
    return render_template('proyecto/proyectos.html', proyecto=proyectos)



@bp.route('/register-proyecto', methods=['GET', 'POST'])
@login_required
def register_proyecto():
    
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        state = request.form['state']
        
        proyecto = Proyecto(title, desc, state, current_user.id ,)
        
        db.session.add(proyecto)
        db.session.commit()
        flash(f"El proyecto fue creado correctamente")
        return redirect(url_for('index'))
    
    return render_template('proyecto/register.html')


def tener_id(id):
    proyecto_id = Proyecto.query.get_or_404(id)
    return proyecto_id



@bp.route('/actualizar-proyecto/<int:id>', methods=['GET', 'POST'])
@login_required
def actualizar_proyecto(id):
    
    proyecto_id = tener_id(id)
    
    if request.method == "POST":
        title = request.form.get('title')
        desc = request.form.get('desc')
        state = request.form.get('state')
        
        db.session.commit()
        return redirect(url_for('proyecto.ver_proyectos'))
    
    return render_template('proyecto/register.html', proyecto_id=proyecto_id)




@bp.route('/eliminar-proyecto/<int:id>', methods=['GET', 'POST'])
@login_required
def eliminar_proyecto(id):
    
    proyecto = tener_id(id)
    
    db.session.delete(proyecto)
    db.session.commit()
    
    return redirect(url_for('proyecto.ver_proyecto'))