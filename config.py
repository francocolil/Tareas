DATA_BASE = "sqlite:///project.db"

class Config():
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = DATA_BASE