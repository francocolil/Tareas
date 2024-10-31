from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()

bcrypt = Bcrypt()

login_manager = LoginManager()

def run_app():
    
    app = Flask(__name__)
    
    bcrypt.init_app(app)
    
    login_manager.init_app(app)
    
    app.config.from_object('config.Config')
    
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    from . import proyecto
    app.register_blueprint(proyecto.bp)
    
    from . import tarea
    app.register_blueprint(tarea.bp)
    
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()
    
    return app