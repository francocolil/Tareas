from flask import Flask, render_template, redirect, request, Blueprint, url_for, flash

from flask_login import login_user, logout_user

from .models import User

from Aplicacion import db, bcrypt, login_manager

bp = Blueprint("auth", __name__, url_prefix="/auth")



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp.route('/register', methods=["GET", "POST"])
def register():
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password_bcrypt = bcrypt.generate_password_hash(password)
        
        user = User(username, password=password_bcrypt)
        
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
        
        user = User.query.filter_by(username=username).first()
        
        if user == None or not bcrypt.check_password_hash(user.password, password):
            flash("El Usuario o Contraseña son ERRONEAS")
        
        else:
            login_user(user)
            return redirect(url_for('index'))

    return render_template('auth/login.html')



@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))