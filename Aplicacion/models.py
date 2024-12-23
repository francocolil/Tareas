from Aplicacion import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    proyecto = db.relationship('Proyecto', back_populates='user', uselist=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User: {self.username}>"

class Proyecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    state = db.Column(db.String(50), nullable=False)
    user = db.relationship('User', back_populates='proyecto')
    tarea = db.relationship('Tarea', back_populates='proyecto', cascade="all, delete-orphan", uselist=True)

    def __init__(self, title, desc, state, created_by):
        self.title = title
        self.desc = desc
        self.state = state
        self.created_by = created_by

    def __repr__(self):
        return f"<Proyecto: {self.title}>"

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    state = db.Column(db.String(50), nullable=False)
    proyecto = db.relationship('Proyecto', back_populates='tarea')

    def __init__(self, proyecto_id, title, desc, state):
        self.proyecto_id = proyecto_id
        self.title = title
        self.desc = desc
        self.state = state

    def __repr__(self):
        return f"<Tarea: {self.title}>"