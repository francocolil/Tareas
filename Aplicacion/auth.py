from flask import Flask, render_template, redirect, request, g, session, Blueprint, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User

from Aplicacion import db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route('/register', methods=["GET", "POST"])
def register():
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = User(username, generate_password_hash(password))
        
        user_name = User.query.filter_by(username=username).first()
        
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f"El usuario {username} ya existe!!!!"
        
        flash(error)
    return render_template('auth/register.html')


@bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        error = None
        
        user = User.query.filter_by(username=username).first()
        
        if username is None or not check_password_hash(user.password, password):
            error = "El Usuario o Contraseña son ERRONEAS"
        
        if error == None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index'))
        
        flash(error)

    return render_template('auth/login.html')