from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()

def run_app():
    
    app = Flask(__name__)
    
    bcrypt.init_app(app)
    
    app.config.from_object('config.Config')
    
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()
    
    return app